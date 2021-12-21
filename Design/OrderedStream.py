# https://leetcode.com/problems/design-an-ordered-stream/submissions/
class OrderedStream:
    # Time complexity       O(n)
    # Space complexity      O(n)
    def __init__(self, n: int):
        self.n = n
        self.stream = [""] * n
        self.ptr = 0

    # Time complexity       O(n) 
    # Space complexity      O(n)
    # in the worst case but amortised O(1) because only linear every n calls
    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey - 1] = value

        chunk = []
        while self.ptr < self.n and self.stream[self.ptr]:
            chunk.append(self.stream[self.ptr])
            self.ptr += 1

        return chunk

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)