# Student Performance Dashboard - README

## 📊 Overview
This interactive dashboard visualizes student performance data across math, reading, and writing scores, with breakdowns by gender, parental education level, and test preparation status.

## ✨ Features
- **Score Distributions**: Histograms for math, reading, and writing scores
- **Gender Analysis**: Comparison of average scores and gender distribution
- **Parental Education**: Counts by education level and score distributions
- **Test Preparation**: Impact on scores across subjects
- **Correlation Analysis**: Heatmap of score relationships
- **Interactive Visuals**: Math vs reading scatter plot and race/ethnicity distribution

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- Required packages:
  ```bash
  pip install dash pandas plotly
  ```

### Installation
1. Clone/download the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the App
```bash
python student.py
```
Access at: http://127.0.0.1:8050/

## 📋 Data Source
The dashboard uses the "StudentsPerformance.csv" dataset containing:
- Math, reading, and writing scores
- Gender information
- Parental education levels
- Test preparation status
- Race/ethnicity categories

## 🛠 Technical Details
- Built with Python Dash framework
- Uses Plotly Express for interactive visualizations
- Responsive layout with flexbox
- Clean data processing pipeline

## 📊 Visualization Types
1. **Histograms**: Score distributions
2. **Bar Charts**: Average scores by category
3. **Pie Chart**: Gender distribution
4. **Box Plots**: Score distributions by factors
5. **Heatmap**: Score correlations
6. **Scatter Plot**: Math vs reading scores

## 📜 License
MIT License
