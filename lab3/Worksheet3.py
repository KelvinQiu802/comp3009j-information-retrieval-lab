#!/usr/bin/env python3
import math
import timeit


# define a class called "SkipList"
class SkipList:
    start = None
    length = 0

    # Constructor:
    # In Python, the first argument to a constructor is a reference to the object itself
    # ... but this is done automatically (you don't pass this in when calling the constructor)
    # Here, the thing to pass in is a list of elements to store in the skip list
    def __init__(self, elements, skip_freq=1):
        size = len(elements)

        if size > 0:
            sorted_elements = sorted(elements, reverse=True)

            # this is how often a skip pointer should be created
            # ... it is a simple calculation that will not result in
            #     exactly even skip lengths if the sqrt is not an integer.
            # ... in practice the first skip in the list might be shorter.
            skip_frequency = skip_freq

            for elem in sorted_elements:
                self.start = SkipNode(elem, self.start)
                if self.length == 0:
                    skip_to = self.start
                elif self.length % skip_frequency == 0:
                    self.start.skip = skip_to
                    skip_to = self.start
                self.length += 1

            if skip_to != self.start:
                self.start.skip = skip_to

# define the nodes that a SkipList will store


class SkipNode:
    next = None    # reference to the next node in the list
    skip = None    # skip pointer: None if it doesn't have a skip pointer, otherwise it's a reference to another node
    element = None  # element stored in this node

    # constructor, pass in:
    #   elem:      the element to store in the node
    #   next_node: reference to the next node in the list
    def __init__(self, elem, next_node):
        self.element = elem
        self.next = next_node


def intersect(list1, list2):
    # a list to store the answer (for now: we will return a SkipList at the end)
    answer = []
    p1 = list1.start  # start the first reference (p1) at the beginning list 1
    p2 = list2.start  # start the second reference (p2) at the beginning list 2

    # haven't reached the end of either list
    while p1 is not None and p2 is not None:
        # if p1 and p2 point to the equal elements, add it to the answer and move both pointers
        if p1.element == p2.element:
            answer.append(p1.element)
            p1 = p1.next
            p2 = p2.next
        # p1's element is smaller, so move p1
        elif p1.element < p2.element:
            p1 = p1.next
        # p2's element is smaller, so move p2
        else:
            p2 = p2.next
    return SkipList(answer)


def intersect_skip(l1: SkipList, l2: SkipList) -> SkipList:
    answer = []
    p1 = l1.start
    p2 = l2.start
    while p1 is not None and p2 is not None:
        if p1.element == p2.element:
            answer.append(p1.element)
            p1 = p1.next
            p2 = p2.next
        elif p1.skip is not None and p1.skip.element <= p2.element:
            p1 = p1.skip
        elif p2.skip is not None and p2.skip.element <= p1.element:
            p2 = p2.skip
        elif p1.element < p2.element:
            p1 = p1.next
        else:
            p2 = p2.next
    return SkipList(answer)


def list_to_string(l: SkipList):
    result = ''
    p = l.start
    while (p.next is not None):
        result += f'{p.element}, '
        p = p.next
    return result


# This is the code that will run when you execute this file with Python.
if __name__ == '__main__':
    list1 = SkipList(range(0, 100000))
    list2 = SkipList([2, 3, 46, 70, 7222, 999999])
    time_taken = timeit.timeit(
        'intersect( list1, list2 )', number=1000, globals=globals()
    )
    print('Normal: Execution took {:.4f} seconds'.format(time_taken))

    for i in range(2, 100):
        list1 = SkipList(range(0, 100000), skip_freq=i)
        list2 = SkipList([2, 3, 46, 70, 7222, 999999], skip_freq=i)

        # measure the time to run the intersect(...) function
        time_taken_skip = timeit.timeit(
            'intersect_skip( list1, list2 )', number=1000, globals=globals()
        )
        print(f'Skip Freq is {i}')
        print('Skip: Execution took {:.4f} seconds'.format(time_taken_skip))
