# If - Else
# condition checher
# if condition:
#    code to run if true
# elif another condition:
#   code to run if another condition is true
# else:
#    code to run if none was true

# condition > true / false


desserts =  ["ice cream", "Chocolate", "apple crisp", "baklava", "cookies", "katmer"]
favorite_dessert = "katmer"

for dessert in desserts:
    if dessert == favorite_dessert:
        print(f"{dessert} is my favorite!!")
        
    else:
        print(f"{dessert} is not the best...")
        
# Logical tests
# a == b -> if a is equal to b (value)
# a != b -> if a is not equal to b (value)
# a > b -> if a is bigger than to b (value)
# a >= b -> if a is bigger than to b or equal (value)
# a < b
# a <= b
# a in b
print(5==5)
print(6==5)
print(6!=5)
print(5>5)
print(5<=5)

print(3 in [4,5])
print("a" in "car")

print("Cat" == "cat")
print("Cat".lower() == "cat")

print(5==5) #true
print(6==5) #false
print(6!=5)
print(5>5)
print(5<=5)

print(10==10)
print("Dog".lower() in "dog")
print(6<5)
print(5>6)
print(9<=5)

students = ["bedir", "tarık", "yusuf", "jonas", "diana", "huzeyfe", "joseph"]

if len(students) > 4:
    print("The class is big enough")
    
for student in students:
    if len(student) > 5:
        print(f"the latters here are too crowded: {student}")
        
    elif student[0] == "j":
        print(f"Well, who do we have here! Such an honor: {student}")
        
    else:
        print(f"Well this one is just perfect: {student}")
        
        
lists = ["bedir", "tarık", "jonas", "huzeyfe"]


if len(lists) > 3:
    print("This room being crowded than 3 people")
    
lists.pop()
lists.pop()

if len(lists) > 3:
    print("This room being crowded than 3 people")
    
def crowd_test():
    lists = ["bedir", "tarık", "jonas", "huzeyfe"]


    if len(lists) > 3:
        print("This room being crowded than 3 people")
    
    lists.pop()
    lists.pop()

    if len(lists) > 3:
        print("This room being crowded than 3 people")
    
    else:
        print(f"Yes this room uncrowded {lists}")
        


lists = ["bedir", "tarık", "jonas", "huzeyfe"]


if len(lists) > 3:
    print("This room being crowded than 3 people")
    
lists.pop()
lists.pop()

if len(lists) > 3:
    print("This room being crowded than 3 people")
    
else:
    print("Yes this room uncrowded")
    
lists.append("nilgün")
lists.append("yusuf")
lists.append("diana")
lists.append("huzeyfe")

if len(lists) > 5:
    print("there being a mob in the room")
elif len(lists) >= 3:
    print("room being crowded")
elif len(lists) == 1 or 2:
    print("room not being crowded")
elif len(lists) == 0:
    print("The room is being empty")
    
    
# Every value has a truth value
def truth_value(value):
    if value:
        print(f"This({value}),{type(value)}evaluates to True.")
        
    else:
        print(f"This({value}),{type(value)}evaluates to False.")
        
        
# int
# 0 - false
# anything else is true
truth_value(0)
truth_value(1)
truth_value(-1)

# Strings
truth_value("")

# Special - None
truth_value(None)


# Boolean
truth_value(True)
truth_value(False)

# Floats truth values ?
truth_value(0.1)


# Make a list of ten aliens, each of which is one color: 'red', 'green', or 'blue'.
    # You can shorten this to 'r', 'g', and 'b' if you want, but if you choose this option you have to include a comment explaining what r, g, and b stand for.
    # Red aliens are worth 5 points, green aliens are worth 10 points, and blue aliens are worth 20 points.
    # Use a for loop to determine the number of points a player would earn for destroying all of the aliens in your list.

aliens = ["green", "blue","red","blue","green","red","blue","green","red","blue"]
puan = 0

for alien in aliens:
    if alien == "green":
        puan += 10
        
    elif alien == "red":
        puan += 5
        
    elif alien == "blue":
        puan += 20

print(puan)



people = ['t', 't', 'p1', 'p2', 'p4', 'p6', 's1', 's2', 's5', 's4', 's3']


def calculate_points(people):
    sum_point = 0
    for person in people:
        if person == "t":
            sum_point += 5
            
        elif person[0] == "p":
            sum_point += 15
        
        else:
            num = person[1]
            if "p" + num in people:
                sum_point += 10
    print(sum_point)
 
calculate_points(people)
