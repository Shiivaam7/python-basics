# dictonary = {
#     "cat": "a small animal",
#     "table": ["a piece of furniture", "list of facts & figure"]
# }
# print(dictonary)
# subjects = {
#     "python", "java", "c++","python", "javacript", "java","python","java","c++","c"
# }
# print(subjects)
marks = {}

x = int(input("enter phy:" ))
marks.update({"phy" :x})

x = int(input("enter math:" ))
marks.update({"math" :x})

x = int(input("enter chem:" ))
marks.update({"chem" :x})

print(marks)
