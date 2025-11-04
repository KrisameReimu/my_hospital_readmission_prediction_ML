# Git Workflow Guide

This document outlines the professional Git workflow for the Hospital Readmission Prediction ML project.

## Branch Strategy

### Main Branches

- **`main`** - Production-ready code. Always stable and deployable.
- **`develop`** - Integration branch for features. The latest delivered development changes.

### Supporting Branches

- **Feature branches** - For developing new features
  - Naming: `feature/<feature-name>` or `<username>/<feature-name>`
  - Branch from: `develop`
  - Merge back into: `develop`
  - Examples: `feature/data-preprocessing`, `feature/model-training`

- **Bugfix branches** - For fixing bugs in development
  - Naming: `bugfix/<issue-name>`
  - Branch from: `develop`
  - Merge back into: `develop`

- **Hotfix branches** - For urgent production fixes
  - Naming: `hotfix/<issue-name>`
  - Branch from: `main`
  - Merge back into: `main` and `develop`

## Workflow Steps

### Starting a New Feature

```bash
# Update your local develop branch
git checkout develop
git pull origin develop

# Create a new feature branch
git checkout -b feature/my-new-feature

# Work on your feature...
# Make commits as you go
git add <files>
git commit -m "feat: add feature description"
```

### Working on a Feature

```bash
# Check your current changes
git status
git diff

# Stage and commit changes
git add .
git commit -m "feat: descriptive commit message"

# Push to remote regularly
git push origin feature/my-new-feature
```

### Syncing with Latest Changes

```bash
# Fetch latest changes
git fetch origin

# Rebase your feature branch on latest develop
git checkout feature/my-new-feature
git rebase origin/develop

# Or merge if you prefer
git merge origin/develop
```

### Completing a Feature

```bash
# Ensure your branch is up to date
git checkout develop
git pull origin develop
git checkout feature/my-new-feature
git rebase develop

# Push your final changes
git push origin feature/my-new-feature

# Create a Pull Request on GitHub
# After PR is approved and merged, delete the feature branch
git checkout develop
git pull origin develop
git branch -d feature/my-new-feature
```

## Commit Message Convention

Follow the Conventional Commits specification:

### Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- **feat**: A new feature
- **fix**: A bug fix
- **docs**: Documentation only changes
- **style**: Code style changes (formatting, missing semi-colons, etc.)
- **refactor**: Code refactoring without changing functionality
- **perf**: Performance improvements
- **test**: Adding or updating tests
- **chore**: Maintenance tasks, dependency updates

### Examples

```bash
feat(data): add diabetes dataset fetching script

fix(model): correct model evaluation metrics calculation

docs: update README with installation instructions

test(api): add unit tests for prediction endpoint

chore(deps): update scikit-learn to version 1.3.0
```

## Best Practices

### Do's ✓

- **Commit frequently** with meaningful messages
- **Pull before you push** to avoid conflicts
- **Use descriptive branch names** that indicate the feature/fix
- **Write clear commit messages** following conventions
- **Keep commits focused** - one logical change per commit
- **Review your changes** before committing (`git diff`)
- **Test your code** before pushing
- **Delete branches** after they're merged

### Don'ts ✗

- **Don't commit directly to `main`** - always use Pull Requests
- **Don't commit large binary files** without Git LFS
- **Don't commit secrets** or sensitive data (API keys, passwords)
- **Don't force push** to shared branches without team coordination
- **Don't commit broken code** - ensure tests pass
- **Don't use vague messages** like "fix", "update", "changes"

## Pull Request Guidelines

### Creating a PR

1. Ensure your branch is up to date with the target branch
2. Write a clear PR title following commit conventions
3. Provide a detailed description:
   - What changes were made
   - Why the changes were needed
   - How to test the changes
4. Link related issues
5. Request reviews from team members

### PR Template

```markdown
## Description
Brief description of what this PR does

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] Manual testing completed

## Checklist
- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex logic
- [ ] Documentation updated
- [ ] No new warnings generated
```

## Useful Git Commands

### Viewing History

```bash
# View commit history
git log --oneline --graph --all

# View changes in last commit
git show HEAD

# View file history
git log --follow <file>
```

### Undoing Changes

```bash
# Unstage a file
git reset HEAD <file>

# Discard local changes
git checkout -- <file>

# Amend last commit
git commit --amend

# Revert a commit
git revert <commit-hash>
```

### Branch Management

```bash
# List all branches
git branch -a

# Delete local branch
git branch -d <branch-name>

# Delete remote branch
git push origin --delete <branch-name>

# Rename current branch
git branch -m <new-name>
```

### Stashing

```bash
# Stash current changes
git stash

# List stashes
git stash list

# Apply most recent stash
git stash apply

# Apply and remove stash
git stash pop
```

## Environment Setup

### Setting Up Your Git Identity

```bash
# Set your name and email
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Set default branch name
git config --global init.defaultBranch main

# Enable colored output
git config --global color.ui auto
```

### Recommended Git Aliases

Add these to your `~/.gitconfig`:

```ini
[alias]
    st = status
    co = checkout
    br = branch
    ci = commit
    cp = cherry-pick
    unstage = reset HEAD --
    last = log -1 HEAD
    visual = log --oneline --graph --all --decorate
    amend = commit --amend --no-edit
```

## Conda Environment Integration

When working with this project's Conda environment:

```bash
# Activate the project environment before working
conda activate hospital_ml

# Verify you're in the correct environment
conda env list

# Your prompt should show (hospital_ml) not (base)
```

## Additional Resources

- [Git Documentation](https://git-scm.com/doc)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [GitHub Flow](https://guides.github.com/introduction/flow/)
- [Atlassian Git Tutorials](https://www.atlassian.com/git/tutorials)
