from linkedlist import build_linked_list
from referential_array import build_array



class HashTable:
    """
    A class for creating a hash table object
    """
    def is_digit(self, integer):
        """
        A function to check if an item is an integer
        :param integer: The integer to be checked
        :return: Boolean value true if it is, false if not
        """
        try:
            int(integer)
            return True
        except ValueError:
            return False

    def __init__(self, size):
        """
        Initialises the hash_table with an array storing any given data
        :param table_size: the size of the hash_table in which array
        :return: None
        :raise: ValueError when string is given
        """
        if not self.is_digit(size):
            raise ValueError("Please give a number for table size")
        self.hash_table = build_array(size)
        self.count = 0
        self.collision = 0
        self.size = size

    def hash_value(self, key):
        a = 149
        h = 0
        for c in str(key):
            h = (h * a + ord(c)) % self.size
        return h

    def __str__(self):
        """
        A function for when str is called on a object
        :complexity: O(n) being the size of the table
        :precondition: None
        :postcondition: A string that holds all the values in the hash-table
        :return: returns the values of the hashtable
        """
        string = ""
        for index in range(self.size):
            temp = self.hash_table[index]
            if self.hash_table[index] is None:
                pass
            elif type(self.hash_table[index]) == tuple:
                string += str(self.hash_table[index])
                string += ","
            else:
                for item in self.hash_table[index]:
                    string += str(item)
                    string += ","
        return string

    def __getitem__(self, key):
        """
        Gets the value that corresponds to the key
        :complexity: Best case O(1), worst case O(1+m), m being the size of the linked list
        :precondition: A key existing in the table
        :postcondition: If the key exists in the table, the value stored with it
        :param key: A unique value that when hashed will give you the position of the value
        :return: The value unique to the key
        """
        pos = self.hash_value(key)
        for x in range(self.size):
            if self.hash_table[pos] is None:
                raise KeyError("Value does not exist")
            elif self.hash_table[pos][0] == key:
                return self.hash_table[pos][1]
            else:
                for item in self.hash_table[pos]:
                    if item.value[0] == key:
                        return item.value[1]
                raise KeyError("Value does not exist")

    def __len__(self):
        """
        The length of the hash-table
        :complexity: O(1)
        :precondition: None
        :Postcondition: length of the table
        :return: The length of the table
        """
        return self.count

    def max_size(self):
        sum = 0
        for item in self.hash_table:
            if item is not None and type(item) != tuple:
                sum += len(item)
        return sum

    def __setitem__(self, key, data):
        """
         Sets the value at given key position, if there is already the same key, if there is a collision, creates a linked list and stores the values there
         :complexity: Best case O(1), worst case O(1+m), m being the size of the linked list
         :precondition: A key and pair of data
         :postcondition: A hashtable with a key and data pair
         :param key: The key to which you want to place the data
         :param data: The data you want to store with the key
         :return: None
         """
        pos = self.hash_value(key)
        for x in range(self.size):
            if self.hash_table[pos] is None:
                self.count += 1
                self.hash_table[pos] = (key, data)
                return
            elif self.hash_table[pos][0] == key:
                self.hash_table[pos] = (key, data)
                return
            else:
                self.collision += 1
                temp = self.hash_table[pos]
                if type(self.hash_table[pos]) == tuple:
                    self.hash_table[pos] = build_linked_list()
                    self.hash_table[pos].append(temp)
                    self.hash_table[pos].append((key,data))
                else:
                    self.hash_table[pos].append((key,data))
                self.count += 1
                return


    def __contains__(self, key):
        """
        Checks if a hashtable contains a given key
        :complexity: Best case O(1), worst case O(1+m), m being the size of the linked list
        :precondition: A key existing in the table
        :postcondition: A boolean value of the result
        :param key: A key that could be in the table
        :return: True or false depending if in the table
        """
        pos = self.hash_value(key)
        for x in range(self.size):
            if self.hash_table[pos] is None:
                return False
            elif self.hash_table[pos][0] == key:
                return True
            else:
                for item in self.hash_table[pos]:
                    if item[0] == key:
                        return True
                return False

def readfile(filename):
    """
    Asks user for a file name, reads it onto the objects list
    @precondition: A valid filename, without .txt
    @postcondition: A list with the files contents loaded onto the object
    :param filename: the filename of the file to be loaded
    :return: Nothing
    """
    try:
        with open(str(filename) + ".txt") as f:
            lines = ([line.rstrip('\n') for line in f])
        hashtable = HashTable(10000)
        for line in lines:
            hashtable[line] = line
        f.close()
    except FileNotFoundError:
        print("No file of that type!")

    print("Collisions:", hashtable.collision)
    print("Avg Probe:", hashtable.collision / len(hashtable))
    print("Load:", str(len(hashtable)) + "/" + str(hashtable.max_size()))
    print("\n")



alist = ["english_small", "english_large", "french"]
for item in alist:
    readfile(item)

def testhashvalue():
    tests = [1234, "abc", ""]
    test = HashTable(10)
    for item in tests:
        print(test.hash_value(item))


def teststr():
    hashtable = HashTable(5)
    hashtable[12] = "test 2"
    hashtable[5] = "test 3"
    print(hashtable)
    hashtable = HashTable(5)
    hashtable[12] = 1
    hashtable[5] = 2
    print(hashtable)
    hashtable = HashTable(5)
    hashtable[12] = 1
    hashtable[5] = 'a'
    print(hashtable)
    hashtable = HashTable(5)
    print(hashtable)


def testget():
    hashtable = HashTable(5)
    hashtable[12] = "test 2"
    hashtable[5] = "test 3"
    print(hashtable[12])
    hashtable = HashTable(5)
    hashtable["aa"] = "test 2"
    hashtable["bb"] = "test 3"
    print(hashtable["bb"])
    hashtable = HashTable(5)
    try:
        print(hashtable["bb"])
    except KeyError:
        pass


def testlen():
    hashtable = HashTable(5)
    print(len(hashtable))
    hashtable[12] = "test 2"
    hashtable[5] = "test 3"
    print(len(hashtable))
    hashtable[8] = "test 3"
    print(len(hashtable))

def testset():
    hashtable = HashTable(15)
    hashtable[""] = "test 1"
    hashtable[12] = "test 2"
    hashtable["aa"] = "test 3"
    hashtable["a23"] = "test 4"
    hashtable[10] = "test 5"
    hashtable["bbv"] = "test 6"
    print(hashtable)
    hashtable[12] = "test 13"
    print(hashtable)
    hashtable["aa"] = "test 14"
    print(hashtable)

def testcointains():
    hashtable = HashTable(100)
    hashtable[""] = "test 1"
    hashtable[12] = "test 2"
    hashtable["aa"] = "test 3"
    hashtable["a23"] = "test 4"
    hashtable[10] = "test 5"
    hashtable["bbv"] = "test 6"
    print(12 in hashtable)
    print("aa" in hashtable)
    print("zcv" in hashtable)
    print("" in hashtable)


testhashvalue()
teststr()
testget()
testlen()
testset()
testcointains()
