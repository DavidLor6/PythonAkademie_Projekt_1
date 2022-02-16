# Projekt_1 - Textový analyzátor
'''
author = David Lorenc
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
# registrovani uzivatele
users = {
    "bob" : "123",
    "ann" : "pass123",
    "mike" : "password123",
    "liz" : "pass123"
}
# overeni hesla
username = input("username:")
password = input("password:")
if users.get(username) == password:
    print(f"Welcome to the app, {username}.")
    print(f"We have {len(TEXTS)} texts to be analyzed.")
else:
    print("unregistered user, terminating the program..")
    exit()

# vyber textu k analyze
cislo_textu = int(input("Enter a number btw. 1 and 3 to select:"))
if cislo_textu not in [1, 2, 3]:
    print(f"Text no. {cislo_textu} is not available")
    exit()
else:
    vybrany_text = TEXTS[cislo_textu - 1]

