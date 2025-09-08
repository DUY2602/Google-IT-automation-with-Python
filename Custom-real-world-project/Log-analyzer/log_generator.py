import random
from datetime import datetime, timedelta

# Cấu hình log
levels = ["INFO", "WARNING", "ERROR"]
messages = [
    "User logged in",
    "Database connection failed",
    "Disk space low",
    "File not found",
    "User logged out",
    "Permission denied",
    "Timeout occurred"
]

def random_ip():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

def random_timestamp():
    start = datetime(2025, 9, 1, 0, 0, 0)
    end = datetime(2025, 9, 30, 23, 59, 59)
    delta = end - start
    random_second = random.randint(0, int(delta.total_seconds()))
    return start + timedelta(seconds=random_second)

with open("sample.log", "w", encoding="utf-8") as f:
    for _ in range(100):
        ts = random_timestamp().strftime("%Y-%m-%d %H:%M:%S")
        level = random.choice(levels)
        ip = random_ip()
        msg = random.choice(messages)
        line = f"[{ts}] {level} {ip} {msg}\n"
        f.write(line)

print("sample.log is created with 100 saple log lines.")
