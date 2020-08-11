
class deque:
    def __init__(self):
        self.item = []

    def addFront(self, val):
        self.item.append(val)

    def addRear(self, val):
        self.item.insert(0, val)

    def removeFront(self):
        return self.item.pop()

    def removeRear(self):
        return self.item.pop(0)

    def size(self):
        return len(self.item)

def palchecker(mystr):
    pal = deque()

    for ch in mystr:
        pal.addRear(ch)

    isequal = True

    while pal.size() > 1 and isequal:
        first = pal.removeFront()
        last = pal.removeRear()
        if first != last:
            isequal = False

    return isequal

print(palchecker("radar"))
print(palchecker("lsdkjfskf"))