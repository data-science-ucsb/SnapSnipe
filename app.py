"""SnapSnipe web app.

Before week 6 it uses zero-shot CLIP (guesses from category names).
After you add model.joblib (week 6), it uses YOUR trained classifier.
"""
from pathlib import Path

import gradio as gr
import joblib

from config import APP_DESCRIPTION, APP_TITLE, CATEGORIES, TRAINED_MODEL_PATH
from model_utils import embed, zero_shot

trained = None
if Path(TRAINED_MODEL_PATH).exists():
    trained = joblib.load(TRAINED_MODEL_PATH)  # {"clf": ..., "categories": [...]}
    print("✅ Using your trained model")
else:
    print("ℹ️ No model.joblib yet — using zero-shot CLIP")


def predict(image):
    if image is None:
        return {}
    if trained is not None:
        probs = trained["clf"].predict_proba(embed([image]))[0]
        return {str(c): float(p) for c, p in zip(trained["clf"].classes_, probs)}
    return zero_shot(image, CATEGORIES)


mode = "your trained model" if trained else "zero-shot mode (no training yet)"

demo = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil", label="Your photo"),
    outputs=gr.Label(num_top_classes=3, label="SnapSnipe thinks it's..."),
    title=APP_TITLE,
    description=f"{APP_DESCRIPTION}\n\n*Running on {mode}.*",
    flagging_mode="never",
)

if __name__ == "__main__":
    demo.launch()
