target = int(input())
n = int(input())
l = list(map(int, input().split()))


left = 0
right = n - 1
found = False


while left <= right:
   mid = (left + right) // 2
   if l[mid] == target:
       found = True
       break
   elif l[mid] > target:
       right = mid - 1
   else:
       left = mid + 1
      
if found == True:
   print("Target is present")
else:
   print("Target is not present")


Bubble sort

n = int(input())
l = list(map(int, input().split()))


fixThis = n - 1
while fixThis > 0:
   for index in range(fixThis):
       if l[index] > l[index + 1]:
           l[index], l[index + 1] = l[index + 1], l[index]
   fixThis -= 1
print(*l)


