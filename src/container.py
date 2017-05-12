class _Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


class Bag(object):

    def __init__(self):
        self._head = None
        self._count = 0

    def is_empty(self):
        return self._head is None

    def size(self):
        return self._count

    def __len__(self):
        return self._count

    def add(self, item):
        self._head = _Node(item, self._head)
        self._count += 1

    def __iter__(self):
        current = self._head
        while current:
            yield current.data
            current = current.next

    def __str__(self):
        string = "("
        for item in iter(self):
            string += str(item) + ", "
        return string[:-2] + ")"

    def __repr__(self):
        return "BAG: " + str(self)



class Queue(object):

    def __init__(self):
        self._head = None
        self._tail = None
        self._count = 0

    def size(self):
        return self._count

    def is_empty(self):
        return self._head is None

    def enqueue(self, item):
        node = _Node(item, None)
        if self._tail is None:
            self._tail = node
            self._head = self._tail
        else:
            self._tail.next = node
            self._tail = node
        self._count += 1

    def dequeue(self):
        if self._count == 0:
            raise Exception("QUEUE: underflow")
        item = self._head.data
        if self._head is self._tail:
            self._head = None
            self._tail = None
        else:
            self._head = self._head.next
        self._count -= 1
        return item

    def __len__(self):
        return self._count

    def __iter__(self):
        current = self._head
        while current:
            yield current.data
            current = current.next

    def __str__(self):
        string = "("
        for item in iter(self):
            string += str(item) + ", "
        return string[:-2] + ")"

    def __repr__(self):
        return "QUEUE: " + str(self)



class Stack(object):

    def __init__(self):
        self._top = None
        self._count = 0

    def size(self):
        return self._count

    def is_empty(self):
        return self._top is None

    def push(self, item):
        self._top = _Node(item, self._top)
        self._count += 1

    def pop(self):
        if self._top is None:
            raise Exception("STACK: underflow")
        item = self._top.data
        self._top = self._top.next
        self._count -= 1
        return item

    def __len__(self):
        return self._count

    def __iter__(self):
        current = self._top
        while current:
            yield current.data
            current = current.next

    def __str__(self):
        string = "("
        for item in iter(self):
            string += str(item) + ", "
        return string[:-2] + ")"

    def __repr__(self):
        return "STACK: " + str(self)



class MaxPQ(object):

    def __init__(self, pq_size=20):
        self._array = [None] * pq_size
        self._count = 0
        self._capacity = pq_size

    def max(self):
        return self._array[0]

    def is_empty(self):
        return self._count == 0

    def size(self):
        return self._count

    def __len__(self):
        return self._count

    def _exchange(self, index1, index2):
        self._array[index1], self._array[index2] = self._array[index2], self._array[index1]

    def _less(self, index1, index2):
        return self._array[index1] < self._array[index2]

    def _swim(self, key):
        while key > 0 and self._less((key-1)//2, key):
            self._exchange((key-1)//2, key)
            key = (key-1)//2

    def insert(self, item):
        if self._count < self._capacity:
            self._array[self._count] = item
            self._count += 1
            self._swim(self._count-1)
        else:
            raise Exception("MaxPQ: overflow")

    def _sink(self, key):
        while 2*key+1 <= self._count-1:
            index = 2*key+1
            if index < self._count-1 and self._less(2*key+1, 2*key+2):
                index += 1
            if not self._less(key, index):
                break
            self._exchange(key, index)
            key = index

    def del_max(self):
        if self._count == 0:
            raise Exception("MaxPQ: underflow")
        item = self._array[0]
        self._array[0] = self._array[self._count - 1]
        self._array[self._count-1] = None
        self._count -= 1
        self._sink(0)
        return item

    def __iter__(self):
        return iter(self._array)

    def __str__(self):
        item_list = [item for item in self._array if item]
        return str(item_list)

    def __repr__(self):
        return "MaxPQ: " + str(self)


class MinPQ(object):

    def __init__(self, pq_size=20):
        self._array = [None] * pq_size
        self._count = 0
        self._capacity = pq_size

    def min(self):
        return self._array[0]

    def is_empty(self):
        return self._count == 0

    def size(self):
        return self._count

    def __len__(self):
        return self._count

    def _exchange(self, index1, index2):
        self._array[index1], self._array[index2] = self._array[index2], self._array[index1]

    def _less(self, index1, index2):
        return self._array[index1] < self._array[index2]

    def _swim(self, key):
        while key > 0 and self._less(key, (key-1)//2):
            self._exchange((key-1)//2, key)
            key = (key-1)//2

    def insert(self, item):
        if self._count < self._capacity:
            self._array[self._count] = item
            self._count += 1
            self._swim(self._count-1)
        else:
            raise Exception("MinPQ: overflow")

    def _sink(self, key):
        while 2*key+1 <= self._count-1:
            index = 2*key+1
            if index < self._count-1 and self._less(2*key+2, 2*key+1):
                index += 1
            if self._less(key, index):
                break
            self._exchange(key, index)
            key = index

    def del_min(self):
        if self._count == 0:
            raise Exception("MinPQ: underflow")
        item = self._array[0]
        self._array[0] = self._array[self._count - 1]
        self._array[self._count-1] = None
        self._count -= 1
        self._sink(0)
        return item

    def __iter__(self):
        return iter(self._array)

    def __str__(self):
        item_list = [item for item in self._array if item]
        return str(item_list)

    def __repr__(self):
        return "MinPQ: " + str(self)


class Steque(object):

    def __init__(self):
        self._head = None
        self._tail = None
        self._count = 0

    def size(self):
        return self._count

    def is_empty(self):
        return self._head is None

    def enqueue(self, item):
        node = _Node(item, None)
        if self._tail is None:
            self._tail = node
            self._head = self._tail
        else:
            self._tail.next = node
            self._tail = node
        self._count += 1

    def pop(self):
        if self._count == 0:
            raise Exception("STEQUE: underflow")
        item = self._head.data
        if self._head is self._tail:
            self._head = None
            self._tail = None
        else:
            self._head = self._head.next
        self._count -= 1
        return item

    def push(self, item):
        self._head = _Node(item, self._head)
        if self._tail is None:
            self._tail = self._head
        self._count += 1

    def __len__(self):
        return self._count

    def __iter__(self):
        current = self._head
        while current:
            yield current.data
            current = current.next

    def __str__(self):
        if self.is_empty():
            string = "()"
        else:
            string = "("
            for item in iter(self):
                string += str(item) + ", "
            string = string[:-2] + ")"
        return string

    def __repr__(self):
        return "STEQUE: " + str(self)


class Deque(object):
    def __init__(self):
        self._head = None
        self._tail = None
        self._count = 0

    class _Node(object):
        def __init__(self, item):
            self.data = item
            self.prev = None
            self.next = None

    def is_empty(self):
        return self._head is None

    def size(self):
        return self._count

    def push_left(self, item):
        node = _Node(item)
        if self._head is None:
            self._head = node
            self._tail = node
        else:
            node.next = self._head
            self._head.prev = node
            self._head = node
        self._count += 1

    def push_right(self, item):
        node = _Node(item)
        if self._tail is None:
            self._tail = node
            self._head = node
        else:
            self._tail.next = node
            node.prev = self._tail
            self._tail = node
        self._count += 1

    def pop_left(self):
        if self._head is None:
            raise Exception("DEQUE: underflow")
        item = self._head.data
        if self._head == self._tail:
            self._head = None
            self._tail = None
        else:
            self._head = self._head.next
            self._head.prev = None
        self._count -= 1
        return item

    def pop_right(self):
        if self._tail is None:
            raise Exception("DEQUE: underflow")
        item = self._tail.data
        if self._tail == self._head:
            self._tail = None
            self._head = None
        else:
            self._tail = self._tail.prev
            self._tail.next = None
        self._count -= 1
        return item

    def __iter__(self):
        current = self._head
        while current:
            yield current.data
            current = current.next

    def __len__(self):
        return self._count

    def __str__(self):
        if self.is_empty():
            string = "()"
        else:
            string = "("
            for item in iter(self):
                string += str(item) + ", "
            string = string[:-2] + ")"
        return string

    def __repr__(self):
        return "DEQUE: " + str(self)



class ResizingArrayDeque(object):
    def __init__(self):
        self._head_index = 0
        self._tail_index = 0
        self._array = [None]
        self._count = 0
        self._capacity = 1

    def size(self):
        return self._count

    def is_empty(self):
        return self._count == 0

    







    









