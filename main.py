
"""
JARVIS Earning Agent - Version 1
A lightweight, zero-API-cost lead organizer.
"""

import json
from pathlib import Path
from datetime import datetime

DATA_FILE = Path("leads.json")


def load_leads():
    if DATA_FILE.exists():
        try:
            return json.loads(DATA_FILE.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            return []
    return []


def save_leads(leads):
    DATA_FILE.write_text(
        json.dumps(leads, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )


def add_lead(leads):
    print("\n--- Add Potential Client ---")
    name = input("Business name: ").strip()
    service = input("Service they may need: ").strip()
    contact = input("Public business contact or website: ").strip()

    if not name or not service:
        print("Business name and service are required.")
        return

    leads.append({
        "business": name,
        "service": service,
        "contact": contact,
        "status": "new",
        "created_at": datetime.now().isoformat(timespec="minutes")
    })
    save_leads(leads)
    print("Lead saved successfully!")


def draft_offer(leads):
    if not leads:
        print("No leads yet. Add a lead first.")
        return

    for i, lead in enumerate(leads, start=1):
        print(f"{i}. {lead['business']} — {lead['service']}")

    try:
        number = int(input("Choose lead number: "))
        lead = leads[number - 1]
        if number < 1:
            raise ValueError
    except (ValueError, IndexError):
        print("Invalid selection.")
        return

    message = (
        f"Hello {lead['business']} team! I came across your business "
        f"and wanted to introduce my {lead['service']} service. "
        "I can prepare a small sample for you to review, with no "
        "obligation. Would you be interested? Thank you!"
    )

    print("\n--- Draft only: review before sending ---\n")
    print(message)
    print("\nNo message has been sent.")


def main():
    leads = load_leads()

    while True:
        print("\n===== JARVIS v1 =====")
        print("1. Add a potential client")
        print("2. View saved clients")
        print("3. Draft a personalized offer")
        print("4. Exit")
print("5. View CSV leads")
        choice = input("Select 1-4: ").strip()
        if choice == "1":
            add_lead(leads)
        elif choice == "2":
            if not leads:
                print("No clients saved yet.")
            else:
                for lead in leads:
                    print(
                        f"- {lead['business']} | {lead['service']} "
                        f"| Status: {lead['status']}"
                    )
        elif choice == "3":
            draft_offer(leads)
        elif choice == "4":
            print("JARVIS shutting down. Goodbye!")
            break
elif choice == "5":
    read_csv_leads()
else:
    print("Please choose 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    main()
import csv
from pathlib import Path

def read_csv_leads():
    file_path = Path("leads.csv")

    if not file_path.exists():
        print("leads.csv file not found.")
        return

    with file_path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for lead in reader:
            print(
                lead.get("business", ""),
                "|",
                lead.get("service", ""),
                "|",
                lead.get("status", "")
            )
