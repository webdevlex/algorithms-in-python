class Heap:
    def __init__(self):
        self.heap = []

    # ----------------------------------
    # Print
    # ----------------------------------
    def print_heap(self):
        print(self.heap)

    # ----------------------------------
    # Get parent index
    # ----------------------------------
    def get_parent_idx(self, idx):
        return (idx - 1) // 2

    # ----------------------------------
    # Get left child
    # ----------------------------------
    def get_first_child_idx(self, current_idx):
        return (current_idx * 2) + 1

    # ----------------------------------
    # Get right child
    # ----------------------------------
    def get_second_child_idx(self, current_idx):
        return (current_idx * 2) + 2

    # ----------------------------------
    # Push
    # ----------------------------------
    def __bubble_up(self, currentValue, valueIdx):
        if valueIdx > 0:
            parentIdx = self.get_parent_idx(valueIdx)
            parentValue = self.heap[parentIdx]

            if currentValue < parentValue:
                self.heap[valueIdx], self.heap[parentIdx] = (
                    self.heap[parentIdx],
                    self.heap[valueIdx],
                )
                self.__bubble_up(parentValue, parentIdx)

    def push(self, data):
        self.heap.append(data)
        self.__bubble_up(data, len(self.heap) - 1)

    # ----------------------------------
    # Pop
    # ----------------------------------
    def __bubble_down(self, current_idx):
        first_child_idx = self.get_first_child_idx(current_idx)
        second_child_idx = self.get_second_child_idx(current_idx)
        min_idx = current_idx

        if (
            first_child_idx < len(self.heap)
            and self.heap[first_child_idx] < self.heap[min_idx]
        ):
            min_idx = first_child_idx

        if (
            second_child_idx < len(self.heap)
            and self.heap[second_child_idx] < self.heap[min_idx]
        ):
            min_idx = second_child_idx

        if min_idx != current_idx:
            self.heap[current_idx], self.heap[min_idx] = (
                self.heap[min_idx],
                self.heap[current_idx],
            )
            self.__bubble_down(min_idx)

    def pop(self):
        if len(self.heap) == 0:
            return

        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        data = self.heap.pop()

        self.__bubble_down(0)
        return data
