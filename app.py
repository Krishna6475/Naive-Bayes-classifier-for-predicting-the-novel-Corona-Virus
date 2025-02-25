import streamlit as st
import json
import time

# Set Streamlit page config
st.set_page_config(page_title="COVID-19 Predictor", page_icon="🦠", layout="wide")

# Function to load trained data
@st.cache_data
def load_model():
    with st.spinner("🔄 Loading Trained Data... Please wait!"):
        time.sleep(2)  # Simulating loading delay
        with open('trained_data.txt') as f:
            data = f.read()
            trained_data = json.loads(data)
    return trained_data

# Function to make predictions
def predict_covid(trained_data, user_input):
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
    
    confidence = max(probYes, probNo) * 100  # Confidence in percentage
    
    if probYes > probNo:
        return "🟥 High Risk of COVID-19", confidence
    else:
        return "🟩 Low Risk of COVID-19", confidence

# Load trained model
trained_data = load_model()

# Streamlit UI Layout
st.title("🦠 COVID-19 Prediction System")
st.write("🔍 Enter symptoms below to predict the likelihood of COVID-19.")

# Sidebar for user inputs
st.sidebar.header("📝 Enter Symptoms")

features = trained_data.keys() - {"totalYes", "totalNo"}  # Exclude total counts
user_input = {}

for feature in features:
    user_input[feature] = st.sidebar.radio(f"{feature}:", ["yes", "no"], horizontal=True)

# Predict Button
if st.sidebar.button("🚀 Predict"):
    with st.spinner("🤖 Analyzing Symptoms... Please wait!"):
        time.sleep(2)  # Simulating processing delay
        prediction, confidence = predict_covid(trained_data, user_input)

    # Display Results
    st.subheader("🧪 Prediction Result:")
    st.success(prediction)
    
    # Confidence Bar
    st.progress(int(confidence))  # Dynamic confidence progress bar
    st.write(f"🛡️ Confidence Level: **{confidence:.2f}%**")

    # Explanation
    st.info("📝 This result is based on a probabilistic analysis of the provided symptoms. "
            "For a professional diagnosis, please consult a medical expert.")

# Footer
st.markdown("---")
st.markdown("🔬 *This tool is for educational purposes only and should not replace medical advice.*")

