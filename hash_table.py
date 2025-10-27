class Contact:
    '''
    Contact class to represent a contact with a name and number.
    Attributes:
        name (str): The name of the contact.
        number (str): The phone number of the contact.
    '''
    def __init__(self, name, number):
        self.name = name
        self.number = number
    
    def __str__(self):
        return f'{self.name}: {self.number}'


class Node:
    '''
    Node class to represent a single entry in the hash table.
    Attributes:
        key (str): The key (name) of the contact.
        value (Contact): The value (Contact object) associated with the key.
        next (Node): Pointer to the next node in case of a collision.
    '''
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
   

class HashTable:
    '''
    HashTable class to represent a hash table for storing contacts.
    Attributes:
        size (int): The size of the hash table.
        data (list): The underlying array to store linked lists for collision handling.
    Methods:
        hash_function(key): Converts a string key into an array index.
        insert(key, value): Inserts a new contact into the hash table.
        search(key): Searches for a contact by name.
        print_table(): Prints the structure of the hash table.
    '''
    def __init__(self, size=10):
        self.size = size
        self.data = [None] * self.size

    def hash_function(self, key):
        hash_value = 0
        for char in key:
            hash_value += ord(char)
        return hash_value % self.size
    
    def insert(self, key, value):
        index = self.hash_function(key)
        new_node = Node(key, value)
        
        if self.data[index] is None:
            self.data[index] = new_node
        else:
            current = self.data[index]
            while True:
                if current.key == key:
                    current.value = value  # Update existing contact
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = new_node
    
    def search(self, key):
        index = self.hash_function(key)
        current = self.data[index]
        
        while current is not None:
            if current.key == key:
                return f'{current.key}: {current.value}'
            current = current.next
        return None
    
    def print_table(self):
        for i, node in enumerate(self.data):
            if node is not None:
                current = node
                chain = []
                while current is not None:
                    chain.append(f"{current.key}: {current.value}")
                    current = current.next
                print(f"Index {i}: - " + " - ".join(chain))
            else:
                print(f"Index {i}: Empty")
    

# Test your hash table implementation here.  
contact_1 = Contact("Riley", "123-456-7890")
print(contact_1) # Riley: 123-456-7890 

contact_1 = Contact("Riley", "123-456-7890")
node_1 = Node(contact_1.name, contact_1)
print(node_1.key) # Riley 
print(node_1.value) # Riley: 123-456-7890 
print(node_1.next) # None 

table = HashTable(10)
table.insert("John", "909-876-1234")
table.insert("Rebecca", "111-555-0002")
table.print_table()

contact = table.search("John") 
print("\nSearch result:", contact)  # Search result: John: 909-876-1234

# Edge Case #1 - Hash Collisons (assuming these hash to the same index) 
table.insert("Amy", "111-222-3333") 
table.insert("May", "222-333-1111")  # May collide with Amy depending on hash function 
table.print_table()

# Edge Case #2 - Duplicate Keys 
table.insert("Rebecca", "999-444-9999")  # Should update Rebecca's number 
table.print_table()

# Edge Case #3 - Searching for a value not in the table
print(table.search("Chris")) # None

'''

Why is a hash table the right structure for fast lookups?
Hash Tables are designed to provide the constant-time average lookups, instead of checking all other entries. Always going to be used when you need fast key-value pairs lookups.

How did you handle collisions?
I handled collisions using chianning, so each index in the hash table can store a linked list of nodes. This way, if multiple keys hash to the same index, they can be stored in a linked list at the same index, rather than overwriting each other.

When might an engineer choose a hash table over a list or tree?
An engineer will choose a has table over a list or tree when they need efficient and fast lookups, insertions, and deletions of key-value pairs. Using a list or tree would make all these operations much slower, especially when the lists or trees grow bigger.

'''