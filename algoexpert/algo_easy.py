'''
1, Two Number sum

input = [3, 5, -4, 8, 11, 1, -1, 6]
sum = 10
output = [11, -1]

'''

#using for loop
#tc - o(n^2) sc - o(1)

# def twosum(input, sum):
#     for i in range(len(input)-1 ):
#         fn = int(input[i])
#         for j in range(i+1, len(input)):
#             if fn + int(input[j]) == sum:
#                 return [i,j]
#     return []

#using hash map
#tc o(n) sc o(n)

# def twosum(input, sum):
#     d = {}
#     for i in input:
#         if sum - i in d:
#             return [i, sum-i]
#         else:
#             d[i] = True
#     return []

#using sort and 2 pointer
#tc o(nlogn) 0(1)

# def twosum(input, sum):
#     input.sort()
#     print(input)
#     left = 0
#     right = len(input) -1
#     print(right)
#     while left < right:
#         cs = input[left] + input[right]
#         if cs == sum:
#             return [input[left], input[right]]
#         elif cs < sum:
#             left += 1
#         elif cs > sum:
#             right -= 1
#     return []

# input = [3, 5, -4, 8, 11, 1, -1, 6]
# sum = 10
# print(twosum(input, sum))

'''
2, Validate subsequence
'''
# o(n) | o(1)
# def isValidSubsequence(array, sequence):
#     fi = 0
#     for a in array:
#         if fi == len(sequence):
#             break
#         if sequence[fi] == a:
#             fi += 1
#     return fi == len(sequence)

#0(n) | o(1)

# def isValidSubsequence(array, sequence):
#     si = ai = 0
# 	while si < len(sequence) and ai < len(array):
# 		if sequence[si] == array[ai]:
# 			si += 1
# 		ai += 1
# 	return si == len(sequence)

# array = [5, 1, 22, 25, 6, -1, 8, 10, 12, 45, 67]
# sequence = [1, 6, -1, 10]
# print(isValidSubsequence(array, sequence))

'''
3, find closest value in BST
'''

# def findClosestValueInBst(tree, target):
#     return findClosestValueInBsthelper(tree, target, tree.value)
#
# def findClosestValueInBsthelper(tree, target, closest):
#         if tree is None:
#             return closest
#         if abs(target - closest)  > abs(target - tree.value):
#             closest = tree.value
#         if target > tree.value:
#             return findClosestValueInBsthelper(tree.right, target, closest)
#         elif target
#             return findClosestValueInBsthelper(tree.right, target, closest)
#         else:
#             return closest


#
#
#         # This is the class of the input tree. Do not edit.
# class BST:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None


'''
creating a vehicle and parking lot
'''

# class minmaxstack():
#     def __init__(self):
#         self.cont = []
#         self.minmax = []
#
#     def peek(self):
#         return self.cont[len(self.cont)-1]
#
#     def pop(self):
#         self.minmax.pop()
#         return self.cont.pop()
#
#     def push(self, no):
#         newminmax = {"min": no, "max": no}
#         if len(self.cont):
#             oldminmax = self.minmax(len(self.minmax)-1)
#             newminmax['min'] = min(oldminmax['min'], no)
#             newminmax['max'] = max(oldminmax['max'], no)
#         self.minmax.append(newminmax)
#         self.cont.append(no)
#
#     def getmin(self):
#         return self.minmax[len(self.minmax)-1]['min']
#
#     def getmax(self):
#         return self.minmax[(len(self.minmax)-1)]['max']


# string = 'karthik'
# for ch in range(len(string)):
#     print(ch)
#     print(string[ch])

class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        # Write your code here.
        for i in range(len(string)):
            self.insertSubString(i, string)
            print(self.root)

    def insertSubString(self, i, string):
        print(i)
        print(string)
        node = self.root
        for j in range(i, len(string)):
            letter = string[j]
            print(letter)
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node[self.endSymbol] = True

    def contains(self, string):
        # Write your code here.
        node = self.root
        for ch in string:
            if ch not in node:
                return False
            node = node[ch]
        return self.endSymbol in node

SuffixTrie('babc')