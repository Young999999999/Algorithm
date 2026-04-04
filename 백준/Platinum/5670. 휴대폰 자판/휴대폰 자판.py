import sys
input = sys.stdin.readline

class Node:
    def __init__(self):
        self.isEnd = False
        self.child = {}

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.child:
                node.child[c] = Node()
            node = node.child[c]
        node.isEnd = True

    def search(self, word):
        cnt = 1
        node = self.root.child[word[0]]

        for c in word[1:]:
            if len(node.child) > 1 or node.isEnd:
                cnt += 1
            node = node.child[c]

        return cnt

while True:
    line = input()
    if not line:
        break

    n = int(line.strip())
    trie = Trie()
    words = []

    for _ in range(n):
        word = input().strip()
        words.append(word)
        trie.insert(word)

    total = 0
    for word in words:
        total += trie.search(word)

    print(f"{total / n:.2f}")