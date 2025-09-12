## Project Overview
This project scrapes LinkedIn job postings related to **Data Science** and performs data cleaning, analysis, and visualization to extract insights about the job market, salaries, skills, and trends.

**Key Objectives:**
- Collect Data Science job listings from LinkedIn.
- Clean and preprocess the data for analysis.
- Analyze salary ranges, skill requirements, and experience trends.
- Visualize patterns and insights to support decision-making for job seekers.


## Features

### Web Scraping
- Dynamically extracts:
  - Job Title
  - Company
  - Location
  - Salary
  - Experience Level
  - Description (contains Required Skills)
- Uses `requests` and `Selenium` for dynamic scraping.

### Data Cleaning
- Uses `pandas` and `re` for processing and cleaning.

### Data Analysis
- Identifies most in-demand skills.
- Salary distribution and ranges.
- Trends over time.
- Required experience analysis.

### Visualization
- Graphs and charts using `Matplotlib` and `Seaborn`.



## Tech Used
- Libraries:
  - `requests`, `Selenium` – web scraping
  - `pandas` – data processing
  - `matplotlib`, `seaborn` – data visualization
  - `re` – text cleaning
