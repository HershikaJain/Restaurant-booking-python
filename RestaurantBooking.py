from datetime import datetime

class Restaurant:
    def __init__(self, name, city, area, cuisine, rating, cost_for_two, is_veg):
        self.name = name
        self.city = city
        self.area = area
        self.cuisine = cuisine
        self.rating = rating
        self.cost_for_two = cost_for_two
        self.is_veg = is_veg
        self.slots = []
    
    def add_slot(self, start_time, end_time):
        self.slots.append((start_time, end_time))
    
    def find_available_slots(self, start_time, end_time):
        available_slots = []
        for slot in self.slots:
            if slot[0] >= start_time and slot[1] <= end_time:
                available_slots.append(slot)
        return available_slots

class BookingSystem:
    def __init__(self):
        self.restaurants = []
    
    def register_restaurant(self):
        print("Enter restaurant details:")
        name = input("Name: ")
        city = input("City: ")
        area = input("Area: ")
        cuisine = input("Cuisine: ")
        rating = float(input("Rating (1-5): "))
        cost_for_two = float(input("Cost for two: "))
        is_veg = input("Vegetarian (True/False): ").lower() == 'true'
        
        restaurant = Restaurant(name, city, area, cuisine, rating, cost_for_two, is_veg)
        self.restaurants.append(restaurant)
        print(f"Restaurant '{name}' registered successfully.")
    
    def add_slots(self):
        print("\nEnter slot details:")
        restaurant_name = input("Restaurant name: ")
        start_time_str = input("Start time (YYYY-MM-DD HH:MM): ")
        end_time_str = input("End time (YYYY-MM-DD HH:MM): ")
        
        try:
            start_time = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M")
            end_time = datetime.strptime(end_time_str, "%Y-%m-%d %H:%M")
        except ValueError:
            print("Invalid datetime format. Please use YYYY-MM-DD HH:MM.")
            return
        
        for restaurant in self.restaurants:
            if restaurant.name == restaurant_name:
                restaurant.add_slot(start_time, end_time)
                print(f"Slot added for '{restaurant_name}' from {start_time} to {end_time}.")
                return
        
        print(f"No restaurant found with name '{restaurant_name}'.")
    
    def search_restaurants(self):
        print("\nEnter search criteria (leave blank for any):")
        name = input("Name: ").strip()
        city = input("City: ").strip()
        area = input("Area: ").strip()
        cuisine = input("Cuisine: ").strip()
        min_rating = float(input("Minimum rating (1-5): ").strip() or 0)
        is_veg = input("Vegetarian (True/False): ").strip()
        
        filtered_restaurants = []
        for restaurant in self.restaurants:
            if (not name or restaurant.name.lower() == name.lower()) and \
               (not city or restaurant.city.lower() == city.lower()) and \
               (not area or restaurant.area.lower() == area.lower()) and \
               (not cuisine or restaurant.cuisine.lower() == cuisine.lower()) and \
               (restaurant.rating >= min_rating) and \
               (is_veg.lower() == 'true' and restaurant.is_veg or
                is_veg.lower() == 'false' and not restaurant.is_veg or
                is_veg == ''):
                filtered_restaurants.append(restaurant)
        
        if filtered_restaurants:
            print("\nSearch results:")
            for restaurant in filtered_restaurants:
                print(f"- {restaurant.name} | {restaurant.city} | {restaurant.area} | Cuisine: {restaurant.cuisine} | Rating: {restaurant.rating} | Cost for two: {restaurant.cost_for_two} | Veg: {restaurant.is_veg}")
        else:
            print("No restaurants found matching the criteria.")
    
    def book_table(self):
        print("\nEnter booking details:")
        restaurant_name = input("Restaurant name: ")
        start_time_str = input("Start time (YYYY-MM-DD HH:MM): ")
        end_time_str = input("End time (YYYY-MM-DD HH:MM): ")
        number_of_people = int(input("Number of people: "))
        
        try:
            start_time = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M")
            end_time = datetime.strptime(end_time_str, "%Y-%m-%d %H:%M")
        except ValueError:
            print("Invalid datetime format. Please use YYYY-MM-DD HH:MM.")
            return
        
        restaurants = [r for r in self.restaurants if r.name.lower() == restaurant_name.lower()]
        
        if not restaurants:
            print(f"No restaurant found with name '{restaurant_name}'.")
            return
        
        selected_restaurant = restaurants[0]  # Assuming first restaurant from search result
        
        available_slots = selected_restaurant.find_available_slots(start_time, end_time)
        
        if not available_slots:
            print("No available slots for the requested time.")
            return
        
        # Assuming we're booking the first available slot
        selected_slot = available_slots[0]  # This could be further refined based on business rules
        
        # Confirm booking
        if selected_slot[0] == start_time and selected_slot[1] == end_time:
            print(f"Table booked at {selected_restaurant.name} for {number_of_people} people from {start_time} to {end_time}.")
        else:
            print("Booking failed. Slot might be unavailable or already booked.")
    
    def show_restaurants(self):
        print("\nRegistered Restaurants:")
        for restaurant in self.restaurants:
            print(f"- {restaurant.name} | {restaurant.city} | {restaurant.area} | Cuisine: {restaurant.cuisine} | Rating: {restaurant.rating} | Cost for two: {restaurant.cost_for_two} | Veg: {restaurant.is_veg}")

# Example usage with user input
if __name__ == "__main__":
    booking_system = BookingSystem()
    
    while True:
        print("\nWelcome to the Restaurant Booking System")
        print("1. Register Restaurant")
        print("2. Add Booking Slot")
        print("3. Search Restaurants")
        print("4. Book Table")
        print("5. Show Registered Restaurants")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            booking_system.register_restaurant()
        elif choice == '2':
            booking_system.add_slots()
        elif choice == '3':
            booking_system.search_restaurants()
        elif choice == '4':
            booking_system.book_table()
        elif choice == '5':
            booking_system.show_restaurants()
        elif choice == '6':
            print("Exiting Restaurant Booking System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
