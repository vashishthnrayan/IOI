# .format printing method
tour_locations = ['New York', 'Paris', 'Tokyo', 'Sydney','Hong_Kong', 'London', 'Rome', 'Barcelona', 'Dubai', 'Singapore','New York']
target_city = 'New York'
def linear_search(search_list, target_element):
    matches = []
    for idx in range(len(search_list)):
        if search_list[idx] == target_element:
            matches.append(idx)     

    if not matches:
        raise ValueError("{} not found in the list".format(target_element))
    else:
        return matches

result = linear_search(tour_locations, target_city)
print("The target city {} is found at the following indices: {}".format(target_city, result))