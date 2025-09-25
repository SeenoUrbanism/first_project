# NYC Jobs Data Analysis & Data Cleaning Project

## Overview

This project focuses on cleaning, transforming, and analyzing public job postings for New York City, using a structured Python (Pandas) workflow and custom functions for robust data wrangling. The source data includes large CSVs with diverse job roles, salary ranges, and categorical features. The main goal is to provide clean, analysis-ready datasets for insights into salary distributions, contract types, agency trends, and demand for data-centric skills.

The project is organized into modular Jupyter notebooks and Python scripts, with a special emphasis on reproducible preprocessing and targeted extraction of roles related to data analysis, engineering, and modern data skills.

---

## Data Sources

- **NYC Jobs CSV files:** Two separate CSVs with thousands of job postings, each containing up to 30 columns.
- **YAML configuration:** Used to manage file paths and input/output references dynamically.

---

## Main Notebooks and Scripts

### 1. `data_wrangling.ipynb`

- Loads raw CSVs and YAML config.
- Applies custom cleaning functions from `functions.py`:
  - Standardizes column names.
  - Drops duplicates by job ID.
  - Removes irrelevant columns (retaining only those needed for analysis).
  - Cleans punctuation and normalizes text fields (e.g., job titles, skills).
  - Standardizes date columns to pandas datetime objects.
- Filters jobs by:
  - **Business title** (extracts "data analyst", "data engineer", etc.).
  - **Preferred skills** (finds posts mentioning SQL, Python, BI, Tableau, ML, etc.).
  - Separates non-data jobs.
- Outputs three grouped CSVs:
  - All other jobs.
  - Data analyst/engineer roles.
  - Jobs requiring data-centric skills.
- Each step includes summary tables of nulls, column types, and value counts.

### 2. `functions.py`

- Contains all custom data cleaning and transformation functions:
  - Standardize column names.
  - Drop duplicates.
  - Concatenate DataFrames.
  - Remove punctuation and lowercase.
  - Drop irrelevant columns.
  - Regex-based row filtering.
  - Standardize dates.
- Functions are written for flexible, repeatable use in notebooks.

### 3. `data_insights - Copy.ipynb`

- Loads cleaned CSVs and applies further transformation as needed.
- Explores:
  - Salary distributions by role type and skill requirements.
  - Contract frequency (annual, hourly, daily) by group.
  - Posting trends over time, highlighting recent demand for data talent.
- Produces visualizations (matplotlib, seaborn):
  - KDE plots for salary bands.
  - Grouped bar charts for contract type.
  - Histograms for posting year.
- Documented code cells explain what each plot means and how to interpret results.

---

## Key Features

- **Robust Data Cleaning:** Handles missing values, inconsistent text, irrelevant columns, and duplicates.
- **Skill Filtering:** Extracts jobs by business title and by presence of data-related keywords in the skills field using regex.
- **Date Normalization:** Converts multiple date formats to pandas datetime for time-series analysis.
- **Modular Outputs:** Splits the cleaned data into logical groups for focused analysis.
- **Configurable Workflow:** Uses YAML for paths, making the notebooks portable and reusable.

---

## Example Insights

- **Salary Distribution:** Data analyst and engineering roles tend to offer higher starting salaries than general job postings. Roles mentioning modern data skills also skew toward higher pay.
- **Contract Type:** Most data-related roles are annual contracts, with hourly and daily contracts being rare.
- **Trends Over Time:** Demand for data-centric jobs is increasing, with a larger proportion of postings appearing in recent years.

---

## How to Use

1. **Configure file paths:** Update `config.yaml` as needed for input/output CSVs.
2. **Run `data_wrangling.ipynb`:** This notebook processes raw data into analysis-ready CSVs.
3. **Run `data_insights - Copy.ipynb`:** Generates summary tables and visualizations for further insights.
4. **Customize filtering:** Adjust regex patterns or column lists in the notebooks/scripts to target different roles or skills.

---

## Files Included

- `data_wrangling.ipynb` — Main notebook for data cleaning and preparation.
- `functions.py` — Library of custom preprocessing functions.
- `data_insights - Copy.ipynb` — Notebook for data exploration and visualization.
- **CSV Outputs:** Grouped/cleaned datasets for further analysis (paths managed via YAML).
- **YAML config:** Dynamic file management for all steps.

---

## Authors
- Janna Julian
- Sina Yazdi
- Luis Pablo Aiello

---

## License

This repository is for educational, analytical, and non-commercial purposes only. Data is derived from publicly available NYC jobs datasets.