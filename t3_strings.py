# statement = 'ABCXDEFXMNO'
# st2 = statement.split()
# print(st2)

# # String Immutability
# str1 = "India"
# str1[0] = "D"
# str1 = "SriLanka"


# Single, Double and Triple Quotes
# news = "As the \"BJP-Shiv Sena\" combine inched closer"
# news = 'As the "BJP-Shiv Sena" combine inched closer'
# news = 'As the "BJP-Shiv Sena" \'combine\' inched closer'
# news = '''As the "BJP-Shiv Sena" 'combine' inched closer'''
    
# print(news)



#               Dynamic Data passing
# name = "Ajith"
# place = "Delhi"

# out = "I am {1}, and I am from {1}".format(name, place)
# out = f"I am {name}, and I am from {place}"

# print(out)
# # data = [("Ajith", "Delhi"), ("Virat", "Bangalore"), ("Rohit", "Mumbai")]

# # for name, place in data:
# #     Out = f"I am {name}, and I am from {place}"
# #     print(Out)


# Builtin Methods in String

# upper()
# lower()
# capitalise()
# count('a')
# endswith("closer")
# find("the")


# str1 = """From 84 seats in the 2017 elections, his party Shiv Sena (UBT), 
# formed three years ago, won 64 seats this time. 
# Eknath Shinde, who is the claimant of the Shiv Sena now, 
# got only 27 seats in Mumbai. The results show a consolidation 
# of the Marathi vote bank, after the Thackerays trumped Eknath 
# Shinde in the core Marathi voter belts of Mumbai."""

# out = str1.find("2017DEC12")

# print(out)

# import os

# print(os.listdir())

# for file in os.listdir():
#     if file.endswith(".py"):
#         print(file)
