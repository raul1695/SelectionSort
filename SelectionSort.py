"""
Selection sort is one of the simpler sorting algorithms. It is not very fast or efficient but it has the benefit of consuming a very small amount of resources. Thus it could be useful to use in certain (specific) situations.

In the python implementation of the selection sort algorithm, a new list is created where the "sorted" elements are appended to.

Even though I like this property of python it is worth mentioning that in other high level languages (such as Java or C++)
elements are not added to new arrays, instead the "sorted" index serves as the point from which the sorting occurs.

In other words, once the lowest value in the "unsorted" array is found, the value is swapped with the nearest element to the sorted
index and from there, the element is sorted into the "sorted" section of the array (which of course increases with the addition)
of the new element.

"""


def selection_sort(arr):
    for i in range(0,len(arr)-1):
        min_pos = i

        for j in range(i+1, len(arr)):
            if(arr[j] < arr[min_pos]):
                min_pos = j

        # Performing the swap of contents
        temp = arr[i]
        arr[i] = arr[min_pos]
        arr[min_pos] = temp




ar = [63,9,5,1,94,9,7,55]
print(ar)

selection_sort(ar)

print(ar)

