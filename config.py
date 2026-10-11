"""SnapSnipe settings — this is the first file you should edit!"""

# 👉 Week 3: change these to your own 3–5 categories.
# Folder names in data/raw/ must match these exactly (lowercase, no spaces is easiest).
CATEGORIES = ["pizza", "salad", "burrito"]

# How CLIP "reads" each category before you've trained anything (zero-shot mode).
# Tweak it if guesses are off, e.g. "a photo of {}, a type of food".
PROMPT_TEMPLATE = "a photo of {}"

# Text shown on the app page — vibecode these!
APP_TITLE = "📸 SnapSnipe"
APP_DESCRIPTION = "Upload a photo and SnapSnipe will tell you what's in it."

# The pretrained model we borrow (transfer learning). No need to change.
MODEL_NAME = "openai/clip-vit-base-patch32"

# Where the trained model is saved in week 6.
TRAINED_MODEL_PATH = "model.joblib"
