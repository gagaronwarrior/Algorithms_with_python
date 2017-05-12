'''
Question:
1.3.33 Deque. A double-ended queue or deque (pronounced “deck”) is like a stack or
a queue but supports adding and removing items at both ends. A deque stores a collec-
tion of items and supports the following API:
public class Deque<Item> implements Iterable<Item>
Deque() create an empty deque
isEmpty() is the deque empty?
size() number of items in the deque
void pushLeft(Item item) add an item to the left end
void pushRight(Item item) add an item to the right end
Item popLeft() remove an item from the left end
Item popRight() remove an item from the right end
boolean
int
API for a generic double-ended queue
Write a class Deque that uses a doubly-linked list to implement this API and a class
ResizingArrayDeque that uses a resizing array.

Answer: Please refer lib/container.py file for the class Deque implementation.
