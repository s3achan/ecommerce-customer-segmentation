# 🛍️ E-Commerce Customer Analytics & Clustering Project

## 📌 Project Overview

This project analyzes real-world e-commerce transaction data to uncover customer purchasing behavior, revenue patterns, and actionable business insights.

The analysis combines:

- 🧹 Data Cleaning & Preprocessing  
- 📊 Exploratory Data Analysis (EDA)  
- 👥 Cohort Analysis  
- 🎯 Customer Segmentation using K-Means Clustering  
- 📈 Executive-Level Business Insights  

The goal is to transform raw transaction-level data into strategic intelligence that supports marketing optimization, retention strategy, and revenue growth decisions.

---

## 📂 Dataset

**Source:** Public UK-based Online Retail Dataset  

The dataset contains:

- Invoice-level transactions  
- Product descriptions  
- Quantities purchased  
- Unit prices  
- Customer IDs  
- Country information  
- Invoice dates  

---

## 🛠️ Tech Stack

- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- Scikit-learn  
- Jupyter Notebook  

---

## 🔎 Project Workflow

### 1️⃣ Data Cleaning & Preparation

- Removed null `CustomerID` values  
- Filtered out negative quantities (returns)  
- Converted `InvoiceDate` to datetime format  
- Created derived features:
  - `Revenue = Quantity × UnitPrice`
  - Purchase Month
  - Customer-level aggregates  

---

### 2️⃣ Exploratory Data Analysis (EDA)

Key analyses performed:

- Revenue by country  
- Unique customers by geography  
- Monthly revenue trends  
- Top revenue-generating products  
- Customer purchase frequency distribution  

Visualizations include:

- Bar charts  
- Line charts with markers  
- Pie charts  
- Distribution plots  
- Revenue trends over time  

---

### 3️⃣ Cohort Analysis

Cohort analysis was performed to evaluate customer retention patterns:

- Grouped customers by first purchase month  
- Tracked repeat purchase behavior over time  
- Identified churn and retention trends  

This analysis answers:

- Are customers returning?
- How long do customers remain active?
- Which acquisition months generate the highest retention?

---

### 4️⃣ Customer Segmentation (K-Means Clustering)

Customer-level features engineered:

- Total Revenue  
- Purchase Frequency  
- Recency  
- Average Order Value  

Steps:

1. Feature scaling using `StandardScaler`
2. Applied `KMeans` clustering
3. Visualized clusters with centroids
4. Interpreted segment behaviors

#### 🏷️ Segment Naming

Clusters were renamed for business clarity:

- **VIP - High-Value Loyal Customers**
- **Regular- Low-Engagement Occasional Buyers**

Segments were defined based on revenue contribution and engagement levels.

---

## 📊 Key Business Insights

- A small percentage of customers generate a disproportionate share of revenue (Pareto effect).
- The UK dominates overall customer distribution.
- Retention declines after first purchase for certain cohorts.
- High-value customers demonstrate both high purchase frequency and higher average order value.
- Behavioral segmentation enables targeted marketing strategies.

---

## 💼 Business Applications

This analysis can support:

- 🎯 Targeted marketing campaigns  
- 💰 Revenue optimization  
- 📉 Churn reduction strategies  
- 📦 Inventory forecasting  
- 📊 Executive performance dashboards  

---

## 📈 Executive Summary

This project demonstrates how transaction-level data can be transformed into actionable customer intelligence.

By combining structured data engineering, cohort retention analysis, and unsupervised machine learning, the project converts raw e-commerce activity into business-driven insights that support strategic growth decisions.

---

## 🚀 How to Run

1. Clone the repository: https://github.com/s3achan/ecommerce-customer-segmentation
2. Install required libraries: pip install pandas numpy matplotlib seaborn scikit-learn
3. Launch the notebook: jupyter notebook EcommerceDataset.ipynb
4. Run all cells sequentially.

## 🔮 Future Enhancements

- Implement RFM scoring model  
- Compare with DBSCAN clustering  
- Build interactive dashboard (Streamlit / Power BI)  
- Apply anomaly detection for fraud analysis  
- Develop revenue forecasting models  
