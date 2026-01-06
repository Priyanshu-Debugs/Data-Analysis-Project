# 📊 Dynamic Analytics Dashboard

A **Power BI-style interactive dashboard** built with Python, Dash, and Plotly for visualizing the Bank Loan Analysis and Blinkit Sales Analysis projects.

## ✨ Features

### 🏦 Bank Loan Analysis Dashboard
- **KPI Cards**: Total Applications, Funded Amount, Received Amount, Interest Rate, Good/Bad Loan %
- **Interactive Charts**:
  - Monthly Funded Amount Trend (Area Chart)
  - Loan Status Distribution (Donut Chart)
  - Funded Amount by State (Horizontal Bar)
  - Loan Purpose Breakdown
  - Term Distribution (Donut)
  - Employment Length Analysis
  - Home Ownership (Treemap)
- **Dynamic Filters**: State, Purpose, Term, Home Ownership

### 🛒 Blinkit Sales Dashboard
- **KPI Cards**: Total Sales, Average Sales, Items Sold, Average Rating
- **Interactive Charts**:
  - Sales by Item Type
  - Fat Content Distribution (Donut)
  - Sales by Establishment Year (Line)
  - Fat Content by Outlet Location (Grouped Bar)
  - Outlet Size Distribution (Donut)
  - Sales by Outlet Type
  - Sales by Location Tier
- **Dynamic Filters**: Location, Size, Item Type, Fat Content

## 🚀 Quick Start

### 1. Install Dependencies
```bash
cd Dashboard
pip install -r requirements.txt
```

### 2. Run the Dashboard
```bash
python app.py
```

### 3. Open in Browser
Navigate to: **http://127.0.0.1:8050**

## 📁 Project Structure
```
Dashboard/
├── app.py              # Main dashboard application
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## 🎨 Dashboard Features

| Feature | Description |
|---------|-------------|
| 🎯 **Dynamic Filtering** | All charts update in real-time based on filter selections |
| 📈 **Interactive Charts** | Hover for details, zoom, pan, and export |
| 🌙 **Dark Theme** | Modern dark theme for better visualization |
| 📱 **Responsive** | Works on desktop and tablet screens |
| 🔄 **Cross-filtering** | Multiple filters work together |

## 🛠️ Technologies Used

- **Dash** - Python web framework for analytics
- **Plotly** - Interactive charting library
- **Dash Bootstrap Components** - UI components
- **Pandas** - Data manipulation
- **NumPy** - Numerical operations

## 📸 Screenshots

The dashboard provides a modern, Power BI-like experience with:
- Navigation bar to switch between dashboards
- KPI cards with icons and values
- Multiple chart types (Area, Bar, Pie, Donut, Treemap, Line)
- Dropdown filters for data exploration

---

**Built with ❤️ for Data Analysis**
