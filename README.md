\# 🚀 AegisOpt – Intelligent Code Optimization System



AegisOpt is a multi-agent AI system designed to analyze, optimize, and automatically fix Python code using machine learning and static analysis techniques.



\---



\## 🔥 Features



\- 🧠 Multi-Agent Architecture

\- ⚙️ Code Profiling \& Optimization Suggestions

\- 🔐 Security Analysis (detects unsafe patterns like eval)

\- 🤖 ML-based Optimization Decisions

\- 🔄 Auto-Fix Engine (AST-based code transformation)

\- 📊 Dashboard (Streamlit)

\- 🌐 FastAPI Backend

\- 💾 SQLite Run History Tracking



\---



\## 🧩 Architecture



Code → Profiling → Security Scan → ML Decision → AutoFix → Safe Execution → Logging → API Response



\---



\## 🚀 API Endpoints



\### POST /analyze

Upload Python file and get:

\- Code analysis

\- Security issues

\- ML decision

\- Auto-fixed code



\### GET /runs

Get recent execution history



\---



\## ▶️ Run Locally



```bash

pip install -r requirements.txt

python -m uvicorn api:app --reload

