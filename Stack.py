class stack():
  def __init__(self, size=None):
    self.data = []
    if size == None or size <= 0:
      size = 1    
    for i in range(size):
      self.data.append(None)
    self.top = -1 
  
  def __str__(self):
    return str(self.data)
  
  def getTop(self):
    return self.data[self.top]

  def push(self, value):
    if (self.top+1)>(len(self.data)-1):
      self.data.append(value)
      self.top += 1
      return None
    self.top += 1
    self.data[self.top] = value
    return None
  
  def pop(self):
    self.data[self.top] = None
    self.top -= 1    
    return None

myStack = stack(2)
myStack.push(1)
myStack.push(1)
myStack.push(1)
print(myStack)
print(myStack.top)
print(myStack.getTop())
