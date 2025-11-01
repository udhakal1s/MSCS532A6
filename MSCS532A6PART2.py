# Umesh Dhakal
# MSCS532A6 - Part 2
# Arrays and Matrices, Stacks and Queues, and Singly Linked List in one file
# I included short demos so I can see outputs directly.

# Arrays and Matrices

class ArrayList:
    # I use a Python list underneath to simulate a dynamic array.
    def __init__(self):
        self.arraylist = []

    def insertitem(self, index, value):
        if index < 0 or index > len(self.arraylist):
            raise IndexError("index out of bounds")
        self.arraylist.insert(index, value)

    def appenditem(self, value):
        self.arraylist.append(value)

    def deleteitem(self, index):
        if index < 0 or index >= len(self.arraylist):
            raise IndexError("index out of bounds")
        return self.arraylist.pop(index)

    def getitem(self, index):
        if index < 0 or index >= len(self.arraylist):
            raise IndexError("index out of bounds")
        return self.arraylist[index]

    def setitem(self, index, value):
        if index < 0 or index >= len(self.arraylist):
            raise IndexError("index out of bounds")
        self.arraylist[index] = value

    def __len__(self):
        return len(self.arraylist)

    def __repr__(self):
        return f"ArrayList({self.arraylist})"


class MatrixList:
    # I use a list of lists to represent a matrix.
    def __init__(self, rows, columns, fill=0):
        if rows <= 0 or columns <= 0:
            raise ValueError("rows/columns must be positive")
        self.matrix = [[fill for _ in range(columns)] for _ in range(rows)]

    def getcell(self, row, column):
        return self.matrix[row][column]

    def setcell(self, row, column, value):
        self.matrix[row][column] = value

    def insertrow(self, rowindex, newrow=None):
        cols = len(self.matrix[0])
        if newrow is None:
            newrow = [0] * cols
        if len(newrow) != cols:
            raise ValueError("new row must match column count")
        if rowindex < 0 or rowindex > len(self.matrix):
            raise IndexError("row index out of bounds")
        self.matrix.insert(rowindex, newrow)

    def deleterow(self, rowindex):
        if rowindex < 0 or rowindex >= len(self.matrix):
            raise IndexError("row index out of bounds")
        self.matrix.pop(rowindex)

    def rows(self):
        return len(self.matrix)

    def cols(self):
        return len(self.matrix[0])

    def __repr__(self):
        return "\n".join(str(r) for r in self.matrix)


# Stacks and Queues

class StackList:
    # I use a list and append/pop for stack behavior.
    def __init__(self):
        self.stacklist = []

    def pushitem(self, value):
        self.stacklist.append(value)

    def popitem(self):
        if not self.stacklist:
            raise IndexError("pop from empty stack")
        return self.stacklist.pop()

    def peekitem(self):
        return self.stacklist[-1] if self.stacklist else None

    def isempty(self):
        return len(self.stacklist) == 0

    def __len__(self):
        return len(self.stacklist)

    def __repr__(self):
        return f"StackList({self.stacklist})"


class QueueList:
    # I use a list and pop(0) for queue behavior. This is simple and clear for assignments.
    def __init__(self):
        self.queuelist = []

    def enqueueitem(self, value):
        self.queuelist.append(value)

    def dequeueitem(self):
        if not self.queuelist:
            raise IndexError("dequeue from empty queue")
        return self.queuelist.pop(0)

    def peekfront(self):
        return self.queuelist[0] if self.queuelist else None

    def isempty(self):
        return len(self.queuelist) == 0

    def __len__(self):
        return len(self.queuelist)

    def __repr__(self):
        return f"QueueList({self.queuelist})"


# Singly Linked List

class Node:
    # I store a value and a pointer to the next node.
    def __init__(self, value, nextnode=None):
        self.value = value
        self.nextnode = nextnode


class LinkedList:
    # I manage the list through the head pointer and a length counter.
    def __init__(self):
        self.headnode = None
        self.listlength = 0

    def insertfront(self, value):
        self.headnode = Node(value, self.headnode)
        self.listlength += 1

    def insertback(self, value):
        newnode = Node(value)
        if self.headnode is None:
            self.headnode = newnode
        else:
            tempnode = self.headnode
            while tempnode.nextnode:
                tempnode = tempnode.nextnode
            tempnode.nextnode = newnode
        self.listlength += 1

    def deletevalue(self, value):
        prevnode, curnode = None, self.headnode
        while curnode:
            if curnode.value == value:
                if prevnode:
                    prevnode.nextnode = curnode.nextnode
                else:
                    self.headnode = curnode.nextnode
                self.listlength -= 1
                return True
            prevnode, curnode = curnode, curnode.nextnode
        return False

    def findvalue(self, value):
        index, curnode = 0, self.headnode
        while curnode:
            if curnode.value == value:
                return index
            index += 1
            curnode = curnode.nextnode
        return -1

    def traverse(self):
        curnode = self.headnode
        while curnode:
            yield curnode.value
            curnode = curnode.nextnode

    def __len__(self):
        return self.listlength

    def __repr__(self):
        values = [str(v) for v in self.traverse()]
        return " -> ".join(values) if values else "Empty"


# outputs

if __name__ == "__main__":
    print("\nArrays and Matrices")
    arr = ArrayList()
    arr.appenditem(10)
    arr.insertitem(1, 20)
    arr.setitem(0, 5)
    print("arraylist now:", arr)
    print("getitem(1):", arr.getitem(1))
    arr.deleteitem(1)
    print("after delete index 1:", arr)

    mat = MatrixList(2, 3, fill=0)
    mat.setcell(1, 2, 7)
    mat.insertrow(1, [9, 9, 9])
    print("matrix now:\n", mat, sep="")
    mat.deleterow(0)
    print("after delete row 0:\n", mat, sep="")

    print("\nStacks and Queues")
    st = StackList()
    st.pushitem(1)
    st.pushitem(2)
    st.pushitem(3)
    print("stack peek:", st.peekitem())
    print("stack pop:", st.popitem())
    print("stack now:", st)

    q = QueueList()
    q.enqueueitem("A")
    q.enqueueitem("B")
    q.enqueueitem("C")
    print("queue front:", q.peekfront())
    print("queue dequeue:", q.dequeueitem())
    print("queue now:", q)

    print("\nLinked List")
    ll = LinkedList()
    ll.insertfront(2)
    ll.insertfront(1)
    ll.insertback(3)
    print("list now:", ll, "length:", len(ll))
    print("find 3:", ll.findvalue(3))
    ll.deletevalue(2)
    print("after delete value 2:", ll, "length:", len(ll))
