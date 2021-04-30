#  File: BabyNames.py

#  Description: Reads from a file of baby names and costructs a class that performs different tasks on the data

#  Student Name: Dane Piper

#  Student UT EID: dap3498

#  Course Name: CS 313E

#  Unique Number: 50300

#  Date Created: 2/7/2020

#  Date Last Modified: 2/10/2020


class BabyNames(object):
    """Class to store all the baby names"""

    # Initializes the dictionary that will hold all the baby names
    def __init__(self):
        # key: name
        # value: list of ranks
        self.names = {}

    # Reads in the file and adds to the dictionary
    def fill_data(self, file_name):
        # opens file and reads each line
        file_in = open(file_name)
        lines = file_in.readlines()
        # takes each line and adds it to dictionary
        for x in range(0, len(lines)):
            lines[x] = lines[x].rstrip()
            list1 = lines[x].split()
            key = list1.pop(0)
            for y in range(len(list1)):
                list1[y] = int(list1[y])
            self.names.update({key: list1})

    # True if a name exists in the dictionary and False otherwise.
    def contains_name(self, name):
        # checks if dictionary contains name
        return name in self.names

    # Returns all the rankings for a given name. Assume the name exists
    def find_ranking(self, name):
        # returns item that is a list from the dictionary
        return self.names[name]

    # Returns a list of names that have a rank in all the decades in sorted order by name.
    def ranks_of_all_decades(self):
        # if all elements of the list items are not equal to zero adds and returns list
        all_decades = []
        for key in self.names.keys():
            items = self.names[key]
            if 0 in items:
                pass
            else:
                all_decades.append(key)
        return all_decades

    #  Returns a list of all the names that have a rank in a given decade in order of rank.
    def ranks_of_a_decade(self, decade):
        # if a valid decade continue i.e. 1981 not a valid decade
        if 1900 <= decade <= 2000 and decade % 10 == 0:
            decade_elem = int((decade - 1900) / 10)
            length = 0
            ordered_names = []
            # creates a string with length equal to the rankings
            ordered_names = [0] * 1001
            # adds names to list in order they are ranked
            for key in self.names.keys():
                item = self.names[key]
                if item[decade_elem] != 0:
                    ordered_names[int(item[decade_elem])] = key
            ordered_names.remove(0)
            return ordered_names


    # Return all names that are getting more popular in every decade. The list must be sorted by name.
    def getting_popular(self):
        # searches the dict keys
        popular_names = []
        for key in self.names.keys():
            items = self.names[key]
            popular = True
            previous = int(items[0])
            for x in range(1, 11):
                # if all items are more popular add to list of names
                if int(items[x]) < previous and int(items[x]) != 0:
                    previous = int(items[x])
                else:
                    popular = False
            if popular:
                popular_names.append(key)
        return popular_names

    # Return all names that are getting less popular in every decade. The list must be sorted by name.
    def less_popular(self):
        # searches each key in dict
        popular_names = []
        for key in self.names.keys():
            items = self.names[key]
            # changes 0 in each list to 1001
            for x in range(0, len(items)):
                if items[x] == 0:
                    items[x] = 1001
            popular = True
            previous = int(items[0])
            # if each item is less than before add name to list
            for x in range(1, 11):
                if int(items[x]) > previous:
                    previous = int(items[x])
                else:
                    popular = False
            if popular:
                popular_names.append(key)
        return popular_names


def main():
    bn = BabyNames()
    bn.fill_data(file_name='names.txt')
    # create the menu with choices
    while True:
        # creates menu
        print('')
        print('Options:')
        print('Enter 1 to search for names.')
        print('Enter 2 to display data for one name.')
        print('Enter 3 to display all names that appear in only one decade.')
        print('Enter 4 to display all names that appear in all decades.')
        print('Enter 5 to display all names that are more popular in every decade.')
        print('Enter 6 to display all names that are less popular in every decade.')
        print('Enter 7 to quit.')
        print('')
        choice = input('Enter choice: ')
        if choice == '1':
            name = input('Enter a name: ')
            print('')
            # if name is in dict print the highest ranking of the name
            if bn.contains_name(name):
                print('The matches with their highest ranking decade are:')
                lst = bn.names[name]
                decade = 1900
                rank = int(lst[0])
                for x in range(0, 11):
                    if int(lst[x]) <= rank:
                        rank = int(lst[x])
                        decade += x * 10
                print(name, decade)
                print('')
            else:
                print(name, 'does not appear in any decade.')
                print('')
        elif choice == '2':
            # if name is in dict print the rankings for the name
            name = input('Enter a name: ')
            print('')
            if bn.contains_name(name):
                years = bn.find_ranking(name)
                whole_lst = ''
                for num in range(0, len(years)):
                    whole_lst += ' ' + str(years[num])
                print('{}:{}'.format(name, whole_lst))
                begin = 1900
                for x in range(0, len(years)):
                    print('{}: {}'.format(begin, years[x]))
                    begin += 10
                print('')
            else:
                print(name, 'does not appear in any decade.')
                print('')

        elif choice == '3':
            # prints every name that apears in one decade
            decade = input('Enter decade: ')
            decade = int(decade)
            one_decade = bn.ranks_of_a_decade(decade)
            print(bn.ranks_of_a_decade(decade))
            for x in range(0, 1000):
                print('{}: {}'.format(one_decade[x], x + 1))

        elif choice == '4':
            # Prints every name that appears in every decade
            print(bn.ranks_of_all_decades())
            all_names = bn.ranks_of_all_decades()
            print(len(bn.ranks_of_all_decades()), 'names appear in every decade. The names are: ')
            for x in range(0, len(bn.ranks_of_all_decades())):
                print(all_names[x])
        elif choice == '5':
            # prints all the names of the increasingly popular names
            print(bn.getting_popular())
            pop_list = bn.getting_popular()
            print(len(pop_list), 'names are more popular in every decade.')
            for x in range(0, len(pop_list)):
                print(pop_list[x])
        elif choice == '6':
            # prints all the increasely unpopular names
            print(bn.less_popular())
            unpop_list = bn.less_popular()
            print(len(unpop_list), 'names are less popular in every decade.')
            for x in range(0, len(unpop_list)):
                print(unpop_list[x])
        elif choice == '7':
            # exits loop
            print('')
            print('')
            print('Goodbye')
            break


if __name__ == '__main__':
    main()
