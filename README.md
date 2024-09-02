# Supply Chain Optimization using Machine Learning

Case Study: **KEMSA**

![ML supply chain optimization](https://live.staticflickr.com/1936/44103687154_04281ced4d_b.jpg)

The **Kenya Medical Supplies Authority (KEMSA)** is a specialized government agency responsible for procuring, storing, and distributing medical supplies and pharmaceuticals to public health facilities across Kenya. As the backbone of Kenya’s healthcare supply chain, KEMSA ensures that essential medicines, medical equipment, and health commodities reach every corner of the country efficiently and in a timely manner. The organization plays a critical role in maintaining the integrity of the healthcare supply chain, from managing complex logistics networks to ensuring the availability of critical health supplies during emergencies.

Given the vast geographical coverage and the high demand for medical supplies, KEMSA’s supply chain faces numerous challenges, including fluctuating demand, logistical delays, and the risk of overstocking or understocking in regional facilities. By leveraging data-driven approaches and modern technology like machine learning, there is significant potential to optimize these processes, leading to more efficient distribution, minimized waste, and improved healthcare outcomes.

---

## Project Overview

![KEMSA supply chain](images\KEMSA_Supply_Chain_DFD.png)

This project aims to optimize the supply chain operations at the **Kenya Medical Supplies Authority (KEMSA)** by leveraging machine learning techniques. The system will predict medical supply demands based on historical data, with the ultimate goal of reducing waste, improving delivery efficiency, and ensuring optimal distribution of medical supplies across various regions.

## Key Objectives

- **Predictive Analytics**: Develop a machine learning model to forecast medical supply needs for different regions in Kenya, based on historical consumption and distribution patterns.
- **Delivery Insights**: Provide insights into delivery times and optimal replenishment schedules, helping to streamline logistics and reduce delays.
- **Stock Optimization**: Enhance stock management by predicting demand, reducing overstock or understock scenarios, and ensuring timely replenishment of essential medical supplies.

## Features

- **Demand Forecasting**: Predict medical supply demand by region using machine learning algorithms.
- **Supply Chain Insights**: Analyze delivery times and provide recommendations to improve stock replenishment and reduce logistical delays.
- **Data-Driven Decisions**: Leverage historical data to make informed decisions regarding the distribution of medical supplies.

## Tech Layout: Prerequisitess

- **Python**: The core language for data processing and machine learning.
- **Scikit-learn**: For building and evaluating predictive models.
- **TensorFlow/Keras**: For developing deep learning models, if necessary, for complex data patterns.
- **Pandas & NumPy**: For data manipulation and analysis.
- **Matplotlib/Seaborn**: For data visualization and reporting.

> All required libraries will be available under `requirements.txt` file(refer to usage section) as the projects progresses.

## Project Structure

1. **Data Collection & Preparation**: Gather historical data on medical supply distribution, demand patterns, and regional factors.
2. **Data Cleaning & Exploration**: Clean and explore the dataset to gain insights and ensure it’s ready for modeling.
3. **Model Development**: Build predictive models using machine learning to forecast supply demands.
4. **Model Evaluation**: Test and evaluate model performance to ensure accurate predictions.
5. **Insights & Optimization**: Generate reports and visualizations to provide actionable insights for stock replenishment and delivery improvements.
6. **Deployment**: Package the model for deployment and integration.

## Usage

To use this project, follow the instructions for setting up the environment and running the models.

## Installation

1. Clone this repository:
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

<i>DFD generation (Not a must for the project)</i>:

```bash
py dfdGen.py
```

Output will be saved in the images section unless destination is altered to a different location

```python
...
if not os.path.exists('images'):
   os.makedirs('images')
...
dfd.render('images/KEMSA_Supply_Chain_DFD', format='png', cleanup=False)
```

---

---

DISCLAIMER!

> This project is built for educational purposes and may require further modifications before being used in real-world scenarios..
