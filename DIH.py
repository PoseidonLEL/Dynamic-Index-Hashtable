class dynamic_index_hashtable:
    # A class that implements a dynamic hash table for tracking indices of strings    

    def __init__(self, data): 
        self.HashMap = self.__hashArrs(data)
        self.conditionStack = []
    

    # Private helper method to create initial hash map from array
    def __hashArrs(self,array): 
        return {x:i for (i,x) in enumerate(array)}
    

    # Returns the adjusted index of a string, accounting for removed elements
    def indexOf(self, string):
        value = self.HashMap[string]
        retVal = 0
        for i in self.conditionStack:
            if(value>i):
                retVal-=1
        return value+retVal
    

    # Adds a new string to the hash table (if it doesn't already exist)
    def add(self, string):
        if(string not in self.HashMap): 
            self.HashMap[string] = next(reversed(self.HashMap.values()))+1
            

    # Removes a string from the hash table and tracks its index
    def remove(self, string):
        if(string in self.HashMap): 
            self.conditionStack.append(self.HashMap[string])
            del self.HashMap[string]