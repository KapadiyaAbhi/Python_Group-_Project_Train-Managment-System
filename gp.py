class Train:
    """
    Represents a train with its details.
    """
    def __init__(self, name, number, source, destination, route, timings, fare):
        self.name = name
        self.number = number
        self.source = source
        self.destination = destination
        self.route = route
        self.timings = timings
        self.fare = float(fare)

    def __str__(self):
        # Returns a string representation of the train's details.
        return (f"Train: {self.name} (#{self.number})\n"
                f"Source: {self.source} -> Destination: {self.destination}\n"
                f"Route: {self.route}\n"
                f"Timings: {self.timings}\n"
                f"Fare: ₹{self.fare}\n")


class RailwaySystem:
    """
    Main system for managing trains, tickets, and user accounts.
    """
    def __init__(self):
        # Default admin credentials are set here.
        self.admins = {"admin": "admin123"}
        self.customers = {}
        self.trains = []
        self.tickets = []

    def admin_menu(self):
        """
        Displays the admin menu and handles admin choices.
        """
        while True:
            print("\n" + "=" * 30)
            print("         ADMIN MENU       ")
            print("=" * 30)
            print("1️  ➜ Add Train")
            print("2️  ➜ View All Trains")
            print("3️  ➜ Remove Train")
            print("4️  ➜ Update Train Details")
            print("5️  ➜ Logout")
            print("-" * 30)
            choice = input(" Enter your choice: ")

            if choice == "1":
                self.add_train()
            elif choice == "2":
                self.view_trains()
            elif choice == "3":
                self.remove_train()
            elif choice == "4":
                self.update_train()
            elif choice == "5":
                print(" Logging out...\n")
                break
            else:
                print(" Invalid choice! Please enter a valid option.")

    def add_train(self):
        """
        Adds a new train to the system.
        """
        print("\n🔹 Adding a New Train")
        print("-" * 30)
        name = input(" Enter Train Name: ")
        number = input(" Enter Train Number: ")
        source = input(" Enter Source Station: ")
        destination = input(" Enter Destination Station: ")
        route = input(" Enter Train Route: ")
        timings = input(" Enter Train Timings: ")
        fare = input(" Enter Fare (₹): ")

        train = Train(name, number, source, destination, route, timings, fare)
        self.trains.append(train)
        print(" Train Added Successfully!")

    def remove_train(self):
        """
        Removes a train based on its number.
        """
        self.view_trains()
        print("\n Removing a Train")
        print("-" * 30)
        number = input(" Enter Train Number to Remove: ")

        initial_length = len(self.trains)
        self.trains = [train for train in self.trains if train.number != number]

        if len(self.trains) == initial_length:
            print(" Train not found!")
        else:
            print(" Train Removed Successfully!")

    def update_train(self):
        """
        Updates details of an existing train.
        """
        self.view_trains()
        print("\n  Update Train Details")
        print("-" * 30)
        train_number = input(" Enter Train Number to Update: ")

        selected_train = next((train for train in self.trains if train.number == train_number), None)
        if not selected_train:
            print(" Train not found!")
            return

        print("Leave field blank to keep the current value.")
        new_name = input(" Enter new Train Name: ")
        if new_name:
            selected_train.name = new_name

        new_source = input(" Enter new Source Station: ")
        if new_source:
            selected_train.source = new_source

        new_destination = input(" Enter new Destination Station: ")
        if new_destination:
            selected_train.destination = new_destination

        new_route = input(" Enter new Train Route: ")
        if new_route:
            selected_train.route = new_route

        new_timings = input(" Enter new Train Timings: ")
        if new_timings:
            selected_train.timings = new_timings

        new_fare = input(" Enter new Fare (₹): ")
        if new_fare:
            try:
                selected_train.fare = float(new_fare)
            except ValueError:
                print(" Invalid fare entered. Keeping previous fare.")

        print(" Train details updated successfully!")

    def view_trains(self):
        """
        Displays all available trains.
        """
        print("\n" + "=" * 30)
        print("        AVAILABLE TRAINS      ")
        print("=" * 30)

        if not self.trains:
            print(" No trains available. Please add trains first!")
        else:
            for train in self.trains:
                print(train)
                print("-" * 40)

    def search_train(self):
        """
        Searches for trains based on name or number.
        """
        print("\n SEARCH TRAIN")
        print("-" * 30)
        criteria = input("Enter Train Name or Number to search: ")
        found_trains = [train for train in self.trains if criteria.lower() in train.name.lower() or criteria == train.number]

        if not found_trains:
            print(" No matching trains found.")
        else:
            print(" Matching Trains:")
            for train in found_trains:
                print(train)
                print("-" * 40)

    def book_ticket(self, username):
        """
        Books a ticket for a customer.
        """
        if not self.trains:
            print(" No trains available to book tickets.")
            return

        self.view_trains()
        print("\n Booking a Ticket")
        print("-" * 30)
        number = input(" Enter Train Number: ")
        selected_train = next((t for t in self.trains if t.number == number), None)

        if not selected_train:
            print(" Invalid Train Number!")
            return

        name = input(" Enter Passenger Name: ")
        age = input(" Enter Passenger Age: ")

        ticket = {
            "username": username,
            "passenger_name": name,
            "age": age,
            "train_number": number,
            "train_name": selected_train.name,
            "fare": selected_train.fare
        }
        self.tickets.append(ticket)
        print(f" Ticket Booked Successfully for {name} in {selected_train.name}!")

    def view_tickets(self, username):
        """
        Displays all tickets booked by a customer.
        """
        print("\n YOUR BOOKED TICKETS ")
        print("-" * 30)
        user_tickets = [ticket for ticket in self.tickets if ticket["username"] == username]

        if not user_tickets:
            print(" No tickets booked yet.")
        else:
            for ticket in user_tickets:
                print(f" {ticket['passenger_name']} |  {ticket['train_name']} |  Fare: ₹{ticket['fare']}")
                print("-" * 30)

    def cancel_ticket(self, username):
        """
        Cancels a ticket for a customer.
        """
        self.view_tickets(username)
        print("\n Cancelling a Ticket")
        print("-" * 30)
        number = input(" Enter Train Number for Ticket Cancellation: ")

        initial_length = len(self.tickets)
        self.tickets = [t for t in self.tickets if not (t["username"] == username and t["train_number"] == number)]

        if len(self.tickets) == initial_length:
            print(" Ticket not found or already cancelled!")
        else:
            print(" Ticket Cancelled Successfully!")

    def signup(self, user_type):
        """
        Handles user signup for Admins and Customers.
        """
        print("\n SIGN UP")
        print("-" * 30)
        username = input(" Enter Username: ")
        password = input(" Enter Password: ")

        if user_type == "Admin":
            self.admins[username] = password
            print(" Admin Account Created!")
        else:
            self.customers[username] = password
            print(" Customer Account Created!")

    def login(self, user_type):
        """
        Handles user login.
        """
        print("\n LOGIN")
        print("-" * 30)
        username = input(" Enter Username: ")
        password = input(" Enter Password: ")

        users = self.admins if user_type == "Admin" else self.customers
        if users.get(username) == password:
            print(f" Welcome {user_type}: {username}")
            if user_type == "Admin":
                self.admin_menu()
            else:
                self.customer_menu(username)
        else:
            print(" Invalid Credentials!")

    def customer_menu(self, username):
        """
        Displays the customer menu and handles customer actions.
        """
        while True:
            print("\n" + "=" * 30)
            print(f"     CUSTOMER MENU ({username})     ")
            print("=" * 30)
            print("1️  ➜ Book Ticket")
            print("2️  ➜ View Booked Tickets")
            print("3️  ➜ Cancel Ticket")
            print("4️  ➜ Search Train")
            print("5️  ➜ Logout")
            print("-" * 30)
            choice = input(" Enter your choice: ")

            if choice == "1":
                self.book_ticket(username)
            elif choice == "2":
                self.view_tickets(username)
            elif choice == "3":
                self.cancel_ticket(username)
            elif choice == "4":
                self.search_train()
            elif choice == "5":
                print(" Logging out...\n")
                break
            else:
                print(" Invalid choice!")

    def main(self):
        """
        Entry point of the Railway Management System.
        """
        while True:
            print("\n" + "=" * 35)
            print("    RAILWAY MANAGEMENT SYSTEM    ")
            print("=" * 35)
            print("1️  ➜ Admin Signup")
            print("2️  ➜ Admin Login")
            print("3️  ➜ Customer Signup")
            print("4️  ➜ Customer Login")
            print("5️  ➜ Exit")
            print("-" * 35)
            choice = input(" Enter your choice: ")

            if choice == "1":
                self.signup("Admin")
            elif choice == "2":
                self.login("Admin")
            elif choice == "3":
                self.signup("Customer")
            elif choice == "4":
                self.login("Customer")
            elif choice == "5":
                print(" Exiting system. Goodbye!")
                break
            else:
                print(" Invalid choice! Please enter a valid option.")
if __name__ == "__main__":
    system = RailwaySystem()
    system.main()