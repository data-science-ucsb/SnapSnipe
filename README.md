# 📸 SnapSnipe

**Build an app that recognizes what's in a photo, then send your friends the link.**

Upload a photo → SnapSnipe tells you what's in it, using 3–5 categories *you* pick (dining hall food, campus spots, sneakers…).

No experience needed. Everything runs in Google Colab or on GitHub's website — nothing to install.

---

## 🚀 Start here (Week 3)

1. Click **Fork** (top right) to get your own copy.
2. Open the starter notebook in Colab:
   [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR-USERNAME/snapsnipe/blob/main/notebooks/00_run_app.ipynb)
   *(after forking, edit this link: replace `YOUR-USERNAME` with your GitHub username)*
3. Type your username in the first cell → **Runtime → Run all** → click the `gradio.live` link.

## 🗓️ Roadmap

| Week | GM | You'll… | Notebook / file |
|------|----|---------|-----------------|
| 3 · 10/13 | AI Vibecoding | Run the app, pick categories, vibecode the UI, start collecting photos | `00_run_app.ipynb`, `config.py`, `app.py` |
| 4 · 10/20 | Project Mgmt / Kanban / PRs | Set up your board, add photos via a PR, write a dataset card | `data/README.md` |
| 5 · 10/27 | Data Analytics | Explore & clean your dataset | `01_explore_data.ipynb` |
| 6 · 11/2  | Classical ML | Train a classifier, find its mistakes, save `model.joblib` | `02_train_model.ipynb` |
| 7 · 11/9  | Deployment | Put it on Hugging Face Spaces and share the link | `app.py` + friends |
| 8 · 11/16 | Talking about your project | Polish this README, demo, resume bullet | this file |

Each week's tasks are GitHub Issues on the club repo — copy them onto your own board.

## 🗂️ What's in here

```
config.py          ← your categories + app text (edit me first!)
app.py             ← the web app (Gradio)
model_utils.py     ← CLIP helpers (no need to edit)
notebooks/         ← one Colab notebook per week
data/raw/<category>/  ← your photos go here
data/README.md     ← your dataset card
model.joblib       ← appears in week 6 after you train
```

## 🧠 How it works

1. **CLIP** (a model pretrained on 400M images) turns each photo into 512 numbers. → *transfer learning*
2. A **logistic regression** learns which numbers mean which category. → *classical ML*
3. **Gradio** wraps it in a web page; **Hugging Face Spaces** hosts it for free. → *deployment*

Before you train (weeks 3–5), the app uses CLIP "zero-shot" — it guesses by comparing your photo to the category *names*.

---

## ✨ Showcase  (fill this in during week 8)

**Headline:** _SnapSnipe tells a ___ from a ___ __% of the time._

**🔗 Live demo:** _link to your Hugging Face Space_

**🎬 Demo:** _GIF or video link_

**The problem:** _Why did you pick these categories? Who would use this?_

**Results:**

| model | test accuracy |
|-------|---------------|
|       |               |

**Mistakes it makes & why:** _…_

**What I'd do next:** _…_

**Resume bullet:** _Built and deployed ___ using ___ that ___._
