class ListKeeper:
    def __init__(self):
        self.dictio={'example': [1,2,3,4,5]}
    
    def show(self):
        print(self.dictio)
            
    def add(self, name, addedlist):
        self.dictio[name]=addedlist
        
    def delete(self, name):
        del self.dictio[name]
        
    def sort(self, name):
        self.mylist=self.dictio.get(name)
        self.mylist.sort()
        
    def append(self, name, extlist):
        self.dictio[name].extend(extlist)
    