# Hospital Readmission Prediction ML Project

ML-powered API for predicting hospital readmission risk using clinical data from the Diabetes 130-US Hospitals dataset.

## Overview

This project uses machine learning to predict hospital readmission risk for diabetic patients, helping healthcare providers identify high-risk patients and improve patient outcomes.

**Dataset**: Diabetes 130-US Hospitals for Years 1999-2008 (UCI ML Repository, ID: 296)

## Quick Start

### Prerequisites

- Python 3.10+
- Conda or Miniconda
- Git

### Installation

```bash
# Clone the repository
git clone https://github.com/KrisameReimu/my_hospital_readmission_prediction_ML.git
cd my_hospital_readmission_prediction_ML

# Create and activate Conda environment
conda create -n hospital_ml python=3.10 -y
conda activate hospital_ml

# Install dependencies
pip install -r requirements.txt

# Fetch the dataset
python src/data/fetch_ucirepo.py
```

## Project Structure

```
my_hospital_readmission_prediction_ML/
├── .vscode/                    # VS Code settings
│   └── settings.json          # Editor and Copilot configuration
├── data/                      # Data directory
│   ├── raw/                   # Raw data files
│   └── processed/             # Processed data files
├── notebooks/                 # Jupyter notebooks for exploration
├── src/                       # Source code
│   ├── api/                   # API endpoints
│   ├── data/                  # Data fetching and processing
│   │   └── fetch_ucirepo.py  # Dataset fetching script
│   └── models/                # Model training and evaluation
├── GIT_WORKFLOW.md           # Git workflow guide
├── VSCODE_SETUP.md           # VS Code and Copilot setup guide
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## Documentation

- **[Git Workflow Guide](GIT_WORKFLOW.md)** - Learn about branching strategies, commit conventions, and best practices
- **[VS Code Setup Guide](VSCODE_SETUP.md)** - Configure VS Code and GitHub Copilot for this project

## Development

### Setting Up Your Environment

1. **Configure VS Code**: Follow the [VS Code Setup Guide](VSCODE_SETUP.md)
2. **Learn Git Workflow**: Read the [Git Workflow Guide](GIT_WORKFLOW.md)
3. **Activate Environment**: Always work with `conda activate hospital_ml`

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src
```

### Code Style

This project follows PEP 8 with some modifications:
- Line length: 100 characters
- Formatter: Black
- Linter: Flake8

Code is automatically formatted on save if you use the provided VS Code settings.

## Contributing

1. Create a feature branch: `git checkout -b feature/your-feature`
2. Make your changes following the code style
3. Write tests for new functionality
4. Commit with conventional commit messages
5. Push and create a Pull Request

See [GIT_WORKFLOW.md](GIT_WORKFLOW.md) for detailed guidelines.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Dataset Attribution

**Dataset**: Diabetes 130-US hospitals for years 1999-2008  
**Source**: UCI Machine Learning Repository  
**DOI**: 10.24432/C5230J  
**Citation**: Clore,John, Cios,Krzysztof, DeShazo,Jon, and Strack,Beata. (2014). Diabetes 130-US hospitals for years 1999-2008. UCI Machine Learning Repository. https://doi.org/10.24432/C5230J

## Acknowledgments

- UCI Machine Learning Repository for providing the dataset
- The healthcare data science community for research and insights
