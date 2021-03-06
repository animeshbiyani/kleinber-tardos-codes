class binHeap:
  def __init__(self):
    self.heapList = [0]
    self.currentSize = 0
    
  def percUp(self,i):
    while (i // 2) > 0:
      if self.heapList[i] < self.heapList[i // 2]:
        tmp = self.heapList[i]
        self.heapList[i] = self.heapList[i // 2]
        self.heapList[i // 2] = tmp
      i = i // 2
    
  def insert(self,k):
    self.heapList.append(k)
    self.currentSize += 1
    self.percUp(self.currentSize)
    
  def percDown(self,i):
    while (i * 2) <= self.currentSize:
      mc = self.minChild(i)
      if self.heapList[mc] < self.heapList[i]:
        tmp = self.heapList[mc]
        self.heapList[mc] = self.heapList[i]
        self.heapList[i] = tmp
      i = i * 2
      
  def minChild(self,i):
    if (i * 2 + 1) > self.currentSize:
      return i * 2
    else:
      if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
        return i * 2
      else:
        return i * 2 + 1
  
  def delMin(self):
    retval = self.heapList[1]
    self.heapList[1] = self.heapList[-1]
    self.heapList.pop()
    self.percDown(1)
    self.currentSize -= 1
    return retval
    
  def buildHeap(self,aList):
    i = len(aList) // 2  
    self.heapList = [0] + aList[:]
    self.currentSize = len(aList)
    while i > 0:
      self.percDown(i)
      i = i - 1
      i = i 
