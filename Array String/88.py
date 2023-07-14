class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[:] = nums2[:]
            return

        done = False
        i = 0
        j = 0
        while not done:
            if i >= m:
                nums1[i:] = nums2[j:]
                break

            if j >= n:
                break

            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                nums1[i+1:] = nums1[i:m]
                nums1[i] = nums2[j]
                j += 1
                m += 1
            else:
                nums1[i+1:] = nums1[i:m]
                nums1[i] = nums1[i+1] = nums2[j]
                i += 2
                j += 1
                m += 1
