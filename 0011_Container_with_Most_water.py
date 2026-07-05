class Solution(object):
    def maxArea(self, height):
        l=0
        r=len(height)-1
        res=0
        while l<r:
            d=r-l
            w=min(height[r],height[l])
            a=d*w
            if res<a:
                res=a
            elif height[l]<height[r]:
                l=l+1
            else:
                r=r-1
        return res


# time complexity -->O(n)
# space complexity -->O(1)
