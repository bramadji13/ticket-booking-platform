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


delete_event(concerts)