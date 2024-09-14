# Quick Sort

In quick_sort.py you can find a quick sort implementation. Using the PivotSelection enum you can choose between a random or deterministic pivot selection algorithm.
You can run the profiling code using:
```
python quick_sort.py
```

### Quick Sort: Performance analysis

There are 2 steps to Quick Sort that affect its performance analysis: the Partition Step, and the Recursion Depth.

Regardless of the case, in each partition step Quick Sort compares each element to the pivot. Thus partitioning an array of size n takes O(n).

#### Best-case: O(n log n)

For Quick Sort, the best case occurs when the array is consistently divided into two nearly equal parts.

##### Recursion Depth:
This means that for an array of size n, after the first partition we will have two arrays of size n/2, then four arrays of n/4, etc. Until the arrays reach size 1. Since the arrays get twice as small on each step, this shows a Recursion Depth of log2(n).

##### Total complexity:

Since as established above, the partition step if always O(N), while best case recursion depth complexity is O(logn), total complexity in the best case scenario is O (n log n)


#### Average-case: O(n log n)

In the average case, the pivot does not split the array into equal halves, but they are still reasonably balanced. This means they would be divided, on average, into one part containing 25% and one containing 75% of elements.

#### Recursion Depth:
Even in this case, the arrays tend to be sufficiently balanced. The size of the partitions still reduces geometrically, leading to a recursion depth proportional to log2n, similar to the best case.

#### Total complexity:

The average-case complexity of Quick Sort, as seen above, is similar to the best-case complexity. Since Recursion Depth complexity is still O(log n), total complexity is O(n * logn)


#### Worst-case: O(n^2)

The worst case occurs when the pivot is always the highest or lower element in the array, leaving to the partitioning step creating one empty array, and one of size n-1.

#### Recursion Depth:
Since the array is only reduced by 1 in each recursion step, there will be N recursion steps needed for an array of size N, leading to a complexity of the Recursion Depth step of O(n^2)

#### Total complexity:

Since the partitioning step and recursion depth steps both take O(n), this leads to a total complexity in the worst-case scenario of O(N^2).

### Quick Sort: Space complexity & Additional Overhead

Quick Sort is an in-place sorting algorithm, so it does not require extra arrays in order to perform the sorting operation.

However, it does require additional space in order to hold the function call stack, due to the recursive nature of the algorithm. 
The complexity is thus directly depentant on the recursion depth. In the best and average cases, it remains O(logn), same as the time complexity, since the recursion tree has a height of logn. In the worst case scenario, the space complexity becomes O(n), since as seen above, the recursion tree will have a height of n.

As far as additional overhead, it is worth mentioning that in the case of random quick sort, generating the random number requires an additional overhead. Additionally, simply storying the partition index requires O(1) of extra space when startin the partitioning step.


### Randomized Quick sort: performance implications

Randomized quick sort selects the pivot randomly at each step. This random selection reduces the probability of consistently picking bad pivots, for example if the array is already sorted.

This leads to a significant reduction in the probability the worst case will happen. Consider that the probability of choosing the worst pivot is 1/n. If the worst-case happens once, the probability of it happening again in the next partition is 1/(n-2). Thus, the probability of the worst-case scenario happening is: 1/n * 1/(n-1)* 1/(n-2) ... * 1/2 * 1 = 1/(n!).

This shows that the likelihood of the worst-case scenario occuring decreases exponentially as the input size increases.

### Empyrical Analysis: Randomized vs Deterministic Quick Sort

The output of the quick_sort.py file is as follows:

```

Random array with PivotSelection.RANDOM :  0.01711893081665039
Random array with PivotSelection.DETERMINISTIC :  0.014617204666137695
Deterministic pivot selection is faster by  2.5017261505126953  milliseconds

Already sorted array with PivotSelection.RANDOM :  0.017080068588256836
Already sorted array with PivotSelection.DETERMINISTIC :  4.956334114074707
Random pivot selection is faster by  4939.25404548645  milliseconds

Reverse sorted array with PivotSelection.RANDOM :  0.01712203025817871
Reverse sorted array with PivotSelection.DETERMINISTIC :  3.1925089359283447
Random pivot selection is faster by  3175.386905670166  milliseconds

Repeated elements array with PivotSelection.RANDOM :  0.11308574676513672
Repeated elements array with PivotSelection.DETERMINISTIC :  0.10984516143798828
Deterministic pivot selection is faster by  3.2405853271484375  milliseconds

All elements equal array with PivotSelection.RANDOM :  4.925328969955444
All elements equal array with PivotSelection.DETERMINISTIC :  4.894295930862427
Deterministic pivot selection is faster by  31.033039093017578  milliseconds

```

As expected, when sorting a random array, the difference in speed between the random and deterministic pivot is marginal: I assume the deterministic pivot is marginally faster simply because generating a random number takes a small amount of time. The same applies to the "repeated elements" array since it is still random, albeit with less variation of elements inside.

In the already sorted and reverse sorted arrays, we see the main benefit of the random pivot: by choosing an element at random, it avoids going into the O(N^2) worst case scenario fo the basic quick search, resulting in drastically improved performance.

In the "all equal elements" case, I believe the implementations should have almost identical speeds: I believe the slight time difference comes due to my implementation of the partitioning algorithm, which could be optimized further for such edge case. Both of them fall into the O(N^2) worst case time in this scenario.
