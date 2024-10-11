import tkinter as tk
from tkinter import messagebox
import numpy as np
import joblib


model = joblib.load('logistic_model.pkl')
scaler = joblib.load('scaler.pkl')

def predict_merchandise(features):
    scaled_features = scaler.transform(features)
    return model.predict(scaled_features)

def make_prediction():
    try:

        feature_values = [float(entry.get()) for entry in entries]
        feature_array = np.array(feature_values).reshape(1, -1)

        print("Feature Array:", feature_array)

        prediction = predict_merchandise(feature_array)

        if prediction[0] == 1:
            messagebox.showinfo("Prediction Result", "Merchandise Purchases will be >= 2.")
        else:
            messagebox.showinfo("Prediction Result", "Merchandise Purchases will be < 2.")
    except ValueError as e:
        messagebox.showerror("Input Error", "Please enter valid numbers for all features.")
        print(e)

root = tk.Tk()
root.title("Merchandise Purchases Predictor")

feature_names = [
    'Fan Challenges Completed',
    'Predictive Accuracy (%)',
    'Sponsorship Interactions (Ad Clicks)',
    'Time on Live 360 (mins)',
    'Real-Time Chat Activity (Messages Sent)'
]

entries = []

# Create labels and entry fields for each feature
for feature in feature_names:
    label = tk.Label(root, text=f"Enter {feature}:")
    label.pack()
    entry = tk.Entry(root)
    entry.pack()
    entries.append(entry)

# Create a predict button
predict_button = tk.Button(root, text="Predict", command=make_prediction)
predict_button.pack()

# Start the GUI event loop
root.mainloop()
