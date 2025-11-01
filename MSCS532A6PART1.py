# Umesh Dhakal
# MSCS532A6 - Part 1
# Randomized and Deterministic Selection (Quickselect & Median-of-Medians)
import random
import time
import tracemalloc
import sys
sys.setrecursionlimit(10000)

def _partition_by_pivotvalue(arraylist, pivotvalue):
    # spliting the list into three parts: less than pivot, equal to pivot, and greater than pivot.
    smallerlist, equalist, greaterlist = [], [], []
    for item in arraylist:
        if item < pivotvalue:
            smallerlist.append(item)
        elif item > pivotvalue:
            greaterlist.append(item)
        else:
            equalist.append(item)
    return smallerlist, equalist, greaterlist

def _median_of_five(block):
    # takeing up to five items, sorting them, and returning the middle one. 
    b = sorted(block)
    return b[len(b) // 2]

def _choose_pivot_median_of_medians(arraylist):
    # chooseing a safe pivot by using the median-of-medians.
    n = len(arraylist)
    if n <= 5:
        return _median_of_five(arraylist)
    medianlist = []
    for i in range(0, n, 5):
        medianlist.append(_median_of_five(arraylist[i:i+5]))
    # finding the median of these medians as the final pivot.
    return deterministic_select(medianlist, len(medianlist) // 2)

def randomized_quickselect(arraylist, kthindex):
    # picking a random pivot
    if not arraylist:
        raise ValueError("arraylist must not be empty")
    if kthindex < 0 or kthindex >= len(arraylist):
        raise IndexError("kthindex out of range")

    if len(arraylist) == 1:
        return arraylist[0]

    pivotvalue = random.choice(arraylist)
    smallerlist, equalist, greaterlist = _partition_by_pivotvalue(arraylist, pivotvalue)

    if kthindex < len(smallerlist):
        return randomized_quickselect(smallerlist, kthindex)
    elif kthindex < len(smallerlist) + len(equalist):
        return pivotvalue
    else:
        return randomized_quickselect(greaterlist, kthindex - len(smallerlist) - len(equalist))

def deterministic_select(arraylist, kthindex):
    # useing the median-of-medians pivot to avoid worst cases.
    if not arraylist:
        raise ValueError("arraylist must not be empty")
    if kthindex < 0 or kthindex >= len(arraylist):
        raise IndexError("kthindex out of range")

    if len(arraylist) == 1:
        return arraylist[0]

    pivotvalue = _choose_pivot_median_of_medians(arraylist)
    smallerlist, equalist, greaterlist = _partition_by_pivotvalue(arraylist, pivotvalue)

    if kthindex < len(smallerlist):
        return deterministic_select(smallerlist, kthindex)
    elif kthindex < len(smallerlist) + len(equalist):
        return pivotvalue
    else:
        return deterministic_select(greaterlist, kthindex - len(smallerlist) - len(equalist))

def _make_datasets(test_size):
    # four datasets for testing and comparison.
    return {
        "Sorted Data": list(range(1, test_size + 1)),
        "Reverse Data": list(range(test_size, 0, -1)),
        "Random Data": [random.randint(1, test_size) for _ in range(test_size)],
        "Repeated Data": [5] * test_size
    }

def _runtest(algorithm, dataset, dataset_name, kthindex):
    arraylist = dataset[:]
    tracemalloc.start()
    t0 = time.perf_counter()
    result = algorithm(arraylist, kthindex)
    t1 = time.perf_counter()
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # Results
    print(f"{algorithm.__name__} on {dataset_name} took {t1 - t0:.5f}s and used {peak/1024:.2f}KB memory")
    return result, (t1 - t0), peak

if __name__ == "__main__":
    # test size 2000
    test_size = 2000
    datasets = _make_datasets(test_size)

    print("\nSelection Algorithms Performance Analysis\n")
    for dataset_name, dataset in datasets.items():
   
        kthindex = len(dataset) // 2
        ground_truth = sorted(dataset)[kthindex]
        # randomized version
        res1, _, _ = _runtest(randomized_quickselect, dataset, dataset_name, kthindex)
        # deterministic version
        res2, _, _ = _runtest(deterministic_select, dataset, dataset_name, kthindex)
        assert res1 == ground_truth, f"randomized_quickselect incorrect on {dataset_name}"
        assert res2 == ground_truth, f"deterministic_select incorrect on {dataset_name}"