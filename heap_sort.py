from heapq import heappop
class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        # code here
        largest = i
        left = 2*i + 1
        right = 2*i + 2 
        if left < n and arr[left] > arr[largest]:
            largest = left 
        if right < n and arr[right] > arr[largest]: 
            largest = right 
        if largest != i: 
            arr[i], arr[largest] = arr[largest], arr[i] 
            self.heapify(arr, n, largest)
         
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        leng = len(arr)
        for idx in range(leng-1, -1, -1):
            self.heapify(arr, n, idx)

    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code 
        ans = []
        self.buildHeap(arr,n)
        leng = len(arr)
        while leng >0:
        
            arr[0], arr[leng -1] = arr[leng-1], arr[0]
            leng -=1

            self.heapify(arr, leng, 0)
