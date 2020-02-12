import random
import sys

class Container:
    maxelements = 0
    elements = []


def create(container, maxelements):
      #container is a list, maxelements is the maximum number of elements the list can contain.  
      # maxelements is stored in a class variable so you can assume it’s available throughout the class.
    container = Container()
    container.maxelements = maxelements
    return container

def add(n, container):
    #adds n to the container list, returns 1 if it was able to add it without exceeding maxelements
    # or returns 0 if adding it would exceed the maxelements and therefore was not added
    if len(container.elements)+1 > container.maxelements:
        return 0

    container.elements.append(n)
    return 1 

def inList(n, container):
     #returns 1 if n is in container and 0 if it’s not
    if n in container:
        return 1

    return 0

def remove(n, container):
    #returns 1 if n was in the container and removes n from the container, 
    #returns 0 if n was not in the container

    if n in container.elements:
        container.elements.remove(n)
        return 1

    return 0

def removeAll(n, container):
    #removes all occurrences of n from container and 
    #returns the total number of n elements that were removed
    count = 0
    while n in container:
        container.remove(n)
        count += 1
    
    return count

def size(container):
    #returns the number of elements in container
    return len(container)


def test_remove_removeAll():
    print("none")
    #use all functions in library

def test_add_remove():
    #boundary test for add and remove
    container = None
    container = create(container, 10)

    # test case 1 
    # check all boundaries:
    #  - 0, small negative & large negative, small & large positive 
    vals = [0, -1, -sys.maxsize, 1, 1 -sys.maxsize]

    i = 0
    for val in vals:
        if add(val, container) != 0:
            assert val == container.elements[i]
            i += 1

    assert len(vals) == len(container.elements)

    i = 0
    for val in vals:
        assert 1 == remove(val, container) 
        i += 1
    
    # assert i == len(vals) - 1

def test_rand_add():
    #vals = [random.randint(1 -sys.maxsize, sys.maxsize), random.randint(1 -sys.maxsize, sys.maxsize)]
    #use add, remove, and inList
    print("none")


def main():
    test_remove_removeAll()
    test_add_remove()
    test_rand_add()

main()