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

update_event(concerts)
