# VS Code and GitHub Copilot Setup Guide

This guide helps you configure your VS Code environment for this machine learning project.

## Prerequisites

1. **VS Code** installed ([Download](https://code.visualstudio.com/))
2. **GitHub Copilot** subscription ([Sign up](https://github.com/features/copilot))
3. **Python extension** for VS Code
4. **Conda** or **Miniconda** installed

## Required VS Code Extensions

Install these extensions in VS Code:

```bash
# Required
- Python (ms-python.python)
- GitHub Copilot (GitHub.copilot)
- Pylance (ms-python.vscode-pylance)

# Recommended
- Black Formatter (ms-python.black-formatter)
- Jupyter (ms-toolsai.jupyter)
- GitLens (eamodio.gitlens)
```

To install, open VS Code and:
1. Press `Cmd+Shift+X` (Mac) or `Ctrl+Shift+X` (Windows/Linux)
2. Search for each extension
3. Click "Install"

## Project Configuration

The repository includes a `.vscode/settings.json` file with pre-configured settings:

### GitHub Copilot Settings

- **Enabled for**: Python files, Markdown
- **Comment Language**: English (even if your system locale is different)
- **Disabled for**: Plain text files

These settings ensure Copilot suggestions and generated comments are always in English, which is helpful for:
- Code consistency across the team
- Better documentation for international collaboration
- Interview preparation with English code comments

### Python Environment Settings

The configuration automatically:
- Detects the `hospital_ml` Conda environment
- Activates the environment in the integrated terminal
- Sets up Python linting with Flake8
- Configures Black formatter with 100-character line length
- Formats code on save

## Creating the Conda Environment

If you haven't created the project environment yet:

```bash
# Create the environment
conda create -n hospital_ml python=3.10 -y

# Activate the environment
conda activate hospital_ml

# Install dependencies
pip install -r requirements.txt
```

## Verifying Your Setup

### 1. Check Python Interpreter

1. Open any `.py` file in the project
2. Look at the bottom-left corner of VS Code
3. You should see `Python 3.10.x ('hospital_ml')`
4. If not, click on the Python version and select the `hospital_ml` environment

### 2. Check Terminal Environment

1. Open a new terminal in VS Code (`` Ctrl+` `` or `` Cmd+` ``)
2. You should see `(hospital_ml)` at the beginning of your prompt
3. Verify with: `conda env list` (active environment is marked with `*`)

### 3. Test Copilot

1. Create a new Python file
2. Type a comment like `# Function to calculate mean`
3. Press Enter - Copilot should suggest code
4. Suggestions should include English comments

## Customizing Settings

To customize settings for your personal preferences:

### User Settings (Global)
1. Press `Cmd+,` (Mac) or `Ctrl+,` (Windows/Linux)
2. Search for settings
3. Modify in the UI or in `settings.json`

### Workspace Settings (Project-specific)
- Edit `.vscode/settings.json` directly
- These override user settings when working in this project

## Copilot Best Practices

### Getting Better Suggestions

1. **Write clear comments**: Describe what you want in natural language
   ```python
   # Calculate the average readmission rate for diabetic patients
   ```

2. **Provide context**: Include function signatures and docstrings
   ```python
   def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
       """Clean and preprocess the hospital readmission dataset."""
       # Copilot will understand the context better
   ```

3. **Use descriptive names**: Clear variable and function names help Copilot
   ```python
   # Good: readmission_rate
   # Bad: rr
   ```

### Accepting/Rejecting Suggestions

- **Accept**: `Tab` key
- **Reject**: `Esc` key
- **Next suggestion**: `Alt+]` or `Option+]`
- **Previous suggestion**: `Alt+[` or `Option+[`
- **Open Copilot**: `Ctrl+Enter` or `Cmd+Enter` (see 10 suggestions)

### Copilot Chat (if available)

If you have Copilot Chat:
- Press `Cmd+I` (Mac) or `Ctrl+I` (Windows/Linux)
- Ask questions about the code
- Request explanations, refactoring, or tests

## Common Issues and Solutions

### Issue: Copilot not working

**Solutions:**
1. Check GitHub Copilot subscription is active
2. Sign in to GitHub in VS Code: `Cmd+Shift+P` → "GitHub: Sign In"
3. Reload VS Code: `Cmd+Shift+P` → "Developer: Reload Window"
4. Check Copilot status: Look for the Copilot icon in the status bar

### Issue: Wrong Python environment activated

**Solutions:**
1. Click Python version in bottom-left corner
2. Select "Enter interpreter path..."
3. Navigate to your Conda environment's Python:
   - **Mac/Linux**: `~/miniconda3/envs/hospital_ml/bin/python` or `~/anaconda3/envs/hospital_ml/bin/python`
   - **Windows**: `%USERPROFILE%\miniconda3\envs\hospital_ml\Scripts\python.exe`

Alternatively:
```bash
# In terminal
conda activate hospital_ml
code .  # Reopen VS Code from activated environment
```

### Issue: Copilot suggestions in wrong language

**Solutions:**
1. Verify `.vscode/settings.json` contains:
   ```json
   "github.copilot.advanced": {
       "language": "en"
   }
   ```
2. Reload VS Code window
3. If persistent, check your GitHub Copilot settings online

### Issue: Formatting not working on save

**Solutions:**
1. Install Black formatter extension
2. Verify Black is installed: `pip install black`
3. Check settings include:
   ```json
   "[python]": {
       "editor.formatOnSave": true
   }
   ```

## Additional Resources

- [VS Code Python Tutorial](https://code.visualstudio.com/docs/python/python-tutorial)
- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [Conda Environments Guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
- [Python Code Style - PEP 8](https://pep8.org/)

## Quick Reference

### Keyboard Shortcuts

| Action | Mac | Windows/Linux |
|--------|-----|---------------|
| Open Command Palette | `Cmd+Shift+P` | `Ctrl+Shift+P` |
| Open Terminal | `` Cmd+` `` | `` Ctrl+` `` |
| Quick Open File | `Cmd+P` | `Ctrl+P` |
| Accept Copilot | `Tab` | `Tab` |
| Copilot Suggestions | `Cmd+Enter` | `Ctrl+Enter` |
| Format Document | `Shift+Alt+F` | `Shift+Alt+F` |
| Go to Definition | `F12` | `F12` |
| Find References | `Shift+F12` | `Shift+F12` |

### Common Commands

```bash
# Activate environment
conda activate hospital_ml

# Check environment
conda info --envs

# Install package
pip install <package-name>

# Update dependencies
pip install -r requirements.txt

# Run Python script
python src/data/fetch_ucirepo.py

# Start Jupyter
jupyter notebook
```

## Support

For issues specific to this project, please:
1. Check this documentation
2. Review `GIT_WORKFLOW.md` for Git-related questions
3. Open an issue on GitHub with details about your setup
