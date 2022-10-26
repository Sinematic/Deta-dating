"""

import sys
import csv
import string
# from classes import user

try:
    with open("../data/id.csv", "wt", encoding="UTF-8") as file:
        name = "Firstname"
        age = "Age"
        print(name, age, sep=";", file=file)

except FileNotFoundError as e:
    print(f"Document non trouvé. Motif{e}")
    sys.exit(1)

user = user.User()

"""

