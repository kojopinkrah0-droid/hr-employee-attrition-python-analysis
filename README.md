# HR Employee Attrition Analysis with Python

A portfolio-ready exploratory data analysis project examining employee attrition, workforce characteristics, job roles, compensation, overtime, and tenure using Python.

## Project Overview

The dataset contains **1,470 employee records** and **37 original variables**. The objective is to identify workforce patterns associated with employee attrition and present the findings in a clear, reproducible Python analysis.

## Key KPIs

| Metric | Result |
|---|---:|
| Employees | 1,470 |
| Employees who left | 237 |
| Overall attrition rate | 16.1% |
| Average age | 36.9 years |
| Average monthly income | 6,503 |
| Missing values in original dataset | 0 |

## Key Findings

- Overall attrition is **16.1%** (237 of 1470 employees).
- **Sales** has the highest department-level attrition rate at **20.6%**.
- **Sales Representative** has the highest job-role attrition rate at **39.8%**.
- Employees working overtime have an attrition rate of **30.5%**, compared with **10.4%** among employees who do not work overtime.
- The **18–25** age group records the highest age-band attrition rate at **35.8%**.
- Employees in the lowest monthly-income quartile have an attrition rate of **29.3%**, compared with **10.3%** in the highest quartile.
- These are descriptive associations, not proof that any single factor causes attrition.

## Visual Analysis

### Attrition Distribution
![Attrition Distribution](assets/attrition_distribution.png)

### Attrition by Department
![Attrition by Department](assets/attrition_by_department.png)

### Attrition by Job Role
![Attrition by Job Role](assets/attrition_by_job_role.png)

### Overtime and Attrition
![Overtime and Attrition](assets/attrition_by_overtime.png)

### Attrition by Age Group
![Attrition by Age Group](assets/attrition_by_age_group.png)

### Attrition by Income Quartile
![Attrition by Income Quartile](assets/attrition_by_income_quartile.png)

### Numeric Associations with Attrition
![Attrition Correlations](assets/attrition_correlations.png)

## Repository Structure

```text
hr-employee-attrition-python-analysis/
├── README.md
├── analysis.py
├── requirements.txt
├── LICENSE
├── .gitignore
├── data/
│   └── hr_attrition_cleaned.csv
└── assets/
    ├── attrition_distribution.png
    ├── attrition_by_department.png
    ├── attrition_by_job_role.png
    ├── attrition_by_overtime.png
    ├── attrition_by_age_group.png
    ├── attrition_by_income_quartile.png
    ├── attrition_correlations.png
    ├── department_summary.csv
    ├── job_role_summary.csv
    └── overtime_summary.csv
```

## Tools Used

- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter (optional for further exploration)

## How to Run

```bash
pip install -r requirements.txt
python analysis.py
```

## Business Interpretation

The analysis suggests that retention initiatives can be investigated around overtime exposure, selected job roles, younger employees, and lower-income groups. Before taking HR action, these patterns should be validated with employee feedback, organizational context, and appropriate statistical or predictive analysis.

## Dataset

IBM HR Analytics Employee Attrition & Performance sample dataset. The cleaned copy used by this project is included in the `data` folder for reproducibility.

## Portfolio Skills Demonstrated

Data cleaning, exploratory data analysis, KPI development, group-based attrition analysis, feature comparison, data visualization, business interpretation, and reproducible Python project organization.
