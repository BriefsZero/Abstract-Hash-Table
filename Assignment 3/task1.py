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

    def __init__(self, table_size):
        """
        Initialises the hash_table with an array storing any given data
        :param table_size: the size of the hash_table in which array
        :return: None
        :raise: ValueError when string is given
        """
        if not self.is_digit(table_size):
            raise ValueError("Please give a number for table size")
        self.size = table_size
        self.hash_table = build_array(table_size)
        self.count = 0

    def hash_value(self, key):
        a = 101
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
        for item in range(self.size):
            if self.hash_table[item] is not None:
                string += str(self.hash_table[item])
                string += ","
        return string

    def __getitem__(self, key):
        """
        Gets the value that corresponds to the key
        :complexity: Best case O(1), worst case O(1+m), m being the linear probe amount
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
                pos = (pos + 1) % self.size
            raise KeyError("Value does not exist")

    def __len__(self):
        """
        The length of the hash-table
        :return: the length of the table
        """
        return self.count

    def __setitem__(self, key, data):
        """
        Sets the value at given key position, if there is already the same key, updates it
        :complexity: Best case O(1), worst case O(1+m), m being the linear probe amount
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
                pos = (pos+1) % self.size
        if self.size >= self.count:
            raise MemoryError("Table is full and key does not exist")

    def __contains__(self, key):
        """
        Checks if a hashtable contains a given key
        :complexity: Best case O(1), worst case O(1+m), m being the linear probe amount
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
                pos = (pos + 1) % self.size
        return False


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
