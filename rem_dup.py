import array

arr, count = [], [] #declaring two lists/arrays

n = int(input("enter size of array : ")) #getting the array size from user
print()
print("enter elements of array : ")

for x in range(n): #loop for taking array values from user
    i = int(input())
    arr.append(i) 

print("Array entered ", arr) 
print("Array elements after removing duplicates ", end=" ")
m = max(arr)

for x in range(m+1):
    count.append(0) 

for x in range(n): #checking for duplicate value
    count[arr[x]] = count[arr[x]]+1
    if count[arr[x]] == 1:
        print(arr[x], end=" ") 
