# lib/cli.py
import fire
from db.models import Client, Worker, Room
from db import session

class HotelManagementCLI:
    def create_user(self):
        name = input("Enter user name: ")
        phone_number = input("Enter phone number: ")
        address = input("Enter address: ")
        user_type = input("Enter user type (client/worker): ")
        if user_type.lower() == 'client':
            user = Client(name=name, phone_number=phone_number, address=address)
        elif user_type.lower() == 'worker':
            user = Worker(name=name, phone_number=phone_number, address=address)
        else:
            print("Invalid user type. Please specify either 'client' or 'worker'.")
            return

        session.add(user)
        session.commit()
        print(f"{user_type.capitalize()} created successfully!")

    def create_room(self):
        number = input("Enter room number: ")
        capacity = input("Enter room capacity: ")
        hotel_id = input("Enter hotel ID: ")
        # Your create_room logic here
        pass

    def list_users(self):
        user_type = input("Enter user type to list (client/worker): ")
        if user_type.lower() == 'client':
            users = session.query(Client).all()
        elif user_type.lower() == 'worker':
            users = session.query(Worker).all()
        else:
            print("Invalid user type. Please specify either 'client' or 'worker'.")
            return

        if users:
            for user in users:
                print(f"{user_type.capitalize()} ID: {user.id}, Name: {user.name}, Phone Number: {user.phone_number}, Address: {user.address}")
        else:
            print(f"No {user_type}s found.")

if __name__ == '__main__':
    fire.Fire(HotelManagementCLI)
