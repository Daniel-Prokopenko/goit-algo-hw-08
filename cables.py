import heapq


cables = [11, 2, 1, 5, 4, 10, 3, 6, 12, 14]


def heap_sort(iterable, descending=False):
    # Визначаємо, який знак використовувати залежно від порядку сортування
    sign = -1 if descending else 1

    # Створюємо купу, використовуючи заданий порядок сортування
    h = [sign * el for el in iterable]
    heapq.heapify(h)
    # Витягуємо елементи, відновлюємо їхні оригінальні значення (якщо потрібно) і формуємо відсортований масив
    return [sign * heapq.heappop(h) for _ in range(len(h))]


def cost(arr, total=None):
    if total is None:
        total = []
    if arr:
        if total:
            total.append(total[-1] + arr[0])
        else:
            total.append(arr[0])
        return cost(arr[1:], total)
    else:
        return sum(total)


print(cost(cables))
print(cost(heap_sort(cables)))
