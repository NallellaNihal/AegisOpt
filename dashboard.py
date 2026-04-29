import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

DB_PATH = "data/metrics.db"

st.set_page_config(page_title="AegisOpt Dashboard", layout="wide")

st.title("🚀 AegisOpt - Intelligent Code Optimization Dashboard")

# Load data
def load_data():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM runs", conn)
    conn.close()
    return df

df = load_data()

if df.empty:
    st.warning("No data available. Run main.py first.")
    st.stop()

# 📊 Metrics Overview
st.subheader("📊 Recent Runs")
st.dataframe(df.tail(10))

# 📈 Execution Time Graph
st.subheader("⏱ Execution Time Trend")

plt.figure()
plt.plot(df["id"], df["execution_time"], marker='o')
plt.xlabel("Run ID")
plt.ylabel("Execution Time")
plt.title("Execution Time Over Runs")

st.pyplot(plt)

# 📊 Code Complexity Graph
st.subheader("🧩 Code Complexity")

plt.figure()
plt.plot(df["id"], df["functions"], label="Functions")
plt.plot(df["id"], df["loops"], label="Loops")
plt.xlabel("Run ID")
plt.ylabel("Count")
plt.legend()
plt.title("Functions vs Loops")

st.pyplot(plt)

# 🧠 ML Insight
st.subheader("🧠 ML Insight")

avg_time = df["execution_time"].mean()
latest_time = df.iloc[-1]["execution_time"]

if latest_time > avg_time:
    st.error("⚠️ Latest run is slower than average → Optimization Recommended")
else:
    st.success("✅ Latest run is efficient")

# 🔍 Raw JSON-like view
st.subheader("🔍 Raw Data")
st.write(df)
uploaded_file = st.file_uploader("Upload Python Code", type=["py"])

if uploaded_file:
    code = uploaded_file.read().decode("utf-8")
    
    from agents.profiler import ProfilerAgent
    profiler = ProfilerAgent()
    
    profile = profiler.analyze(code)
    st.write("Live Profile:", profile)
st.subheader("🤖 ML Prediction")

st.write("Latest ML Decision:", "Optimize / No Optimization")
plt.figure()
plt.plot(df["id"], df["execution_time"], marker='o', linestyle='-')
plt.grid()
best = df.loc[df["execution_time"].idxmin()]

st.success(f"🚀 Best Run ID: {best['id']} with time {best['execution_time']}")