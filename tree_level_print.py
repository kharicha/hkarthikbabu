class Treenode:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self, level):
        if self.get_level() > level:
            return

        space = ' ' * self.get_level() * 3
        prefix = space + "|_ " if self.parent else ""
        print(prefix + self.name)
        if self.children:
            for child in self.children:
                child.print_tree(level)

def buildorg():

    ind1_state = Treenode("Gujarat")
    ind1_state.add_child(Treenode("Ahmedabad"))
    ind1_state.add_child(Treenode("Baroda"))

    ind2_state = Treenode("Karnataka")
    ind2_state.add_child(Treenode("Bangalore"))
    ind2_state.add_child(Treenode("Mysore"))


    country1 = Treenode("India")
    country1.add_child(ind1_state)
    country1.add_child(ind2_state)

    us1_state = Treenode("New Jersey")
    us1_state.add_child(Treenode("Princeton"))
    us1_state.add_child(Treenode("Trenton"))

    us2_state = Treenode("California")
    us2_state.add_child(Treenode("San Francisco"))
    us2_state.add_child(Treenode("Mountain View"))
    us2_state.add_child(Treenode("Palo Alto"))

    country2 = Treenode("USA")
    country2.add_child(us1_state)
    country2.add_child(us2_state)

    glo = Treenode("Global")
    glo.add_child(country1)
    glo.add_child(country2)

    return glo

if __name__ == '__main__':
    root_node = buildorg()
    root_node.print_tree(3)











