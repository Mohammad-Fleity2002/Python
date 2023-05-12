# Exercice 1:
#   Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.
def ex1(l):
    return len(l) == len(set(l))


# test_list = [1, 12, 2, 3, 6, 658]
test_list = [1, 12, 2, 1, 3, 6, 658]
print("ex1:\nThe list: ", test_list, ".")
if ex1(test_list):
    print("The list has no duplication")
else:
    print("The list contain duplication")


# Exercice 2:
#   Write a Python program that removes and prints every third number from a list of numbers until the list is empty.
def ex2(l):
    count = 0
    while len(l):
        count += 2
        count %= len(l)
        print(l[count], end=" ")
        l.pop(count)
    print()


test_list = [1, 25, 30, 7, 50, 585, 70, 666, 89, 9]
print("\nex2:\nthe list:", test_list, "\nThe Output: ")
ex2(test_list)


#  Exercice 3:
#   Write a Python program to get the smallest number from a list
def ex3(l):
    min = l[0]
    for l in l:
        if l < min:
            min = l
    return min


test_list = [1, 12, 2, 1, 3, 6, 658]
print("\nex3\nminimum in the list is: ", ex3(test_list))

# Exercice 4:
#   Write a Python program to sum all the items in a list.


def ex4(l):
    sum = 0
    for v in l:
        sum += v
    return sum


print("\nex4:\nthe sum of element is: ", ex4(test_list))


# Exercice 5:
#   Write a Python program to find the single element appears once in a list where every element appears four times except for one.
def exer5(l):
    count = 0
    for i in range(len(l)):
        count = 1
        for j in range(len(l)):
            if j != i and l[i] == l[j]:
                count += 1
        if count == 1:
            return l[i]
    return -1


test_list = [2, 1, 5, 2, 5, 2, 5, 2, 5, 3, 6, 3, 6, 3, 6, 6]
if exer5 != -1:
    print("\nex5:\nelement \"", exer5(test_list),
          "\" is repeated once within the list")
else:
    print("no element repeated once in the list (exercice 5)")


# Exercice 6:
#   Write a Python program to check if each number is prime in a given list of numbers. Return True if all numbers are prime otherwise False.
def isPrime(n):
    for d in range(2, n//2+1):
        if n % d == 0:
            return False
    return True


def ex6(l):
    for v in l:
        if isPrime(v) == False:
            return False
    return True


print("\nex6:")
test_list = [1, 2, 3, 17, 13, 19]
# test_list = [1, 2, 4, 17, 13, 19]
if ex6(test_list):
    print("All element in the list are prime.")
else:
    print("there is at least one element which is not prime.")


# Exercice 7:
#   Write a Python program to remove duplicates from a list.
def ex7(l):
    l2 = list()
    for i in l:
        isFound = False
        for v in l2:
            if i == v:
                isFound = True
        if isFound == False:
            l2.append(i)
    return l2


test_list = [2, 1, 5, 2, 5, 2, 5, 2, 5, 3, 6, 3, 6, 3, 6, 6]
result_list = ex7(test_list)
print("\nex7:\nOld list: ", test_list,
      "\nnew list (no duplication): ", result_list)


# Exercice 8:
#   Write a Python program to convert a list of characters into a string.
def ex8(l):
    s = ""
    for c in l:
        s += c
    return s


print("\nex8:")
l1 = list("Python")
print("list: ", l1, ",\nstring: ", ex8(l1), ".")
