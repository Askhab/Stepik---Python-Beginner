# List sorting

# Sorting task
# The task of sorting a list is to rearrange its elements so that they are sorted in ascending or descending order. This is one of the main tasks of programming. We come across it very often: when writing down the names of students in a class journal, when summing up the results of competitions, etc.

# Sorting algorithms
# A sorting algorithm is an algorithm for ordering the elements in a list. Sorting algorithms are rated for execution speed and memory efficiency:

# time is the main parameter characterizing the speed of the algorithm;
# memory - a number of algorithms require the allocation of additional memory for temporary data storage.

# Sorting algorithms that do not consume additional memory are referred to as in-place sorts.


# Basic sorting algorithms
# SLOW:
# 1 - Bubble sort
# 2 - Selection sort
# 3 - Insertion sort

# FAST:
# 1 - Shell sort
# 2 - Quick sort
# 3 - Merge sort
# 4 - Heap sort
# 5 - TimSort (used in Java and Python)

# Most sorting algorithms, such as those listed above, rely on comparing two elements of a list. There are, however, algorithms not based on comparisons. Such algorithms usually use predefined conditions on the elements of the list. For example, the elements of a list are natural numbers or integers in some range, the elements are strings, and so on.

# Algorithms not based on comparisons include the following:
# Counting sort;
# Block sort (Bucket sort);
# Bitwise sort (Radix sort).

# As part of the course, we will consider simple algorithms for bubble sort, selection sort, and simple insertion sort.


# BUBBLE SORT
# The bubble sort algorithm consists of repeated passes through the sorted list. For each pass, the elements are sequentially compared in pairs and, if the order in the pair is incorrect, the elements are exchanged. Passes through the list are repeated n-1n−1 times, where nn is the length of the list. Each time the algorithm passes through the inner loop, the next largest element of the list is put in its place at the end of the list next to the previous "largest element".

# The largest element “pops up” to the right position each time, like a bubble in water - hence the name of the algorithm.

# The bubble sort algorithm is considered educational and is practically not used outside the educational literature, but more efficient ones are used in practice.

# Consider the operation of the algorithm using the example of sorting the list a = [5, 1, 4, 2, 8] in ascending order.

# First pass:
# 1 - [5, 1, 4, 2, 8] → [1, 5, 4, 2, 8]: swap the first and second elements since 5 > 15>1;
# 2 - [1, 5, 4, 2, 8] → [1, 4, 5, 2, 8]: swap the second and third elements since 5 > 45>4;
# 3 - [1, 4, 5, 2, 8] → [1, 4, 2, 5, 8]: swap the third and fourth elements since 5 > 25>2;
# 4 - [1, 4, 2, 5, 8] → [1, 4, 2, 5, 8]: do not swap the fourth and fifth elements, since 5 < 85<8;
# 5 - The largest element rose ("surfaced") into place.

# Second pass:
# 1 - [1, 4, 2, 5, 8] → [1, 4, 2, 5, 8]: do not swap the first and second elements because 1 < 41<4;
# 2 - [1, 4, 2, 5, 8] → [1, 2, 4, 5, 8]: swap the second and third elements since 4 > 24>2;
# 3 - [1, 2, 4, 5, 8] → [1, 2, 4, 5, 8]: do not swap the third and fourth elements because 4 < 54 < 5;
# 4 - The second largest element rose ("surfaced") into place.

# Now the list is completely sorted, but the algorithm does not know this and it continues to work.

# Third pass:
# 1 - [1, 2, 4, 5, 8] → [1, 2, 4, 5, 8]: do not swap the first and second elements, since 1 < 21<2;
# 2 - [1, 2, 4, 5, 8] → [1, 2, 4, 5, 8]: do not swap the second and third elements because 2 < 42 < 4;
# 3 - The third largest element rose ("surfaced") into place. (on which he was)

# Fourth pass:
# 1 - [1, 2, 4, 5, 8] → [1, 2, 4, 5, 8]:
# 2 - The fourth largest element rose (“surfaced”) into place.

# Now the list is sorted and the algorithm can be completed.


# IMPLEMENTATION OF THE ALGORITHM
# Suppose we want to sort a list of numbers in ascending order: a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6, 8, -2, 99].
a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6, 8, -2, 99]
n = len(a)

for i in range(n - 1):
    for j in range(n - i - 1):
        if a[j] > a[j + 1]:   # if the order of the pair's elements is wrong
            a[j], a[j + 1] = a[j + 1], a[j]   # swap elements of a pair

print('Sorted list:', a)   # [-67, -3, -2, 0, 1, 6, 7, 8, 9, 12, 34, 45, 99, 1000]


# ALGORITHM OPTIMIZATION
# The bubble sort algorithm can be slightly speeded up. If on one of the next passes it turns out that the exchanges are no longer needed, then this means that all the elements of the list are in their places, that is, the list is sorted. To implement such an acceleration, you need to use the signal label, that is the flag and the break operator.


# SELECTION SORT
# Selection sort improves upon bubble sort by making only one swap per pass through the list. To do this, the algorithm looks for the maximum element and places it at the appropriate position. As with bubble sort, after the first pass, the largest element is in the correct place. After the second pass, the next maximum element takes its place. Iterates through the list n-1n−1 times, where nn is the length of the list, since the last one is automatically placed in its place.

# NOTE: The selection sorting algorithm is also considered educational and is practically not used outside of educational literature. In practice, more efficient algorithms are used.

# Consider the operation of the algorithm using the example of sorting the list a = [5, 1, 8, 2, 4] in ascending order.

# First pass:
# We find the maximum element 8 in the unsorted part of the list and change it with the last element of the list:
# [5, 1, 4, 2, 8].

# Second pass:
# We find the maximum element 5 in the unsorted part of the list and change it with the penultimate element of the list:
# [2, 1, 4, 5, 8].

# Third pass:
# We find the maximum element 4 in the unsorted part of the list and change it with the penultimate element of the list:
# [2, 1, 4, 5, 8].

# Fourth pass:
# Find the maximum element 2 in the unsorted part of the list and swap it with the second element of the list:
# [1, 2, 4, 5, 8].

# Now the list is sorted and the algorithm can be completed.

# NOTE: Instead of the maximum element, you can look for the minimum.


# SORTING BY SIMPLE INSERTS
# The sorting algorithm by simple insertions divides the list into 2 parts - sorted and unsorted. The next element is extracted from the unsorted part and inserted at the desired position, as a result of which the sorted part of the list increases, and the unsorted part decreases. This happens until the input data set is exhausted and all elements are sorted.

# Insertion sort is most efficient when the list is already partially sorted and there are few array elements. If there are less than 10 elements in the list, then this algorithm is one of the fastest.

# Consider his work on the example of sorting the list a = [5, 1, 8, 2, 4] in ascending order.

# First pass:
# We divide the list into two parts: sorted [5] and unsorted [1, 8, 2, 4].
# We extract the first element 1 from the unsorted part of the list and find its place in the sorted part:
# [1, 5, 4, 2, 8].
#
# Second pass:
# We divide the list into two parts: sorted [1, 5] and unsorted [8, 2, 4].
# We extract the first element 8 from the unsorted part of the list and find its place in the sorted part:
# [1, 5, 8, 2, 4].

# Third pass:
# We divide the list into two parts: sorted [1, 5, 8] and unsorted [2, 4].
# We extract the first element 2 from the unsorted part of the list and find its place in the sorted part:
# [1, 2, 5, 8, 4].

# Fourth pass:
# We divide the list into two parts: sorted [1, 2, 5, 8] and unsorted [4].
# We extract the first element 4 from the unsorted part of the list and find its place in the sorted part:
# [1, 2, 4, 5, 8].

# Now the list is sorted and the algorithm can be completed.

# IMPLEMENTATION OF THE ALGORITHM
# Suppose we want to sort a list of numbers in ascending order: a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6, 8, -2, 99].

# The following code implements the insertion sort algorithm:
a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
n = len(a)

for i in range(1, n):
    elem = a[i]
    j = i
    while j >= 1 and a[j - 1] > elem:
        a[j] = a[j - 1]
        j -= 1
    a[j] = elem

print("Sorted list:", a)   # [-67, -3, -2, 0, 1, 6, 7, 8, 9, 12, 34, 45, 99, 1000]

# Algorithm optimization
# The sorting algorithm by simple insertions can be significantly accelerated if you search for the right position to insert the next element from the unsorted part of the list using binary search.
