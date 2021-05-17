# make a list of your favorite musicians

musician = []
musician.append("Justin Bieber")
musician.append("Ariana Grande")
musician.append("Wiz Khalifa")


# make a taple of place's longitude and latitude that you've ever visited

places = ((43.0351, 141.2049), (35.4922, 138.4259), (18.2678, 129.3621))


# make a dictionary of your characters

characters = {"tall": "164.0",
              "weight": "70.0",
              "trend": "mood"
}


# a program asking to input an optional key of the above dictionary

n = input("input my character:")
if n in characters:
    character = characters[n]
    print(character)
else:
    print("not found")


# add your favorite musicians to a dictionary key
# the keys have lists of songs of the musicians as a value

songs = {"Justin Bieber": ("Sorry", "What Do You Mean?"),
         "Ariana Grande": ("Break Free", "Last One Time"),
         "Wiz Khalifa": ("Black and Yellow", "See You Again")
}
