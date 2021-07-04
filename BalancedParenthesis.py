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

def checkParenthesis(input):
  s = stack()
  for i in input:
    if i == "[" or i == "{" or i == "(":
      s.push(i)
    elif i == "]" or i == "}" or i == ")":
      if s.getTop() == "(" and i == ")":
        s.pop()
        continue
      if s.getTop() == "{" and i == "}":
        s.pop()
        continue
      if s.getTop() == "[" and i == "]":
        s.pop()
        continue
  if s.top == -1:
    return True
  else:
    return False

n = "() { (a) + (b) }"
print(checkParenthesis(n))
