# Building Energy Consumption 

This project uses real-world-style energy usage data from a building to determine which 
features most strongly influence electricity consumption. Several regression-based 
machine learning models were applied and compared for predictive performance.

## Features used
- Temperature
- Humidity
- SquareFootage
- Occupancy
- RenewableEnergy
- HVAC_On (binary)
- Lighting_On (binary)

## Models evaluated
- Linear Regression
- Ridge
- Lasso
- Decision Tree (various depths)
- Random Forest

## Key Findings
- Ridge Regression performed best: R² ≈ 0.588
- Temperature is the most influential feature
- SquareFootage and HVAC_On also contribute meaningfully
- Decision Trees showed overfitting at higher depths

## Repository Contents
- `energy_analysis.ipynb`  — full Python & ML workflow
- `Energy_consumption.csv` — data used 
- `plots/` — visualizations & graphs

This project is part of a real-world analysis coursework for understanding and modeling energy dynamics in buildings using data-driven machine learning techniques.
