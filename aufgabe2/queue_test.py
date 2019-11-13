from queue import Queue

q = Queue()
print(q.isEmpty())
#True
q = Queue()
q.enqueue("Kekse")
q.enqueue("Kuchen")
print(q.head())
print(q.dequeue())
print(q.head())
print(q.dequeue())
print(q.head())

#Kekse
