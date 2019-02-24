class ListItt:
    def __init__(self, count, l_list):
        self.max = count
        self.current = l_list.top

    def __iter__(self):
        return self

    def __next__(self):
        item = self.current
        if self.current is None:
            raise StopIteration
        else:
            self.current = self.current.next
            return item

class node:
    def __init__(self, item, link=None):
        self.value = item
        self.next = link

    def __str__(self):
        return str(self.value)


class build_linked_list:
    def __init__(self):
        self.count = 0
        self.top = None

    def __str__(self):
        string = ""
        assert self.top, "Please add a element before printing"
        currentNode = self.top
        while currentNode is not None:
            string += str(currentNode)
            string += "\n"
            currentNode = currentNode.next
        return string

    def __len__(self):
        return self.count

    def append(self, item):
        if self.top is None:
            self.top = node(item)
            self.count += 1
            return
        current_node = self.top
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = node(item)
        self.count += 1

    def __contains__(self, item):
        if self.top is None:
            return False
        current_node = self.top
        while current_node.next is not None:
            if current_node.value == item:
                return True
            current_node = current_node.next
        return False

    def __getitem__(self, index):
        assert isinstance(index, int), "Please enter a number"
        if index < (0 - len(self)) or index > (len(self)):
            raise IndexError("Outside of the elements of the array")
        x = 0
        if index < 0:
            index = index + self.count
        current_node = self.top
        while x < index:
            current_node = current_node.next
            x += 1
        return current_node

    def __setitem__(self, index, item):
        assert isinstance(index, int), "Please enter a number"
        if index < (0 - len(self)) or index > (len(self)):
            raise IndexError("Outside of the elements of the array")
        x = 0
        if index < 0:
            index = index + self.count
        current_node = self.top
        while x < index:
            current_node = current_node.next
            x += 1
        current_node.value = item

    def __eq__(self, other):
        if self.count != len(other):
            return False
        current_node = self.top
        x = 0
        while current_node is not None:
            if current_node.value != other[x]:
                return False
            x += 1
            current_node = current_node.next
        return True

    def insert(self, index, item):
        assert isinstance(index, int), "Please enter a number"
        if index < (0 - len(self)) or index > (len(self)):
            raise IndexError("Outside of the elements of the array")
        if index == 0 or index == 0 - self.count:
            raise IndexError("Enter a the index after you want to insert")
        else:
            if index == 0:
                self.top = node(item, self.top)
            else:
                current_node = self.__getitem__(index-1)
                current_node.next = node(item, current_node.next)
            self.count += 1

    def remove(self, item):
        found = False
        current_node = self.top
        if current_node.value == item:
            self.top = self.top.next
            found = True
        while current_node is not None and not found:
            if current_node.next.value == item:
                current_node.next = current_node.next.next
                found = True
            self.count -= 1
        if not found:
            raise ValueError("Does not exist")

    def delete(self, index):
        assert isinstance(index, int), "Please enter a number"
        if index < (0 - len(self)) or index > (len(self) - 1):
            raise IndexError("Outside of the elements of the array")
        if index == 0 or index == 0-self.count:
            self.top = self.top.next
        else:
            current_node = self.__getitem__(index-1)
            current_node.next = current_node.next.next
        self.count -= 1

    def sort(self, reverse):
        if not reverse:
            for i in range(1, len(self)):
                key = self[i].value                               # The next item we are going to insert into the sorted section of the array
                j = i-1                                     # the last item we are going to compare to
                while (j > -1) and key < self[j].value:           # now we keep moving the key back as long as it is smaller than the last item in the array
                    self[j + 1].value = self[j].value                    # if j == -1 means that this key belongs at the start
                    j = j - 1                               # move the last object compared one step ahead to make room for key
                    self[j + 1].value = key                       # observe the next item for next time.
                                                            # i is not greater than key means key belongs at i+1
        else:
            for i in range(1, len(self)):
                key = self[i].value                               # The next item we are going to insert into the sorted section of the array
                j = i-1                                     # the last item we are going to compare to
                while (j > -1) and key > self[j].value:           # now we keep moving the key back as long as it is smaller than the last item in the array
                    self[j + 1].value = self[j].value                    # if j == -1 means that this key belongs at the start
                    j = j - 1                               # move the last object compared one step ahead to make room for key
                    self[j + 1].value = key                       # observe the next item for next time.
                                                            # i is not greater than key means key belongs at i+1

    def __iter__(self):
        return ListItt(self.count, self)