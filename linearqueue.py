class node:
    def __init__(self, value):
        self.data = value
        self.next = None

class cqueue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, new_node):
        if self.rear is None:
            self.front = self.rear = new_node
            self.rear.next = self.front  # Point to itself for 1st node
        else:
            self.rear.next = new_node
            self.rear = new_node
            self.rear.next = self.front  # Maintain circular link

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return
        
        
        if self.front == self.rear:
            self.front = self.rear = None
            print("Now queue is empty")
        else:
            self.front = self.front.next
            self.rear.next = self.front  # Update rear's next to the new front

    def print(self):
        if self.front is None:
            print("Queue is empty")
            return
        
        temp = self.front
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.front:  # Stop when we complete a full circle
                break
        print()         


que = cqueue()
que.enqueue(node(15))
que.enqueue(node(67))
que.enqueue(node(55))
que.enqueue(node(100))
que.enqueue(node(88))
que.print()
que.dequeue()
que.print()
que.dequeue()
que.dequeue()
que.dequeue()
que.print()
que.dequeue()
que.enqueue(node(22))
que.enqueue(node(33))
que.print()