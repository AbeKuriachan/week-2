from collections import Counter, defaultdict

# Server Logs : to be replaced with actual log files path in practice but I am moving forward with static logs

logs = [
"2026-03-10 10:00:01 | INFO | auth | User login successful",
"2026-03-10 10:01:15 | ERROR | database | Connection timeout",
"2026-03-10 10:02:30 | WARNING | api | Slow response detected",
"2026-03-10 10:03:10 | INFO | auth | Token refreshed",
"2026-03-10 10:04:22 | ERROR | api | Endpoint failure",
"2026-03-10 10:05:11 | ERROR | database | Connection timeout",
"2026-03-10 10:06:55 | INFO | payment | Payment processed",
"2026-03-10 10:07:42 | CRITICAL | system | Disk space exhausted",
"2026-03-10 10:08:18 | WARNING | api | Deprecated endpoint used",
"2026-03-10 10:09:30 | ERROR | payment | Transaction failed",
"2026-03-10 10:10:44 | INFO | auth | User logout",
]

# Parse Log Lines
def parse_log(line):
    parts = line.split(" | ")
    return {
        "timestamp": parts[0],
        "level": parts[1],
        "module": parts[2],
        "message": parts[3]
    }

parsed_logs = [parse_log(log) for log in logs]

# Counters
error_counter = Counter()
module_counter = Counter()
level_counter = Counter()

errors_by_module = defaultdict(list)


# Analyze Logs
for log in parsed_logs:

    level = log.get("level")
    module = log.get("module")
    message = log.get("message")

    level_counter[level] += 1
    module_counter[module] += 1

    if level == "ERROR":
        error_counter[message] += 1
        errors_by_module[module].append(message)


# Generate Summary
def generate_summary(parsed_logs):

    total = len(parsed_logs)

    error_count = sum(
        1 for log in parsed_logs
        if log.get("level") == "ERROR"
    )

    error_rate = (error_count / total) * 100

    summary = {
        "total_entries": total,
        "error_rate": round(error_rate, 2),
        "top_errors": error_counter.most_common(3),
        "busiest_module": module_counter.most_common(1)[0][0]
    }

    return summary


# Output Results
print("\nParsed Logs:")
for log in parsed_logs:
    print(log)

print("\nMost Common Errors:")
print(error_counter.most_common())

print("\nMost Active Modules:")
print(module_counter.most_common())

print("\nLog Level Distribution:")
print(level_counter)

print("\nErrors Grouped By Module:")
print(dict(errors_by_module))

print("\nSystem Summary:")
print(generate_summary(parsed_logs))
