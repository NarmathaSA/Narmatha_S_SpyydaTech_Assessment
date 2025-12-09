from bisect import bisect_left

def lis_length(arr):
    if not arr:
        return 0
    tails = []
    for x in arr:
        i = bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)

nums = input("Enter numbers separated by space: ").strip().split()
arr = [int(n) for n in nums]

print("LIS Length:", lis_length(arr))


# The Longest Increasing Subsequence (LIS) problem focuses on finding the longest sequence of numbers within an array that are strictly increasing. The numbers in the subsequence do not need to be adjacent in the input list; they just need to maintain their original order. The logic implemented in this program uses the well-known patience sorting algorithm, which is an optimized technique that solves the problem in O(n log n) time. This approach is significantly faster than the basic dynamic programming method, especially for large datasets.

# The algorithm begins by reading a list of integers entered by the user. These integers form the sequence in which we want to identify the LIS. The main function that carries out the LIS calculation operates on a list called tails. This list does not represent the actual LIS but stores the smallest possible tail values for increasing subsequences of different lengths. For example, tails[0] stores the smallest ending value of all increasing subsequences of length 1, tails[1] stores the smallest ending value of all increasing subsequences of length 2, and so on. By maintaining these values, the algorithm efficiently tracks the potential growth of increasing subsequences without storing every subsequence explicitly.

# The logic then iterates through each element of the input array. For each number, the algorithm determines where the number should be positioned in the tails list. This is done using the bisect_left function, which performs a binary search on tails to find the correct index. If the number is larger than all elements in tails, it is appended to the list. This effectively means we have found a longer increasing subsequence. However, if the number is smaller than or equal to an existing value in tails, the algorithm replaces the element at the found index with the current number. This replacement is intentional and plays a crucial role: it helps maintain the smallest possible tail value for subsequences of that length. Keeping smaller tail values increases the chances of forming a longer subsequence in the future.

# One of the most important aspects of this algorithm is that it does not construct the entire subsequence. Instead, it keeps only the necessary structure to determine the subsequence length. At the end of the iteration, the length of the tails list directly corresponds to the length of the longest increasing subsequence. This is because each entry in tails represents the best (smallest) ending value for subsequences of increasing lengths.

# After computing the LIS length, the program prints the final result to the user. The simplicity of the user interface allows the user to input any sequence of integers while the optimized algorithm ensures that even very large sequences can be handled efficiently.

# In summary, the logic implemented demonstrates a sophisticated and efficient approach to solving the LIS problem. By using binary search and a clever structure to store only essential information, the algorithm achieves excellent performance while remaining conceptually elegant.