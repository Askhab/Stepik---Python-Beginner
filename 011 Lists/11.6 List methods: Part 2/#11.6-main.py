# List methods
# insert()
# index()
# remove()
# pop()
# reverse()
# count()
# clear()
# copy()
# sort()


# insert() - Method
# The insert() method allows you to insert a value into the list at a given position. It takes two arguments:
# index: index specifying where to insert the value;
# value: The value to be inserted.

# When a value is inserted into the list, the list expands in size to accommodate the new value. The value that was previously at the given index position and all elements after it are shifted one position towards the end of the list.

names = ['Gvido', 'Roman', 'Timur']
print(names)  # ['Gvido', 'Roman' , 'Timur']
names.insert(0, 'Anders')
print(names)  # ['Anders', 'Gvido', 'Roman' , 'Timur']
names.insert(3, 'Josef')
print(names)  # ['Anders', 'Gvido', 'Roman' , 'Josef', 'Timur']

# index() - Method
# The index() method returns the index of the first element whose value equals the value passed to the method. Thus, one parameter is passed to the method:
# value: The value whose index is to be found.
names = ['Gvido', 'Roman', 'Timur']
position = names.index('Timur')
print(position)  # 2

# If the element in the list is not found, then an error occurs at run time.
names = ['Gvido', 'Roman', 'Timur']
position = names.index('Anders')
print(position)  # ValueError: 'Anders' is not in list
# To avoid such errors, you can use the index() method along with the in membership operator:
names = ['Gvido', 'Roman', 'Timur']
if 'Anders' in names:
    position = names.index('Anders')
    print(position)
else:
    print('Такого значения нет в списке')

# remove() - Method
# The remove() method removes the first element whose value equals the value passed to the method. One parameter is passed to the method:
# value: The value to be removed.

# The method reduces the size of the list by one element. All elements after the removed element are moved one position to the beginning of the list. If the element in the list is not found, then an error occurs at run time.

food = ['Рис', 'Курица', 'Рыба', 'Брокколи', 'Рис']
print(food)  # ['Рис', 'Курица', 'Рыба', 'Брокколи', 'Рис']
food.remove('Рис')
print(food)  # ['Курица', 'Рыба', 'Брокколи', 'Рис']
# Important: the remove() method only removes the first element with the specified value. All subsequent occurrences of it remain in the list. To remove all occurrences, you need to use a while loop in conjunction with the in membership operator and the remove method.


# pop() - Method
# The pop() method removes the element at the specified index and returns it. One optional argument is passed to the pop() method:
# index: The index of the element to be removed.

# If the index is not specified, then the method removes and returns the last element of the list. If the list is empty or an out-of-range index is specified, then a run-time error occurs.

names = ['Gvido', 'Roman', 'Timur']
item = names.pop()
print(item)  # 'Roman'
print(names)  # ['Gvido', 'Timur']

# count() - Method
# The count() method returns the number of elements in the list whose values are equal to the value passed to the method.
# Thus, one parameter is passed to the method:
# value: value, the number of elements equal to which you want to count.
# If the value is not found in the list, then the method returns 0.

names = ['Timur', 'Gvido', 'Roman', 'Timur', 'Anders', 'Timur']
cnt1 = names.count('Timur')
cnt2 = names.count('Gvido')
cnt3 = names.count('Josef')

print(cnt1)  # 3
print(cnt2)  # 1
print(cnt3)  # 0

# reverse() - Method
# The reverse() method reverses the order of the values in the list, i.e. reverses it.
names = ['Gvido', 'Roman', 'Timur']
names.reverse()
print(names)  # ['Timur', 'Roman', 'Gvido']

# There is a big difference between calling the names.reverse() method and using the slice names[::-1]. The reverse() method reverses the order of the elements in the current list, and the slice creates a copy of the list with the elements in reverse order.


# clear() - Method
# The clear() method removes all elements from the list.
names = ['Gvido', 'Roman', 'Timur']
names.clear()
print(names)  # []

# copy() - Method
# The copy() method creates a shallow copy of the list.
names = ['Gvido', 'Roman', 'Timur']
names_copy = names.copy()

print(names)  # ['Gvido', 'Roman', 'Timur']
print(names_copy)  # ['Gvido', 'Roman', 'Timur']

# A similar result can be achieved using slices or the list() function:
names = ['Gvido', 'Roman', 'Timur']
names_copy1 = list(names)  # create a shallow copy with the list() function
names_copy2 = names[:]  # create a shallow copy using a slice from start to finish

# Note. There is a big difference in how string and list methods work. String methods do not change the contents of the object they are applied to, but return a new value. List methods, on the other hand, change the contents of the object they are applied to.


# sort() - Method
# Lists in Python have a built-in sort() method that sorts the elements of the list in ascending or descending order.
a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6, 8, -2, 99]
a.sort()
print('Отсортированный список:', a)  # Отсортированный список: [-67, -3, -2, 0, 1, 6, 7, 8, 9, 12, 34, 45, 99, 1000]

# By default, the sort() method sorts the list in ascending order. If you want to sort the list in descending order, you must explicitly specify the reverse = True parameter.
a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6, 8, -2, 99]
a.sort(reverse=True)  # сортируем по убыванию
print('Отсортированный список:', a)  # Отсортированный список: [1000, 99, 45, 34, 12, 9, 8, 7, 6, 1, 0, -2, -3, -67]


# Note 1. Using the sort() method, you can sort lists containing not only numbers, but also strings. In this case, the elements of the list are sorted according to lexicographic order.

a = ['бета', 'альфа', 'дельта', 'гамма']
a.sort()
print('Отсортированный список:', a)   # Отсортированный список: ['альфа', 'бета', 'гамма', 'дельта']

# Note 2: The sort() method uses the Timsort algorithm.
