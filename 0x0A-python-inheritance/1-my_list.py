#!/usr/bin/python3
'''Create a class MyList that inherits from list'''


class MyList(list):
    '''Class MyList that inherits from list'''

    def print_sorted(self):
        print(sorted(self))


# my_list = MyList()
# my_list.append('a')
# my_list.append([2, 'b', 4])
# my_list.append([-1, 9, 'c'])
# my_list.print_sorted()
