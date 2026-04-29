from agents.profiler import ProfilerAgent
from agents.optimizer import OptimizerAgent
from agents.security import SecurityAgent
from agents.coordinator import Coordinator
from core.executor import Executor
from core.feedback import Feedback
from core.ml_model import MLModel


def load_code():
    with open("sample_code/test_program.py", "r") as f:
        return f.read()


def main():
    code = load_code()

    profiler = ProfilerAgent()
    optimizer = OptimizerAgent()
    security = SecurityAgent()
    coordinator = Coordinator()
    executor = Executor()

    print("\n--- AegisOpt Running ---\n")

    profile = profiler.analyze(code)
    print("Profile:", profile)

    # 🔥 ML PART (FIXED POSITION + INDENTATION)
    ml = MLModel()
    model = ml.train()
    ml_decision = ml.predict(model, profile)
    print("ML Decision:", ml_decision)

    optimizations = optimizer.suggest(profile)
    print("Optimization Suggestions:", optimizations)

    security_issues = security.scan(code)
    print("Security Issues:", security_issues)

    decision = coordinator.decide(profile, optimizations, security_issues)
    print("Decision:", decision)

    metrics = executor.run(code)
    print("Execution Metrics:", metrics)

    # ✅ FEEDBACK
    feedback = Feedback()

    feedback.log({
        "profile": profile,
        "optimizations": optimizations,
        "security": security_issues,
        "decision": decision,
        "metrics": metrics
    })

    feedback.compare()

    print("\n--- Done ---\n")


if __name__ == "__main__":
    main()