def manage_students():
    students = ['Alice', 'Bob', 'Charlie']
    first_student = students[1]
    last_student = students[-1]
    return first_student, last_student

print('Exercise 1:', manage_students())


def combine_foods():
    foods = ('Pizza', 'Burger', 'Salad')  
    for food in foods:
        meal += food
    return meal

print('Exercise 2:', combine_foods())


def slice_foods():
    foods = ('Pizza', 'Burger', 'Salad') 
    last_two_foods = foods[-2:]
    return last_two_foods

print('Exercise 3:', slice_foods())



def hometown_info():
    home_town = {
        'city': 'Springfield',
        'state': 'Illinois',
        'population': 116250
    }
    home_town_message = f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}"
    return home_town_message

print('Exercise 4:', hometown_info())


def list_home_town_items():
    home_town = {
        'city': 'Springfield',
        'state': 'Illinois',
        'population': 116250
    }
    home_town_items = []
    for key, value in home_town.items():
        home_town_items.append(f"{key} = {value}")
    return home_town_items

print('Exercise 5:', list_home_town_items())


def create_awesome_students():
    students = ['Tina', 'Fred', 'Wilma']
    awesome_students = [f"{student} is awesome!" for student in students]
    return awesome_students

print('Exercise 6:', create_awesome_students())

def filter_foods_with_a():
    foods = ('Taco', 'Burrito', 'Sandwich')
    foods_with_an_a = [food for food in foods if 'a' in food.lower()]
    return foods_with_an_a

print('Exercise 7:', filter_foods_with_a())
