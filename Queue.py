class queue():
  def __init__(self):
    self.data = []

  def enqueue(self, value):
    self.data.append(value)
    return None
  
  def dequeue(self):
    self.data.pop(0)
    return None
  
  def getFront(self):
    if self.data == []:
      return None
    return self.data[0]
  
  def __str__(self):
    return str(self.data)

q = queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()
print(q)
print(q.getFront())
