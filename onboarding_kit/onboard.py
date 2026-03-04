"""
Performs environment checks, optional auto-fixes,
disk space validation, timing metrics, and generates a report.
"""

import sys
import argparse
import subprocess
import importlib
import shutil
import time
from pathlib import Path

REPORT_LINES = []


def record_result(name, status, message="", duration=None, verbose=False):
    """Record and print result of a check."""
    result = f"{name}: {'PASS' if status else 'FAIL'}"
    if message:
        result += f" | {message}"
    if duration is not None and verbose:
        result += f" | {duration:.4f}s"

    print(result)
    REPORT_LINES.append(result)


def timed_check(func):
    """Decorator to measure execution time of a check."""

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start
        return result, duration

    return wrapper


@timed_check
def check_python_version():
    """Ensure Python version is 3.10+."""
    version = sys.version_info
    if version.major > 3 or (version.major == 3 and version.minor >= 10):
        return True, f"{version.major}.{version.minor}"
    return False, f"{version.major}.{version.minor} detected (requires 3.10+)"


@timed_check
def check_virtual_env():
    """Check if running inside virtual environment."""
    in_venv = (
        hasattr(sys, "real_prefix")
        or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix)
    )
    return in_venv, "Running inside venv" if in_venv else "Not in virtual environment"


@timed_check
def check_disk_space():
    """Warn if disk space is below 1GB."""
    total, used, free = shutil.disk_usage(Path.cwd())
    free_gb = free / (1024**3)

    if free_gb < 1:
        return False, f"Low disk space: {free_gb:.2f} GB free"
    return True, f"{free_gb:.2f} GB free"


@timed_check
def check_package_installed(package_name, auto_fix=False):
    """Check if a package is installed. Optionally auto-install."""
    try:
        importlib.import_module(package_name)
        return True, f"{package_name} installed"
    except ImportError:
        if auto_fix:
            subprocess.call([sys.executable, "-m", "pip", "install", package_name])
            try:
                importlib.import_module(package_name)
                return True, f"{package_name} auto-installed"
            except ImportError:
                return False, f"{package_name} installation failed"
        return False, f"{package_name} not installed"


@timed_check
def check_internet():
    """Test internet connectivity using requests."""
    try:
        import requests

        response = requests.get("https://www.google.com", timeout=5)
        return response.status_code == 200, "Internet reachable"
    except Exception as error:  # pylint: disable=broad-except
        return False, str(error)


def save_report():
    """Write report to setup_report.txt."""
    with open("setup_report.txt", "w", encoding="utf-8") as file:
        file.write("SETUP VALIDATION REPORT\n")
        file.write("=" * 40 + "\n")
        for line in REPORT_LINES:
            file.write(line + "\n")


def main():
    """Main execution logic."""
    parser = argparse.ArgumentParser(description="Advanced onboarding validator.")
    parser.add_argument(
        "--verbose", action="store_true", help="Show detailed timing information"
    )
    parser.add_argument(
        "--fix",
        action="store_true",
        help="Attempt to auto-install missing packages",
    )

    args = parser.parse_args()
    total_start = time.time()

    # Python Version
    (status, msg), duration = check_python_version()
    record_result("Python Version", status, msg, duration, args.verbose)

    # Virtual Environment
    (status, msg), duration = check_virtual_env()
    record_result("Virtual Environment", status, msg, duration, args.verbose)

    # Disk Space
    (status, msg), duration = check_disk_space()
    record_result("Disk Space Check", status, msg, duration, args.verbose)

    # Required Packages
    for pkg in ["pylint", "black", "requests"]:
        (status, msg), duration = check_package_installed(pkg, args.fix)
        record_result(
            f"{pkg} Check", status, msg, duration, args.verbose
        )

    # Internet
    (status, msg), duration = check_internet()
    record_result("Internet Connectivity", status, msg, duration, args.verbose)

    total_duration = time.time() - total_start
    print(f"\nTotal Execution Time: {total_duration:.4f}s")

    save_report()
    print("Report saved to setup_report.txt")


if __name__ == "__main__":
    main()
