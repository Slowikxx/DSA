# Given two strings text1 and text2 return the length of the longest common subsequence between the two strings if one exists, otherwise return 0
# A subsequence is a sequence that can be derived from the given sequence by deleting some or no elements withouth changing the relative order of the remaining characters
# A common subsequence of two strings is a subsequence that exists in both strings

def longestCommonSubsequence(text1: str, text2: str) -> int:
    dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
    
    for i in range(len(text1) - 1, -1, -1):
        for j in range(len(text2) - 1, -1, -1):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i+1][j+1]
            else:
                dp[i][j] = max(dp[i][j+1], dp[i+1][j])
    return dp[0][0]

# Test cases
text1_1 = "cat"
text2_1 = "crabt"
text1_2 = "abcd"
text2_2 = "abcd"
text1_3 = "abcd"
text2_3 = "efgh"

print(longestCommonSubsequence(text1_1, text2_1)) # Expected output: 3
print(longestCommonSubsequence(text1_2, text2_2)) # Expected output: 4
print(longestCommonSubsequence(text1_3, text2_3)) # Expected output: 0

# Time complexity: O(m * n), where m is the length of text1 and n is the length of text2
# Space complexity: O(m * n)