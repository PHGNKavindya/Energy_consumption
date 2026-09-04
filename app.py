import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("ridge_energy_model.pkl")

st.set_page_config(
    page_title="Energy Consumption Prediction",
    page_icon="⚡",
    layout="wide"
)

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

h1 {
    text-align: center;
    margin-bottom: 0.2rem;
}

.subtitle {
    text-align: center;
    color: #9ca3af;
    font-size: 1rem;
    margin-bottom: 1.2rem;
}

.section-title {
    font-size: 1.3rem;
    font-weight: 600;
    margin-bottom: 0.5rem;
}

.prediction-box {
    padding: 15px;
    border-radius: 10px;
    border: 1px solid #444;
    text-align: center;
}

.prediction-value {
    font-size: 2.3rem;
    font-weight: 700;
}

.metric-box {
    padding: 10px;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)


# Header
st.markdown(
    "<h1>⚡ Energy Consumption Prediction</h1>",
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Predict building energy consumption using a trained Ridge Regression model.'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# Building Information
st.markdown(
    '<div class="section-title">🏢 Building Information</div>',
    unsafe_allow_html=True
)

# Row 1
col1, col2, col3, col4 = st.columns(4)

with col1:
    temperature = st.number_input(
        "🌡 Temperature",
        value=25.0
    )

with col2:
    humidity = st.number_input(
        "💧 Humidity",
        value=50.0
    )

with col3:
    square_footage = st.number_input(
        "🏢 Square Footage",
        value=2000.0,
        min_value=0.0
    )

with col4:
    occupancy = st.number_input(
        "👥 Occupancy",
        value=10,
        min_value=0
    )


# Row 2
col1, col2, col3, col4 = st.columns(4)

with col1:
    renewable_energy = st.number_input(
        "☀ Renewable Energy",
        value=10.0,
        min_value=0.0
    )

with col2:
    hvac_on = st.selectbox(
        "❄ HVAC",
        options=[0, 1],
        format_func=lambda x: "ON" if x == 1 else "OFF"
    )

with col3:
    lighting_on = st.selectbox(
        "💡 Lighting",
        options=[0, 1],
        format_func=lambda x: "ON" if x == 1 else "OFF"
    )

with col4:
    st.write("")
    st.write("")



# Prediction Button
predict = st.button(
    "🔮 Predict Energy Consumption",
    use_container_width=True
)



# Prediction
if predict:

    input_data = pd.DataFrame({
        "Temperature": [temperature],
        "Humidity": [humidity],
        "SquareFootage": [square_footage],
        "Occupancy": [occupancy],
        "RenewableEnergy": [renewable_energy],
        "HVAC_On": [hvac_on],
        "Lighting_On": [lighting_on]
    })

    prediction = model.predict(input_data)[0]

    st.divider()

    # Results
    result_col, performance_col = st.columns([1, 1])

    # Prediction result
    with result_col:

        st.markdown(
            '<div class="section-title">⚡ Prediction Result</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="prediction-box">
                <div class="prediction-value">
                    {prediction:.2f}
                </div>
                <div>
                    Predicted Energy Consumption
                </div>
                <div style="color:#9ca3af; margin-top:5px;">
                    Ridge Regression
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Model performance
    with performance_col:

        st.markdown(
            '<div class="section-title">📊 Model Performance</div>',
            unsafe_allow_html=True
        )

        m1, m2, m3 = st.columns(3)

        with m1:
            st.metric("R²", "0.5875")

        with m2:
            st.metric("RMSE", "5.044")

        with m3:
            st.metric("MAE", "3.957")


# Footer

st.divider()

st.caption(
    "Machine Learning Project • Energy Consumption Prediction • Ridge Regression"
)