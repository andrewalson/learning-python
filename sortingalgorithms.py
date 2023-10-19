def bubble_sort(numbers_list):
    length = len(numbers_list)
    for i in range(length):
        for j in range(0, length-i-1):
            if numbers_list[j] > numbers_list[j+1]:
                temp = numbers_list[j]
                numbers_list[j] = numbers_list[j+1]
                numbers_list[j+1] = temp

unsorted = [8, 2, 4, 1, -2, 0, 21, -9, 4]
bubble_sort(unsorted)
print(unsorted)

def insertion_sort(numbers_list):
    length = len(numbers_list)
    for i in range(1, length):
        key = numbers_list[i]
        if numbers_list[i] < numbers_list[i-1]:
            for l in range(i-1, -1, -1):
                if numbers_list[l] >  numbers_list[l+1]:
                    temp = numbers_list[l]
                    numbers_list[l] = key
                    numbers_list[l+1] = temp
                    #bunch of if instead of while

unsorted = [-9, 3, 6, -1, 2, 11]
insertion_sort(unsorted)
print(unsorted)

def selection_sort(numbers_list):
    #length = len(numbers_list)
    indexing_length = range(0, len(numbers_list)-1)
    #for i in indexing_length:
    for i in indexing_length:
        min_value = i

        for j in range(i+1, len(numbers_list)):
            if numbers_list[j] < numbers_list[min_value]:
                min_value = j

        if min_value != i:
            numbers_list[min_value], numbers_list[i] - numbers_list[i], numbers_list[min_value]

    return numbers_list

