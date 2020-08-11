class Treenode:
    def __init__(self, name, des):
        self.name = name
        self.des = des
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

    def print_tree(self, property_name):
        if property_name == 'both':
           value = self.name + "(" + self.des + ")"
        elif property_name == 'name':
           value = self.name
        else:
            value = self.des

        space = ' ' * self.get_level() * 3
        prefix = space + "|_ " if self.parent else ""
        print(prefix + value)
        if self.children:
            for child in self.children:
                child.print_tree(property_name)


def buildorg():
    #CTO Org
    infra_head = Treenode("Viswa", "Infrastructure Head")
    infra_head.add_child(Treenode("Dhaval","Cloud Manager"))
    infra_head.add_child(Treenode("Abhijit", "App Manager"))

    app_head = Treenode("Aamir", "Application Head")

    cto_head = Treenode("Chinmay", "CTO")
    cto_head.add_child(infra_head)
    cto_head.add_child(app_head)

    #HR Org

    hr_head = Treenode("Gels", "HR Head")
    hr_head.add_child(Treenode("Peter", "Recruitment Manager"))
    hr_head.add_child(Treenode("Waqas", "Policy Manager"))

    #CEO

    ceo = Treenode("Nilupul", "CEO")
    ceo.add_child(cto_head)
    ceo.add_child(hr_head)

    return ceo

if __name__ == '__main__':
    root_node = buildorg()
    root_node.print_tree("name")
    root_node.print_tree("des")
    root_node.print_tree("both")












