def bubble_sort(items):
    n = len(items)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True

        if not swapped:
            break

    return items


numbers = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(numbers))
