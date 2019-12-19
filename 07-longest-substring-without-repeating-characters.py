import collections
'''
  示例 2:
  输入: "bbbbb"
  输出: 1
  解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

  示例 3:
  输入: "pwwkew"
  输出: 3
  解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
       请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
'''

class Solution(object):
  def _lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    d = collections.defaultdict(int)
    l = ans = 0
    for i, c in enumerate(s):
      while l > 0 and d[c] > 0:
        d[s[i - l]] -= 1
        l -= 1
      d[c] += 1
      l += 1
      ans = max(ans, l)
    return ans

  def lengthOfLongestSubstring(self, s):
    d = {}
    start = 0
    ans = 0
    for i, c in enumerate(s):
      if c in d:
        start = max(start, d[c] + 1)
      d[c] = i
      ans = max(ans, i - start + 1)
    return ans

if __name__ == '__main__':
  sol = Solution()
  ret = sol._lengthOfLongestSubstring("pwwkew")
  print(ret)