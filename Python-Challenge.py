"""
You are tasked with calculating the minimum classes we need to have so we know how many people to employ. 
Write a function which when given a number of students, 
calculates and prints out a string for your proposed number of classes, and a dictionary showing the allocation.
Key Constraints:
The maximum size of a class is 30
There needs to be a minimum of 2 classes
The distribution of each class should be as even as possible.
We want to hire as little people as possible - so where possible focus on bigger classes, and less of them!
"""


# Function to calculate the number of students and allocate classes
def calculate_class_allocation(numberOfStudents):
    minClassSize = 2
    maxClassSize = numberOfStudents // 30

    # Max always takes the larger argument, adding 1 because no class should be larger than 30
    numberOfClasses = max(minClassSize, maxClassSize) + 1

    # Calculate the size of each class using floor division and modulus for the remainder
    classSize = numberOfStudents // numberOfClasses
    remainderStudents = numberOfStudents % numberOfClasses

    # List to allocate students to class
    allocate = [classSize] * numberOfClasses

    for i in range(remainderStudents):
        allocate[i] += 1

    # Message for number of classes
    classes = "We need {} classes".format(numberOfClasses)

    # Dictionary showing the allocation
    allocateDictionary = {}
    for i in range(numberOfClasses):
        allocateDictionary["Class {}".format(i + 1)] = allocate[i]
    return classes, allocateDictionary


numberOfStudents = int(input("How many students are there? Enter a numerical value: "))
classes, allocateDictionary = calculate_class_allocation(numberOfStudents)
print("Proposed Allocation: {}".format(classes))

print("Allocation:")
for class_name, classSize in allocateDictionary.items():
    print("{}: {} students".format(class_name, classSize))