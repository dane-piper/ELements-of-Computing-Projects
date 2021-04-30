class Link(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList(object):
    # initialize the linked list
    def __init__(self):
        self.first = None

    # get number of links
    def get_num_links(self):
        if self.first is None:
            return 0
        current = self.first
        num = 1
        while (current.next != None):
            current = current.next
            num += 1
        return num
        # add an item at the beginning of the list

    def insert_first(self, data):
        new_link = Link(data)

        new_link.next = self.first
        self.first = new_link

        return self

    # add an item at the end of a list
    def insert_last(self, data):
        new_link = Link(data)

        current = self.first
        if (current == None):
            self.first = new_link
            return

        while (current.next != None):
            current = current.next

        current.next = new_link

        return self

    # add an item in an ordered list in ascending order
    def insert_in_order(self, data):
        current = self.first
        new_link = Link(data)
        inserted = False
        while current.next is not None and not inserted:
            if current.data < data < current.next.data:
                new_link.next = current.next
                current.next = new_link
                inserted = True
            current = current.next
        if not inserted:
            current.next = new_link

    # search in an unordered list, return None if not found
    def find_unordered(self, data):
        current = self.first
        while current is not None and current.data != data:
            current = current.next
        if current is None:
            return None
        else:
            return current.data

    # Search in an ordered list, return None if not found
    def find_ordered(self, data):
        current = self.first
        while current.data < data:
            current = current.next
        if current.data == data:
            return current.data
        else:
            return None

    # Delete and return Link from an unordered list or None if not found
    def delete_link(self, data):
        previous = self.first
        current = self.first

        if (current == None):
            return None

        while (current.data != data):
            if (current.next == None):
                return None
            else:
                previous = current
                current = current.next

        if current == self.first:
            self.first = self.first.next
        else:
            previous.next = current.next

        return current.data

    # String representation of data 10 items to a line, 2 spaces between data
    def __str__(self):
        current = self.first
        string = str(current.data)
        line_num = 1
        while current.next is not None:
            current = current.next
            if line_num == 0:
                string = str(current.data)
                line_num += 1
            else:
                string += '  ' + str(current.data)
                line_num += 1
                if line_num == 10:
                    print(string)
                    line_num = 0
        if line_num != 0:
            print(string)

    # Copy the contents of a list and return new list
    def copy_list(self):
        new_list = LinkedList()
        current = self.first
        while current is not None:
            new_list.insert_last(current.data)
            current = current.next
        return new_list

    # Reverse the contents of a list and return new list
    def reverse_list(self):
        current = self.first
        stack = []
        while current is not None:
            stack.append(current.data)
            current = current.next
        new_list = LinkedList()
        for nums in stack:
            new_list.insert_first(nums)
        return new_list

    # Sort the contents of a list in ascending order and return new list
    def sort_list(self):
        head = self.first
        return self.mergesort(head)

    def find_middle_link(self, head):
        length = 1
        current = head
        while current.next is not None:
            current = current.next
            length += 1
        if length > 1:
            middlelink = length // 2 + length % 2
            current = head
            for x in range(middlelink - 1):
                current = current.next
            return current
        else:
            return head.first

    def mergesort(self, head):
        if head is None or head.next is None:
            new = LinkedList()
            new.insert_last(head.data)
            return new
        else:
            middle = self.find_middle_link(head)
            m_next = middle.next
            middle.next = None
            left_list = self.mergesort(head)
            right_list = self.mergesort(m_next)
            sorted = left_list.merge_list(right_list)
            return sorted

    # Return True if a list is sorted in ascending order or False otherwise
    def is_sorted(self):
        current = self.first
        while current.next is not None:
            next = current.next
            if next.data < current.data:
                return False
            current = current.next
        return True

    # Return True if a list is empty or False otherwise
    def is_empty(self):
        if self.get_num_links() == 0:
            return True
        else:
            return False

    # Merge two sorted lists and return new list in ascending order
    def merge_list(self, other):
        current = self.first
        other1 = other.first
        new_list = LinkedList()
        while current is not None and other1 is not None:
            if current.data <= other1.data:
                new_list.insert_last(current.data)
                current = current.next
            else:
                new_list.insert_last(other1.data)
                other1 = other1.next
        while current is not None:
            new_list.insert_last(current.data)
            current = current.next
        while other1 is not None:
            new_list.insert_last(other1.data)
            other1 = other1.next
        return new_list

    # Test if two lists are equal, item by item and return True
    def is_equal(self, other):
        if self.get_num_links() != other.get_num_links():
            return False
        else:
            current = self.first
            cur_other = other.first
            while current.next is not None:
                if current.data != cur_other.data:
                    return False
                current = current.next
                cur_other = cur_other.next
            return True

    # Return a new list, keeping only the first occurence of an element
    # and removing all duplicates. Do not change the order of the elements.
    def remove_duplicates(self):
        current = self.first
        non_dupes = [current.data]
        while current.next is not None:
            previous = current
            current = current.next
            removed = False
            for nums in non_dupes:
                if current.data == nums:
                    previous.next = current.next
                    removed = True
            if not removed:
                non_dupes.append(current.data)
        return self


def main():
    ordered = [1, 2, 3, 5, 8, 9, 13, 16]

    # Test methods insert_first() and __str__() by adding more than
    # 10 items to a list and printing it.
    # Test method insert_last()
    list = [4, 5, 6]
    linked_list = LinkedList()
    for links in list:
        linked_list.insert_last(links)
    new = linked_list.insert_last(4)
    new.__str__()
    # Test method insert_in_order()
    list = [3, 5, 6]
    linked_list = LinkedList()
    for links in list:
        linked_list.insert_last(links)
    new = linked_list.insert_in_order(4)
    new.__str__()
    # Test method get_num_links()
    list = [4, 5, 6]
    linked_list = LinkedList()
    for links in list:
        linked_list.insert_last(links)
    print(linked_list.get_num_links())
    # Test method find_unordered()
    list = [5,3,1]
    linked_list = LinkedList()
    for links in list:
        linked_list.insert_last(links)
    print(linked_list.find_unordered(5))
    print(linked_list.find_unordered(4))
    # Consider two cases - data is there, data is not there

    # Test method find_ordered()
    list = [3, 5, 6]
    linked_list = LinkedList()
    for links in list:
        linked_list.insert_last(links)
    print(linked_list.find_ordered(5))
    print(linked_list.find_ordered(4))
    # Consider two cases - data is there, data is not there

    # Test method delete_link()
    list = [3,2,1]
    linked_list = LinkedList()
    for links in list:
        linked_list.insert_last(links)
    print(linked_list.delete_link(2))
    linked_list.__str__()
    print(linked_list.delete_link(4))
    linked_list.__str__()
    # Consider two cases - data is there, data is not there

    # Test method copy_list()
    new_list = linked_list.copy_list()
    new_list.__str__()
    # Test method reverse_list()
    list = [5,4,3,2,1]
    linked_list = LinkedList()
    for links in list:
        linked_list.insert_last(links)
    new_list = linked_list.reverse_list()
    new_list.__str__()
    # Test method sort_list()
    list = [6,5,7,2,1]
    linked_list = LinkedList()
    for links in list:
        linked_list.insert_last(links)
    sortedlist = linked_list.sort_list()
    sortedlist.__str__()
    # Test method is_sorted()
    list = [2,5,2,4,1]
    linked_list = LinkedList()
    for links in list:
        linked_list.insert_last(links)
    print(linked_list.is_sorted())

    # Consider two cases - list is sorted, list is not sorted

    # Test method is_empty()
    list = []
    linked_list = LinkedList()
    for links in list:
        linked_list.insert_last(links)
    print(linked_list.is_empty())
    # Test method merge_list()

    # Test method is_equal()
    # Consider two cases - lists are equal, lists are not equal

    # Test remove_duplicates()
    list = [4,3,2,2,1]
    linked_list = LinkedList()
    for links in list:
        linked_list.insert_last(links)
    new = linked_list.remove_duplicates()
    new.__str__()


if __name__ == "__main__":
    main()
