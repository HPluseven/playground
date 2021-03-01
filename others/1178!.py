# timeout
class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        ans = [0] * len(puzzles)
        words_cache = []

        for word in words:
            word_set = set(word)
            if len(word_set) <= 7:
                words_cache.append(word_set)

        for idx, puzzle in enumerate(puzzles):
            for word in words_cache:
                if puzzle[0] in word and word <= set(puzzle):
                    ans[idx] += 1

        return ans


class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        frequency = collections.Counter()

        for word in words:
            mask = 0
            for ch in word:
                mask |= (1 << (ord(ch) - ord('a')))
            if str(bin(mask)).count('1') <= 7:
                frequency[mask] += 1

        ans = []
        # for puzzle in puzzles:
        #     total = 0
        #     for choose in range(1 << 6):
        #         mask = 0
        #         for i in range(6):
        #             if choose & (1 << i):
        #                 mask |= (1 << (ord(puzzle[i+1])-ord('a')))
        #         mask |= (1 << (ord(puzzle[0])-ord('a')))
        #         if mask in frequency:
        #             total += frequency[mask]
        #     ans.append(total)

        for puzzle in puzzles:
            total = 0
            mask = 0
            for i in range(1, 7):
                mask |= (1 << (ord(puzzle[i])-ord('a')))
            subset = mask
            while subset:
                s = subset | (1 << (ord(puzzle[0])-ord('a')))
                if s in frequency:
                    total += frequency[s]
                subset = (subset-1) & mask

            if (1 << (ord(puzzle[0]))-ord('a')) in frequency:
                total += frequency[1 << (ord(puzzle[0]))-ord('a')]
            ans.append(total)

        return ans


# trie
class TrieNode:
    def __init__(self):
        self.frequency = 0
        self.child = dict()


class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        root = TrieNode()

        def add(word: List[str]):
            cur = root
            for ch in word:
                idx = ord(ch) - ord("a")
                if idx not in cur.child:
                    cur.child[idx] = TrieNode()
                cur = cur.child[idx]
            cur.frequency += 1

        # 在回溯的过程中枚举 puzzle 的所有子集并统计答案
        # find(puzzle, required, cur, pos) 表示 puzzle 的首字母为 required, 当前搜索到字典树上的 cur 节点，并且准备枚举 puzzle 的第 pos 个字母是否选择（放入子集中）
        # find 函数的返回值即为谜底的数量
        def find(puzzle: List[str], required: str, cur: TrieNode, pos: int) -> int:
            # 搜索到空节点，不合法，返回 0
            if not cur:
                return 0
            # 整个 puzzle 搜索完毕，返回谜底的数量
            if pos == 7:
                return cur.frequency

            ret = 0
            # 选择第 pos 个字母
            if (idx := ord(puzzle[pos]) - ord("a")) in cur.child:
                ret += find(puzzle, required, cur.child[idx], pos + 1)

            # 当 puzzle[pos] 不为首字母时，可以不选择第 pos 个字母
            if puzzle[pos] != required:
                ret += find(puzzle, required, cur, pos + 1)

            return ret

        for word in words:
            # 将 word 中的字母按照字典序排序并去重
            word = sorted(set(word))
            # 加入字典树中
            add(word)

        ans = list()
        for puzzle in puzzles:
            required = puzzle[0]
            puzzle = sorted(puzzle)
            ans.append(find(puzzle, required, root, 0))

        return ans
