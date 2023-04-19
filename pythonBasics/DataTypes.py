print("Hello")
# here are the comments I have defined
print("*************")
a = 3
print(a)
print("*************")
Str = "Gagan Mann"
print(Str)
print("*************")
b, c, d = 4, 6.11, "Gaganpreet"
print(b)
print("*************")
# print(c)
# Concatenation
print("{} {}".format("C value is", c))
print("*************")
print(d)
print(type(d))

# List Data Type Concept
print("*****LIST*****")
StudentList = ["Gagan", 2, 5, "Parvinder"]
print(StudentList[0]) # It would print 0 index value form list
print(StudentList[-1]) # It would print last value form list
print(StudentList[1:3]) # It would print all values from 1st index to 2nd index, It would not consider 3rd Index
StudentList.insert(1, "Mann") # It would add "Mann" at 1 Index
print(StudentList) # ['Gagan', 'Mann', 2, 5, 'Parvinder']
StudentList.append("Pal")  # It would add "Pal" at last Index
print(StudentList) # ['Gagan', 'Mann', 2, 5, 'Parvinder', 'Pal']
StudentList[0] = "GAGAN" # Updating value at 0 index
print(StudentList) # ['GAGAN', 'Mann', 2, 5, 'Parvinder', 'Pal']
del StudentList[2] # Deleting value at 2nd Index
print(StudentList) # ['GAGAN', 'Mann', 5, 'Parvinder', 'Pal']

# Tuple Data Type Concept, Tuple is same as List however difference is Tuple is Immutable, List is not Immutable
# Immutable means we can't change the existing behaviour (For Ex. Can't update any value)
# in List we can declare values under Square Brackets [] howver in Tuple we can declare values under Parentheses ()
print("*****TUPLE****")
Tuple = (1, 2, "Gagan", 4.5, "Pal")
print(Tuple[1]) # It would print 1 index value form Tuple
# Tuple[2] = "GAGAN" # It doesn't allow to update value due to Immutable
print(Tuple)

# Dictionary Data Type Concept, Data in the form of Key-Value Pair
print("*****DICTIONARY****")
Dictionary = {"a":1, 2:"ABC", "c":"Gagan Mann"}
print(Dictionary["c"])
print(Dictionary[2])

dict = {} # Empty Dictionary
dict["firstName"] = "GAGAN"
dict["lastName"] = "MANN"
dict["gender"] = "MALE"
print(dict) # {'firstName': 'GAGAN', 'lastName': 'MANN', 'gender': 'MALE'}










