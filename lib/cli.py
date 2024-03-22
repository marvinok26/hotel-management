# lib/cli.py

from helpers import exit_program
from db import Database
from models.user_model import User

db = Database()

def admin_session():
    # Admin session implementation
    pass

def auth_admin():
    # Admin authentication implementation
    pass

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "1":
            auth_admin()
        elif choice == "0":
            exit_program()
        else:
            print("Invalid choice")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Login as admin")

if __name__ == "__main__":
    main()
