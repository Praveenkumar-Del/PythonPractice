# Ordered
# key value pairs
# Unique key
# Mutable

student_data = {
    "Name": "Ramesh",
    "Age": 10,
    "Skills": ["Cricket", "Football"],
    "Parents": {
                    "Name": "Father Name",
                    "Mother": "Mother Name",
                }
}

# out = student_data['Parents']
out = student_data.get('School', 'Govt')
# out = student_data.keys()
# out = student_data.values()
# out = list(student_data.items())
# # student_data['Age'] = 18
# student_data.update({'Parents':{
#                                 "Father": "Sachin",
#                                 "Mother": "Katrina"
#                                 }
#                                 })

# student_data.pop("Name")
# student_data.popitem() 
# student_data.clear() 


student_data = {
    "Name": "Ramesh",
    "Age": 10,
    "Skills": ["Cricket", "Football"],
    "Parents": {
                    "Name": "Father Name",
                    "Mother": "Mother Name",
                }
}

# print(student_data.get('Skills', {})[1])
# fs1 = frozenset((1, 2,3,4,[]))
# fs2 = frozenset([5,6,7,8])
# out = fs1.union(fs2)
# print(out)


# rng1 = range(10)
# out = list(rng1)
# print(out)

# range(10)
#     ==> 0 to 9
# range (start, end, step)
# range(0, 10, 1)

# rng1 = range(-10, 9)
# out = list(rng1)
# print(out)
# lst1 = [1, 2, 3, 4, 5]
# print(lst1[::-1])