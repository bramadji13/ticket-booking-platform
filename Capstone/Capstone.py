### CAPSTONE PROJECT: Ticket Booking Platform Project (Python Fundamental)
## USER MENU
# Display event function
def display_concerts(concerts):
    while True:
        print("\nMenu:")
        print("1. Show All Concerts")
        print("2. Filter by Genre")
        print("3. Filter by Venue")
        print("4. Sort Concerts")
        print("5. Back to main menu")

        choice = input("Choose menu: ").strip()

        if choice == "1":
            print("\nAll Concerts:")
            header = f"{'ID':<5} {'Genre':<8} {'Artist':<20} {'Venue':<25} {'Date':<12} {'VIP Price':<12} {'Regular Price':<15} {'VIP Capacity':<12} {'Regular Capacity':<8}"
            print(header)
            print("-" * len(header))

            for genre, events in concerts.items():
                for event in events:
                    show_id, artist, venue, date, price_vip, price_regular, vip_capacity, regular_capacity = event
                    print(f"{show_id:<5} {genre:<8} {artist:<20} {venue:<25} {date:<12} {price_vip:<12} {price_regular:<15} {vip_capacity:<12} {regular_capacity:<8}")

        elif choice == "2":
            genre_filter = input("Enter genre: ").strip()
            genre_result = []

            for genre, events in concerts.items():
                if genre == genre_filter:
                    genre_result.extend(events) 

            if genre_result:
                print(f"\nConcerts for {genre_filter}")
                header = f"{'ID':<5} {'Genre':<8} {'Artist':<20} {'Venue':<25} {'Date':<12} {'VIP Price':<15} {'Regular Price':<15} {'VIP Capacity':<12} {'Regular Capacity':<15}"
                print(header)
                print("-" * len(header))

                for event in genre_result:
                    show_id, artist, venue, date, price_vip, price_regular, vip_capacity, regular_capacity = event
                    print(f"{show_id:<5} {genre_filter:<8} {artist:<20} {venue:<25} {date:<12} {price_vip:<15} {price_regular:<15} {vip_capacity:<12} {regular_capacity:<15}")
            else:
                print(f"No concerts found for genre: {genre_filter}")

        elif choice == "3":
            venue_filter = input("Enter venue: ").strip()
            venue_result = []

            for genre, events in concerts.items():
                for event in events:
                    if event[2] == venue_filter: 
                        venue_result.append((genre, *event))  
            
            if venue_result:
                print(f"\nConcerts at {venue_filter}")
                header = f"{'ID':<5} {'Genre':<8} {'Artist':<20} {'Venue':<25} {'Date':<12} {'VIP Price':<15} {'Regular Price':<15} {'VIP Capacity':<12} {'Regular Capacity':<15}"
                print(header)
                print("-" * len(header))

                for genre, show_id, artist, venue, date, price_vip, price_regular, vip_capacity, regular_capacity in venue_result:
                    print(f"{show_id:<5} {genre:<8} {artist:<20} {venue:<25} {date:<12} {price_vip:<15} {price_regular:<15} {vip_capacity:<12} {regular_capacity:<15}")
            else:
                print(f"No concerts found for venue: {venue_filter}")

        elif choice == '4':
            print("Sort by: ")
            print("1. Date")
            print("2. VIP Price")
            print("3. Regular Price")
            print("4. VIP Capacity")
            print("5. Regular Capacity")
            user_sort = int(input("Sorting option: ").strip())

            result = []
            for genre, events in concerts.items():
                for event in events:
                    result.append((genre, *event))  

            if user_sort == 1:
                # Sort by Date
                result.sort(key=lambda x: x[4])  
            elif user_sort == 2:
                # Sort by VIP Price
                result.sort(key=lambda x: int(x[5])) 
            elif user_sort == 3:
                # Sort by Regular Price
                result.sort(key=lambda x: int(x[6])) 
            elif user_sort == 4:
                # Sort by VIP Capacity
                result.sort(key=lambda x: x[7])  
            elif user_sort == 5:
                # Sort by Regular Capacity
                result.sort(key=lambda x: x[8])
            else:
                print("Invalid sorting option.")
                continue

            print("\nSorted Concerts:")
            header = f"{'ID':<5} {'Genre':<8} {'Artist':<20} {'Venue':<25} {'Date':<12} {'VIP Price':<12} {'Regular Price':<15} {'VIP Capacity':<12} {'Regular Capacity':<8}"
            print(header)
            print("-" * len(header))

            for item in result:
                genre, show_id, artist, venue, date, price_vip, price_regular, vip_capacity, regular_capacity = item
                print(f"{show_id:<5} {genre:<8} {artist:<20} {venue:<25} {date:<12} {price_vip:<12} {price_regular:<15} {vip_capacity:<12} {regular_capacity:<8}")

        elif choice == '5':
            break

# Booking ticket function
def booking_ticket(concerts):
    concert_name = input("Enter show ID: ").strip().upper()
    amount_ticket = int(input("Enter amount of ticket: ").strip())
    
    if amount_ticket > 2:
        print("Sorry, maximum amount is 2.")
        return

    class_ticket = input("Enter class (VIP or Regular): ").strip()
    if class_ticket not in ["VIP", "Regular"]:
        print("Invalid ticket class. Only VIP and Regular are available.")
        return

    for genre, events in concerts.items():
        for event in events:
            if event[0].upper() == concert_name:
                ticket_price = int(event[4]) if class_ticket == "VIP" else int(event[5])
                capacity = event[6] if class_ticket == 'VIP' else event[7]

                if amount_ticket > capacity:
                    print(f"Sorry, not enough {class_ticket} tickets available.")
                    return
                
                # Update capacity
                if class_ticket == 'VIP':
                    event[6] -= amount_ticket
                else:
                    event[7] -= amount_ticket
                
                total_cost = ticket_price * amount_ticket

                print(f"You are booking {amount_ticket} {class_ticket} ticket(s) for {event[1]}.")
                print(f"Total cost is {total_cost} Rupiah.")

                while True:
                    try:
                        payment = int(input("Please enter your payment amount: "))
                    except ValueError:
                        print("Invalid input! Please enter a valid amount.")
                        continue

                    if payment < total_cost:
                        print("Insufficient funds! Please enter more money.")
                    else:
                        change = payment - total_cost
                        print(f"Thank you for your purchase! Your change is {change} Rupiah." if change > 0 else "Thank you for your purchase! See you at the show.")
                        break
                return

    print("Invalid show ID. Please try again.")

            
## ADMIN MENU
# Add event function
def Add_event(concerts):
    while True:
        add_genre = input("Enter genre: ")
        add_showID = input("Enter show ID: ")

        # Check if show ID already exists in any genre
        if any(event[0] == add_showID for events in concerts.values() for event in events):
            print("Duplicate ID. Input another: ")
            continue

        add_artist = input("Enter artist name: ")
        add_venue = input("Enter venue: ")
        add_date = input("Enter showdate (YYYY-MM-DD): ")
        add_price_VIP = int(input("Enter VIP price (Rupiah): "))
        add_price_regular = int(input("Enter regular price (Rupiah): "))
        add_VIP_capacity = int(input("Enter VIP Capacity: "))
        add_Regular_capacity = int(input("Enter Regular capacity: "))

        new_event = [add_showID, add_artist, add_venue, add_date, add_price_VIP, add_price_regular, add_VIP_capacity, add_Regular_capacity]

        if add_genre in concerts:
            concerts[add_genre].append(new_event)
        else:
            concerts[add_genre] = [new_event]
        
        print("Event successfully added.")

        add_more = input("Do you want to add more events (y/n): ")
        if add_more.lower() == "n":
            break
    
    # Print updated concert data
    print("\nUpdated Concert Data:")
    header = f"{'ID':<10} {'Genre':<15} {'Artist':<25} {'Venue':<30} {'Date':<12} {'VIP Price':<12} {'Regular Price':<15} {'VIP Capacity':<15} {'Regular Capacity':<15}"
    print(header)
    print("-" * len(header))

    for genre, events in concerts.items():
        for event in events:
            show_id, artist, venue, date, price_vip, price_regular, vip_capacity, regular_capacity = event
            print(f"{show_id:<10} {genre:<15} {artist:<25} {venue:<30} {date:<12} {price_vip:<12} {price_regular:<15} {vip_capacity:<15} {regular_capacity:<15}")

    return concerts


# Delete event function
def delete_event(concerts):
    while True:
        del_genre = input("Enter genre name: ").strip()
        del_showID = input("Enter show ID to delete: ").strip()

        if not del_genre or not del_showID:
            print("Please enter genre and show ID!")
            continue

        if del_genre not in concerts:
            print("Genre not found.")
            continue

        event_found = False
        for event in concerts[del_genre]:
            if event[0] == del_showID:
                concerts[del_genre].remove(event)
                event_found = True
                print("Event deleted.")
                break
        
        if not event_found:
            print("Event not found.")
        
        del_more = input("Delete more events (y/n): ").strip().lower()
        if del_more == "n":
            break

    print("\nUpdated Concert Data:")
    header = f"{'Show ID':<7} {'Genre':<10} {'Artist':<25} {'Venue':<30} {'Date':<12} {'VIP Price':<12} {'Regular Price':<15} {'VIP Capacity':<12} {'Regular Capacity':<15}"
    print(header)
    print("-" * len(header))

    for genre, events in concerts.items():
        for event in events:
            show_id, artist, venue, date, price_vip, price_regular, vip_capacity, regular_capacity = event
            print(f"{show_id:<7} {genre:<10} {artist:<25} {venue:<30} {date:<12} {price_vip:<12} {price_regular:<15} {vip_capacity:<12} {regular_capacity:<15}")
    return concerts

# Update event function
def update_event(concerts):
    while True:
        update_genre = input("Enter genre: ").strip()
        update_showID = input("Enter show ID you want to update: ").strip()

        if not update_genre or not update_showID:
            print("Please enter both genre and show ID!")
            continue

        if update_genre not in concerts:
            print("Genre not found.")
            continue

        events = concerts[update_genre]
        event_found = False
        
        for event in events:
            if event[0] == update_showID:
                event_found = True
                print(f"Current details for Show ID {update_showID}:")
                print(f"Artist: {event[1]}")
                print(f"Venue: {event[2]}")
                print(f"Date: {event[3]}")
                print(f"VIP Price: {event[4]}")
                print(f"Regular Price: {event[5]}")
                print(f"VIP Capacity: {event[6]}")
                print(f"Regular Capacity: {event[7]}")

                while True:
                    print("Which field would you like to update?: ")
                    print("1. Artist")
                    print("2. Venue")
                    print("3. Date")
                    print("4. VIP Price")
                    print("5. Regular Price")
                    print("6. VIP Capacity")
                    print("7. Regular capacity")

                    choice = input("Choose number: ").strip()

                    try:
                        if choice == '1':
                            event[1] = input("Enter artist name: ").strip()
                            break
                        elif choice == '2':
                            event[2] = input("Enter new venue: ").strip()
                            break
                        elif choice == '3':
                            event[3] = input("Enter new show date (YYYY-MM-DD): ").strip()
                            break
                        elif choice == '4':
                            event[4] = int(input("Enter new VIP price: ").strip())
                            break
                        elif choice == '5':
                            event[5] = int(input("Enter new Regular price: ").strip())
                            break
                        elif choice == '6':
                            event[6] = int(input("Enter new VIP capacity: ").strip())
                            break
                        elif choice == '7':
                            event[7] = int(input("Enter new Regular capacity: ").strip())
                            break
                        else:
                            print("Invalid choice. Try again!")
                            continue

                        print("Update success!")
                    except ValueError:
                        print("Invalid input. Try again!")       
        
        
        if not event_found:
            print(f"Event with Show ID {update_showID} not found in genre {update_genre}.")

        update_more = input("Do you want to update another event (y/n): ").strip().lower()
        if update_more != 'y':
            break



    print("\nUpdated Concert Data:")
    header = f"{'Show ID':<7} {'Genre':<10} {'Artist':<25} {'Venue':<30} {'Date':<12} {'VIP Price':<12} {'Regular Price':<15} {'VIP Capacity':<12} {'Regular Capacity':<15}"
    print(header)
    print("-" * len(header))

    for genre, events in concerts.items():
        for event in events:
            show_id, artist, venue, date, price_vip, price_regular, vip_capacity, regular_capacity = event
            print(f"{show_id:<7} {genre:<10} {artist:<25} {venue:<30} {date:<12} {price_vip:<12} {price_regular:<15} {vip_capacity:<12} {regular_capacity:<15}")
    return concerts

def main():
    counter = 0
    while counter != 3:
        print("Welcome to Ticketin!")
        print("\nChoose role: ")
        print("1. User")
        print("2. Admin")
        print("3. Exit Program")

        option = input("Choose role: ").strip()
        # Initialize data
        concerts = {
            "Rock": [
                ["C001", "The Rolling Stones", "Gelora Bung Karno Stadium", "2024-10-01", "3000000", "1500000", 100, 200],
                ["C002", "Led Zeppelin", "Istora Senayan", "2024-11-15", "3500000", "1700000", 120, 180]
            ],
            "Pop": [
                ["C003", "Taylor Swift", "Jakarta International Expo", "2024-12-05", "3800000", "1800000", 150, 250],
                ["C004", "Ariana Grande", "Kota Kasablanka", "2024-12-20", "3500000", "1750000", 130, 220]
            ],
            "Jazz": [
                ["C005", "Miles Davis", "Jakarta Arts Theater", "2024-11-20", "2500000", "1200000", 80, 150],
                ["C006", "John Coltrane", "Gedung Kesenian Jakarta", "2024-12-10", "2800000", "1300000", 90, 160]
            ],
            "K-Pop": [
                ["C007", "BTS", "Gelora Bung Karno Stadium", "2024-11-25", "4000000", "2000000", 200, 300],
                ["C008", "BLACKPINK", "Jakarta International Expo", "2024-12-15", "3800000", "1900000", 180, 270]
            ]
        }

        if option == '1':
            while True:
                print("\nUser Menu: ")
                print("1. Display events")
                print("2. Book tickets")
                print("3. Exit program")
                choice = input("Choose menu: ")

                if choice == '1':
                    display_concerts(concerts)
                elif choice == '2':
                    booking_ticket(concerts)
                elif choice == '3':
                    print("Goodbye!")
                    break
                else:
                    print("Try again.")

        elif option == '2':
            while True:
                print("\nAdmin Menu: ")
                print("1. Add event")
                print("2. Delete event")
                print("3. Update event")
                print("4. Exit program")
                choice = input("Choose menu: ")

                if choice == '1':
                    Add_event(concerts)
                elif choice == '2':
                    delete_event(concerts)
                elif choice == '3':
                    update_event(concerts)
                elif choice == '4':
                    print("Goodbye!")
                    break
                else:
                    print("Invalid option.")
        
        elif option == '3':
            print("Goodbye!")
            break
        
        else:
            counter += 1
            print(f"Invalid role. Attempt {counter}/3")
            

main()
