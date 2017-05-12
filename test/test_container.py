import sys
import os
sys.path.append('/'.join(os.getcwd().split('/')[:-1]))

from lib.container import *

class TestBag(object):
    
    def test_bag_init(self):
        bag = Bag()
        assert bag.size() == 0
        assert bag.is_empty() == True
        assert len(bag) == 0

    def test_bag_add(self):
        bag = Bag()
        bag.add(1)
        assert bag.size() == 1
        assert bag.is_empty() == False
        assert len(bag) == 1
        bag.add(2)
        assert bag.size() == 2
        assert bag.is_empty() == False
        assert len(bag) == 2
        bag.add(3)
        assert bag.size() == 3
        assert bag.is_empty() == False
        assert len(bag) == 3
        bag.add(4)
        assert bag.size() == 4
        assert bag.is_empty() == False
        assert len(bag) == 4
        bag.add(5)
        assert bag.size() == 5
        assert bag.is_empty() == False
        assert len(bag) == 5

    def test_bag_str(self):
        bag = Bag()
        bag.add(1)
        bag.add(2)
        bag.add(3)
        bag.add(4)
        bag.add(5)
        assert str(bag) == "(5, 4, 3, 2, 1)"

    def test_bag_iter(self):
        bag = Bag()
        bag.add(1)
        bag.add(2)
        bag.add(3)
        bag.add(4)
        bag.add(5)
        count = 5
        for item in bag:
            assert item == count
            count -= 1

    def test_bag_repr(self):
        bag = Bag()
        bag.add(1)
        bag.add(2)
        bag.add(3)
        bag.add(4)
        bag.add(5)
        assert repr(bag) == "BAG: (5, 4, 3, 2, 1)"


class TestQueue(object):

    def test_queue_init(self):
        q = Queue()
        assert q.size() == 0
        assert len(q) == 0
        assert q.is_empty() == True

    def test_queue_enqueue(self):
        q = Queue()
        q.enqueue(1)
        assert q.size() == 1
        assert q.is_empty() == False
        q.enqueue(2)
        assert q.size() == 2
        assert q.is_empty() == False
        q.enqueue(3)
        assert q.size() == 3
        assert q.is_empty() == False
        q.enqueue(4)
        assert q.size() == 4
        assert q.is_empty() == False
        q.enqueue(5)
        assert q.size() == 5
        assert q.is_empty() == False

    def test_queue_dequeue(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(3)
        q.enqueue(5)
        q.enqueue(7)
        q.enqueue(9)
        item = q.dequeue()
        assert q.size() == 4
        assert q.is_empty() == False
        assert item == 1
        item = q.dequeue()
        assert q.size() == 3
        assert q.is_empty() == False
        assert item == 3
        item = q.dequeue()
        assert q.size() == 2
        assert q.is_empty() == False
        assert item == 5
        item = q.dequeue()
        assert q.size() == 1
        assert q.is_empty() == False
        assert item == 7
        item = q.dequeue()
        assert q.size() == 0
        assert q.is_empty() == True
        assert item == 9
        try:
            item = q.dequeue()
        except Exception:
            assert q.size() == 0
            assert q.is_empty() == True

    def test_queue_iter(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(3)
        q.enqueue(5)
        q.enqueue(7)
        q.enqueue(9)
        q.dequeue()
        count = 3
        for item in q:
            assert item == count
            count += 2

    def test_queue_str(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(3)
        q.enqueue(5)
        q.enqueue(7)
        q.enqueue(9)
        q.dequeue()
        assert len(q) == 4
        assert str(q) == "(3, 5, 7, 9)"

    def test_queue_repr(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(3)
        q.enqueue(5)
        q.enqueue(7)
        q.enqueue(9)
        q.dequeue()
        assert repr(q) == "QUEUE: (3, 5, 7, 9)"

class TestStack(object):

    def test_stack_init(self):
        q = Stack()
        assert q.size() == 0
        assert len(q) == 0
        assert q.is_empty() == True

    def test_stack_push(self):
        q = Stack()
        q.push(1)
        assert q.size() == 1
        assert q.is_empty() == False
        q.push(2)
        assert q.size() == 2
        assert q.is_empty() == False
        q.push(3)
        assert q.size() == 3
        assert q.is_empty() == False
        q.push(4)
        assert q.size() == 4
        assert q.is_empty() == False
        q.push(5)
        assert q.size() == 5
        assert q.is_empty() == False

    def test_stack_pop(self):
        q = Stack()
        q.push(1)
        q.push(3)
        q.push(5)
        q.push(7)
        q.push(9)
        item = q.pop()
        assert q.size() == 4
        assert q.is_empty() == False
        assert item == 9
        item = q.pop()
        assert q.size() == 3
        assert q.is_empty() == False
        assert item == 7
        item = q.pop()
        assert q.size() == 2
        assert q.is_empty() == False
        assert item == 5
        item = q.pop()
        assert q.size() == 1
        assert q.is_empty() == False
        assert item == 3
        item = q.pop()
        assert q.size() == 0
        assert q.is_empty() == True
        assert item == 1
        try:
            item = q.pop()
        except Exception:
            assert q.size() == 0
            assert q.is_empty() == True

    def test_stack_iter(self):
        q = Stack()
        q.push(1)
        q.push(3)
        q.push(5)
        q.push(7)
        q.push(9)
        q.pop()
        count = 7
        for item in q:
            assert item == count
            count -= 2

    def test_stack_str(self):
        q = Stack()
        q.push(1)
        q.push(3)
        q.push(5)
        q.push(7)
        q.push(9)
        q.pop()
        assert len(q) == 4
        assert str(q) == "(7, 5, 3, 1)"

    def test_stack_repr(self):
        q = Stack()
        q.push(1)
        q.push(3)
        q.push(5)
        q.push(7)
        q.push(9)
        q.pop()
        assert repr(q) == "STACK: (7, 5, 3, 1)"

class TestMaxPQ(object):

    def test_init(self):
        pq = MaxPQ(20)
        assert pq.max() == None
        assert pq.is_empty() == True
        assert pq.size() == 0
        assert len(pq) == 0
        try:
            pq.del_max() 
        except Exception:
            assert pq.size() == 0
            assert pq.is_empty() == True
            assert len(pq) == 0

    def test_insert_delMax(self):
        pq = MaxPQ(20)
        pq.insert('P')
        assert pq.max() == 'P'
        assert pq.is_empty() == False
        assert pq.size() == 1
        assert len(pq) == 1
        assert str(pq) == "['P']"
        assert repr(pq) == "MaxPQ: ['P']"

        pq.insert('Q')
        assert pq.max() == 'Q'
        assert pq.is_empty() == False
        assert pq.size() == 2
        assert len(pq) == 2
        assert str(pq) == "['Q', 'P']"
        assert repr(pq) == "MaxPQ: ['Q', 'P']"

        pq.insert('E')
        assert pq.max() == 'Q'
        assert pq.is_empty() == False
        assert pq.size() == 3
        assert len(pq) == 3
        assert str(pq) == "['Q', 'P', 'E']"
        assert repr(pq) == "MaxPQ: ['Q', 'P', 'E']"

        del_item = pq.del_max()
        assert del_item == 'Q'
        assert pq.max() == 'P'
        assert pq.is_empty() == False
        assert pq.size() == 2
        assert len(pq) == 2
        assert str(pq) == "['P', 'E']"
        assert repr(pq) == "MaxPQ: ['P', 'E']"

        pq.insert('X')
        assert pq.max() == 'X'
        assert pq.is_empty() == False
        assert pq.size() == 3
        assert len(pq) == 3
        assert str(pq) == "['X', 'E', 'P']"
        assert repr(pq) == "MaxPQ: ['X', 'E', 'P']"

        pq.insert('A')
        assert pq.max() == 'X'
        assert pq.is_empty() == False
        assert pq.size() == 4
        assert len(pq) == 4
        assert str(pq) == "['X', 'E', 'P', 'A']"
        assert repr(pq) == "MaxPQ: ['X', 'E', 'P', 'A']"

        pq.insert('M')
        assert pq.max() == 'X'
        assert pq.is_empty() == False
        assert pq.size() == 5
        assert len(pq) == 5
        assert str(pq) == "['X', 'M', 'P', 'A', 'E']"
        assert repr(pq) == "MaxPQ: ['X', 'M', 'P', 'A', 'E']"

        del_item = pq.del_max()
        assert del_item == 'X'
        assert pq.max() == 'P'
        assert pq.is_empty() == False
        assert pq.size() == 4
        assert len(pq) == 4
        assert str(pq) == "['P', 'M', 'E', 'A']"
        assert repr(pq) == "MaxPQ: ['P', 'M', 'E', 'A']"

        pq.insert('P')
        assert pq.max() == 'P'
        assert pq.is_empty() == False
        assert pq.size() == 5
        assert len(pq) == 5
        assert str(pq) == "['P', 'P', 'E', 'A', 'M']"
        assert repr(pq) == "MaxPQ: ['P', 'P', 'E', 'A', 'M']"

        pq.insert('L')
        assert pq.max() == 'P'
        assert pq.is_empty() == False
        assert pq.size() == 6
        assert len(pq) == 6
        assert str(pq) == "['P', 'P', 'L', 'A', 'M', 'E']"
        assert repr(pq) == "MaxPQ: ['P', 'P', 'L', 'A', 'M', 'E']"

        pq.insert('E')
        assert pq.max() == 'P'
        assert pq.is_empty() == False
        assert pq.size() == 7
        assert len(pq) == 7
        assert str(pq) == "['P', 'P', 'L', 'A', 'M', 'E', 'E']"
        assert repr(pq) == "MaxPQ: ['P', 'P', 'L', 'A', 'M', 'E', 'E']"

        del_item = pq.del_max()
        assert del_item == 'P'
        assert pq.max() == 'P'
        assert pq.is_empty() == False
        assert pq.size() == 6
        assert len(pq) == 6
        assert str(pq) == "['P', 'M', 'L', 'A', 'E', 'E']"
        assert repr(pq) == "MaxPQ: ['P', 'M', 'L', 'A', 'E', 'E']"


class TestMinPQ(object):

    def test_init(self):
        pq = MinPQ(20)
        assert pq.min() == None
        assert pq.is_empty() == True
        assert pq.size() == 0
        assert len(pq) == 0
        try:
            pq.del_min() 
        except Exception:
            assert pq.size() == 0
            assert pq.is_empty() == True
            assert len(pq) == 0

    def test_insert_delMin(self):
        pq = MinPQ(20)
        pq.insert('P')
        assert pq.min() == 'P'
        assert pq.is_empty() == False
        assert pq.size() == 1
        assert len(pq) == 1
        assert str(pq) == "['P']"
        assert repr(pq) == "MinPQ: ['P']"

        pq.insert('Q')
        assert pq.min() == 'P'
        assert pq.is_empty() == False
        assert pq.size() == 2
        assert len(pq) == 2
        assert str(pq) == "['P', 'Q']"
        assert repr(pq) == "MinPQ: ['P', 'Q']"

        pq.insert('E')
        assert pq.min() == 'E'
        assert pq.is_empty() == False
        assert pq.size() == 3
        assert len(pq) == 3
        assert str(pq) == "['E', 'Q', 'P']"
        assert repr(pq) == "MinPQ: ['E', 'Q', 'P']"

        del_item = pq.del_min()
        assert del_item == 'E'
        assert pq.min() == 'P'
        assert pq.is_empty() == False
        assert pq.size() == 2
        assert len(pq) == 2
        assert str(pq) == "['P', 'Q']"
        assert repr(pq) == "MinPQ: ['P', 'Q']"

        pq.insert('X')
        assert pq.min() == 'P'
        assert pq.is_empty() == False
        assert pq.size() == 3
        assert len(pq) == 3
        assert str(pq) == "['P', 'Q', 'X']"
        assert repr(pq) == "MinPQ: ['P', 'Q', 'X']"

        pq.insert('A')
        assert pq.min() == 'A'
        assert pq.is_empty() == False
        assert pq.size() == 4
        assert len(pq) == 4
        assert str(pq) == "['A', 'P', 'X', 'Q']"
        assert repr(pq) == "MinPQ: ['A', 'P', 'X', 'Q']"

        pq.insert('M')
        assert pq.min() == 'A'
        assert pq.is_empty() == False
        assert pq.size() == 5
        assert len(pq) == 5
        assert str(pq) == "['A', 'M', 'X', 'Q', 'P']"
        assert repr(pq) == "MinPQ: ['A', 'M', 'X', 'Q', 'P']"

        del_item = pq.del_min()
        assert del_item == 'A'
        assert pq.min() == 'M'
        assert pq.is_empty() == False
        assert pq.size() == 4
        assert len(pq) == 4
        assert str(pq) == "['M', 'P', 'X', 'Q']"
        assert repr(pq) == "MinPQ: ['M', 'P', 'X', 'Q']"

        pq.insert('P')
        assert pq.min() == 'M'
        assert pq.is_empty() == False
        assert pq.size() == 5
        assert len(pq) == 5
        assert str(pq) == "['M', 'P', 'X', 'Q', 'P']"
        assert repr(pq) == "MinPQ: ['M', 'P', 'X', 'Q', 'P']"

        pq.insert('L')
        assert pq.min() == 'L'
        assert pq.is_empty() == False
        assert pq.size() == 6
        assert len(pq) == 6
        assert str(pq) == "['L', 'P', 'M', 'Q', 'P', 'X']"
        assert repr(pq) == "MinPQ: ['L', 'P', 'M', 'Q', 'P', 'X']"

        pq.insert('E')
        assert pq.min() == 'E'
        assert pq.is_empty() == False
        assert pq.size() == 7
        assert len(pq) == 7
        assert str(pq) == "['E', 'P', 'L', 'Q', 'P', 'X', 'M']"
        assert repr(pq) == "MinPQ: ['E', 'P', 'L', 'Q', 'P', 'X', 'M']"

        del_item = pq.del_min()
        assert del_item == 'E'
        assert pq.min() == 'L'
        assert pq.is_empty() == False
        assert pq.size() == 6
        assert len(pq) == 6
        assert str(pq) == "['L', 'P', 'M', 'Q', 'P', 'X']"
        assert repr(pq) == "MinPQ: ['L', 'P', 'M', 'Q', 'P', 'X']"

class TestSteque(object):

    def test_init(self):
        stq = Steque()
        assert stq.size() == 0
        assert len(stq) == 0
        assert stq.is_empty() == True
        assert str(stq) == "()"
        assert repr(stq) == "STEQUE: ()"

    def test_push_pop_enqueue(self):
        stq = Steque()
        stq.enqueue(1)
        assert stq.size() == 1
        assert len(stq) == 1
        assert stq.is_empty() == False
        assert str(stq) == "(1)"
        assert repr(stq) == "STEQUE: (1)"

        item = stq.pop()
        assert item == 1
        assert stq.size() == 0
        assert len(stq) == 0
        assert stq.is_empty() == True
        assert str(stq) == "()"
        assert repr(stq) == "STEQUE: ()"

        stq.push(1)
        assert stq.size() == 1
        assert len(stq) == 1
        assert stq.is_empty() == False
        assert str(stq) == "(1)"
        assert repr(stq) == "STEQUE: (1)"

        item = stq.pop()
        assert item == 1
        assert stq.size() == 0
        assert len(stq) == 0
        assert stq.is_empty() == True
        assert str(stq) == "()"
        assert repr(stq) == "STEQUE: ()"
        try:
            item = stq.pop()
        except Exception:
            assert stq.size() == 0
            assert stq.is_empty() == True

        stq.push(1)
        stq.push(2)
        stq.push(3)
        stq.push(4)
        stq.push(5)
        assert stq.size() == 5
        assert len(stq) == 5
        assert stq.is_empty() == False
        assert str(stq) == "(5, 4, 3, 2, 1)"
        assert repr(stq) == "STEQUE: (5, 4, 3, 2, 1)"

        item = stq.pop()
        assert item == 5
        item = stq.pop()
        assert item == 4
        item = stq.pop()
        assert item == 3
        item = stq.pop()
        assert item == 2
        item = stq.pop()
        assert item == 1
        assert stq.size() == 0
        assert len(stq) == 0
        assert stq.is_empty() == True
        assert str(stq) == "()"
        assert repr(stq) == "STEQUE: ()"

        stq.push(1)
        stq.push(2)
        stq.push(3)
        stq.push(4)
        stq.push(5)
        assert stq.size() == 5
        assert len(stq) == 5
        assert stq.is_empty() == False
        assert str(stq) == "(5, 4, 3, 2, 1)"
        assert repr(stq) == "STEQUE: (5, 4, 3, 2, 1)"
        stq.enqueue(6)
        stq.enqueue(7)
        stq.enqueue(8)
        stq.enqueue(9)
        stq.enqueue(10)
        assert stq.size() == 10
        assert len(stq) == 10
        assert stq.is_empty() == False
        assert str(stq) == "(5, 4, 3, 2, 1, 6, 7, 8, 9, 10)"
        assert repr(stq) == "STEQUE: (5, 4, 3, 2, 1, 6, 7, 8, 9, 10)"


class TestDeque(object):
    def test_deque_init(self):
        dq = Deque()
        assert dq.size() == 0
        assert len(dq) == 0
        assert dq.is_empty() == True
        assert str(dq) == "()"
        assert repr(dq) == "DEQUE: ()"

    def test_deque_push_pop(self):
        dq = Deque()
        dq.push_left(1)
        assert dq.size() == 1
        assert dq.is_empty() == False
        assert len(dq) == 1
        assert str(dq) == "(1)"
        assert repr(dq) == "DEQUE: (1)"

        item = dq.pop_left()
        assert item == 1
        assert dq.size() == 0
        assert len(dq) == 0
        assert dq.is_empty() == True
        assert str(dq) == "()"
        assert repr(dq) == "DEQUE: ()"

        dq.push_right(1)
        assert dq.size() == 1
        assert dq.is_empty() == False
        assert len(dq) == 1
        assert str(dq) == "(1)"
        assert repr(dq) == "DEQUE: (1)"

        item = dq.pop_right()
        assert item == 1
        assert dq.size() == 0
        assert len(dq) == 0
        assert dq.is_empty() == True
        assert str(dq) == "()"
        assert repr(dq) == "DEQUE: ()"

        dq.push_right(1)
        assert dq.size() == 1
        assert dq.is_empty() == False
        assert len(dq) == 1
        assert str(dq) == "(1)"
        assert repr(dq) == "DEQUE: (1)"

        item = dq.pop_left()
        assert item == 1
        assert dq.size() == 0
        assert len(dq) == 0
        assert dq.is_empty() == True
        assert str(dq) == "()"
        assert repr(dq) == "DEQUE: ()"

        dq.push_left(1)
        assert dq.size() == 1
        assert dq.is_empty() == False
        assert len(dq) == 1
        assert str(dq) == "(1)"
        assert repr(dq) == "DEQUE: (1)"

        item = dq.pop_right()
        assert item == 1
        assert dq.size() == 0
        assert len(dq) == 0
        assert dq.is_empty() == True
        assert str(dq) == "()"
        assert repr(dq) == "DEQUE: ()"

        dq.push_right(1)
        dq.push_left(2)
        dq.push_right(3)
        dq.push_left(4)
        dq.push_right(5)
        dq.push_left(6)
        dq.pop_left()
        dq.pop_right()
        dq.pop_left()
        dq.pop_right()
        dq.pop_left()
        dq.pop_right()
        assert dq.size() == 0
        assert len(dq) == 0
        assert dq.is_empty() == True
        assert str(dq) == "()"
        assert repr(dq) == "DEQUE: ()"

        dq.push_right(1)
        dq.push_left(2)
        dq.push_right(3)
        dq.push_left(4)
        dq.push_right(5)
        dq.push_left(6)
        assert dq.size() == 6
        assert len(dq) == 6
        assert dq.is_empty() == False
        assert str(dq) == "(6, 4, 2, 1, 3, 5)"
        assert repr(dq) == "DEQUE: (6, 4, 2, 1, 3, 5)"

















        

















            














