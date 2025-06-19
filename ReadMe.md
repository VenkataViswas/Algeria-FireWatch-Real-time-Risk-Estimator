# Algeria FireWatch - Real time Risk Estimator 🌲🔥

## ✅ Project Overview
This project predicts the *Fire Weather Index (FWI)*, a proxy for fire risk, using meteorological and environmental data across two Algerian regions: Bejaia and Sidi Bel Abbes.  
A machine learning model (Ridge) powered by scikit-learn is wrapped in a Flask web app and deployed AWS EC2.

---

## 📁 Dataset

- **Source**: Algerian Forest Fires dataset  
- **Timeframe**: June–September 2012  
- **Regions**: Bejaia (northeast) & Sidi Bel Abbes (northwest)  
- **Total instances**: 244 (122 per region)  

### Features:

- **Date**  
- **Meteorological**:  
  - Temperature (°C)  
  - Relative Humidity (%)  
  - Wind Speed (km/h)  
  - Rain (mm)  
- **FWI Components**:  
  - FFMC  
  - DMC  
  - DC  
  - ISI  
  - BUI  
- **Target**: Fire Weather Index (FWI)

### Ranges:

| Feature | Min | Max |
|--------|------|------|
| Temp | 22 °C | 42 °C |
| RH | 21 % | 90 % |
| Ws | 6 km/h | 29 km/h |
| Rain | 0 mm | 16.8 mm |
| FFMC | 28.6 | 92.5 |
| DMC | 1.1 | 65.9 |
| DC | 7 | 220.4 |
| ISI | 0 | 18.5 |
| BUI | 1.1 | 68.0 |
| FWI | 0 | 31.1 |

---

## 🔍 Model Development

- **Preprocessing**:  
  - Data cleaning  
  - Type conversion  
  - Scaling using `StandardScaler`  
  - Region encoding

- **Algorithm**:  
  - `Ridge Linear Regression` (L2 regularization)


- **Performance**:
  - **R² score** ≈ 0.98  
  - **Mean Absolute Error (MAE)**: ~0.56

---

## 🏗️ Project Structure

```
algerian_forest_fire_predictor/
├── app.py                           # Flask application entrypoint
├── models/
│   └── ridge.pkl       # Serialized Ridge Linear Regression  model
    └── Scalare.pkl     # Serialized Stadard Scalar Model
├── static/                          # CSS/JS files
├── templates/                       # HTML templates (index, result views)
├── notebooks/
│   ├── …_EDA.ipynb                 # Exploratory Data Analysis
│   └── …_Model_training.ipynb      # Feature engineering & model training
├── requirements.txt                # Dependencies
└── README.md                       # Project documentation
```

---

## 🚀 Quickstart: Run Locally

```bash
git clone https://github.com/VenkataViswas/Algerian-Forest-Fires-Prediction-Using-ElasticCV-mode.git
cd Algerian-Forest-Fires-Prediction-Using-ElasticCV-mode
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

---

## 🌐 Deployment

This application is deployed using **AWS EC2**.  

---

## 📈 EDA & Modeling Insights

- Analyzed feature distributions, correlations, and region-based anomalies  
- Identified strong correlation (>90%) between FWI and other fire indices  
- Evaluated multiple models:
  - Linear Regression  
  - Ridge  
  - Lasso  
  - ElasticNet
---

## 📊 Usage Tips

- Ensure input values are within training data ranges  
- Select the correct region (Bejaia / Sidi Bel Abbes)  

---

## ⚙️ Tech Stack

- **Language**: Python 3.x  
- **Libraries**: numpy, pandas, scikit-learn, Flask  
- **Model**: Ridge
- **Deployment**: AWS EC2


---

## 🤝 Acknowledgements

- Dataset contributors & Algerian Forest Fires community  
- Scikit-learn developers  
