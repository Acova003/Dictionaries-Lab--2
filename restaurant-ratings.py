# your code goes here
def get_restaurant_ratings(filename):
    """prints restaurant name and rating in alphebetical order"""

    scores_file = open(filename)
    restaurant_ratings = {}

    what_to_do = int(raw_input("Do you want to (1) See ratings, (2) Add new restaurant, or (3) quit? (Enter 1, 2, or 3): "))
    if what_to_do == 1:
        for line in scores_file:
            restaurant_name, score = line.strip().split(":")
            restaurant_ratings[restaurant_name] = score

        convert_to_list = restaurant_ratings.items()
        sorted_list = sorted(convert_to_list)

        for restaurant in sorted_list:
            print '%s is rated at %s.' % (restaurant[0], restaurant[1])

    elif what_to_do == 2:
        new_restaurant = raw_input("What restaurant would you like to rate?: ")
        new_rating = -1
        while new_rating not in range(1, 6):
            new_rating = int(raw_input("What is your rating score (1-5)?: "))
        restaurant_ratings[new_restaurant] = new_rating

        what_to_do2 = int(raw_input("Do you want to (1) See ratings, (2) Add new restaurant, or (3) quit? (Enter 1, 2, or 3): "))
        while what_to_do2 == 2:
            new_restaurant = raw_input("What restaurant would you like to rate?: ")
            new_rating = -1
            while new_rating not in range(1, 6):
                new_rating = int(raw_input("What is your rating score (1-5)?: "))
            restaurant_ratings[new_restaurant] = new_rating
            what_to_do2 = int(raw_input("Do you want to (1) See ratings, (2) Add new restaurant, or (3) quit? (Enter 1, 2, or 3): "))
        if what_to_do2 == 1:
            for line in scores_file:
                restaurant_name, score = line.strip().split(":")
                restaurant_ratings[restaurant_name] = score

            convert_to_list = restaurant_ratings.items()
            sorted_list = sorted(convert_to_list)

            for restaurant in sorted_list:
                print '%s is rated at %s.' % (restaurant[0], restaurant[1])

        elif what_to_do2 == 3:
            exit()

    elif what_to_do == 3:
        exit()

    scores_file.close()

get_restaurant_ratings("scores.txt")
