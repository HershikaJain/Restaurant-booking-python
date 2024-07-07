# Restaurant-booking-python

Restaurant Booking System
Overview
This project is a simple restaurant booking system designed to simulate functionalities similar to platforms like Zomato or Swiggy. The system allows restaurant owners to register their restaurants and add booking slots, while users can search for restaurants and book tables.

Features
RegisterRestaurant: Allows restaurant owners to register their restaurants.
AddSlots: Allows restaurant owners to provide available slots for table bookings.
SearchRestaurant: Enables users to search for restaurants based on various attributes such as name, city, area, cuisine, rating, cost for two, and vegetarian/non-vegetarian preferences.
BookTable: Users can book tables for a specified number of people if the table and slot are available.
Requirements
Python 3.x
No additional libraries are required.
Installation
Clone the repository or download the script file.
Ensure you have Python 3.x installed on your system.
Usage
Run the script using the command: python restaurant_booking_system.py
Follow the prompts to interact with the system.
Main Menu
Register Restaurant: Allows a restaurant owner to register a new restaurant.
Add Booking Slot: Allows a restaurant owner to add available booking slots.
Search Restaurants: Allows users to search for restaurants based on various criteria.
Book Table: Allows users to book a table at a selected restaurant.
Show Registered Restaurants: Displays a list of all registered restaurants.
Exit: Exits the application.
Code Structure
Restaurant Class: Represents a restaurant with attributes and methods to manage slots.
BookingSystem Class: Manages the overall system operations including registration, slot addition, searching, and booking.
Example Workflow
Register a restaurant by providing details like name, city, area, cuisine, rating, cost for two, and whether it is vegetarian-friendly.
Add available booking slots for the registered restaurant.
Search for restaurants based on desired criteria.
Book a table by specifying the restaurant name, desired time slot, and number of people.
Error Handling
The system includes basic error handling for input validation, especially for date-time formats and numeric inputs.
Future Enhancements
Extend to handle concurrent booking requests.
Implement a full-fledged web service with exposed APIs.
Add database integration for persistent storage.
