class Heap:
    """an ordered binary tree
        attributes:
            heap_list (list)
            count (int >= 0)
        methods:
            __init__ -- instantiate a Heap object
            is_empty -- check if heap is empty
                returns:
                    empty (bool)
            parent_idx -- find the parent index of an element
                args:
                    idx (int > 0)
                returns:
                    idx (int > 0)
            left_child_idx -- find the left child index of an element
                args:
                    idx (int > 0)
                returns:
                    idx (int > 0)
            right_child_idx -- find the right child index of an element
                args:
                    idx (int > 0)
                returns:
                    idx (int > 0)
            add -- add an item to the heap
                args:
                    element (any type)
            peek --return a copy of the top element
                returns:
                    val (any type)
            pop -- remove and return top element from heap
                returns:
                    val (any type)
    """

    # instantiation
    def __init__(self):
        """instantiate a heap object
        """

        # declaring attributes
        # heap is stored as a list with a sentinel value
        self.heap_list = [None,]
        self.count = 0

    # Helper methods
    def is_empty(self):
        """check if heap is empty
            returns:
                empty (bool)
        """

        empty = self.count == 0
        return empty
    
    def parent_idx(self, idx):
        """find the parent index of an element
            args:
                idx (int > 0)
            returns:
                idx (int > 0)
        """

        idx //= 2
        return idx

    def left_child_idx(self, idx):
        """find the left child index of an element
            args:
                idx (int > 0)
            returns:
                idx (int > 0)
        """

        idx *= 2
        return idx

    def right_child_idx(self, idx):
        """find the right child index of an element
            args:
                idx (int > 0)
            returns:
                idx (int > 0)
        """

        idx *= 2 + 1
        return idx

    # adding an element to the heap
    def add(self, element):
        """add an element to the heap
            args:
                element (any type)
        """

        self.count += 1
        self.heap_list.append(element)

    # peeking at the top of the heap
    def peek(self):
        """return a copy of the top element
            returns:
                val (any type)
        """

        # checking if heap is empty
        if self.is_empty():
            print("Heap is empty")
            return None

        # otherwise return top value without removing
        else:
            val = self.heap_list[1]
            return val

    # popping off the top value from the heap
    # heap properties may not be maintained if used without heapify down
    def pop(self):
        """remove and return top element from heap
            returns:
                val (any type)
        """

        # checking if heap is empty
        if self.is_empty():
            print("Heap is empty")
            return None

        # otherwise swap top item with last item and return
        else:
            val = self.heap_list[1]
            self.heap_list[1] = self.heap_list[-1]
            self.heap_list.pop(-1)
            self.count -= 1

        return val

class MinHeap(Heap):
    """an ordered minimum heap
        attributes:
            heap_list (list)
            count (int >= 0)
        methods:
            __init__ -- instantiate a MinHeap object
            parent_idx -- find the parent index of an element
                args:
                    idx (int > 0)
                returns:
                    idx (int > 0)
            left_child_idx -- find the left child index of an element
                args:
                    idx (int > 0)
                returns:
                    idx (int > 0)
            right_child_idx -- find the right child index of an element
                args:
                    idx (int > 0)
                returns:
                    idx (int > 0)
            get_smaller_child_idx -- find the smaller child index of an element
                args:
                    idx (int > 0)
                returns:
                    idx (int > 0)
            add -- add an item to the heap
                args:
                    element (any type)
            heapify_up -- bubble up from bottom to order heap
            peek -- return a copy of the top element
                returns:
                    val (any type)
            pop -- remove and return minimum element from heap and resort
                returns:
                    mini (any type)
            heapify_down -- bubble down from top to restore order
    """

    # helper method to find the index of the smaller of an element's children
    def get_smaller_child_idx(self, idx):
        """get_smaller_child_idx -- find the smaller child index of an element
            args:
                idx (int > 0)
            returns:
                idx (int > 0)
        """

        left_child = self.heap_list[self.left_child_idx(idx)]

        try:
            right_child = self.heap_list[self.right_child_idx(idx)]
        except IndexError:
            return self.left_child_idx(idx)

        else:
            if left_child < right_child:
                return self.left_child_idx(idx)
            else:
                return self.right_child_idx(idx)

    # adding an element to the heap
    def add(self, element):
        """add an element to the heap
            args:
                element (any type)
        """

        # call superclass method and reorder
        super().add(element)
        self.heapify_up()

    # heapify up method
    def heapify_up(self):
        """bubble up from bottom to restore order
        """

        # setting the index
        idx = self.count

        # perform repeated checkswaps until list is ordered
        while self.parent_idx(idx) > 0:
            child = self.heap_list[idx]
            parent = self.heap_list[self.parent_idx(idx)]

            # check and swap
            if parent > child:
                self.heap_list[idx] = parent
                self.heap_list[self.parent_idx(idx)] = child

            # reindex
            idx = self.parent_idx(idx)

    # pop with reorder
    def pop(self):
        """remove and return minimum element from heap and resort
            returns:
                mini (any type)
        """

        mini = super().pop()
        self.heapify_down()

        return mini

    # heapify down method
    def heapify_down(self):
        """bubble down from top to restore order
        """

        # setting the index
        idx = 1

        # perform repeated checkswaps until list is ordered
        while self.left_child_idx(idx) <= self.count:
            smaller_child_idx = self.get_smaller_child_idx(idx)
            child = self.heap_list[smaller_child_idx]
            parent = self.heap_list[idx]

            # check and swap
            if parent > child:
                self.heap_list[idx] = child
                self.heap_list[smaller_child_idx] = parent

            # reindex
            idx = smaller_child_idx

class MaxHeap(Heap):
    """an ordered maximum heap
        attributes:
            heap_list (list)
            count (int >= 0)
        methods:
            __init__ -- instantiate a MinHeap object
            parent_idx -- find the parent index of an element
                args:
                    idx (int > 0)
                returns:
                    idx (int > 0)
            left_child_idx -- find the left child index of an element
                args:
                    idx (int > 0)
                returns:
                    idx (int > 0)
            right_child_idx -- find the right child index of an element
                args:
                    idx (int > 0)
                returns:
                    idx (int > 0)
            get_larger_child_idx -- find the larger child index of an element
                args:
                    idx (int > 0)
                returns:
                    idx (int > 0)
            add -- add an item to the heap
                args:
                    element (any type)
            heapify_up -- bubble up from bottom to order heap
            peek -- return a copy of the top element
                returns:
                    val (any type)
            pop -- remove and return maximum element from heap and resort
                returns:
                    maxi (any type)
            heapify_down -- bubble down from top to restore order
    """

    # helper method to find the index of the larger of an element's children
    def get_smaller_child_idx(self, idx):
        """get_larger_child_idx -- find the larger child index of an element
            args:
                idx (int > 0)
            returns:
                idx (int > 0)
        """

        left_child = self.heap_list[self.left_child_idx(idx)]

        try:
            right_child = self.heap_list[self.right_child_idx(idx)]
        except IndexError:
            return self.left_child_idx(idx)

        else:
            if left_child > right_child:
                return self.left_child_idx(idx)
            else:
                return self.right_child_idx(idx)

    # adding an element to the heap
    def add(self, element):
        """add an element to the heap
            args:
                element (any type)
        """

        # call superclass method and reorder
        super().add(element)
        self.heapify_up()

    # heapify up method
    def heapify_up(self):
        """bubble up from bottom to restore order
        """

        # setting the index
        idx = self.count

        # perform repeated checkswaps until list is ordered
        while self.parent_idx(idx) > 0:
            child = self.heap_list[idx]
            parent = self.heap_list[self.parent_idx(idx)]

            # check and swap
            if parent < child:
                self.heap_list[idx] = parent
                self.heap_list[self.parent_idx(idx)] = child

            # reindex
            idx = self.parent_idx(idx)

    # pop with reorder
    def pop(self):
        """remove and return maximum element from heap and resort
            returns:
                maxi (any type)
        """

        maxi = super().pop()
        self.heapify_down()

        return maxi

    # heapify down method
    def heapify_down(self):
        """bubble down from top to restore order
        """

        # setting the index
        idx = 1

        # perform repeated checkswaps until list is ordered
        while self.left_child_idx(idx) <= self.count:
            smaller_child_idx = self.get_smaller_child_idx(idx)
            child = self.heap_list[smaller_child_idx]
            parent = self.heap_list[idx]

            # check and swap
            if parent < child:
                self.heap_list[idx] = child
                self.heap_list[smaller_child_idx] = parent

            # reindex
            idx = smaller_child_idx
