# ⚽ Botola Data Engineering & Analytics Pipeline

## 📌 Project Overview

This project showcases an end-to-end data pipeline for football analytics, combining **Data Engineering and Data Analysis** in a real-world use case.

From raw match data to business insights, the pipeline automates data ingestion, transformation, storage, and visualization.

---

## 🏗️ Architecture

API → Python Scripts → Apache Airflow → PostgreSQL → Power BI Dashboard

---

## ⚙️ Tech Stack

- **Python** (Pandas, Requests)
- **Apache Airflow** (workflow orchestration)
- **PostgreSQL** (data storage)
- **Docker** (containerization)
- **Power BI** (data visualization)

---

## 🚀 Pipeline Workflow

### 1. Data Extraction
- Fetch football data using API-Football  
- Collect standings, fixtures, and top scorers  

### 2. Data Transformation
- Clean and preprocess datasets  
- Compute key metrics:
  - Goal difference  
  - Win rate  
  - Player contributions  

### 3. Data Loading
- Store structured data into PostgreSQL  

### 4. Orchestration
- Automate pipeline execution using Airflow DAGs  

### 5. Visualization
- Build an interactive Power BI dashboard  

---

## 📊 Dashboard Features

- League overview (total matches, average goals)  
- Team performance analysis (win rate vs goal difference)  
- Top scorers and player contributions  
- Interactive filtering and insights  

---

## 📸 Dashboard Preview

<img width="587" height="332" alt="image" src="https://github.com/user-attachments/assets/567966a3-e6e4-40b8-85af-fe32fac5baf0" />


---

## 💡 Key Insights

- Renaissance Berkane is the top-performing team in the league  
- Strong correlation between win rate and goal difference  
- Player contributions (goals + assists) significantly impact team performance  

---

## 📁 Project Structure
