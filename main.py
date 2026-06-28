from hotelbookingsystem import HotelBookingSystem

hbs = HotelBookingSystem()

while True:
    print("---------HOTEL BOOKING SYSTEM----------")
    print("1. book room")
    print("2. display all bookings")
    print("3. search booking")
    print("4. update booking")
    print("5. cancel booking")
    print("6. exit")

    choice = input("enter choice:")

    if choice == "1":
        hbs.book_rooms()

    elif choice == "2":
        hbs.display_bookings()

    elif choice == "3":
        hbs.search_booking()

    elif choice == "4":
        hbs.update_booking() 

    elif choice == "5":
        hbs.cancel_booking()

    elif choice == "6":
        print("Thank you")
        break
    
    else:
        print("invalid choice, please try again.")               

