
class Version:
    def __init__(self,hashcode,date,message):
        self.version_info = {
          'hashcode' : hashcode,
          'date' : date,
          'message' : message
        }
    def to_dict(self):
       return self.version_info