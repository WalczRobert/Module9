"""
Robert Walczak
Python Modules Assignment. Write a python module, called my_definitions that include the following:
a function greeting
a function message
a function print_dict()
a function print_set()
"""

def hello(name):
    ''' this function takes in a name and prints a greeting and a message that I am the author.'''
    print ('Hello, I am ' + name + '. ' + 'I am the author of this module.')


def print_dict(dict_input):
    ''' this function takes in a dictionary and prints the keys one per line.'''
    for i in dict_input.keys():
        print(dict_input[i])

def print_set(set_input):
    ''' this function takes in a set and prints the set one per line.'''
    for i in set_input:
        print (i)

if __name__ == '__main__':
    employees = ({"name": "Mack", "years": 23, "Position": "Developer"})
    Billy = ("Goat", 12, "Barn")
    John = ("Dog", 5, "house")
    animals = (Billy, John)
    hello('Robert Walczak')
    print_dict(employees)
    print_set(animals)