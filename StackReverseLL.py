class node():
  def __init__(self, d, n):
    self.data = d
    self.next = n

  def __str__(self):
    return(str(self.data) + " " + str(self.next))

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

def insert(d, index=None):
  temp = head
  if index == None:
    while not temp.next == None:
      temp = temp.next
    temp.next = node(d, None)
  else:
    for i in range(index):
      temp = temp.next
    temp2 = temp.next
    temp.next = node(d, temp2)
  return None

def printLinkedList():
  temp = head
  print(str(temp.data) + " " + str(temp.next))
  return None

def delete(index, head):
  temp = head
  if index == 0:
        head = head.next
  else:
    for i in range(index - 1):
      if (temp.next != None):
        temp = temp.next
      else:
        temp = None
        return
            
  temp2 = temp.next
  if temp2 == None:
    temp = None
    return
  temp.next = temp2.next  

def set(index, data):
  temp = head
  
  for i in range(index):
    if (temp.next != None):
      temp = temp.next;
    else:
      temp.data = data
      return        
  temp.data = data 

def reverse():
  global head
  temp = head
  s = stack()
  while not temp == None:
    s.push(temp.data)
    temp = temp.next
  
  temp = head
  for i in range(s.top+1):
    temp.data = s.data[s.top-i]
    temp = temp.next
  s = None
  return None

head = node(1, None)
insert(2)
insert(3)
insert(4)
insert(5)
insert(6)
insert(7)
insert(8)
printLinkedList()
reverse()
printLinkedList()
