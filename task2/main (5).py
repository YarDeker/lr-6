def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    
    less = [x for x in arr[1:] if x <= pivot]  
    greater = [x for x in arr[1:] if x > pivot] 
    return quick_sort(less) + [pivot] + quick_sort(greater)

def print_list(arr):
    print("Відсортований список:", arr)

arr = [35, 12, 43, 8, 51, 24, 7]
print(f'Стартовий список: {arr}')

sorted_arr = quick_sort(arr)

print_list(sorted_arr)
