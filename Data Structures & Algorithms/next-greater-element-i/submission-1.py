class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        for i in nums1:
            flag =-1
            for j in range(len(nums2)-1,-1,-1):
                if nums2[j] > i:
                    flag = nums2[j]
                elif nums2[j] == i:
                    break

            output.append(flag)

        return output
