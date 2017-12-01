#Auther nmap
import queue

q=queue.PriorityQueue()

q.put((-1,'jack -1'))
q.put((3,'lily 3'))
q.put((10,'lucy 10'))

while q.not_empty:
    print(q.get())
