import requests

def calculate_probability(verb, obj):
    response = requests.get('http://api.conceptnet.io/relatedness?node1=/c/en/' + verb + '&node2=/c/en/' + obj)
    obj = response.json()
    return obj.get('value')

objects = ["bell_pepper", "bowl" , "bread" ,"bread_container" ,"cabinet" ,"cheese" ,"cheese_container" ,"condiment_container" ,"cooking_utensil" ,"cucumber" ,"cup" ,"cutting_board" ,"drawer" ,"eating_utensil" ,"egg" ,"fridge" ,"fridge_drawer","grocery_bag","lettuce","oil_container" ,"onion" ,"pan" ,"paper_towel" ,"plate" ,"pot","seasoning_container" ,"sponge" ,"tomato" ,"tomato_container"];

verbs = ["close", "cut", "divide/pull apart", "mix", "move around", "open", "operate", "pour", "put", "take", "wash"];

for i in range(0, len(verbs)):
    for j in range(0, len(objects)):
        verb = verbs[i]
        obj = objects[j]
        action = verb + ' ' + obj
        prob = calculate_probability(verb, obj)
        print("Probability for action relating verb ->", verb, "and object ->", obj, "is", prob )