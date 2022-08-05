# Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Example 4:
# Input: s = ""
# Output: 0

# Example 5:
# Input: s = "dvdf"
# Output: 0


def lengthOfLongestSubstring(s: str) -> int:
    if not s:
        return 0
    if len(s) == 1:
        return 1
        
    indexes = {}
    start_idx = 0
    max_substr_len = 0

    for idx in range(len(s)):
        letter = s[idx]
        if letter in indexes and indexes[letter] >= start_idx:
            start_idx = indexes[letter] + 1
        max_substr_len = max(max_substr_len, idx - start_idx + 1)
        indexes[letter] = idx

    return max_substr_len

if __name__ == '__main__':
    print(lengthOfLongestSubstring("abcabcbb"))
