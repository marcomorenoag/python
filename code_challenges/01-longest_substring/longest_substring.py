class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l, r = 0, 0
        max_length = 0
        for r in range(len(s)):
            char = s[r]

            """
            seen[char] >= l used to know if that seen char is between the analyzed substring, since this approach
            does not remove the char from the seen dict (Hash Map), so that's why this extra condition
            e.g.
                  l   r
            a,b,c,a,c,b,d,d
            0 1 2 3 4 5 6 7

            length = 3
            seen = {a: 3, b: 1, c: 4}
            """
            if char in seen and seen[char] >= l:
                l = seen[char] + 1
            else:
                distance = r - l + 1
                max_length = max(max_length, distance)
            seen[char] = r
        return max_length


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


if __name__ == "__main__":
    print(lengthOfLongestSubstring("abcabcbb"))
