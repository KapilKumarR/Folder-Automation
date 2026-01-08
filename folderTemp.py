from pathlib import Path
from datetime import datetime
import time
import sys


def print_banner():
    width = 60
    print("\n" + "═" * width)
    print("FOLDER AUTOMATION TOOL".center(width))
    print("Author : KAPIL KUMAR RAHUL".center(width))
    print("═" * width + "\n")


def create_folder_structure(company_name, role_name, current_date):
    try:
        base_path = Path(company_name) / role_name / current_date

        folders = [
            "INTERESTED",
            "NOT INTERESTED",
            "LATER",
            "SENT CV"
        ]

        for folder in folders:
            folder_path = base_path / folder
            folder_path.mkdir(parents=True, exist_ok=True)
            print(f"Folder created: {folder_path}")

        # Log file
        data_log = Path(company_name) / "dataLog.txt"
        with data_log.open("a", encoding="utf-8") as file:
            file.write(
                f"\n-----------------------------------\n"
                f"Company   : {company_name}\n"
                f"Role      : {role_name}\n"
                f"Date      : {current_date}\n"
                f"Status    : Folder structure created successfully\n"
                f"Author    : KAPIL KUMAR RAHUL\n"
            )

        print("\nFolder structure created successfully!")
        print(f"Log updated: {data_log}")

        print("\nProgram will close in 10 seconds...")
        time.sleep(10)

        print("\nThank you for using this tool.")
        print("— KAPIL KUMAR RAHUL")
        input("\nPress Enter to close this window...")

    except Exception as e:
        print(f"\nError while creating folders: {e}")
        input("Press Enter to exit...")
        sys.exit(1)


def main():
    print_banner()

    company_name = input("Enter Company Name: ").strip()
    role_name = input(f"Enter Role for {company_name}: ").strip()

    # SAFE date format for Windows folders
    current_date = datetime.now().strftime("%d-%m-%Y")

    if not company_name or not role_name:
        print("\nCompany name and Role name cannot be empty.")
        input("Press Enter to exit...")
        sys.exit(1)

    print("\nCreating folder structure...\n")
    create_folder_structure(company_name, role_name, current_date)


if __name__ == "__main__":
    main()
