# Version 3 - From LC. Stack
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curNum = 0
        curString = ''
        
        for c in s:
            if c.isdigit():
                curNum = curNum * 10 + int(c)
            elif c == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num * curString
            else:
                curString += c
                
        return curString

# Version 2 - Like my CPP solution but tried to use join to save time. Was as fast as just += 
class Solution:
    def decodeString(self, s: str) -> str:
        self.s = s
        return self.expand(0, len(s))
    
    def expand(self, start_idx, end_idx):
        segments = []
        unenc_start, cur_k = start_idx, 0

        i = start_idx
        while (i < end_idx):
            if self.s[i].isdigit():
                if cur_k == 0 and unenc_start != i:
                    segments.append( (0, unenc_start, i) )
                cur_k = (cur_k * 10) + int(self.s[i])
            elif self.s[i] == '[':
                enc_start = i + 1
                num_open = 1
                while num_open != 0:
                    i += 1
                    if self.s[i] == '[':
                        num_open += 1
                    elif self.s[i] == ']':
                        num_open -= 1
                segments.append( (cur_k, enc_start, i))
                unenc_start, cur_k = i + 1, 0
            i += 1
        segments.append( (0, unenc_start, i) )

        return "".join(self.s[start_idx:end_idx] if not k else k * self.expand(start_idx, end_idx) for k, start_idx, end_idx in segments)

# Version 1 - Not working 
# Could build a tree
#       Each run looks like letters + number + [nested run]
#       We mark the start of each run with an index
#       When the section of letters comes to an end we mark that with an index
#       We iterate to work out what count we have
#       When we hit a bracket we set child
#       When we encounter an open bracket we create a child
#       When we encounter a closed bracket we go back to parent
# At the end we do a DFS of the tree to get the string
class Node:
    def __init__(self, parent=None, let_idxs=[], ks=[], children=[]):
        self.parent = parent
        self.letters_idxs = let_idxs
        self.ks = ks
        self.children = children

class Solution:
    def decodeString(self, s: str) -> str:
        node = Node()
        start_idx, num_letters, cur_k = 0, 0, 0

        n = len(s)
        for i in range(n):
            if s[i].isalpha():
                num_letters += 1
                continue
            elif s[i].isdigit():
                cur_k = (cur_k * 10) + int(s[i])
                continue
            elif s[i] == '[':
                node.letters_idxs.append( (start_idx, start_idx + num_letters) )
                node.ks.append(cur_k)
                child = Node(parent=node)
                node.children.append(child)
                node = child
            elif s[i] == ']':
                node = node.parent
            start_idx, num_letters, cur_k = i + 1, 0, 0

        # def dfs(node):
        #     return "".join("".join(s[idxs[0]:idxs[1]], k * dfs(child)) for idxs, k, child in zip(node.letters_idxs, node.ks, node.children))
        
        def dfs(node):
            output = ""
            for idx, k, child in zip(node.letters_idxs, node.ks, node.children):
                output += s[idx[0]:idx[1]] + k * dfs(child)
            return output

        return dfs(node)