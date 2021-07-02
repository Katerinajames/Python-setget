class Time:
 def __init__(self,h,m,s):
    self._hour=h
    self._minute=m
    self._second=s	 	


 def sethour(self,h):
  self._hour=h


 def gethour(self):
   return  self._hour

 def setminute(self,m):
     self._minute=m


 def getminute(self):
  return self._minute  


 def setsecond(self,s):
       self._second=s


 def getsecond(self):
  return  self._second
  
  
  
  print"_--------------_"
  
  
p=Time(1,2,3)
  
print "%d"% (p.gethour())
  
print "%d"% (p.getminute())
print "%d"% (p.getsecond())
