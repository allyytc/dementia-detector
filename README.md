# 🧠 Dementia Risk Predictor

A machine learning web app that predicts dementia risk from clinical patient measurements, built with Python and deployed with Streamlit.

🔗 **[Try the Live App](https://allyytc-dementia-detector.streamlit.app/)**

---

## About The Project

Dementia affects millions of people worldwide and early detection is critical for effective treatment. This project uses real patient data from the OASIS longitudinal study to train a Random Forest classifier that predicts whether a patient is at risk of dementia based on clinical measurements.

The model achieves **82.6% accuracy** on unseen patient data.

> ⚠️ This tool is for educational purposes only and is not a substitute for professional medical diagnosis.

---

## How It Works

1. Enter patient measurements using the sliders
2. Click **Predict**
3. The model returns either **Dementia Detected** or **No Dementia Detected**

---

## Features Used To Predict

| Feature | Description |
|---------|-------------|
| Age | Patient's age |
| MMSE | Mini Mental State Exam score (cognitive test) |
| EDUC | Years of education |
| SES | Socioeconomic status (1-5) |
| eTIV | Estimated total brain volume |
| nWBV | Normalized whole brain volume |
| ASF | Atlas scaling factor |
| Sex | Patient's sex |

---

## Model Performance

| Metric | Score |
|--------|-------|
| Accuracy | 82.6% |
| Precision | 0.83 |
| Recall | 0.81 |
| Algorithm | Random Forest (100 trees) |

---

## Built With

- Python
- scikit-learn
- Pandas
- Streamlit
- Joblib

---

## Dataset

[OASIS Longitudinal MRI Data](https://www.kaggle.com/datasets/jboysen/mri-and-alzheimers) — Open Access Series of Imaging Studies
