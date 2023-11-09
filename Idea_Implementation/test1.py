import conceptnet5

# Load the ConceptNet API
conceptnet = conceptnet5.Client()

# Define a function to calculate the probability of an action for an object
def calculate_probability(action_concept, obj_form, verb_form):
    # Query ConceptNet for the probability
    results = conceptnet.query(rel='HasA', source=verb_form, target=action_concept)

    # If there is a result, extract the probability
    if results:
        probability = results[0]['value'] / 100.0
        return probability
    else:
        return 0.0
    
verb = "cut"
obj = "fridge"

results = conceptnet.query(rel='IsA', source=verb, target=obj)

                # If there is a result, calculate the probability
if results:
    action_concept = results[0]['target']['label']                   
    action_prob = calculate_probability(action_concept, obj, verb)
                    
                    

    print (action_prob)