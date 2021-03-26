class ListKeeper:
    '''This class is used to work with named list in a dictionnary. It initialized with an example. Currently, it can show existing lists, add a new named list, delete a
    list by his name, sort a list in ascending order and append a list to an existing one'''
    
    def __init__(self): 
        '''Init the class with a dictionnary'''
        self.dictio={'example': [1,2,3,4,5]}
    
    def show(self):
        '''Show dictionnary'''
        print(self.dictio)
            
    def add(self, name, addedlist):
        '''Add a new named list to the dictionnary'''
        self.dictio[name]=addedlist
        
    def delete(self, name):
        '''Delete a list by his name'''
        del self.dictio[name]
        
    def sort(self, name):
        '''Sort a named list by ascending order'''
        self.mylist=self.dictio.get(name)
        self.mylist.sort()
        
    def append(self, name, extlist):
        '''Method to append a list to an existing one'''
        self.dictio[name].extend(extlist)
    