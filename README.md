# Dementia Risk Predictor

A Streamlit prototype that scores eight clinical measurements with a saved random forest and returns a binary label: **Dementia Detected** or **No Dementia Detected**.

**[Open the hosted app](https://allyytc-dementia-detector.streamlit.app/)**

Educational demo only. It is not a medical device and is not a substitute for a clinical diagnosis.

## What it does

`app.py` loads `dementia_model.pk1` at startup and renders one page of inputs. **Predict** sends a single row to the forest. Class `1` is shown as an error state, "Dementia Detected". Every other class is shown as a success state, "No Dementia Detected". The page does not display a probability or a risk score. `predict` is the only model call.

The serialized model is a scikit-learn `RandomForestClassifier` with 100 trees, Gini splits, `max_features="sqrt"`, and `random_state=42`. The pickle records scikit-learn 1.6.1. Stored feature names, in model order, are `M/F`, `Age`, `EDUC`, `SES`, `MMSE`, `eTIV`, `nWBV`, and `ASF`.

Those column names match the clinical fields in the [OASIS longitudinal MRI dataset](https://www.kaggle.com/datasets/jboysen/mri-and-alzheimers) (Open Access Series of Imaging Studies), which this project links as its data source. The CSV and the training script are not in this repository. The repo ships the fitted forest and the page that calls it.

## Inputs

Sex is encoded as the model's `M/F` column: Male is `1`, Female is `0`. The select box lists Male first, and Streamlit uses the first option when no index is set.

The page lays the sliders out as Age, MMSE, EDUC, SES, eTIV, nWBV, ASF, then Sex. The predict call reorders them to `[sex, age, EDUC, SES, MMSE, eTIV, nWBV, ASF]`.

| Model feature | Control | Range in the app | Default |
| --- | --- | --- | --- |
| M/F | Sex | Male (1), Female (0) | Male |
| Age | Age | 18–120 | 75 |
| EDUC | Years of education | 0–23 | 12 |
| SES | Socioeconomic status | 1–5 | 3 |
| MMSE | Mini-Mental State Examination score | 0–30 | 25 |
| eTIV | Estimated total intracranial volume, labeled "Brain Volume" | 1000–2500 | 1600 |
| nWBV | Normalized whole-brain volume | 0.6–0.9 | 0.72 |
| ASF | Atlas scaling factor | 0.8–1.5 | 1.0 |

Descriptions are the standard meanings of those OASIS column names. The sliders do not label physical units. The app does not ask for CDR, visit number, or MRI id.

## Architecture

```text
sliders and sex select box
        |
        v
app.py  -- joblib.load("dementia_model.pk1") --> RandomForestClassifier
        |
        v
predict([[M/F, Age, EDUC, SES, MMSE, eTIV, nWBV, ASF]])
        |
        v
class 1 --> "Dementia Detected"
class 0 --> "No Dementia Detected"
```

Inference only. There is no training code, database, account system, or API in this repo.

## Tech stack

Declared in `requirements.txt` (versions are not pinned):

- **Streamlit** — the interface
- **scikit-learn** — the random forest
- **numpy** — array data inside the pickle
- **pandas** — listed as a dependency; `app.py` does not import it

`app.py` imports **joblib** to load the forest. joblib is not named in `requirements.txt`; installing scikit-learn brings it in.

## Run locally

From the repository root:

```bash
pip install -r requirements.txt
streamlit run app.py
```

Streamlit serves the app on port 8501. No environment variables are required.

### Dev container

`.devcontainer/devcontainer.json` uses the image `mcr.microsoft.com/devcontainers/python:1-3.11-bookworm`. On create it installs `requirements.txt` when that file exists, then installs Streamlit for the user. On attach it starts:

```bash
streamlit run app.py --server.enableCORS false --server.enableXsrfProtection false
```

Port 8501 is forwarded and labeled Application. `README.md` and `app.py` open by default in Codespaces.

## Dataset

[MRI and Alzheimers on Kaggle](https://www.kaggle.com/datasets/jboysen/mri-and-alzheimers) — the longitudinal OASIS table. Feature names on the saved model match that table's clinical columns. Holdout metrics are not included here, because this repository has no evaluation script or results file.

## Team

Draft roles, inferred from git history.

| Name | Role (draft) |
| --- | --- |
| Ally Chen ([allyytc](https://github.com/allyytc)) | Streamlit app, saved model, dev container, documentation |
