#Build Min Heap (Heapify)
# Time: 0(n), Space: 0(1)

A = [-4,3,1,0,2,5,10,8,12,9]
import heapq

heapq.heapify(A)
print(A)

#Heap Push(Insert Element)
# Time: O(log n)
heapq.heappush(A,4)
print(A)

#Heap Pop (Extract Min)
#Time: 0(log n)
minn = heapq.heappop(A)
print(A)

#Heap Sort
#Time: 0(n log n), Space: 0 (n)
#NOTE: 0(1) Space is possible via swapping, but this is complex

def heapsort(arr):
    heapq.heapify(arr)
    n = len(arr)
    new_list = [0] * n

    for i in range(n):
        minn = heapq.heappop(arr)
        new_list[i] = minn

    return new_list

print(heapsort([1,3,5,7,9,2,4,6,8,0]))

#Heap Push Pop: 0(log n)
heapq.heappushpop(A,99)
print(A)

#Peak at min: Time 0(1)
print(A[0])

#Max Heap
B = [-4,3,1,0,2,5,10,8,12,9]
n = len(B)

for i in range(n):
    B[i] = -B[i]

heapq.heapify(B)
print(B)

largest = -heapq.heappop(B)
print(largest)

heapq.heappush(B, -7) # Insert 7 into max heap
print(B)

#Build heap from scratch - Time: 0(n log n)
C = [-5,4,2,1,7,0,3]

heap =[]

for x in C:
    heapq.heappush(heap,x)
    print(heap, len(heap))

#I always saw in LeetCode problems Putting TUples of Items on the Heap

D = [5,4,3,5,5,4,3,5,5,4]

from collections import Counter

#Getting the occurence of the numbers in here like we have 5:4(four of 5)
counter = Counter(D)
print(counter)

heap = []
for k, v in counter.items():
    print(k, v)
    heapq.heappush(heap,(v,k))

print(heap)