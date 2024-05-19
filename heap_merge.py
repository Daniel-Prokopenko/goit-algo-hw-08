import heapq

ls = [
    [11, 32, 36, 45, 73, 75, 98],
    [2, 23, 56, 58, 61, 70, 100],
    [4, 6, 20, 37, 63, 93, 94],
    [2, 11, 43, 76, 77, 80, 88],
    [6, 10, 18, 34, 36, 45, 73],
]


def merge_k_lists(lists):
    heap = []

    for l in lists:
        for elem in l:
            heapq.heappush(heap, elem)

    merged = []
    while heap:
        merged.append(heapq.heappop(heap))

    return merged


print(merge_k_lists(ls))
