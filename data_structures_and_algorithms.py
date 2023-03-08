# DATA STRUCTURES
# List - mutable, anything inside
test_list = [1, 2, 3, "GFG", 2.3]

# Tuple - immutable, anything inside
test_tuple = (1, 2, 3, "GFG", 2.3)

# Set - mutable, only hashable objects inside
# Complexity O(1) because it's like a dict with dummy values and using hashmap
# for operations (insert,update, delete)
test_set = ([1, 2, 3, "Something"])

# A frozen set - immutable, only hashable objects inside
# Complexity O(1) because it's like a dict with dummy values and using hashmap
# for operations (insert,update, delete)
test_frozen_set = frozenset([1, "f", 3])

# Stings - immutable, only unicode characters inside
test_string = "ABCDEFG"

# Dictionary - mutable, only hashable objects inside
# Complexity O(1) because it's using hashmap for operations
# (insert,update, delete)
test_dict = {'1': 1, 2: 'Hello'}

# Matrix - mutable, anything inside
# is a 2D array where each element is of strictly the same size
matrix = [[x for x in range (0,3)] for y in range(0, 3)]

# Bytearray - mutable, bytes
# Bytearray gives a mutable sequence of integers in the range 0 <= x < 256.
a = bytearray((12, 8, 25, 2))

# Linked List - mutable, anything inside
# A linked list is a linear data structure, in which the elements are not
# stored at contiguous memory locations. The elements in a linked list are
# linked using pointers.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None


# Stack - mutable, anything inside
# A stack is a linear data structure that stores items in a
# Last-In/First-Out (LIFO). In stack, a new element is added at one end
# and an element is removed from that end only.
# For methods like empty(), size(), top(), push(), pop() complexity is O(1)
stack = []
stack.append('g')
stack.append('f')
stack.append('g')
stack.pop()
stack.pop()
stack.pop()

# Queue - mutable, anything inside
# As a stack, the queue is a linear data structure that stores items in a
# First In First Out (FIFO) manner. With a queue, the least recently
# added item is removed first. # For methods like enqueue(), dequeue(),
# front(), rear() complexity is O(1)
queue = []
queue.append('g')
queue.append('f')
queue.append('g')
queue.pop(0)
queue.pop(0)
queue.pop(0)

# Priority Queue - mutable, anything inside
# Priority Queues are abstract data structures where each data/value in the
# queue has a certain priority. For example, In airlines, baggage with the
# title “Business” or “First-class” arrives earlier than the rest. Priority
# Queue is an extension of the queue with the following properties:
# An element with high priority is dequeued before an element with low priority.
# If two elements have the same priority, they are served according to their
# order in the queue.


class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def isEmpty(self):
        return len(self.queue) == 0

    def insert(self, data):
        self.queue.append(data)

    def delete(self):
        if not self.isEmpty():
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max]:
                    max = i
            item = self.queue[max]
            del self.queue[max]
            return item


# Heap - mutable, elements which can be sorted
# heapq module in Python provides the heap data structure that is mainly
# used to represent a priority queue. The property of this data structure
# is that it always gives the smallest element (min heap) whenever the
# element is popped. Whenever elements are pushed or popped, heap structure
# is maintained. The heap[0] element also returns the smallest element each
# time. It supports the extraction and insertion of the smallest element in
# the O(log n) times.


import heapq
li = [5, 7, 9, 1, 3]
heapq.heapify(li)
heapq.heappush(li, 4)

# Binary Tree - mutable, elements which can be sorted
# A binary tree is a tree whose elements can have almost two children.
# Since each element in a binary tree can have only 2 children,
# we typically name them the left and right children.
# Time complexity for searching, insertion and deletion operations is O(n).


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Depth First Traversals
# Algorithm Inorder(tree)
# Traverse the left subtree, i.e., call Inorder(left-subtree)
# Visit the root.
# Traverse the right subtree, i.e., call Inorder(right-subtree)
# Algorithm Preorder(tree)
# Visit the root.
# Traverse the left subtree, i.e., call Preorder(left-subtree)
# Traverse the right subtree, i.e., call Preorder(right-subtree)
# Algorithm Postorder(tree)
# Traverse the left subtree, i.e., call Postorder(left-subtree)
# Traverse the right subtree, i.e., call Postorder(right-subtree)
# Visit the root.
# Breadth-First or Level Order Traversal -> Time Complexity –  O(n)
# For each node, first, the node is visited and then its child nodes
# are put in a FIFO queue. Below is the algorithm for the same –
# Create an empty queue q
# temp_node = root /*start from root*/
# Loop while temp_node is not NULL
# print temp_node->data.
# Enqueue temp_node’s children (first left then right children) to q
# Dequeue a node from q

# Binary Search Tree - mutable, elements which can be sorted
# Binary Search Tree is a node-based binary tree data structure that has
# the following properties:
# The left subtree of a node contains only nodes with keys lesser
# than the node’s key.
# The right subtree of a node contains only nodes with keys greater than
# the node’s key.
# The left and right subtree each must also be a binary search tree.
# Time complexity for searching, insert and delete operations in general O(h)
# where h is the height of BST. Worst case complexity of O(n).


# ALGORITHMS

# Searching Algorithms
# Linear Search -> Time Complexity O(n)
# Start from the leftmost element of arr[] and one by one compare x with
# each element of arr[]
# If x matches with an element, return the index.
# If x doesn’t match with any of the elements, return -1.


def search(arr, n, x):
    for i in range(0, n):
        if arr[i] == x:
            return i
    return -1
# Binary Search -> Time Complexity O(log(n))
# Search a sorted array by repeatedly dividing the search interval in half.
# Begin with an interval covering the whole array. If the value of the search
# key is less than the item in the middle of the interval, narrow the interval
# to the lower half. Otherwise, narrow it to the upper half. Repeatedly check
# until the value is found or the interval is empty.


def binarySearch(arr, left, right, x):
    if right >= left:
        mid = left + (right - left) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, left, mid - 1, x)
        else:
            return binarySearch(arr, mid + 1, right, x)
    else:
        return -1

# Sorting Algorithms
# Selection Sort -> Time Complexity O(n2) as there are two nested loops.
# The selection sort algorithm sorts an array by repeatedly finding the minimum
# element (considering ascending order) from unsorted part and putting it at
# the beginning. In every iteration of selection sort, the minimum element
# (considering ascending order) from the unsorted subarray is picked and moved
# to the sorted subarray.


A = [64, 25, 12, 22, 11]

for i in range(len(A)):
    min_idx = i
    for j in range(i + 1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j
    A[i], A[min_idx] = A[min_idx], A[i]

# Bubble Sort -> Time Complexity O(n2) as there are two nested loops.
# is the simplest sorting algorithm that works by repeatedly swapping the
# adjacent elements if they are in wrong order.


def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Insertion Sort -> Time Complexity O(n2)
# To sort an array of size n in ascending order using insertion sort:
# Iterate from arr[1] to arr[n] over the array.
# Compare the current element (key) to its predecessor.
# If the key element is smaller than its predecessor, compare it to the
# elements before. Move the greater elements one position up to make space
# for the swapped element.


def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Merge Sort -> Time Complexity  O(n(logn))
# Like QuickSort, Merge Sort is a Divide and Conquer algorithm. It divides
# the input array into two halves, calls itself for the two halves, and then
# merges the two sorted halves. The merge() function is used for merging
# two halves. The merge(arr, l, m, r) is a key process that assumes that
# arr[l..m] and arr[m+1..r] are sorted and merges the two sorted
# sub-arrays into one.


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left, right = arr[:mid], arr[mid:]
        mergeSort(left)
        mergeSort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

# QuickSort -> Time Complexity O(n(logn))
# Like Merge Sort, QuickSort is a Divide and Conquer algorithm. It picks an
# element as pivot and partitions the given array around the picked pivot.
# There are many different versions of quickSort that pick pivot in different
# ways.


def partition(start, end, array):
    pivot_index = start
    pivot = array[pivot_index]
    while start < end:
        while start < len(array) and array[start] <= pivot:
            start += 1
        while array[end] > pivot:
            end -= 1
        if start < end:
            array[start], array[end] = array[end], array[start]
    array[end], array[pivot_index] = array[pivot_index], array[end]
    return end


def quick_sort(start, end, array):
    if start < end:
        p = partition(start, end, array)
        quick_sort(start, p - 1, array)
        quick_sort(p + 1, end, array)

# ShellSort -> Time Complexity O(n2)
# ShellSort is mainly a variation of Insertion Sort. In insertion sort,
# we move elements only one position ahead. When an element has to be moved
# far ahead, many movements are involved. The idea of shellSort is to allow
# the exchange of far items. In shellSort, we make the array h-sorted for a
# large value of h. We keep reducing the value of h until it becomes 1.
# An array is said to be h-sorted if all sublists of every hth element
# is sorted.
def shellSort(arr):
    gap = len(arr) // 2
    while gap > 0:
        i = 0
        j = gap
        while j < len(arr):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
            k = i
            while k - gap > -1:
                if arr[k - gap] > arr[k]:
                    arr[k - gap], arr[k] = arr[k], arr[k - gap]
                k -= 1
        gap //= 2
