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
            if self.current < self.capacity:
                print("WHEEEEE!!!")
            else:
                #reset to 0 if at capacity
                self.current = 0   
            count = 0
            current = self.storage.head
            #increment through, looking for current spot in queue
            while current != None:
                #Overwrite values here
                if count == self.current:
                    current.value = item
                    return
                current = current.next
                count += 1





        

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
