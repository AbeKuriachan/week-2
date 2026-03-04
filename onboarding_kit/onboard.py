import sys
import importlib
import subprocess

report = []


# -----------------------------
# Helper function
# -----------------------------
def record_result(check_name, status, message=""):
    result = f"{check_name}: {'PASS' if status else 'FAIL'}"
    if message:
        result += f" | {message}"
    print(result)
    report.append(result)


# -----------------------------
# 1️⃣ Check Python Version
# -----------------------------
required_major = 3
required_minor = 10

current_version = sys.version_info

if (current_version.major > required_major) or (
    current_version.major == required_major and current_version.minor >= required_minor
):
    record_result(
        "Python Version Check", True, f"{current_version.major}.{current_version.minor}"
    )
else:
    record_result(
        "Python Version Check",
        False,
        f"Detected {current_version.major}.{current_version.minor}, requires 3.10+",
    )


# -----------------------------
# 2️⃣ Check Virtual Environment
# -----------------------------
if hasattr(sys, "real_prefix") or (
    hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix
):
    record_result("Virtual Environment Check", True)
else:
    record_result("Virtual Environment Check", False, "Not running inside a venv")


# -----------------------------
# 3️⃣ List Installed Packages
# -----------------------------
try:
    packages = subprocess.check_output([sys.executable, "-m", "pip", "freeze"])
    packages = packages.decode().splitlines()
    record_result("Installed Packages Listing", True, f"{len(packages)} packages found")
    print("\nInstalled Packages:")
    for pkg in packages:
        print(pkg)
except Exception as e:
    record_result("Installed Packages Listing", False, str(e))


# -----------------------------
# 4️⃣ Check pylint and black
# -----------------------------
for tool in ["pylint", "black"]:
    try:
        importlib.import_module(tool)
        record_result(f"{tool} Installation Check", True)
    except ImportError:
        record_result(f"{tool} Installation Check", False, "Not installed")


# -----------------------------
# 5️⃣ Internet Connectivity Test
# -----------------------------
try:
    import requests

    response = requests.get("https://www.google.com", timeout=5)
    if response.status_code == 200:
        record_result("Internet Connectivity Check", True)
    else:
        record_result(
            "Internet Connectivity Check", False, f"Status code {response.status_code}"
        )
except Exception as e:
    record_result("Internet Connectivity Check", False, str(e))


# 6️⃣ Save Report

try:
    with open("setup_report.txt", "w") as f:
        f.write("SETUP VALIDATION REPORT\n")
        f.write("=" * 30 + "\n")
        for line in report:
            f.write(line + "\n")
    print("\nReport saved to setup_report.txt")
except Exception as e:
    print("Failed to write report:", e)
