import json
from difflib import get_close_matches

data = json.load(open("data.json"))

print("English Dictionary")
print("==================")
print('\n')


def translate(word):
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        match = input(
            f"Do you mean {get_close_matches(word , data.keys())[0]} instead? Enter Yes or No: ").upper()[0]
        if match == 'Y':
            return data[get_close_matches(word, data.keys())[0]]
        elif match == 'N':
            return "Please check your word"
        else:
            return "We didn't understand your entry."
    else:
        return "Please check your word"


while True:
    word = input("Enter Word: ").lower()
    output = translate(word)

    if type(output) == list:
        for item in output:
            print(item)
            print("\n")
    else:
        print(output)
        print("\n")
