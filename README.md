# Goodreads Pipeline — Day 1 (Scaffold + CI)

This is the Day 1 starting point for your EC2‑based Airflow project. It includes:
- Minimal DAG skeleton
- GitHub Actions workflow to import‑test DAGs
- Clean repo layout you'll extend on later days

## Repo Layout
```
goodreads-pipeline/
├── dags/
│   └── goodreads_weekly.py
├── plugins/
│   └── __init__.py
├── include/
├── docker/
│   └── README.md  # placeholder; Day 3 will add docker-compose.yml here
├── .github/
│   └── workflows/
│       └── ci.yml
├── .gitignore
└── requirements.txt
```

## Push to GitHub
```bash
git init
git branch -m main
git add .
git commit -m "Day 1: scaffold with DAG skeleton + CI import test"
git remote add origin https://github.com/<your-username>/goodreads-pipeline.git
git push -u origin main
```
