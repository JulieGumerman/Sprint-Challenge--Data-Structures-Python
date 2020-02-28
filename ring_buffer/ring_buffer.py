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
        if self.current < self.capacity:
            self.storage.add_to_head(item)
            self.current += 1
            return
        #if there is stuff...
        else:
            pass



        

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
