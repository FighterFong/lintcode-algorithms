

class Solution(object):
  def findMedianSortedArrays(self, nums1, nums2):
    a, b = sorted((nums1, nums2), key=len)
    print(a,b)
    m, n = len(a), len(b)
    print(m,n)
    # 两个数组合并排序之后，最中间那个数的索引，-1是因为数组索引从 0 开始
    after = (m + n - 1) // 2  # /2
    lo, hi = 0, m
    while lo < hi:
      i = (lo + hi) // 2  # /2
      if after - i - 1 < 0 or a[i] >= b[after - i - 1]:
        hi = i
      else:
        lo = i + 1
    i = lo
    nextfew = sorted(a[i:i + 2] + b[after - i:after - i + 2])
    return (nextfew[0] + nextfew[1 - (m + n) % 2]) / 2.0

def main():
  # 按题目意思，两个数组是必须是从低到高排列好的数组
  result = Solution().findMedianSortedArrays(nums1=[1,2], nums2=[3,4])
  print(result)

if __name__ == '__main__':
  main()