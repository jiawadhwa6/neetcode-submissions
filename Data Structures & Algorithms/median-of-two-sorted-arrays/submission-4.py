class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = nums1 + nums2
        l = sorted(l)
        if (len(l)%2 == 0):
            print("even:", (l[len(l)//2] + l[(len(l)//2)-1])/2)
            return (l[len(l)//2] + l[(len(l)//2)-1])/2
        else:
            #print(len(l))
            #print("odd: ",l[int((len(l)-1)/2)])
            return (l[int((len(l)-1)/2)])

        