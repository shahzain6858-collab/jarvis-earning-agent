
import csv
from pathlib import Path
from datetime import datetime

FILE = Path("leads.csv")
FIELDS = ["business", "service", "contact", "status", "created_at"]


def load_leads():
    if not FILE.exists():
        return []
    with FILE.open("r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def save_leads(leads):
    with FILE.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(leads)


def main():
    leads = load_leads()

    while True:
        print("\n===== JARVIS v1 =====")
        print("1. Add potential client")
        print("2. View saved clients")
        print("3. Draft an offer")
        print("4. View CSV leads")
        print("5. Exit")

        choice = input("Choose 1-5: ").strip()

        if choice == "1":
            business = input("Business name: ").strip()
            service = input("Service to offer: ").strip()
            contact = input("Public contact or website: ").strip()

            if business and service:
                leads.append({
                    "business": business,
                    "service": service,
                    "contact": contact,
                    "status": "new",
                    "created_at": datetime.now().isoformat(
                        timespec="minutes"
                    )
                })
                save_leads(leads)
                print("Lead saved!")
            else:
                print("Business name and service are required.")

        elif choice == "2":
            if not leads:
                print("No clients saved yet.")
            for lead in leads:
                print(
                    lead["business"], "|",
                    lead["service"], "|",
                    lead["status"]
                )

        elif choice == "3":
            if not leads:
                print("Add a client first.")
                continue

            for i, lead in enumerate(leads, start=1):
                print(i, lead["business"], "-", lead["service"])

            try:
                number = int(input("Choose client number: "))
                lead = leads[number - 1]
                if number < 1:
                    raise ValueError
            except (ValueError, IndexError):
                print("Invalid number.")
                continue

            print("\n--- Draft only; not sent ---")
            print(
                f"Hello {lead['business']} team! "
                f"I offer {lead['service']} services. "
                "Would you be interested in seeing a sample? "
                "Thank you!"
            )

        elif choice == "4":
            if FILE.exists():
                print(FILE.read_text(encoding="utf-8"))
            else:
                print("No CSV file yet. Add a client first.")

        elif choice == "5":
            print("JARVIS closed.")
            break

        else:
            print("Please choose 1, 2, 3, 4, or 5.")


if __name__ == "__main__":
    main()

