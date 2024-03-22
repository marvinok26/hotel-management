from models import Client, Worker, Room, session

def seed_data():
    # Seed clients
    client1 = Client(name="John Doe", phone_number="1234567890", address="123 Main St")
    client2 = Client(name="Jane Smith", phone_number="9876543210", address="456 Oak St")
    session.add_all([client1, client2])

    # Seed workers
    worker1 = Worker(name="Alice Johnson", phone_number="1112223333", address="789 Elm St")
    worker2 = Worker(name="Bob Brown", phone_number="4445556666", address="321 Pine St")
    session.add_all([worker1, worker2])

    # Seed rooms
    room1 = Room(room_number=101)
    room2 = Room(room_number=102)
    session.add_all([room1, room2])

    session.commit()
    print("Database seeded successfully!")

if __name__ == "__main__":
    seed_data()
