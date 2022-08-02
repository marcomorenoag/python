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


def longest_substring(word):
    if not word:
        return 0

    substring = []
    max_length = 0

    for letter in word:
        if not letter in substring:
            substring.append(letter)
            continue
        max_length = max(max_length, len(substring))
        substring.clear()

    return len(substring)


if __name__ == '__main__':
    print(longest_substring("pwwkew"))
