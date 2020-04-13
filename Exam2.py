# Sam Cole
# This is exam 2
from random import randint
from Search_Methods import bubble_sort
from Search_Methods import selection_sort
from Search_Methods import insertion_sort
from Search_Methods import merge_sort
from Search_Methods import merge_lists
from Search_Methods import quick_sort_recursion
from Search_Methods import quick_sort
from Search_Methods import partition

examList = []
algorithm = 0
# menu for choosing sort method
while algorithm != 6:
    print("Hello please pick the number of the sorting method you would like to use")
    print("""   
    1. Bubble sort
    2. Selection Sort
    3. Insertion Sort
    4. Merge Sort
    5. Quick Sort
    6. Quit""")
    algorithm = int(input())
    if algorithm != 6:
        # asking user for length of list
        print("How many numbers would you like in the list")
        listLength = int(input())
        # creating the list and putting it into the algorithm
        for x in range(listLength):
            examList.append(randint(0, 100000))
        if algorithm == 1:
            examList = bubble_sort(examList)
        elif algorithm == 2:
            examList = selection_sort(examList)
        elif algorithm == 3:
            examList = insertion_sort(examList)
        elif algorithm == 4:
            examList = merge_sort(examList)
        elif algorithm == 5:
            examList = quick_sort(examList)
        # printing and clearing the list to run it again
        print("This is the sorted list after using the method you selected")
        print(examList)
        examList.clear()

