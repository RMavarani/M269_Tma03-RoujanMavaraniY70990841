import m269_priority
import m269_tree
from collections import Counter

"""
A partial implementation of the Bag ADT, using the Counter class.
"""

class Bag:

    def __init__(self):
        """Create a new empty bag."""
        self.items = Counter()
        self.count = 0

    def size(self) -> int:
        """Return the total number of copies of all items in the bag."""
        return self.count

    def add(self, item: object) -> None:
        """Add one copy of item to the bag.
           Multiple copies are allowed."""
        self.items[item] =  self.items[item] + 1
        self.count = self.count + 1

    def discard(self, item: object) -> None:
        """ Remove at most one copy of item from the bag.
            No effect if item is not in the bag.
        """
        if self.items[item] > 0:
           self.items[item] =  self.items[item] - 1   
           self.count = self.count - 1


    def contains(self, item: object) -> bool:
        """ Return True if there is at least
            one copy of item in the bag.
        """
        # Add your own code here to replace the following statement
        if self.items[item]!=0:
            return True
        else:
            return False

        

    def multiplicity(self, item: object) -> int:
        """Return the number of copies of item in the bag.      
        Return zero if the item doesn't occur in the bag.
        """
        # Add your own code here to replace the following statement
        copies=self.items[item]
        return copies


    def ordered(self) :     
        """Return the items ordered by decreasing multiplicity.
        Return a list of (count, item) pairs.
        """
        # You will be asked to add your own code here later
        sorted(self.items)
        return self.items 



""" ============================================================================ """
""" Test code for Q1(a) - you should run this code but do not need to change it. """

# failed = 0
# ran = 0

# def test(name: str, actual: object, expected: object) -> None:
#     """Report if test passed or failed."""
#     global ran, failed
#     if actual == expected:
#         print(name, 'OK')
#     else:
#         print(name, 'FAILED: got', actual, 'instead of', expected)
#         failed += 1
#     ran += 1

# words = Bag()
# words.add('once')
# words.add('twice')
# words.add('twice')
# words.add('thrice')
# words.add('thrice')

# words.add('thrice')

# test('size after adds', words.size(), 6)
# test('non-existing item', words.multiplicity('none'),  0)
# test('twice occurs twice', words.multiplicity ('twice'),  2)
# test('thrice occurs thrice', words.multiplicity ('thrice'), 3)


# #Note attempting to remove more copies of 'twice' than are in the bag
# words.discard('twice')
# words.discard('twice')
# words.discard('twice')
# words.discard('twice')

# words.discard('thrice')


# test('size after discards', words.size(), 3)
# test('once remains once', words.multiplicity('once'), 1)
# test('twice gone', words.multiplicity('twice'), 0)
# test('thrice remains twice', words.multiplicity('thrice'), 2)


# test('contains once', words.contains('once'), True)
# test('does not contain twice', words. contains ('twice'), False)
# test('contains thrice', words.contains('thrice'), True)
# print(words.ordered())

# print()
# print('Ran', ran, 'tests:', ran - failed, 'OK,', failed, 'FAILED')

# if failed == 0:
#     print('You passed all our tests. Well done!')