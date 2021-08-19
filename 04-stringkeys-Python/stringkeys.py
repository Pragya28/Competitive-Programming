"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in 
        the table."""
        n = self.calculate_hash_value(string)
        self.table[n] = string
        
    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        n = self.calculate_hash_value(string)
        if self.table[n] == string:
            return n
        else:
            return -1

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        return ord(string[0]) * 100 + ord(string[1])

