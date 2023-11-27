def madlib():
    noun1 = input("Noun: ")
    place1 = input("Place: ")
    verb = input("Verb: ")
    place2 = input("Place: ")
    famous_person = input("Famous Person: ")
    noun2 = input("Noun: ")
    
    madlib = f"Jonathan has a/an {noun1} big enough to fill a whole {place1}.\nHe loves it so much and he even {verb} \
with it every day.\nOne time he went to a/an {place2} and showed it to {famous_person}.\n{famous_person} loved it and gave him \
a/an {noun2} in return."
    
    print(madlib)