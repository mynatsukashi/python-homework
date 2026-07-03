"""
4. Pick a random letter
Pick a random city from the cities list using random.choice(). Take its first letter and store it as the required letter for the round.
5. Ask the player for a city
Print the required letter. Ask the player to type a city name.
6. Validate the input
Check the following conditions in order:

The input is not empty.
The input starts with the required letter.
The input is in the cities list.
The input is not already in used_cities.

7. Update game state based on validation

If all checks pass: add the city to used_cities, increase score by 1, print a success message.
If any check fails: print a message stating which check failed. Do not change the score.

8. Repeat for multiple rounds
Use a for loop to repeat steps 4–7 for 5 rounds.
9. Display final results
After the loop, print the final score and the full used_cities list.
10. Save results to a file
Open results.txt in write mode. Write the final score and the list of used cities to the file. Wrap this in try/except.
"""

# File cities.txt was created. To make it more comfortable to use, rename it CITY (constant)

CITY = "cities.txt"

# Create a list with cities for easier transfer to our file
cities = ["Tbilisi", "Kutaisi", "Telavi", "Batumi", "Rustavi", "Gori", "Tskhaltubo", "Poti"]

# Define function to easily read a list of cities. In case of non-existed file, print an empty file.
def read_city():
    try:
        with open (CITY) as f:
            return [item.strip() for item in f if item.strip()]
    except FileNotFoundError:
        return []

# Add cities to the file
with open(CITY, "w") as f:
    for city in cities:
        f.write(city + "\n")

# Set up game state
chosen_cities_by_user = []
score = 0
