from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        #current is our record of how many items we have in our RingBuffer. We have to set it to zero so we can start counting
        if self.current == None:
            self.current = 0

        #temp variable
        current_head = self.storage.head

        #if there's nothing in the RingBuffer, 
        if current_head == None:
            self.storage.add_to_head(item)
            self.current += 1
            return
        #if there is stuff but we are not at capacity (filling buffer for the first time)
        elif self.storage.__len__() < self.capacity:
            self.storage.add_to_tail(item)
            self.current += 1
        #storage is full
        else:
            #increment self.current by one
            self.current += 1
            if self.current == self.capacity:
                self.current == 0
            if self.current == 0:
                self.storage.head.value == item.value
            else:
                #won't work: can't subscript a doubly linked list
                #self.storage[self.current] == item.value
                count = 0
                current = self.storage.head
                while current != None:
                    if count == self.current:
                        self.current.value == item.value
                    current = current.next





        

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        dll_item = self.storage.head
        while dll_item != None:
            list_buffer_contents.append(dll_item.value)
            dll_item = dll_item.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
