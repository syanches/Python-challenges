import csv
list = [["Star Wars", "Terminator","AI"], ["Dumb", "Matilda", "Leviafan"], ["Men in Black", "I am a Robot", "Evolution"]]

with open("Desktop/Python challenges/movies.csv", "w") as file:
    w = csv.writer(file, delimiter=",")
    w.writerows(list)