# Quick Sort

In quick_sort.py you can find a quick sort implementation. Using the PivotSelection enum you can choose between a random or deterministic pivot selection algorithm.

### Analysis

We will prove that the average-case time complexity of Randomized Quicksort is at most O(n log n).

Consider that when we pick a pivot on an array of size X, we then perform X-1 comparisons (compare all other elements to it in order to partition them). Depending on the pivot, the resulting array lengths will be one of: (0, X-1), (1, X-2), ..., (X-1, 0). Since the pivot selection is random, the probability of picking either of these is random.

Therefore, we can write a recurrence relation for the expected number of comparisons required:

T(x) = (x - 1) + 1/x \*

$$
\ \sum_{i=0}^{x-1} T(i) + T(x-i-1)
$$

By using the general expression for expectation of random variable X, we can rewrite the equation, simplifying it and getting rid of T(0):

T(x) = (x - 1) + 2/x \*

$$
\ \sum_{i=1}^{x-1} T(i)
$$

We can solve this function using the induction method. Let's prove that T(i) <= ci ln(i) fir i<=n-1. For T(1) = 0 the proof is simple: if there is only one element, there are no comparisons to make.
Deriving from that, we get:

T(x) <= (x-1) + 2/x \_

$$
\ \sum\_{i=1}^{x-1} (ci _ ln(i))
$$

<= (x-1) + 2/x \_

$$
\int_1^x (cx _ ln(x))dx \
$$

<= (x-1) + 2/x ((c/2)x^2 _ ln(x) - c(n^2)/4 + c/4)
<= cx _ ln(x), for c = 2

Which shows that the aerage-case running time for Randomized quicksort is O(_n_ log _n_)

### Comparisons

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
