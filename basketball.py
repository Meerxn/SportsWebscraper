import sports 
import csv
import time
import pprint

# Removes empty sports 
def clean_dict(dictionary):
    return {keys:values for keys, values in dictionary.items() if len(values) != 0}

# gets all the sports with upcomming events 
def get_matches():
    all_matches = sports.all_matches()
    # print(type(all_matches)) = 'dict'
    filtered_sports = {}
    for keys, values in all_matches.items():
        matches = str(values).split(',')
        filtered_matches = [x.split("0-0") for x in matches if "0-0" in x]
        filtered_sports[keys] = filtered_matches
    
    return clean_dict(filtered_sports)
    
pp = pprint.PrettyPrinter(depth=6)
pp.pprint(get_matches())
