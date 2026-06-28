class Booking:
    def __init__(self, booking_id, customer_name, room_number, days):
         self.booking_id = booking_id
         self.customer_name = customer_name
         self.room_number = room_number
         self.days = days

    def calculate_bill(self):
         room_charge = 2000
         return self.days * room_charge 
    
    def display(self):
         print("booking details.")
         print("booking_id:", self.booking_id)
         print("customer_name:", self.customer_name)
         print("room_number:", self.room_number)
         print("days:", self.days)
         print("total_bill:", self.calculate_bill())
         print("-" * 50)
         
                 