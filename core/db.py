import sqlite3

DB_PATH = "data/metrics.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS runs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        functions INTEGER,
        loops INTEGER,
        optimizations TEXT,
        security_issues TEXT,
        decision TEXT,
        execution_time REAL
    )
    """)

    conn.commit()
    conn.close()


def insert_run(data):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO runs (
        timestamp, functions, loops,
        optimizations, security_issues,
        decision, execution_time
    ) VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        data["timestamp"],
        data["profile"]["functions"],
        data["profile"]["loops"],
        str(data["optimizations"]),
        str(data["security"]),
        str(data["decision"]),
        data["metrics"]["execution_time"]
    ))

    conn.commit()
    conn.close()


def get_last_runs(limit=5):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM runs
    ORDER BY id DESC
    LIMIT ?
    """, (limit,))

    rows = cursor.fetchall()
    conn.close()
    return rows