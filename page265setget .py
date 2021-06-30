
class Time:
  def __init__(self,hour,minute,second):	
         self.hour=hour
         self.minute=minute
         self.second=second
  def print_time  (self):
           return "%.2d:%.2d:%.2d" % (self._hour, self._minute, self._second ) 
  def __setattr__(self,name,value):
    if name=="hour":
      if   0<=value<24:	 
        self.__dict__["_hour"]=value
      else:
          raise ValueError,"Invalid hour value %d" %value

    elif name=="minute" or name=="second":
         if 0<=value<60:
           self.__dict__[ "_"+name]=value         
         else:
              raise ValueError,"Invalid %s value:%d" %(name,value)
    else:
         self.__dict__[ name ] = value

    def __getattr__(self,name):
       if name=="hour":
          return self.hour 
       elif name=="minute":
           return self.minute 
       elif name == "second":
        return self._second
       else:
           raise AttributeError, name
     	    
    	
  




print "-------------------------------------------"



time1 = Time(4,2,2)


print('Hour is :', getattr(time1, "_hour"))
print('Minute is :', getattr(time1, "_minute"))

print time1.print_time()
