# Define the flight routes for our airline and the competitor
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

# Task 1: Find destinations that both airlines fly to
common_routes = our_routes.intersection(competitor_routes)
print("Destinations that both airlines fly to:", common_routes)

# Task 2: Find destinations unique to our airline
unique_our_routes = our_routes.difference(competitor_routes)
print("Destinations unique to our airline:", unique_our_routes)

# Task 3: Check for destinations that neither airline shares
# Combine both routes to find all destinations
all_routes = our_routes.union(competitor_routes)

# Find destinations that neither airline flies to
# Assuming we have a list of all possible destinations
all_possible_destinations = {"LAX", "JFK", "CDG", "DXB", "LHR", "BKK", "NRT", "SIN"}
neither_airline_routes = all_possible_destinations.difference(all_routes)

print("Destinations that neither airline shares:", neither_airline_routes)
