from copy import copy
from random import randrange
import copy

arr = [
    [1, 1, 2, 8, 5, 7, 6, 6, 6, 6, 7, 3, 3, 1, 2],
    [7, 3, 2, 3, 1, 6, 4, 4, 2, 4, 5, 3, 8, 1, 4],
    [7, 7, 4, 7, 5, 3, 7, 4, 5, 1, 6, 8, 4, 3, 4],
    [2, 6, 5, 2, 7, 4, 1, 6, 7, 2, 3, 7, 7, 1, 6],
    [7, 5, 7, 8, 1, 4, 2, 1, 7, 8, 4, 7, 6, 2, 7],
    [1, 7, 1, 2, 2, 7, 6, 4, 1, 3, 3, 2, 4, 5, 7]
    ]
# for member in arr :
#     fit = 0
#     for i in range(15) : 
#         for j in range(i+1,15) :
#             if member[i]==member[j] :
#                 fit+=1
#     print(member,"==>",fit)



#crossover
next_generation1 = []
for i in range(len(arr)) :
    for j in range(i+1,len(arr)) :
        index = randrange(15)
        next_generation1.append(arr[i][:index]+arr[j][index:])
    
#mutation 
next_generation2 = []
for member in arr : 
    index = randrange(15)
    color = randrange(1,9)
    while(color == member[index]) :
        color = randrange(1,9)
    new_member = copy.deepcopy(member)
    new_member[index] = color
    next_generation2.append(new_member)

print("crossover : ")
for member in next_generation1 :
    print(member)

print("MUTATION : ")
for member in next_generation2 :
    print(member)
print("\n\n\n")
new_arr = next_generation1 + next_generation2
for member in new_arr :
    fit = 0
    for i in range(15) : 
        for j in range(i+1,15) :
            if member[i]==member[j] :
                fit+=1
    print(member,"==>",fit)