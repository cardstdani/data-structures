class stack():
  def __init__(self, size):
    self.data = []
    for i in range(size):
      self.data.append(None)
    self.top = -1 
  
  def __str__(self):
    return str(self.data)

  def push(self, value):
    print(self.top)
    print(len(self.data))
    if (self.top+1)>(len(self.data)-1):
      print("Error: Stack overflow")
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
