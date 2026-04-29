from datetime import datetime
from core.db import init_db, insert_run, get_last_runs

class Feedback:
    def __init__(self):
        init_db()

    def log(self, data):
        data["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        insert_run(data)

    def compare(self):
        runs = get_last_runs(5)

        print("\n--- Last Runs Comparison ---\n")

        for r in runs:
            print(f"Run ID: {r[0]}")
            print(f"Time: {r[1]}")
            print(f"Functions: {r[2]}, Loops: {r[3]}")
            print(f"Exec Time: {r[7]}")
            print("-" * 40)