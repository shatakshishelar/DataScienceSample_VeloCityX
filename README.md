# Merchandise Sales Prediction Project

This repository contains a data analysis and prediction project aimed at forecasting merchandise sales based on user activity data during race events. The project explores different machine learning models and includes visualizations to understand the relationships between features. Additionally, a GUI application allows users to interact with the model and get predictions based on their input.

## Project Structure

The project is divided into two main parts:

### 1. Model Exploration and Visualization
- **File:** `sample.ipynb`
- This file contains code for exploring and evaluating different machine learning models to find the best fit for predicting merchandise sales.
- It includes:
  - Data preprocessing and feature engineering.
  - Implementation of various models to determine the one that gives the most accurate predictions.
  - Visualizations to analyze how different user activities correlate with merchandise sales and sponsorship interactions.

### 2. GUI for Merchandise Prediction
- **File:** `predictionGUI.py`
- This file contains a graphical user interface (GUI) built using `tkinter`.
- The GUI allows users to enter specific details about user activities, such as:
  - Fan Challenges Completed
  - Predictive Accuracy (%)
  - Sponsorship Interactions (Ad Clicks)
  - Time on Live 360 (mins)
  - Real-Time Chat Activity (Messages Sent)
- Based on the input data, the GUI uses a Logistic Regression model to predict whether the number of merchandise purchases will be greater than or less than a certain threshold.
- The prediction result is displayed on the screen, providing instant feedback to the user.

## Getting Started

### Prerequisites
- Python 3.x
- Required Python libraries:
  - `numpy`
  - `pandas`
  - `scikit-learn`
  - `matplotlib` (for visualizations)
  - `tkinter` (pre-installed with Python)
  
### Installation
To install the required libraries, use the following command:
```bash
pip install numpy pandas scikit-learn matplotlib
```

### How to Run

1. **Model Exploration and Visualization:**
   - Run the `model_exploration_and_visualization.py` file to explore different models and visualize the relationships between features.
   - The visualizations will help you understand how user activities correlate with merchandise sales.

2. **GUI for Merchandise Prediction:**
   - Open and run the `gui_merchandise_prediction.py` file.
   - Enter the relevant user activity data into the input fields on the GUI.
   - Click the "Predict" button to get a prediction about the number of merchandise purchases.

## Usage

- This project is designed to help identify user activities that most strongly correlate with merchandise sales during events.
- The GUI interface allows non-technical users to easily input data and get predictions on merchandise sales.

## Future Improvements
- Expand the dataset to include more user activity features.
- Optimize the logistic regression model or try different algorithms to improve prediction accuracy.
- Enhance the GUI to include more interactive features and data visualization capabilities.

## License
This project is licensed under the MIT License.

## Contact
For any questions or suggestions, please feel free to contact me.
