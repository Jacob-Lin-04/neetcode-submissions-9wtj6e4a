class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        # Ensure 'a' is the smaller array to minimize binary search range
        # and prevent index out of bounds errors in the larger array.
        if len(b) < len(a):
            a, b = b, a

        # binary search range for the partition point in array 'a
        l, r = 0, len(a) - 1

        while True:
            i = (l + r) // 2 # i is middle index of a

            # j is corresponding index in array b such that
            # (i+1) + (j+1) equals the 'half' size of the total elements
            j = half - i - 2 

            # Boundary Values for partition in a
            a_left = a[i] if i >= 0 else float("-infinity")
            a_right = a[i + 1] if (i + 1) < len(a) else float("infinity")

            # Boundary Values for partition in b
            b_left = b[j] if j >= 0 else float("-infinity")
            b_right = b[j + 1] if (j + 1) < len(b) else float("infinity")

            # Check if partition is correct
            # all elements on left side must be <= all elements on right side
            if a_left <= b_right and b_left <= a_right:
                # if total elements is odd, the median is smalles element
                # of the right (larger) half.
                if total % 2:
                    return min(a_right, b_right)
                
                # if even median is average of the max of the left and the min of the right
                return (max(a_left, b_left) + min(a_right, b_right)) / 2

            # if a_left is too big, must move partition in a to the left
            elif a_left > b_right:
                r = i - 1

            # if b_left is too big, must move partition in a to the right
            else:
                l = i + 1
