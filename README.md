# ↕️ Sort a Dataset (Pandas)

Sort a dataset using numerical and categorical columns in ascending and descending order with Pandas `sort_values()`.

## Objective
Understand how sorting helps organize and analyze datasets.

## Tools
- Python
- Pandas
- Jupyter Notebook
- Streamlit (for the deployed demo)

## Dataset
Sample Employee dataset (`employees.csv`, 30 rows, 7 columns):
`employee_id, name, department, city, experience_years, salary, rating`
The notebook creates this file itself, so no download is needed.

## Project Structure
```
├── Sort_Dataset.ipynb   # Main notebook
├── employees.csv        # Dataset
├── app.py               # Streamlit web app
├── requirements.txt     # Dependencies
└── README.md
```

## Sorting Cheat Sheet

| Goal | Code |
|---|---|
| Ascending (default) | `df.sort_values('salary')` |
| Descending | `df.sort_values('salary', ascending=False)` |
| Categorical (A to Z) | `df.sort_values('name')` |
| Multiple columns | `df.sort_values(['department', 'salary'])` |
| Mixed order | `df.sort_values(['department', 'salary'], ascending=[True, False])` |
| Reset row numbers | `df.sort_values('salary', ignore_index=True)` |
| Top / bottom N | `df.nlargest(5, 'salary')`, `df.nsmallest(5, 'salary')` |

`sort_values()` returns a **new** DataFrame. The original is unchanged unless you assign the result back.

## What the Notebook Covers
- Ascending sort on numerical and categorical columns
- Descending sort on numerical and categorical columns
- Sorting by two and three columns, including mixed orders
- `ignore_index`, `nlargest()`, `nsmallest()`, `sort_index()`

## Run Locally
```bash
git clone https://github.com/<your-username>/pandas-sort-dataset.git
cd pandas-sort-dataset
pip install -r requirements.txt

jupyter notebook Sort_Dataset.ipynb   # notebook
streamlit run app.py                  # web app
```

## Deploy (Streamlit Community Cloud)
1. Push this repo to GitHub (include `employees.csv`).
2. Go to share.streamlit.io and click **New app**.
3. Select the repo, branch `main`, main file `app.py`.
4. Click **Deploy**.

## Interview Questions
- **How do you sort a DataFrame?** `df.sort_values('column')`.
- **What does `ascending=False` do?** It sorts from highest to lowest (or Z to A).
- **Can a DataFrame be sorted by multiple columns?** Yes: `df.sort_values(['col1', 'col2'])`, and each column can have its own order with `ascending=[True, False]`.

## Author
Swetha, AI & ML Track, Veda Technology
