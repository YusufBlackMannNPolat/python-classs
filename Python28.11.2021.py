# Lists and Tuples
# Lists
# Variable_name = [items]
students = ["tarik", "diana", "yusuf", "nilgün", "jonas", "huze"]


# Naming and Defining
colors = ["r", "g", "b"]

# Accesing elements
# 0, 1, 2, 3, ....., n
# ith element -> name_of_the_variable[i]
print(colors[0])

the_color = colors[0]
print(the_color)
print(colors[1])

# Access reverse
print(colors[-1])

# no no no
# print(colors[-4])
# IndexError: list index out of range
# print(colors[3])
# IndexError: list index out of range

# Exercises
# -1
programminglangu = ["python", "c", "java"]
print(programminglangu)

# -2
# Store the values "python", "c", amd "java" in a list.
# Print a statement about each of these values, using their position in the list
# Your statement could simply be, "A nice programming language is value."
for y in programminglangu:
    print(y + " A nice programming language")

# -3
donanımparça = ["display card", "processor", "motherboard", "ram"]
print(donanımparça[2] + " nothing on my list can work without it")

# Loops in Lists
for name in students:
    print(name)
    
# syntax
# for var_name in list_name:
#   whatever code to run

for x in students:
    print(x + " is not that great.")
    print("And " + x + " knows it!")
print("That's all a joke")

# Enumerate
tech_comps = ["Microsoft", "Apple", "Google"]

for i, comp in enumerate(tech_comps):
    print(str(i + 1), comp.title())

l1 = ["1", "2", "3"]
l2 = ["one", "two", "three"]    
for i in range(len(l1)):
    print(l1[i], l2[i])
    
# Exercises
# -0:
# repeat first list, but this time use a loop to print out each value in the list.
for y in students:
    print(y + " A good student")

# -1:
# repeat first list, but this time usa a loop to print out your statements. make sure you are writing the same sentence for all values in your list. 
# loops are not effective when you are trying to generate different outout for each value in your list

# Common Op.
tech_comps[0] = "Amazon"

print(tech_comps)

# Find
#print(tech_comps.index("Microsoft"))
# ValueError: 'Microsoft' is not in list

# If exists
print("Microsoft" in tech_comps)
print("Apple" in tech_comps)

# Appending
tech_comps.append("Microsoft")
print(tech_comps)

# Inserting
tech_comps.insert(0, "DeepMine")
print(tech_comps)

social_medias = []

# add comps
social_medias.append("Facebook")
social_medias.append("İnstagram")
social_medias.append("WhatsApp")

for i, sm in enumerate(social_medias):
    print(str(i +1) + "-" + sm.title())
    
# sorting a list
tech_comps.sort()
for i, tc in enumerate(tech_comps):
    print(str(i +1) + "-" + tc.title())
    
tech_comps.sort(reverse=True)
for tc in tech_comps:
    print(tc)

#sort vs sorted
tech_comps_sorted = sorted(tech_comps)
print(tech_comps_sorted)

# Exercise
# 0: Reverse print a list

students.reverse()
print(students)

# Numerical sorting
nums = [1,3,2,6,5,4]
print(sorted(nums))
print(sorted(nums, reverse=True))
nums.reverse()
print(nums)

# length
length = len(nums)
print(length)

# - Start with the list you created in exercise 0:0
# - You are going to print out the list in a number of diffrent orders.
# Each time you print the list use a for loop rather than printing the raw list
# print a massage each time telling us what order we should see the list in

for i in students:
    print(i + " Normal sıra")

students_sorted = sorted(students)
    
for i in students_sorted:
    print(i + " Alfabetik sıra")

students_sorted.reverse()

for i in students_sorted:
    print(i + " Ters alfabetik sıra")
    
for i in students_sorted:
    print(i + " Alfabetik sıra")
    
    
    
    
# remove
# by pos
nums = [1,3,2,5,4]
del nums[0]
print(nums)

# by value
nums.remove(2)
print(nums)

nums = [2, 2, 3, 4]
nums.remove(2)
print(nums)

# pop
nums = [1, 2 ,3 ,4 ,5]
last = nums.pop()
print(nums)
print(last)

one = nums.pop(0)
print(nums)
print(one)

# Exercise
# 0:

#famous_people =["Bill Gates", "Jeff Bezos", "Elon Musk", "Mark Zuckerberg"]


# Slicing
# variable_name[start_idx:stop_index:step_size]
# [0:end:1]
nums = [1, 2 ,3 ,4 ,5]
print(nums[0: 3])
print(nums[::2])

copy_nums = nums[:]
copy_nums_wrong = nums
nums[0] = 2
print(nums)
print(copy_nums)
print(copy_nums_wrong)

# range
# range(start, end, step)

for n in range(1 , 11, 2):
    print(n)
    
    
nums = list(range(1, 11, 2))
print(nums)



# min, max, sum
ages = [23 ,25 ,35 ,18 ,16 ,77]

young = min(ages)
oldest = max(ages)
total_age = sum(ages)

print(young,oldest,total_age)