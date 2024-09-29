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

    print("\nUpdated Concert Data:")
    header = f"{'ID':<10} {'Genre':<15} {'Artist':<25} {'Venue':<30} {'Date':<12} {'VIP Price':<12} {'Regular Price':<15} {'VIP Capacity':<15} {'Regular Capacity':<15}"
    print(header)
    print("-" * len(header))

    for genre, events in concerts.items():
        for event in events:
            show_id, artist, venue, date, price_vip, price_regular, vip_capacity, regular_capacity = event
            print(f"{show_id:<10} {genre:<15} {artist:<25} {venue:<30} {date:<12} {price_vip:<12} {price_regular:<15} {vip_capacity:<15} {regular_capacity:<15}")
    
    return concerts

Add_event(concerts)




