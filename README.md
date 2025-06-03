# Python_Group-_Project_Train-Managment-System
Railway Management System

This is a simple console-based Railway Management System built using Python. The system supports two types of users:

Admins: Can manage train details.

Customers: Can book, view, and cancel tickets.

🔧 Features

Admin Features:

Add Train: Add a new train with route, timing, fare, etc.

View All Trains: Display the list of all available trains.

Remove Train: Delete any train by train number.

Update Train: Modify the details of any train.

Customer Features:

Book Ticket: Book a ticket for a selected train.

View Booked Tickets: Display all booked tickets for the user.

Cancel Ticket: Cancel a ticket that was previously booked.

Search Train: Search trains by name or number.

👥 User Roles

1. Admin:

Can sign up and log in.

Can add, update, delete, and view trains.

2. Customer:

Can sign up and log in.

Can book, view, and cancel tickets.

Can search for available trains.

🛠️ How It Works

Signup/Login

Admin and Customer both need to sign up first.

After signing up, they can log in using their credentials.

Admin Menu

After logging in, admins can manage the train list.

Customer Menu

After logging in, customers can book, view, cancel tickets, and search trains.

Booking a Ticket

Customer chooses a train from the available list and enters passenger details to confirm booking.

Canceling a Ticket

Customer enters the train number to cancel the corresponding ticket.

📂 Code Structure

Train Class: Holds individual train details.

RailwaySystem Class: Handles all logic including user management, train management, and ticket booking.

main() Function: Entry point to the program that shows the main menu.

▶️ How to Run

Make sure you have Python 3.x installed.

Save the code in a file, e.g., railway_system.py.

Open terminal/command prompt and navigate to the folder where the file is saved.

Run the program:

python railway_system.py

Follow the on-screen instructions to use the system.

✅ Requirements

Python 3.x

No external libraries required. The system uses basic Python functionality.

📌 Notes

This system is console-based and uses in-memory storage. Once the program stops, all data will be lost.

No database or file handling is used in this version.

💡 Future Improvements

Add data persistence (save trains and tickets to files).

Add date selection for train booking.

Add seat availability.

Add PNR generation for tickets.
