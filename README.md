# Dynamic-Index-Hashtable
An index hash table that is built to track the indices of large sets of unique elements while also allowing for addition and deletion of elements. Even after addition/deletion of elements, the indexOf() function will always return the correct index.


## Functions:

- __hashArrs(array): Private helper method to create initial hash map from array
  
- indexOf(string): Returns the adjusted index of a string, accounting for removed elements
  
- add(string): Adds a new string to the hash table (if it doesn't already exist)
  
- remove(string): Removes a string from the hash table and tracks its index
