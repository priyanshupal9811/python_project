import re
import csv
from datetime import datetime

# Common weak patterns to warn about
weak_patterns = ["123", "password", "qwerty", "admin", "abc", "111"]

def check_password_strength(password):
    strength = 0
    remarks = []

    # Length
    if len(password) >= 8:
        strength += 2
    else:
        remarks.append("❌ Too short (min 8 characters).")

    # Upper + Lowercase
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        strength += 2
    else:
        remarks.append("❌ Use both uppercase and lowercase letters.")

    # Numbers
    if re.search(r'\d', password):
        strength += 2
    else:
        remarks.append("❌ Include at least one number (0–9).")

    # Special characters
    if re.search(r'[@$!%*#?&]', password):
        strength += 2
    else:
        remarks.append("❌ Add special characters (@, $, %, etc).")

    # Weak pattern detection
    if any(pattern in password.lower() for pattern in weak_patterns):
        strength -= 2
        remarks.append("⚠️ Contains a weak pattern like '123', 'password', or 'qwerty'.")

    # Ensure strength stays within 0–10
    strength = max(0, min(10, strength))

    # Final rating
    if strength >= 8:
        rating = "Strong 💪"
    elif strength >= 5:
        rating = "Moderate ⚠️"
    else:
        rating = "Weak ❌"

    return strength, rating, remarks


import csv
from datetime import datetime

def save_to_csv(password, score, rating, filename="password_log.csv"):
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), password, score, rating])


# === MAIN ===
user_password = input("Enter your password: ")
score, rating, suggestions = check_password_strength(user_password)

print(f"\nPassword Strength: {rating} ({score}/10)")

if suggestions:
    print("\nSuggestions:")
    for remark in suggestions:
        print("-", remark)

# Save to CSV
save_to_csv(user_password, score, rating)
print("\n✅ Result saved to 'password_check_log.csv'")