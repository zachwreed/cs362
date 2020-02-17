import random
import sys

class Container:
    maxelements = 0 # max number of elements allowed in list
    elements = []   # list for elements in container


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
    if n in container.elements:
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
    #use all functions in library
    container = None
    count = 1000
    container = create(container, count * 2)
    list = [] # stores all added values

    # --------------------------------------------------------
    # Test remove
    for i in count:
        # add positive and negative i values
        assert add(i, container) == 1
        assert add(i * -1, container) == 1
        assert inList(i, container) == 1
        assert inList(i * -1, container) == 1
        list.append(i)
        list.append(i * -1)

    # assert size is equal to count * 2
    assert count * 2 == size(container)
    assert list == count.elements

    for i in count:
        assert inList(i, container) == 1
        assert inList(i * -1, container) == 1
        assert remove(i, container) == 1
        assert remove(i * -1, container) == 1

    assert size(container) == 0

    # --------------------------------------------------------
    # test removeAll
    list.clear()
    # reinitialize container elements with duplicates of each i
    for i in count:
        duplicate = random.randint(1, 100)
        list.append(duplicate)
        # add i values to removeAll duplicate number of times
        for j in duplicate:
            assert add(i, container) == 1
            assert inList(i, container) == 1


    # assert count of duplicates removed is equal to number removed
    for i in count:
        assert list(i) == removeAll(i, container)
        assert inList(i, container) == 0


def test_add_remove():
    #boundary test for add and remove
    container = None
    container = create(container, 10)

    # test case 1 
    # check all boundaries:
    vals = [0, -1, -sys.maxsize, 1, 1 -sys.maxsize]

    i = 0
    # add all vals to container
    for val in vals:
        if add(val, container) != 0:
            assert val == container.elements[i]
            i += 1

    # assert len(elements) == len(vals)
    assert len(vals) == len(container.elements)

    # remove the values added
    i = 0
    for val in vals:
        assert 1 == remove(val, container) 
        i += 1

    # assert number of removals == len(vals)
    assert i == len(vals)

def test_rand_add():
    #vals = [random.randint(1 -sys.maxsize, sys.maxsize), random.randint(1 -sys.maxsize, sys.maxsize)]
    #use add, remove, and inList

    # get a random value to loop
    count = random.randint(1, sys.maxsize)
    container = None
    # only 1 element will be added, checked inList, and then removed in the loop
    container = create(container, 1)

    for i in count:
        val = random.randint(-sys.maxsize, 1 -sys.maxsize)
        # assert added and append to list
        assert add(val, container) == 1
        assert inList(val, container) == 1
        assert remove(val, container) == 1

    # assert no elements in list
    assert len(container.elements) == 0

def main():
    test_remove_removeAll()
    test_add_remove()
    test_rand_add()

main()