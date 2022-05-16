# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2019 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 16.5 Balanced trees

### 16.5.1 Complexity of search

### 16.5.2 Balanced trees

#### Exercise 16.5.1

### 16.5.3 Checking balance

# CELL 1

# %run -i ../m269_tree

def height(tree: Tree) -> int:
    """Return how many levels the tree has."""
    if is_empty(tree):
        return 0
    return max(height(tree.left), height(tree.right)) + 1

def is_balanced(tree: Tree) -> bool:
    """Return True if and only if the tree is balanced."""
    if is_empty(tree):
        return True
    valid_factor = -1 <= height(tree.left) - height(tree.right) <= 1
    left_balanced = is_balanced(tree.left)
    right_balanced = is_balanced(tree.right)
    return valid_factor and left_balanced and right_balanced


#### Exercise 16.5.2

#### Exercise 16.5.3

