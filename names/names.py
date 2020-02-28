import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

##Before refactoring, this code was polynomial (O(n^2)) because of its nested for-loop
##Now, it is operating at O(n), or linear.
f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


duplicates = []  # Return the list of duplicates in this data structure

BST = BinarySearchTree("names")

for name_1 in names_1:
    BST.insert(name_1)

for name_2 in names_2:
    if BST.contains(name_2):
        duplicates.append(name_2)
# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)




end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
