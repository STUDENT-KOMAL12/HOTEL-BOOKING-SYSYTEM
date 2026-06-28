from booking import Booking

class HotelBookingSystem:
    def __init__(self):
        self.bookings = []

    def book_rooms(self):
        booking_id = int(input("enter booking id:"))
        customer_name = input("enter customer name:")
        room_number = int(input("enter room number:"))
        days = int(input("enter number of days:"))
        booking = Booking(booking_id, customer_name, room_number, days)
        self.bookings.append(booking)
        print("room booked sucessfully.")

    def display_bookings(self):
        if len(self.bookings) == 0:
            print("no booking available.")
        else:
            for booking in self.bookings:
                booking.display()

    def search_booking(self):
        booking_id = int(input("enter booking id:"))
        for booking in self.bookings:
            if booking.booking_id == booking_id:
                print("booking found.")
                booking.display()
                return
        print("booking not found.")

    def update_booking(self):
        booking_id = int(input("enter booking id to update:"))
        for booking in self.bookings:
            if booking.booking_id == booking_id:
                booking.customer_name = input("enter new customer name:")
                booking.room_number = int(input("enter new room number:"))
                booking.days = int(input("enter new number of days to update:"))
                print("booking updated sucessfully.")
                return
        print("booking not found.")

    def cancel_booking(self):
        booking_id = int(input("enter booking id:"))
        for booking in self.bookings:
            if booking.booking_id == booking_id:
                self.bookings.remove(booking)
                print("booking canceled sucessfully.")
                return
        print("booking not found.")
        






                
                
           

            
                 