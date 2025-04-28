# You are given two words, beginWord and endWord and also a list of words wordList.
# All of the given words are the same length, consisting of lowercase English letters and are all distinct
# Your goal is to transform beginWord into endWord by following the rules:
# - You may transform beginWord to any word within wordList, provided that at exactly one position the words have a different character and the rest of the positions have the same character
# - You may repeat the previous step with the new word that you obtain and you may do this as many times as needed.
# Return the minimum number of words within the transformation sequence needed to obtain the endWord or 0 if no such sequence exists

import collections
from typing import List


def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    if endWord not in wordList:
        return 0

    nei = collections.defaultdict(list)
    wordList.append(beginWord)
    for word in wordList:
        for j in range(len(word)):
            pattern = word[:j] + "*" + word[j+1:]
            nei[pattern].append(word)
    
    visit = set([beginWord])
    q = collections.deque([beginWord])
    res = 1

    while q:
        for i in range(len(q)):
            word = q.popleft()
            if word == endWord:
                return res
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                for neiWord in nei[pattern]:
                    if neiWord not in visit:
                        visit.add(neiWord)
                        q.append(neiWord)
        res += 1
    return 0

# Test cases
beginWord = "cat"
endWord = "sag"
wordList1 = ["bat", "bag", "sag", "dag", "dot"]
wordList2 = ["bat", "bag", "sat", "dag", "dot"]

print(ladderLength(beginWord, endWord, wordList1)) # Expected output: 4
print(ladderLength(beginWord, endWord, wordList2)) # Expected output: 0

# Time complexity: O(m*n^2), where n is the length of the word and m is the number of words
# Space complexity: O(m*n^2)