"""
Password Strength Checker
Author: Your Name
Project: DecodeLabs Cyber Security Internship - Project 1

Features:
- Length validation
- Uppercase letter detection
- Lowercase letter detection
- Digit detection
- Special character detection
- Password strength scoring
- Security recommendations
"""

import re


class PasswordStrengthChecker:
    def __init__(self, password: str):
        self.password = password

    def analyze(self) -> dict:
        checks = {
            "length": len(self.password) >= 8,
            "uppercase": bool(re.search(r"[A-Z]", self.password)),
            "lowercase": bool(re.search(r"[a-z]", self.password)),
            "digit": bool(re.search(r"\d", self.password)),
            "special_char": bool(re.search(r"[!@#$%^&*()_+\-=\[\]{};:'\"\\|,.<>/?]", self.password)),
        }

        score = sum(checks.values())

        if score <= 2:
            strength = "Weak"
        elif score == 3 or score == 4:
            strength = "Medium"
        else:
            strength = "Strong"

        recommendations = []

        if not checks["length"]:
            recommendations.append("Use at least 8 characters.")

        if not checks["uppercase"]:
            recommendations.append("Add uppercase letters.")

        if not checks["lowercase"]:
            recommendations.append("Add lowercase letters.")

        if not checks["digit"]:
            recommendations.append("Include numbers.")

        if not checks["special_char"]:
            recommendations.append("Include special characters.")

        return {
            "score": score,
            "strength": strength,
            "checks": checks,
            "recommendations": recommendations,
        }


def display_report(result: dict) -> None:
    print("\n" + "=" * 40)
    print("PASSWORD SECURITY REPORT")
    print("=" * 40)

    print(f"Strength : {result['strength']}")
    print(f"Score    : {result['score']}/5\n")

    print("Validation Results:")
    for check, status in result["checks"].items():
        print(f"  {check.capitalize():15} : {'PASS' if status else 'FAIL'}")

    if result["recommendations"]:
        print("\nRecommendations:")
        for recommendation in result["recommendations"]:
            print(f"  • {recommendation}")
    else:
        print("\nExcellent! Your password meets all requirements.")

    print("=" * 40)


def main():
    print("=== Professional Password Strength Checker ===")
    password = input("Enter Password: ")

    checker = PasswordStrengthChecker(password)
    result = checker.analyze()

    display_report(result)


if __name__ == "__main__":
    main()