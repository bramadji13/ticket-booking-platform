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

        

booking_ticket(concerts)
        