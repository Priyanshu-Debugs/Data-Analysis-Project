# 📊 Data Analysis Projects

A comprehensive collection of data analysis projects featuring interactive dashboards, insightful visualizations, and business intelligence metrics.

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Charts-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![Dash](https://img.shields.io/badge/Dash-Dashboard-00D4AA?style=for-the-badge&logo=plotly&logoColor=white)

---

## 🗂️ Project Structure

```
Data-Analysis-Project/
├── Bank-Loan-Analysis/          # Bank loan performance analysis
│   ├── bank_loan_analysis.ipynb
│   ├── financial_loan.xlsx
│   └── README.md
├── Blinkit-Sales-Analysis/      # Blinkit grocery sales analysis
│   ├── data_analysis_blinkit.ipynb
│   ├── blinkit_data.csv
│   └── README.md
├── Dashboard/                    # Interactive Power BI-style dashboard
│   ├── app.py
│   ├── requirements.txt
│   └── README.md
└── README.md                     # This file
```

---

## 🏦 Bank Loan Analysis

Comprehensive analysis of bank loan data to identify trends, assess loan performance, and derive actionable business insights.

### Key Metrics (KPIs)
| Metric | Description |
|--------|-------------|
| Total Loan Applications | Count of all loan applications |
| Total Funded Amount | Sum of all disbursed loan amounts |
| Total Amount Received | Sum of all payments received |
| Average Interest Rate | Mean interest rate across loans |
| Average DTI Ratio | Mean Debt-to-Income ratio |
| Good Loan % | Percentage of Fully Paid + Current loans |
| Bad Loan % | Percentage of Charged Off loans |

### Visualizations
- 📈 Monthly Trends (Funded Amount, Received Amount, Applications)
- 🗺️ Regional Analysis by State
- 🍩 Loan Term Distribution (36 vs 60 months)
- 📊 Loan Purpose Breakdown
- 👔 Employment Length Analysis
- 🏠 Home Ownership Treemap

---

## 🛒 Blinkit Sales Analysis

In-depth analysis of Blinkit (grocery delivery) sales data to understand sales patterns, outlet performance, and product insights.

### Key Metrics (KPIs)
| Metric | Description |
|--------|-------------|
| Total Sales | Sum of all sales revenue |
| Average Sales | Mean sales per transaction |
| Number of Items Sold | Total count of items |
| Average Rating | Mean customer rating |

### Visualizations
- 🥧 Sales by Fat Content (Low Fat vs Regular)
- 📊 Sales by Item Type (16 categories)
- 📍 Fat Content by Outlet Location Tier
- 📅 Sales by Outlet Establishment Year
- 📐 Sales by Outlet Size
- 🏪 Sales by Outlet Type & Location

---

## 🖥️ Interactive Dashboard

A **Power BI-style dynamic dashboard** built with Python that combines both analyses into an interactive web application.

### Features
- ✨ **Real-time filtering** - All charts update instantly
- 📈 **Interactive charts** - Hover, zoom, pan, export
- 🌙 **Modern dark theme** - Professional appearance
- 🔄 **Cross-filtering** - Multiple filters work together
- 📱 **Responsive design** - Works on various screen sizes

### Tech Stack
| Technology | Purpose |
|------------|---------|
| Dash | Web framework for dashboards |
| Plotly | Interactive charting library |
| Dash Bootstrap Components | UI components |
| Pandas | Data manipulation |
| NumPy | Numerical computing |

### Quick Start
```bash
# Navigate to Dashboard folder
cd Dashboard

# Install dependencies
pip install -r requirements.txt

# Run the dashboard
python app.py

# Open in browser
# http://127.0.0.1:8050
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.11 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Priyanshu-Debugs/Data-Analysis-Project.git
   cd Data-Analysis-Project
   ```

2. **Install dependencies**
   ```bash
   pip install pandas numpy matplotlib seaborn plotly openpyxl dash dash-bootstrap-components
   ```

3. **Run Jupyter Notebooks** (for individual analysis)
   ```bash
   jupyter notebook
   ```

4. **Run Interactive Dashboard**
   ```bash
   cd Dashboard
   python app.py
   ```

---

## 📊 Dashboard Screenshots

### Bank Loan Analysis Dashboard
- KPI cards showing key metrics
- Monthly trend area charts
- Loan status donut chart
- State-wise funding analysis
- Purpose breakdown horizontal bars
- Term distribution & employment analysis

### Blinkit Sales Dashboard
- Sales KPI cards
- Item type sales bar chart
- Fat content pie chart
- Year-wise sales trend line
- Outlet analysis charts
- Location tier comparisons

---

## 🛠️ Technologies Used

| Category | Technologies |
|----------|--------------|
| **Languages** | Python |
| **Data Analysis** | Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn, Plotly |
| **Dashboard** | Dash, Dash Bootstrap Components |
| **Data Sources** | Excel (.xlsx), CSV |
| **IDE** | Jupyter Notebook, VS Code |

---

## 📁 Data Sources

| Project | File | Records | Columns |
|---------|------|---------|---------|
| Bank Loan | `financial_loan.xlsx` | 38K+ | 24 |
| Blinkit | `blinkit_data.csv` | 8.5K+ | 12 |

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 👤 Author

**Priyanshu**
- GitHub: [@Priyanshu-Debugs](https://github.com/Priyanshu-Debugs)
