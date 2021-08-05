class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return # node already exists

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else :
                self.left = BSTNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BSTNode(data)

    def search(self, val):
        if val == self.data:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        else:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def iot(self):
        elements = []

        if self.left:
            elements += self.left.iot()

        elements.append(self.data)

        if self.right:
            elements += self.right.iot()

        return elements

    def prot(self):
        elements = [self.data]

        if self.left:
            elements += self.left.prot()

        if self.right:
            elements += self.right.prot()

        return elements

    def pot(self):
        elements = []
        if self.left:
            elements += self.left.pot()

        if self.right:
            elements += self.right.pot()

        elements.append(self.data)

        return elements

    def sum(self):
        elements = 0
        elements += self.data
        if self.left:
            elements += self.left.sum()
        if self.right:
            elements += self.right.sum()
        return elements

    def mi(self):
        elements = []
        if self.left:
            elements += self.left.pot()

        if self.right:
            elements += self.right.pot()

        elements.append(self.data)

        return min(elements)

    def ma(self):
        elements = []
        if self.left:
            elements += self.left.pot()

        if self.right:
            elements += self.right.pot()

        elements.append(self.data)

        return max(elements)

    def find_min(self):
        if not self.left:
            return self.data
        return self.left.find_min()

    def find_max(self):
        if not self.right:
            return self.data
        return self.right.find_max()

    def cal_sum(self):
        left_sum = self.left.cal_sum() if self.left else 0
        right_sum = self.right.cal_sum() if self.right else 0
        return self.data + left_sum + right_sum


def build_tree(elements):
    print("Building tree with these elements:", elements)
    root = BSTNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    countries = ["India", "Pakistan", "Germany", "USA", "China", "India", "UK", "USA"]
    country_tree = build_tree(countries)

    print("UK is in the list? ", country_tree.search("UK"))
    print("Sweden is in the list? ", country_tree.search("Sweden"))

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print("In order traversal gives this sorted list:", numbers_tree.iot())
    print("Pre order traversal gives this sorted list:", numbers_tree.prot())
    print("Post order traversal gives this sorted list:", numbers_tree.pot())
    print("Sum of all the elements:", numbers_tree.sum())
    print("Sum of all the elements:", numbers_tree.cal_sum())
    print("Minimum of all the elements:", numbers_tree.mi())
    print("Minimum of all the elements:", numbers_tree.find_min())
    print("Maximum of all the elements:", numbers_tree.ma())
    print("Maximum of all the elements:", numbers_tree.find_max())




