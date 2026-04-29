from fastapi import FastAPI, UploadFile, File, HTTPException
from agents.profiler import ProfilerAgent
from agents.optimizer import OptimizerAgent
from agents.security import SecurityAgent
from agents.coordinator import Coordinator
from core.executor import Executor
from core.feedback import Feedback
from core.ml_model import MLModel
from core.db import get_last_runs
from agents.autofix import AutoFixAgent

app = FastAPI(title="AegisOpt API")

# Initialize agents
profiler = ProfilerAgent()
optimizer = OptimizerAgent()
security = SecurityAgent()
coordinator = Coordinator()
executor = Executor()
feedback = Feedback()
ml = MLModel()
autofix = AutoFixAgent()   # 🔥 NEW


@app.get("/")
def home():
    return {"message": "AegisOpt API is running 🚀"}


@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    code = (await file.read()).decode("utf-8")

    profile = profiler.analyze(code)
    optimizations = optimizer.suggest(profile)
    security_issues = security.scan(code)

    model = ml.train()
    ml_decision = ml.predict(model, profile)

    decision = coordinator.decide(profile, optimizations, security_issues)

    # 🔥 FIX FIRST
    fixed_code = autofix.fix(code)

    # 🔥 THEN EXECUTE SAFE CODE
    metrics = executor.run(fixed_code)

    feedback.log({
        "profile": profile,
        "optimizations": optimizations,
        "security": security_issues,
        "decision": decision,
        "metrics": metrics
    })

    return {
        "profile": profile,
        "optimizations": optimizations,
        "security_issues": security_issues,
        "decision": decision,
        "ml_decision": ml_decision,
        "metrics": metrics,
        "fixed_code": fixed_code   # 🔥 IMPORTANT
    }

@app.get("/runs")
def get_runs():
    runs = get_last_runs(10)

    result = []
    for r in runs:
        result.append({
            "id": r[0],
            "timestamp": r[1],
            "functions": r[2],
            "loops": r[3],
            "execution_time": r[7]
        })

    return result