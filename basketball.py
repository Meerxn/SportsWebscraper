import sports 
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
    
def convert_db(dictionary):
    valid_sports = {
        'cricket':'CRICKET',
        'rugby-league':'RUGBY_L',
        'rugby-union':'RUGBY_U',
        'hockey':'HOCKEY',
        'baseball':'BASEBALL',
        'basketball':'BASKETBALL',
        'football':'FOOTBALL',
        'handball':'HANDBALL',
        'soccer':'SOCCER',
        'tennis':'TENNIS',
        'volleyball':'VOLLEYBALL'
    }
    for keys,values in dictionary.items():
        for teams in values:
            try:
                match_information = sports.get_match(valid_sports[keys],teams[0], teams[1])
                print(match_information.match_date)
            except Exception as e:
                print(e)


# pp = pprint.PrettyPrinter(depth=6)
# print(get_matches().keys())

convert_db(get_matches())
