Hotel Management CLI Project
This is a command-line interface (CLI) application for managing a hotel, allowing administrators to create users (clients and workers), manage rooms, and perform various tasks related to hotel management.

Features
User Management: Create and manage clients and workers of the hotel.
Room Management: Add, delete, and view rooms available in the hotel.
Data Persistence: Uses a SQLite database to store user and room data.
CLI Interface: Provides a user-friendly command-line interface for interacting with the application.
Installation
Clone the repository to your local machine:

bash
Copy code
git clone <repository-url>
Navigate to the project directory:

bash
Copy code
cd hotel-management-cli-project
Install dependencies using Pipenv:

Copy code
pipenv install
Usage
Run the CLI application:

arduino
Copy code
pipenv run python lib/cli.py
Follow the on-screen prompts to perform various tasks such as creating users, managing rooms, etc.

Dependencies
Python 3.x
SQLAlchemy
Fire (for command-line interface)

Contributing
Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.