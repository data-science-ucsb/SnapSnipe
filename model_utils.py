"""Helpers for CLIP. You don't need to edit this file — just use the functions.

- zero_shot(image, categories)  -> guess using only category *names* (no training)
- embed(images)                 -> turn photos into 512 numbers each (for training)
"""
from functools import lru_cache

import numpy as np
import torch
from PIL import Image

from config import MODEL_NAME, PROMPT_TEMPLATE


@lru_cache(maxsize=1)
def load_clip():
    """Download (first time only) and load CLIP."""
    from transformers import CLIPModel, CLIPProcessor

    model = CLIPModel.from_pretrained(MODEL_NAME).eval()
    processor = CLIPProcessor.from_pretrained(MODEL_NAME)
    return model, processor


def _to_rgb(img):
    """Accept a file path or a PIL image; return an RGB PIL image."""
    if not isinstance(img, Image.Image):
        img = Image.open(img)
    return img.convert("RGB")


@torch.no_grad()
def embed(images, batch_size=32):
    """Turn a list of images (paths or PIL images) into an (N, 512) array."""
    model, processor = load_clip()
    chunks = []
    for start in range(0, len(images), batch_size):
        batch = [_to_rgb(img) for img in images[start:start + batch_size]]
        inputs = processor(images=batch, return_tensors="pt")
        feats = model.get_image_features(**inputs)
        feats = feats / feats.norm(dim=-1, keepdim=True)  # normalize length to 1
        chunks.append(feats.cpu().numpy())
    return np.concatenate(chunks)


@torch.no_grad()
def zero_shot(image, categories, template=PROMPT_TEMPLATE):
    """Return {category: probability} without any training."""
    model, processor = load_clip()
    prompts = [template.format(c) for c in categories]
    inputs = processor(text=prompts, images=_to_rgb(image), return_tensors="pt", padding=True)
    probs = model(**inputs).logits_per_image.softmax(dim=-1)[0]
    return {c: float(p) for c, p in zip(categories, probs)}
