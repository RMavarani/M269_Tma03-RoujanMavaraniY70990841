# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2019 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 16.4 Binary search trees

# CELL 1

# %run -i ../m269_tree

KEY = 0
VALUE = 1

# CELL 2

ONE = (1, 'I')
FOUR = (4, 'IV')
FIVE = (5, 'V')
SIX = (6, 'VI')
EIGHT = (8, 'VIII')

one = join(ONE, Tree(), Tree())
six = join(SIX, Tree(), Tree())
bst = join(FOUR, one, join(EIGHT, join(FIVE, Tree(), six), Tree()))

### 16.4.1 Search

# CELL 3

def has(tree: Tree, key: object) -> bool:
    """Return True if and only if a node of tree has the key.
    Preconditions: tree is a BST
    """
    if is_empty(tree):
        return False
    elif tree.root[KEY] == key:
        return True
    elif tree.root[KEY] < key:
        return has(tree.right, key)
    else:
        return has(tree.left, key)

has(bst, 2)

# CELL 4

has(bst, 6)

#### Exercise 16.4.1

# CELL 5

# %run -i ../m269_util


def lookup(tree: Tree, key: object) -> object:
    """Return the value associated to the key.
    Preconditions: tree is a BST and has the key""" 
    if tree.root[KEY] == key:
        return tree.root[VALUE]
    elif tree.root[KEY] < key:
        return lookup(tree.right, key)
    else:
        return lookup(tree.left, key)

#### Exercise 16.4.2

#### Exercise 16.4.3

# CELL 6


def smallest(tree: Tree) -> object:
    """Return the item in the tree with the smallest key.
    Preconditions: tree is a non-empty BST
    """
    pass

# CELL 7

smallest(bst) == ONE

# CELL 8

smallest(six) == SIX    # this tree has a single node

### 16.4.2 Add node

# CELL 9

def associate(tree: Tree, key: object, value: object) -> None:
    """Associate the value to the key in the tree.
    Preconditions: tree is a BST
    Postconditions:
    - if there's a node with the key, replace its value with the given one
    - otherwise, add the key-value pair to the tree
    """
    # Base case: if tree is empty, create a leaf
    if is_empty(tree):
        tree.root = (key, value)
        tree.left = Tree()
        tree.right = Tree()
    # Base case: if the key is in the root, replace the value
    elif tree.root[KEY] == key:
        tree.root = (key, value)
    # Recurrence relation: add/replace in the appropriate subtree
    elif tree.root[KEY] < key:
        associate(tree.right, key, value)
    else:
        associate(tree.left, key, value)

# CELL 10

def write(tree: Tree, level: int) -> None:
    """Print the tree as in file browsers, with subtrees indented.
    Preconditions: level >= 0 is the initial indentation level
    """
    if is_empty(tree):
        print(' ' * 4 * level, 'EMPTY')
    else:
        print(' ' * 4 * level, tree.root)
        write(tree.left, level + 1)
        write(tree.right, level + 1)



### 16.4.3 Remove node

# CELL 12

def smallest(tree: Tree) -> object:
    """Return the item in the tree with the smallest key.
    Preconditions: tree is a non-empty BST
    """
    while not is_empty(tree.left):
        tree = tree.left
    return tree.root

def remove(tree: Tree, key: object):
    """Remove the tree's node with the key.
    Do nothing if there's no such node.
    """
    if is_empty(tree):
        pass                        # key not found
    elif tree.root[KEY] < key:
        remove(tree.right, key)
    elif key < tree.root[KEY]:
        remove(tree.left, key)
    else:                           # key found: it's in the root
        if is_empty(tree.left):     # replace tree with right subtree
            tree.root = tree.right.root
            tree.left = tree.right.left
            tree.right = tree.right.right
        elif is_empty(tree.right):    # replace tree with left subtree
            tree.root = tree.left.root
            tree.right = tree.left.right    # note different order
            tree.left = tree.left.left      # of assignments
        else:                       # replace root with successor
            tree.root = smallest(tree.right)
            remove(tree.right, tree.root[KEY])

