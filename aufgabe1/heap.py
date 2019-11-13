import heapq

heap = []
nums = [ 28, 37, 55, 31, 22, 40, 7 ]

for num in nums:
	heapq.heappush(heap, num)
	print(heap)

HEAPSORT-WITH-HEAP(A)
// Heapsort mit HEAP-Datenstruktur
H = INIT()
for i = 1 to A.length
HEAP-INSERT(H, A[i] )
for i = A.length downto 1
A[i] = HEAP-EXTRACT-MAX(H)