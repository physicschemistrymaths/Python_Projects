import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

# Mock data for train routes and schedule
routes = {
    '1': {'origin': 'Delhi', 'destination': 'Mumbai', 'departure_time': '08:00', 'arrival_time': '12:00', 'price': 50},
    '2': {'origin': 'Delhi', 'destination': 'Bangalore', 'departure_time': '10:00', 'arrival_time': '14:00', 'price': 60},
    '3': {'origin': 'Mumbai', 'destination': 'Delhi', 'departure_time': '09:30', 'arrival_time': '13:30', 'price': 55},
    '4': {'origin': 'Bangalore', 'destination': 'Delhi', 'departure_time': '11:30', 'arrival_time': '15:30', 'price': 65},
    '5': {'origin': 'Delhi', 'destination': 'Chennai', 'departure_time': '07:00', 'arrival_time': '13:00', 'price': 70},
    '6': {'origin': 'Chennai', 'destination': 'Delhi', 'departure_time': '14:00', 'arrival_time': '20:00', 'price': 75},
    '7': {'origin': 'Mumbai', 'destination': 'Bangalore', 'departure_time': '06:30', 'arrival_time': '10:30', 'price': 45},
    '8': {'origin': 'Bangalore', 'destination': 'Mumbai', 'departure_time': '16:00', 'arrival_time': '20:00', 'price': 55},
    '9': {'origin': 'Chennai', 'destination': 'Mumbai', 'departure_time': '12:00', 'arrival_time': '18:00', 'price': 65},
    '10': {'origin': 'Mumbai', 'destination': 'Chennai', 'departure_time': '08:30', 'arrival_time': '14:30', 'price': 70},
    '11': {'origin': 'Bangalore', 'destination': 'Chennai', 'departure_time': '09:00', 'arrival_time': '13:00', 'price': 50},
    '12': {'origin': 'Chennai', 'destination': 'Bangalore', 'departure_time': '15:30', 'arrival_time': '19:30', 'price': 60},
}

# Mock data for seat availability
seat_availability = {
    '1': {'economy': 50, 'business': 20},
    '2': {'economy': 40, 'business': 10},
    '3': {'economy': 60, 'business': 30},
    '4': {'economy': 30, 'business': 15},
    '5': {'economy': 45, 'business': 25},
    '6': {'economy': 35, 'business': 15},
    '7': {'economy': 55, 'business': 25},
    '8': {'economy': 50, 'business': 20},
    '9': {'economy': 40, 'business': 15},
    '10': {'economy': 35, 'business': 10},
    '11': {'economy': 45, 'business': 20},
    '12': {'economy': 40, 'business': 15},
}

# Tkinter GUI for Train Ticket Booking
class TrainTicketApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Realistic Train Ticket Booking')

        self.create_widgets()

    def create_widgets(self):
        # Frame for selecting route
        route_frame = ttk.LabelFrame(self.root, text='Select Route', padding=(10, 10))
        route_frame.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W+tk.E)

        ttk.Label(route_frame, text="Origin:").grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.origin_var = tk.StringVar()
        origin_combo = ttk.Combobox(route_frame, textvariable=self.origin_var, values=['Delhi', 'Mumbai', 'Bangalore', 'Chennai'])
        origin_combo.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)
        origin_combo.current(0)

        ttk.Label(route_frame, text="Destination:").grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.destination_var = tk.StringVar()
        dest_combo = ttk.Combobox(route_frame, textvariable=self.destination_var, values=['Delhi', 'Mumbai', 'Bangalore', 'Chennai'])
        dest_combo.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)
        dest_combo.current(1)

        # Frame for selecting date and time
        date_frame = ttk.LabelFrame(self.root, text='Select Date and Time', padding=(10, 10))
        date_frame.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W+tk.E)

        ttk.Label(date_frame, text="Date:").grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.date_var = tk.StringVar()
        date_entry = ttk.Entry(date_frame, textvariable=self.date_var, width=15)
        date_entry.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)
        date_entry.insert(tk.END, datetime.now().strftime('%Y-%m-%d'))

        # Frame for selecting seats and class
        seat_frame = ttk.LabelFrame(self.root, text='Select Seats and Class', padding=(10, 10))
        seat_frame.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W+tk.E)

        ttk.Label(seat_frame, text="Number of Seats:").grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.seats_var = tk.IntVar()
        seats_entry = ttk.Entry(seat_frame, textvariable=self.seats_var, width=15)
        seats_entry.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)

        ttk.Label(seat_frame, text="Class:").grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.class_var = tk.StringVar()
        class_combo = ttk.Combobox(seat_frame, textvariable=self.class_var, values=['Economy', 'Business'])
        class_combo.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)
        class_combo.current(0)

        # Button for booking
        ttk.Button(self.root, text="Book Ticket", command=self.book_ticket).grid(row=3, column=0, padx=10, pady=10, sticky=tk.W+tk.E)

    def book_ticket(self):
        origin = self.origin_var.get()
        destination = self.destination_var.get()
        travel_date = self.date_var.get()
        num_seats = self.seats_var.get()
        seat_class = self.class_var.get()

        if not origin or not destination or not travel_date or num_seats <= 0:
            messagebox.showerror("Error", "Please fill in all fields correctly.")
            return

        # Mocking booking process (can be replaced with actual booking logic)
        selected_route = None
        for route_id, route in routes.items():
            if route['origin'] == origin and route['destination'] == destination:
                selected_route = route
                break

        if not selected_route:
            messagebox.showerror("Error", "No route found for selected origin and destination.")
            return

        # Check seat availability
        if route_id not in seat_availability:
            messagebox.showerror("Error", "Seats are not available for the selected route.")
            return

        seats_available = seat_availability[route_id][seat_class.lower()]
        if num_seats > seats_available:
            messagebox.showerror("Error", f"Only {seats_available} {seat_class} seats available.")
            return

        # Calculate total price
        total_price = selected_route['price'] * num_seats

        # Simulate payment process (can be extended with actual payment gateway)
        payment_success = self.process_payment(total_price)
        if not payment_success:
            messagebox.showerror("Payment Error", "Payment was not successful. Please try again.")
            return

        # Booking confirmation message
        messagebox.showinfo("Booking Successful", f'Ticket booked successfully!\n\n'
                                                  f'Route: {origin} to {destination}\n'
                                                  f'Date: {travel_date}\n'
                                                  f'Time: {selected_route["departure_time"]} - {selected_route["arrival_time"]}\n'
                                                  f'Seats: {num_seats} ({seat_class})\n'
                                                  f'Total Price: ${total_price}')

    def process_payment(self, amount):
        # Simulate payment processing (can be replaced with actual payment gateway integration)
        return messagebox.askyesno("Payment Confirmation", f"Total Amount:${amount}\n\nProceed With Payment?")


if __name__ == "__main__":
    root = tk.Tk()
    app = TrainTicketApp(root)
    root.mainloop()




    
