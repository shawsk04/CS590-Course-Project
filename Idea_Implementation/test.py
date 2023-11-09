# import requests

# verb = "cut"
# obj = "fridge"
# def get_action_probability(verb, obj):
#     # Define the ConceptNet API endpoint
#     api_endpoint = "http://api.conceptnet.io/query"

#     # Define the query to retrieve information about the verb-object relationship
#     query = f"/c/en/{verb}_{obj}"

#     # Make a GET request to the ConceptNet API
#     response = requests.get(api_endpoint + query)

#     if response.status_code == 200:
#         data = response.json()
#         # Extract the weight (probability) of the relationship from the response
#         if 'edges' in data and data['edges']:
#             weight = data['edges'][0]['weight']
#             return weight
#         else:
#             return 0.0  # If no data is found, assume probability is 0
#     else:
#         print("Error:", response.status_code)
#         return 0.0

# if __name__ == "__main__":
#     verb = "eat"
#     obj = "apple"

#     probability = get_action_probability(verb, obj)

#     print(f"The probability of the action '{verb} {obj}' is: {probability:.4f}")


# import conceptnet5 as cn5

# def get_probability(verb, object):
#     # Get the edges from ConceptNet
#     edges = cn5.query_edge(
#         node1=verb,
#         node2=object,
#         rel="/r/HasProperty/d"
#     )

#     # Count the number of edges
#     count = 0
#     for edge in edges:
#         count += 1

#     # Calculate the probability
#     probability = count / len(edges)

#     return probability

# # Example usage
# verb = "eat"
# object = "apple"
# probability = get_probability(verb, object)
# print(f"The probability of '{verb}' '{object}' is {probability:.2f}")


# import conceptnet5 as cn5

# verb = "eat"
# object = "apple"
# relation = "/r/CauseOf"

# edges = cn5.edges(nodes=[{"id": verb}, {"id": object}], rels=[relation])

# probability = 0
# for edge in edges:
#     probability += edge["weight"]

# print("Probability of action:", probability)


# import conceptnet5 as cn
# import numpy as np

# def calculate_probability(verb, object):
#   # Get the edges from ConceptNet for the verb and object
#   verb_edges = cn.query_graph(source=verb, rel="/r/IsA", limit=100)
#   object_edges = cn.query_graph(source=object, rel="/r/IsA", limit=100)

#   # Calculate the intersection of the verb and object edges
#   intersection = set(verb_edges).intersection(set(object_edges))

#   # Calculate the probability of the action as the ratio of the intersection to the union of the verb and object edges
#   probability = len(intersection) / (len(verb_edges) + len(object_edges) - len(intersection))

#   return probability

# # Example usage
# verb = "eat"
# object = "apple"

# probability = calculate_probability(verb, object)
# print("Probability of action \"{}\" with verb \"{}\" and object \"{}\": {}".format(verb, object, probability))

import requests

def find_num_edges(node1, node2):
  # Construct the API URL
  url = "https://api.conceptnet.io/v1/query?start=/c/en/" + node1 + "&end=/c/en/" + node2 + "&rel=/r/Knows"

  # Send the GET request to the API
  response = requests.get(url)

  # Check if the request was successful
  if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Extract the number of edges
    num_edges = len(data['edges'])

    return num_edges
  else:
    print("Error:", response.status_code)
    return None

# Example usage
num_edges = find_num_edges('cat', 'dog')
print(num_edges)