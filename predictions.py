import pandas as pd
import json
import time

def load_model():
    print("Loading Trained Data from trained_data.txt...")
    time.sleep(2)
    with open('trained_data.txt') as f:
        data = f.read()
        trained_data = json.loads(data)
    print("Loaded!\n")
    return trained_data

def predict_covid(trained_data):
    features = trained_data.keys() - {"totalYes", "totalNo"}  # Exclude total counts
    user_input = {}
    
    print("Please provide values for the following symptoms:")
    for feature in features:
        value = input(f"{feature}: ").strip().lower()  # Assuming input is case insensitive
        user_input[feature] = value
    
    totalYes = trained_data["totalYes"]
    totalNo = trained_data["totalNo"]
    sum1Yes = (totalYes / (totalYes + totalNo))
    sum2Yes = 1
    for feature, value in user_input.items():
        if value in trained_data[feature]:
            sum1Yes *= (trained_data[feature][value]['yes'] / totalYes)
            sum2Yes *= (trained_data[feature][value]['total'] / (totalYes + totalNo))
    
    probYes = sum1Yes / sum2Yes
    
    sum1No = (totalNo / (totalYes + totalNo))
    sum2No = 1
    for feature, value in user_input.items():
        if value in trained_data[feature]:
            sum1No *= (trained_data[feature][value]['no'] / totalNo)
            sum2No *= (trained_data[feature][value]['total'] / (totalYes + totalNo))
    
    probNo = sum1No / sum2No
    
    if probYes > probNo:
        return "COVID-19 is likely present."
    else:
        return "COVID-19 is likely not present."

trained_data = load_model()
prediction = predict_covid(trained_data)
print("Prediction Result:", prediction)
