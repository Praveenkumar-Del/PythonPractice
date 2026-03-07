# # data1 = 123
# # data2 = False
# # data3 = "Good Day!"
# # data4 = None

# # data5 = []
# # data5 = list()
# # data5 = list("it defined")
# # data5 = "it defined".split()
# # data5 = ['a'] * 4

# # data = ["ABC", "BCD", "XYZ", "Y12", "Z23", 123, None]

# # Add
# # delete
# # modify

# # n_states = ["AS", "BI", "OR", "HR"]
# # s_states = ["KA", "KE", "TN", "AP"]

# # # all_states.append(n_states)
# # # all_states.append(s_states)

# # all_states.extend(n_states)

# # print(all_states)

# # all_states.extend(s_states)


# # print(all_states)


# # n_states + s_states

# # states = ["AS", "BI", "OR", "HR"]

# # out = states.remove("BI")

# # print(out)


# # states = ["AS", "BI", "OR", "HR"]
# # n_states = states.copy()


# # print(f"States ==> {states}, {id(states)}")
# # print(f"Northen States ==> {n_states}, {id(n_states)}")

# # import copy

# # states = [["AS", "BI"], ["KA", "KE"]]

# # n_states = copy.deepcopy(states)

# # states[0].append(123)

# # print(f"States ==> {states}")
# # print(f"Northen States ==> {n_states}")



# # str1 = "Trump also ‘has a lot to lose’ from threatened tariffs: French Minister"

# # str2lst = str1.split()

# # print(str2lst)


# # lst1 = ', '.join(str2lst)

# # print(lst1)

# lst1 = ["JAVA_11", "JAVA_07", "JAVA_08"]

# split_data = lst1[0].split('JAVA_')[1]

# split_data = split_data.zfill(4)

# joined_data = f'JAVA_{split_data}'

# print(joined_data)



lst1 = [2, 4, 6, 8]


# x = lambda x: x ** 2


# out = list(map(x, lst1))

# print(out)

# people = [12, 33, 45, 8, 67, 18, 24, 17]

# y = lambda x: x >= 18


# voters = list(filter(y, people))
# print(voters)


# from functools import reduce


# z = lambda a, b: a+b
# people = [1, 2, 3]


# r = reduce(z, people)

# print(r)




# "".split()


print(type("abc"))