# Git Practice Project

A tiny command-line task tracker written in Python. It is intentionally small so you can practise Git basics without needing external packages.

## Requirements
- Python 3.9 or newer

## Run it
Open a terminal in this folder and run:

```bash
python app.py add "Study Git"
python app.py add "Practise commits"
python app.py list
python app.py done 1
python app.py list
```

The app creates `tasks.json` automatically when you add your first task. That file is runtime data and is ignored by Git.

## Run the tests

```bash
python -m unittest -v
```

## Suggested Git practice

```bash
git init
git status
git add README.md app.py test_app.py .gitignore
git commit -m "Initial commit"
git log --oneline
git branch feature/improve-help
git switch feature/improve-help
```

Make a small change to `app.py`, then:

```bash
git diff
git add app.py
git commit -m "Improve task tracker"
git switch main
git merge feature/improve-help
```

To connect this local repository to a GitHub repository, create an empty repository on GitHub, then use the remote URL GitHub gives you:

```bash
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```
