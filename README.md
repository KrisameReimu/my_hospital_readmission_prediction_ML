# Hospital Readmission Prediction - ML Project

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Machine learning system for predicting 30-day hospital readmission risk in diabetic patients using clinical and administrative data from 130 US hospitals (1999-2008).

## 📊 Project Overview

**Problem Statement**: Predict whether a diabetic inpatient will be readmitted within 30 days of discharge.

**Business Impact**:
- Reduces hospital costs and Medicare penalties
- Improves patient outcomes through early intervention
- Optimizes resource allocation for high-risk patients

**Dataset**: Diabetes 130-US Hospitals (UCI ML Repository)
- **Volume**: 101,766 hospital encounters
- **Features**: 48 clinical and administrative variables
- **Target**: Binary classification (readmitted <30 days: Yes/No)
- **Challenge**: Severe class imbalance (11.2% positive class)

## 🎯 Key Findings from EDA

### Data Quality Assessment

| Issue | Details | Resolution |
|-------|---------|------------|
| **Missing Values** | `weight` (97%), `medical_specialty` (49%), `payer_code` (40%) | Drop weight; impute others with "Unknown" |
| **Class Imbalance** | 8:1 ratio (negative:positive) | SMOTE + class weights |
| **Data Encoding** | `'?'` used as missing placeholder | Standardize to NaN |
| **High Cardinality** | Diagnosis codes, medical specialties | Group by ICD9 chapters |

### Feature Insights

**Predictive Features Identified**:
1. **Healthcare Utilization**: Prior inpatient/outpatient/emergency visits
2. **Medication Management**: Changes in diabetes medications
3. **Lab Testing**: HbA1c test performed (glycemic control monitoring)
4. **Diagnosis Complexity**: Number of diagnoses, primary diagnosis severity
5. **Length of Stay**: Time in hospital × number of procedures

**Statistical Findings**:
- Multiple encounters per patient → Requires patient-level stratification
- Low linear correlations → Tree-based models likely to outperform linear models
- Medication changes correlate with readmission (potential disease severity proxy)

## 🛠️ Technical Stack

**Core**:
- Python 3.10+
- scikit-learn (modeling, pipelines)
- pandas, numpy (data processing)
- XGBoost, LightGBM (advanced models)

**Visualization**:
- matplotlib, seaborn
- SHAP (model interpretability)

**Development**:
- Jupyter Notebook (exploration)
- Git (version control)
- pytest (testing)

## 📁 Project Structure

```
my_hospital_readmission_ML/
├── data/
│   ├── raw/                    # Original dataset
│   │   └── diabetic_data.csv
│   └── processed/              # Cleaned and engineered features
├── notebooks/
│   ├── 01_data_exploration.ipynb    # ✅ Complete EDA
│   └── 02_model_training.ipynb      # 🚧 In progress
├── src/
│   ├── data/
│   │   ├── fetch_ucirepo.py         # Dataset downloader
│   │   ├── preprocessing.py         # 🚧 Data cleaning pipeline
│   │   └── feature_engineering.py   # 🚧 Feature transformation
│   ├── models/                      # Model training & evaluation
│   └── api/                         # Inference API (planned)
├── tests/                           # Unit tests
├── requirements.txt                 # Python dependencies
└── README.md
```

## 🚀 Quick Start

### 1. Clone Repository

```bash
git clone https://github.com/KrisameReimu/my_hospital_readmission_prediction_ML.git
cd my_hospital_readmission_ML
```

### 2. Set Up Environment

```bash
# Create conda environment
conda create -n hospital_ml python=3.10 -y
conda activate hospital_ml

# Install dependencies
pip install -r requirements.txt
```

### 3. Download Dataset

```bash
python src/data/fetch_ucirepo.py
```

### 4. Run EDA Notebook

```bash
jupyter notebook notebooks/01_data_exploration.ipynb
```

## � Documentation

- **[Git Workflow Guide](GIT_WORKFLOW.md)** - Branching strategy and commit conventions
- **[VS Code Setup Guide](VSCODE_SETUP.md)** - Editor and Copilot configuration

## �📈 Project Progress

- [x] **Data Acquisition**: UCI dataset downloaded and validated
- [x] **EDA Complete**: Comprehensive analysis with statistical tests
- [x] **Git Workflow**: Feature branch strategy established
- [ ] **Preprocessing Pipeline**: Data cleaning and encoding (next)
- [ ] **Baseline Models**: Logistic Regression, Random Forest
- [ ] **Advanced Models**: XGBoost, LightGBM with hyperparameter tuning
- [ ] **Model Evaluation**: SHAP analysis, fairness testing
- [ ] **Deployment**: FastAPI inference endpoint

## 📊 Proposed Modeling Strategy

### Preprocessing Pipeline
```python
1. Missing Value Handling
   - Drop: weight (97% missing)
   - Impute: medical_specialty, payer_code → "Unknown"
   - Create indicators: For informative missingness

2. Feature Encoding
   - One-hot: Low cardinality (<10 unique)
   - Target encoding: Medium cardinality (10-50)
   - ICD9 grouping: Diagnosis codes by disease chapters

3. Feature Engineering
   - Total diabetes medications (sum of med flags)
   - Healthcare utilization score (prior visits)
   - HbA1c test indicator
   - Medication change flag
   - Lab/procedure intensity (per day ratios)

4. Imbalance Handling
   - SMOTE for training set
   - Class weights in models
   - Stratified K-fold validation
```

### Model Evaluation Metrics

Given severe class imbalance, we prioritize:
- **Primary**: AUC-ROC, PR-AUC (Precision-Recall)
- **Secondary**: Recall, F1-score
- **Avoid**: Accuracy (misleading for imbalanced data)

## 🔬 Modeling Roadmap

1. **Baseline** (Simple, interpretable)
   - Logistic Regression with class weights
   - Random Forest with balanced sampling

2. **Advanced** (Higher performance)
   - XGBoost with custom objective
   - LightGBM with focal loss
   - Ensemble stacking

3. **Evaluation**
   - 5-fold stratified cross-validation
   - Time-based validation (train: 1999-2006, test: 2007-2008)
   - Subgroup analysis (by age, race, gender)

## 📚 Data Source & Citation

**Dataset**: Diabetes 130-US Hospitals for Years 1999-2008  
**Repository**: [UCI Machine Learning Repository (ID: 296)](https://archive.ics.uci.edu/dataset/296)

**Citation**:
> Strack, B., DeShazo, J. P., Gennings, C., Olmo, J. L., Ventura, S., Cios, K. J., & Clore, J. N. (2014). Impact of HbA1c measurement on hospital readmission rates: analysis of 70,000 clinical database patient records. *BioMed Research International*, 2014.

## 🤝 Contributing

This is a personal project for ML portfolio demonstration. Feedback and suggestions are welcome via issues.

## 📄 License

MIT License - See LICENSE file for details

## 📧 Contact

**Author**: KrisameReimu  
**Repository**: [github.com/KrisameReimu/my_hospital_readmission_prediction_ML](https://github.com/KrisameReimu/my_hospital_readmission_prediction_ML)

---

**Last Updated**: November 6, 2025  
**Status**: 🚧 EDA Complete | Preprocessing Pipeline In Progress
