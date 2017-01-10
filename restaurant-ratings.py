# your code goes here
def get_restaurant_ratings(filename):
    """prints restaurant name and rating in alphebetical order"""

    scores_file = open(filename)
    restaurant_ratings = {}

    for line in scores_file:
        token = line.strip().split(":")
        restaurant_name = token[0]
        score = token[1]
        restaurant_ratings[restaurant_name] = score

    convert_to_list = restaurant_ratings.items()
    sorted_list = sorted(convert_to_list, key=lambda tup: tup[0])
    # print sorted_list

    for restaurant in sorted_list:
        print '%s is rated at %s.' % (restaurant[0], restaurant[1])

    scores_file.close()

get_restaurant_ratings("scores.txt")
