# Supply Chain Optimization Using Machine Learning

**Case Study: Kenya Medical Supplies Authority (KEMSA)**

![ML Supply Chain Optimization](https://live.staticflickr.com/1936/44103687154_04281ced4d_b.jpg)

The **Kenya Medical Supplies Authority (KEMSA)** is a pivotal government agency tasked with the procurement, storage, and distribution of medical supplies and pharmaceuticals across public health facilities in Kenya. As a cornerstone of Kenya’s healthcare supply chain, KEMSA ensures the timely and efficient delivery of essential medicines, medical equipment, and health commodities, playing a crucial role in maintaining healthcare integrity and readiness across the country.

Faced with extensive geographical coverage and high demand, KEMSA’s supply chain encounters various challenges, including fluctuating demand, logistical inefficiencies, and risks of stock imbalances. This project aims to leverage advanced data-driven techniques and machine learning to enhance these processes, striving for more efficient distribution, reduced waste, and improved healthcare outcomes.

---

## Project Overview

![KEMSA Supply Chain](./images/KEMSA_Supply_Chain_DFD.png)

This project focuses on optimizing supply chain operations at **Kenya Medical Supplies Authority (KEMSA)** through machine learning methodologies. The goal is to forecast medical supply demands using historical data, thereby improving distribution efficiency, minimizing waste, and ensuring optimal medical supply availability across various regions.

### Key Objectives

- **Predictive Analytics**: Develop machine learning models to forecast medical supply requirements by region, utilizing historical consumption and distribution data.
- **Delivery Insights**: Generate insights on delivery timings and optimal restocking schedules to streamline logistics and minimize delays.
- **Stock Optimization**: Enhance stock management by predicting demand accurately, reducing both overstock and understock scenarios, and ensuring timely restocking of essential supplies.

### Features

- **Demand Forecasting**: Utilize machine learning algorithms to predict medical supply demand for different regions.
- **Supply Chain Insights**: Analyze delivery metrics and recommend strategies to optimize stock replenishment and reduce logistical delays.
- **Data-Driven Decisions**: Employ historical data to inform strategic decisions regarding medical supply distribution.

## Tech Layout: Prerequisites

- **Python**: The primary programming language for data processing and machine learning tasks.
- **Scikit-learn**: For developing and evaluating predictive models.
- **TensorFlow/Keras**: Optional libraries for creating advanced deep learning models for complex data patterns.
- **Pandas & NumPy**: Essential libraries for data manipulation and analysis.
- **Matplotlib/Seaborn**: For creating visualizations and reports.

> All required libraries are listed in the `requirements.txt` file (refer to the Installation section for setup).

## Project Structure

1. **Data Collection & Preparation**: Acquire historical data on medical supply distribution, demand patterns, and regional variables.
2. **Data Cleaning & Exploration**: Clean and analyze the dataset to prepare it for modeling.
3. **Model Development**: Construct machine learning models to forecast supply demands.
4. **Model Evaluation**: Assess model performance to ensure accuracy and reliability.
5. **Insights & Optimization**: Produce reports and visualizations for actionable insights into stock management and delivery improvements.
6. **Deployment**: Package the model for practical deployment and integration.

## Usage

To utilize this project, follow these steps to set up the environment and execute the models.

### Installation

1. Clone this repo:
   ```bash
   git clone https://github.com/your-username/KEMSA-SupplyChain-Optimization.git
   ```
2. Navigate to the project directory:

   ```bash
   cd KEMSA-SupplyChain-Optimization
   ```

3. Install the required Python libraries:

   ```bash
   pip install -r requirements.txt
   ```

---

<i>DFD generation (Optional)</i>:

```bash
py dfdGen.py
```

Output will be saved in the images section unless defined otherwise

```python
...
if not os.path.exists('images'):
   os.makedirs('images')
...
dfd.render('images/KEMSA_Supply_Chain_DFD', format='png', cleanup=False)
```

<i>CSV Data Sample Used</i>

```csv
Region,Month,Supply_Category,Demand_Quantity,Delivery_Time_Days,Stock_Level,Restock_Flag
Nairobi,January,Medicine,120,5,300,0
Baringo,February,Medicine,140,4,250,0
```

## Headers:

1. Region - Geographic area for distribution. Includes major regions like Nairobi, Mombasa, Kisumu, Eldoret, and Nakuru.
2. Month - Month of data recording, covering January through December to track seasonal variations.
3. Supply_Category - The type of medical supply being tracked. Categories include:
   - Medicine: General medication needed in healthcare facilities.
   - PPE: Personal protective equipment such as gloves, masks, etc.
   - Surgical Equipment: Specialized medical tools and equipment used in surgeries.

- Different categories have unique demand patterns and logistical requirements.

4. Demand_Quantity - Quantity of supplies required.
5. Restock_Flag - A binary indicator (0 or 1) used to signal whether restocking is needed:
   0: No restock required (stock level is sufficient for the near future).
   1: Restocking is required due to low stock levels o increased demand.
6. Delivery_Time_Days - The number of days taken for the supplies to be delivered to the healthcare facilities. Delivery times can vary due to logistics, road conditions, or inventory issues, and can range from 2 to 7 days in this dataset.
7. Stock_Level - The number of items left in stock after the demand has been met for that region and month. This helps in tracking stock consumption and is critical for understanding when restocking is needed. A higher stock level means the region has enough supplies, while a lower stock level indicates potential shortages.

---

### Model Evaluation Metrics

```bash
Model Accuracy: 100.00%

Confusion Matrix:
[[ 6  0]
 [ 0 14]]

Classification Report:
              precision    recall  f1-score   support

         0.0       1.00      1.00      1.00         6
         1.0       1.00      1.00      1.00        14

    accuracy                           1.00        20
   macro avg       1.00      1.00      1.00        20
weighted avg       1.00      1.00      1.00        20
```

![Confusion matrix](./images/reports/confusion_matrix.png)

![Feature importance](./images/reports/Featyre%20Importance.png)

---

DISCLAIMER!

> This project is built for educational purposes and may require further modifications before being used in real-world scenarios.
