# Overview
This Python-based system allows users to easily book concert tickets and admins to efficiently manage event details. It provides a seamless user experience by integrating event browsing, ticket purchasing, seat capacity tracking, and payment processing.

## Features ##
**User**
1. View available concerts by artist, genre, and venue.
2. Filter events based on date or ticket class (VIP or Regular).
3. Book up to 2 tickets per event.
4. Track available VIP and Regular seat capacity.
5. Make secure payments with automatic change calculation. 

**Admin**
1. Manage concert events (add, update, delete).
2. Update artist, venue, date, ticket prices, and seat capacity.
3. Delete events using the artist name.
4. Ensure accurate seat capacity tracking for each ticket class.

## Data Structure ##
Concert data is structured with:
<br>
* Show ID: Unique identifier for each event.
* Artist: Name of the performing artist.
* Venue: Event location.
* Date: Concert date.
* VIP/Regular Price: Ticket pricing by class.
* VIP/Regular Capacity: Available seats for each class.
