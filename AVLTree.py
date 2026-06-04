# id1:
# name1:
# username1:
# id2:
# name2:
# username2:


"""A class representing a node in an AVL tree"""


class AVLNode(object):
    """Constructor, you are allowed to add more fields.

    @type key: int
    @param key: key of your node
    @type value: string
    @param value: data of your node
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = -1
        self.virtual = False

    """returns whether self is not a virtual node 

    @rtype: bool
    @returns: False if self is a virtual node, True otherwise.
    """

    def is_real_node(self):
        return not self.virtual


"""
A class implementing an AVL tree.
"""


class AVLTree(object):
    """
    Constructor, you are allowed to add more fields.

    @type is_avl: boolean
    @param is_avl: If True then tree is AVL, otherwise it is just a "regular" binary search tree, without rotations.
    """
    avl = False
    virtual = AVLNode(-1, -1)
    virtual.virtual = True
    virtual.left = virtual
    virtual.right = virtual

    def __init__(self, is_avl):
        self.root = None
        self.avl = is_avl

    """searches for a node in the dictionary corresponding to the key (starting at the root)

    @type key: int
    @param key: a key to be searched
    @rtype: (AVLNode,int)
    @returns: a tuple (x, search_time) where x is the node corresponding to key (or None if not found)
    and search_time is the search time, as defined and explained in the assignment.
    """

    def rotate_right(self, y):
        x = y.left
        B = x.right

        x.right = y
        y.left = B

        x.parent = y.parent

        if y.parent is None:
            self.root = x
        elif y.parent.left is y:
            y.parent.left = x
        else:
            y.parent.right = x

        y.parent = x

        if B.is_real_node():
            B.parent = y

        y.height = max(y.left.height,
                       y.right.height) + 1

        x.height = max(x.left.height,
                       x.right.height) + 1

        return x

    def rotate_left(self, x):
        y = x.right
        B = y.left

        y.left = x
        x.right = B

        y.parent = x.parent

        if x.parent is None:
            self.root = y
        elif x.parent.left is x:
            x.parent.left = y
        else:
            x.parent.right = y

        x.parent = y

        if B.is_real_node():
            B.parent = x

        x.height = max(x.left.height,
                       x.right.height) + 1

        y.height = max(y.left.height,
                       y.right.height) + 1

        return y

    def balance_factor(self, node):
        return node.left.height - node.right.height

    def search(self, key):
        search_time = 0  # represents the number of nodes in the path from the root to the node
        curr_node = self.root
        if self.root is None:
            return None, 1
        while curr_node.is_real_node():
            if key == curr_node.key:
                search_time += 1
                return curr_node, search_time
            if key < curr_node.key:
                curr_node = curr_node.left
                search_time += 1
            else:
                curr_node = curr_node.right
                search_time += 1
        return None, search_time + 1

    """inserts a new node into the dictionary with corresponding key and value (starting at the root)

    @type key: int
    @pre: key currently does not appear in the dictionary
    @param key: key of item that is to be inserted to self
    @type val: string
    @param val: the value of the item
    @rtype: (AVLNode,int,int,int)
    @returns: a 4-tuple (x, search_time, rotations, height_changes), where x is the new node
    and the other 3 return values are as defined and explained in the assignment.
    """

    def insert(self, key, val):

        if self.root is None:
            node = AVLNode(key, val)
            node.left = self.virtual
            node.right = self.virtual
            node.height = 0
            self.root = node
            return node, 1, 0, 0

        curr = self.root
        search_time = 0

        while curr.is_real_node():
            parent = curr
            if key < curr.key:
                curr = curr.left
            else:
                curr = curr.right
            search_time += 1

        inserted_node = AVLNode(key, val)
        inserted_node.left = self.virtual
        inserted_node.right = self.virtual
        inserted_node.parent = parent
        inserted_node.height = 0

        if key < parent.key:
            parent.left = inserted_node
        else:
            parent.right = inserted_node

        if not self.avl:
            return inserted_node, search_time + 1, 0, 0

        rotations = 0
        height_changes = 0

        curr = parent

        while curr is not None:
            old_height = curr.height
            curr.height = (
                    max(curr.left.height,
                        curr.right.height)
                    + 1
            )

            bf = self.balance_factor(curr)

            if abs(bf) < 2 and curr.height == old_height:
                break
            elif abs(bf) < 2 and curr.height != old_height:
                height_changes += 1
                curr = curr.parent
            else:
                if bf > 1:
                    if self.balance_factor(curr.left) >= 0:
                        self.rotate_right(curr)
                        rotations += 1
                    else:
                        self.rotate_left(curr.left)
                        self.rotate_right(curr)
                        rotations += 2
                else:
                    if self.balance_factor(curr.right) <= 0:
                        self.rotate_left(curr)
                        rotations += 1
                    else:
                        self.rotate_right(curr.right)
                        self.rotate_left(curr)
                        rotations += 2
                break
        return (
            inserted_node,
            search_time + 1,
            rotations,
            height_changes
        )

    """deletes node from the dictionary

    @type node: AVLNode
    @pre: node is a real pointer to a node in self
    """

    def delete(self, node):
        return

    """returns a list representing dictionary 

    @rtype: list
    @returns: a list of (key, value) tuples sorted by key, representing the data structure
    """

    def avl_to_list(self):
        return None

    """returns the number of items in dictionary 

    @rtype: int
    @returns: the number of items in dictionary 
    """

    def size(self):
        return -1

    """returns the root of the tree representing the dictionary

    @rtype: AVLNode
    @returns: the root, None if the dictionary is empty
    """

    def get_root(self):
        return None

    """returns the height of the tree

        @rtype: int
        @returns: the height of the tree 
        """

    def get_height(self):
        return -1
