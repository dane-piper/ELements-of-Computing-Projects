import os


class Link(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class CircularList(object):
    # Constructor
    def __init__(self):
        self.first = None

    # Insert an element (value) in the list
    def insert(self, data):
        new_link = Link(data)
        if self.first is None:
            self.first = new_link
            self.first.next = self.first

        else:
            current = self.first
            while current.next != self.first:
                current = current.next
            current.next = new_link
            new_link.next = self.first



    # Find the link with the given data (value)
    def find(self, data):
        current = self.first
        while current.next != self.first:
            if current.data == data:
                return current
            current = current.next
        if current.data == data:
            return current
        else:
            return None

    # Delete a link with a given data (value)
    def delete(self, data):
        previous = self.first
        current = self.first
        while current.next != self.first:
            current = current.next
        last = current
        current = self.first
        if (current == None):
            return None

        while (current.data != data):
            if (current.next == self.first):
                return None
            else:
                previous = current
                current = current.next

        if current == self.first:
            self.first = self.first.next
            last.next = self.first
        else:
            previous.next = current.next

        return current.data
    # Delete the nth link starting from the Link start
    # Return the next link from the deleted Link
    def delete_after(self, start, n):
        current = self.find(start)
        for x in range(n - 1):
            current = current.next
        next = current.next
        print(current.data)
        self.delete(current.data)
        return next.data
    # Return a string representation of a Circular List
    def __str__(self):
        current = self.first
        string = ''
        while current.next != self.first:
            string +=str(current.data) + ' '
            current = current.next
        string += str(current.data) + ' '
        print(string)



def main():

    soldiers = 12
    start = 1
    count = 3

    soldiersleft = CircularList()
    for num in range(1, soldiers + 1):
        soldiersleft.insert(num)
    soldiersleft.__str__()
    while soldiersleft.first.next != soldiersleft.first:
        soldiersleft.__str__()
        start = soldiersleft.delete_after(start, count)
    print(soldiersleft.first.data)

    # add code here


main()