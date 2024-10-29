# Module3Lesson3
Assignment

1. Python Sets Adventure
   Explanation of the Code:
Intersection:

common_routes = our_routes.intersection(competitor_routes) finds the destinations that both airlines fly to.
Difference:

unique_our_routes = our_routes.difference(competitor_routes) finds the destinations unique to your airline.
Union and Difference for Non-Shared Destinations:

all_routes = our_routes.union(competitor_routes) combines the destinations of both airlines.
The program then compares this with a predefined set of all possible destinations to find those that neither airline serves.

2. Set Operations in Data Analysis
  Explanation:
Input List: The list customer_ids contains IDs with duplicates.
Set Conversion: By converting the list to a set (set(customer_ids)), Python automatically filters out the duplicate entries.
Output: The unique customer IDs are printed as a set, which will look something like {'C001', 'C002', 'C003', 'C004'}. Note that the order of elements in a set is not guaranteed.
