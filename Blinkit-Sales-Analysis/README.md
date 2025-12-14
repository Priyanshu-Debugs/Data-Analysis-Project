# Blinkit Sales Analysis 📊

A comprehensive data analysis project examining sales patterns, customer preferences, and business insights from Blinkit's grocery delivery operations.

## 📋 Project Overview

This project analyzes Blinkit's sales data to uncover key insights about product performance, outlet characteristics, customer ratings, and sales trends. The analysis helps understand factors influencing sales and provides actionable recommendations for business optimization.

## 🗂️ Dataset Information

The dataset contains **8,523 records** with the following attributes: 

- **Item Fat Content**: Product fat content category (Low Fat, Regular, etc.)
- **Item Identifier**: Unique product ID
- **Item Type**: Product category (Fruits and Vegetables, Snack Foods, Household, etc.)
- **Outlet Establishment Year**: Year the outlet was established
- **Outlet Identifier**: Unique outlet ID
- **Outlet Location Type**:  Outlet tier classification (Tier 1, 2, 3)
- **Outlet Size**: Size of the outlet (Small, Medium, High)
- **Outlet Type**: Type of outlet (Supermarket Type1/2/3, Grocery Store)
- **Item Visibility**: Product visibility percentage in the outlet
- **Item Weight**: Weight of the product
- **Sales**: Product sales amount
- **Rating**: Customer rating (1-5 scale)

## 🎯 Key Analysis Areas

### 1. **Sales Performance Analysis**
- Total sales across different outlet types
- Sales distribution by product categories
- Year-over-year sales trends

### 2. **Product Analysis**
- Top-performing product categories
- Fat content preference analysis
- Item visibility impact on sales

### 3. **Outlet Analysis**
- Performance comparison across outlet sizes
- Location tier impact on sales
- Outlet age vs. sales correlation

### 4. **Customer Insights**
- Rating distribution analysis
- Product preferences by outlet type
- Customer satisfaction metrics

## 🛠️ Technologies Used

- **Python 3.x**
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computations
- **Matplotlib** - Data visualization
- **Seaborn** - Statistical visualizations
- **Jupyter Notebook** - Interactive analysis environment

## 📂 Project Structure

```
Blinkit-Sales-Analysis/
│
├── blinkit_data. csv              # Dataset file
├── data_analysis_blinkit.ipynb   # Jupyter notebook with analysis
└── README.md                      # Project documentation
```

## 🚀 Getting Started

### Prerequisites

```bash
pip install pandas numpy matplotlib seaborn jupyter
```

### Running the Analysis

1. Clone the repository:
```bash
git clone https://github.com/Priyanshu-Debugs/Data-Analysis-Project.git
```

2. Navigate to the project directory:
```bash
cd Data-Analysis-Project/Blinkit-Sales-Analysis
```

3. Open the Jupyter notebook:
```bash
jupyter notebook data_analysis_blinkit.ipynb
```

## 📊 Key Findings

### Product Categories
- **16 distinct product categories** including: 
  - Fruits and Vegetables
  - Snack Foods
  - Household items
  - Dairy products
  - Frozen Foods
  - Health and Hygiene products

### Outlet Distribution
- **Tier 3 locations**:  Highest number of outlets
- **Tier 2 locations**: Medium coverage
- **Tier 1 locations**: Premium locations with specific characteristics

### Outlet Types
- Supermarket Type1 (Most common)
- Supermarket Type2
- Supermarket Type3
- Grocery Store (Smaller format)

### Ratings
- Average customer rating: **4.5-5.0** across most products
- High customer satisfaction across all outlet types

## 💡 Business Insights

1. **Location Strategy**:  Tier 3 locations show significant market presence
2. **Product Mix**:  Diverse product portfolio across 16+ categories
3. **Outlet Performance**: Medium-sized outlets appear frequently in the dataset
4. **Customer Satisfaction**:  Consistently high ratings indicate good service quality

## 📈 Visualizations

The analysis includes various visualizations:
- Sales distribution charts
- Product category performance
- Outlet type comparisons
- Rating distributions
- Temporal trends (2000-2022)

## 🔍 Future Enhancements

- [ ] Predictive modeling for sales forecasting
- [ ] Customer segmentation analysis
- [ ] Seasonal trend analysis
- [ ] Price optimization recommendations
- [ ] Interactive dashboard development

## 👤 Author

**Priyanshu**
- GitHub: [@Priyanshu-Debugs](https://github.com/Priyanshu-Debugs)

## 📄 License

This project is open source and available for educational purposes.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  Feel free to check the issues page. 

---

**Note**: This analysis is based on sample data for educational and analytical purposes. 
