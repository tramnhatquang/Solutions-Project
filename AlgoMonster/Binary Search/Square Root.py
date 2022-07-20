def square_root(n: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    # Time: O(log n)
    # Space: O(1)
    if n == 0:
        return 0
    l, r = 1, n
    ans = -1
    while l <= r:
        mid = (l + r) // 2
        if mid * mid <= n:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    return ans
