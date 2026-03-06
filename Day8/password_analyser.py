import string
import random

def analyze_password(password: str) -> tuple:
    score = 0
    missing = []

    # Length check
    if len(password) >= 16:
        score += 3
    elif len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        missing.append("too short")

    # Character type checks
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*" for c in password)

    if has_upper: score += 1
    else: missing.append("uppercase")
    if has_lower: score += 1
    else: missing.append("lowercase")
    if has_digit: score += 1
    else: missing.append("digit")
    if has_special: score += 1
    else: missing.append("special char")

    # No repeated characters more than 2 in a row
    repeat_flag = True
    for i in range(len(password) - 2):
        if password[i] == password[i+1] == password[i+2]:
            repeat_flag = False
            break
    if repeat_flag and password:
        score += 1
    else:
        missing.append("no triple repeats")

    return score, missing


def strength_rating(score: int) -> str:
    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    elif score <= 6:
        return "Strong"
    else:
        return "Very Strong"


def password_generator(length: int) -> str:
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password


# Main loop: keep asking until strength ≥ 5
while True:
    pwd = input("Enter password (or type 'gen' to generate one): ")

    if pwd.lower() == "gen":
        length = int(input("Enter desired length: "))
        pwd = password_generator(length)
        print(f"Generated password: {pwd}")

    score, missing = analyze_password(pwd)
    rating = strength_rating(score)

    print(f">> Strength: {score}/7 ({rating})")
    if score < 5:
        print(f">> Missing: {', '.join(missing)}")
        print(">> Try again...")
    else:
        print(">> Password accepted!")
        break