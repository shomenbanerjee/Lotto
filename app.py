import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from prediction import simulate_draws
from utils import load_draws

st.title("🎰 Lottery Prediction Dashboard")

# Upload section
st.sidebar.header("📤 Upload Draw History")
uploaded_file = st.sidebar.file_uploader("Choose CSV", type="csv")

# Load example or user-uploaded draws
if uploaded_file:
    draws, draw_df = load_draws(uploaded_file)
else:
    draw_df = pd.read_csv("data/example_draws.csv")
    draws, _ = load_draws("data/example_draws.csv")

# Display data
st.subheader("📊 Historical Draws")
st.dataframe(draw_df)

# Run simulation
top_combos, freq = simulate_draws(draws)
st.subheader("🎯 Predicted Number Sets")
for combo, count in top_combos:
    st.write(f"**{combo}** → {count} simulations")

# Plot frequency heatmap
heatmap = [freq.get(i+1, 0) for i in range(50)]
st.subheader("🌡️ Number Frequency Heatmap")
fig, ax = plt.subplots(figsize=(12, 2))
sns.heatmap([heatmap], cmap="Reds", xticklabels=list(range(1, 51)), yticklabels=[], cbar=True, ax=ax)
st.pyplot(fig)
