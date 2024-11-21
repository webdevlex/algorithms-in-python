from collections import Counter
from typing import List
import heapq


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # If the total number of cards is not divisible by the group size,
        # it is impossible to form groups
        if len(hand) % groupSize != 0:
            return False

        # Create a frequency map to count occurrences of each card
        myMap = Counter(hand)

        # Create a min-heap with unique cards (keys of the frequency map)
        uniqueHeap = list(myMap.keys())  # Extract unique cards
        heapq.heapify(uniqueHeap)  # Transform the list into a min-heap

        # Process the heap until all cards are grouped
        while uniqueHeap:
            # Get the smallest card from the heap (starting point for the group)
            minItem = uniqueHeap[0]

            # Attempt to form a group starting with `minItem`
            for i in range(groupSize):
                curValue = minItem + i  # Card value needed for the group

                # If the required card is missing or its count is zero, fail
                if curValue not in myMap or myMap[curValue] == 0:
                    return False

                # Use one instance of the current card
                myMap[curValue] -= 1

                # If the count of the current card reaches zero, remove it from the heap
                if myMap[curValue] == 0:
                    # Ensure the card to remove matches the root of the heap
                    if curValue != uniqueHeap[0]:
                        return False  # Invalid sequence
                    heapq.heappop(uniqueHeap)  # Remove the card from the heap

        # If all groups are successfully formed, return True
        return True


# Test case
solution = Solution()
res = solution.isNStraightHand([1, 2, 4, 2, 3, 5, 3, 4], 4)
print(res)  # Expected output: True or False depending on validity
