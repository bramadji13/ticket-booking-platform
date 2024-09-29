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


display_concerts(concerts)

