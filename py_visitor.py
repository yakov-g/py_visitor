
class File(object):
   def accept(self, v):
     v.visit(self)

class Text(File):
   data = "Text"

class Picture(File):
   data = "Picture"


class Visitor(object):

   def visit(self, o):
      method_name = "visit_" + o.__class__.__name__
      method = getattr(self, method_name, False)

      # if there is no attribute 'visit_ClassName' in Visitor class
      # error message will be printed
      if not method:
         self.error_message(o)
         return

      if callable(method):
         method(o)
      else:
         print "%s is not callable attribute"%(method_name)

   def error_message(self, o):
      print "Error: '%s' can't save '%s'"%(self.__class__.__name__, o.data)

class txtSaver(Visitor):
   def visit_Text(self, o):
      print "Saving '%s' in 'txt' format"%(o.data)

class jpgSaver(Visitor):
   def visit_Picture(self, o):
      print "Saving '%s' in 'jpg' format"%(o.data)

class blobSaver(Visitor):
   def visit_Text(self, o):
      print "Saving '%s' in 'blob' format"%(o.data)
   def visit_Picture(self, o):
      print "Saving '%s' in 'blob' format"%(o.data)

def main():
  lst = [Text(), Picture()]
  vst = [txtSaver(), jpgSaver(), blobSaver()]
  for o in lst:
    for v in vst:
      #First dispatch, accept() will be called for needed type of object:
      o.accept(v)

if __name__ == "__main__":
  main()



