'''
(a) Constructs and prints a frequency table for all characteres in the string st.

- Input:    A string st (max len 256)
- Output:   Print each character in st together with the number of times it appears
'''
def frequency_table(st):
    frequencies = {}
    for char in st:
        frequencies[char] = frequencies.get(char, 0) + 1

    print(frequencies)

    # also return frequencies for use with other parts
    return frequencies


'''
(b) Builds a Huffman tree from the input string and generates the Huffman code for each character. Print the code assigned to each character.

- Input:    A string st (max len 256)
- Output:   Print each character along with its Huffman code
'''
class Node:
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq

        self.left = left
        self.right = right

class Heap:
    def __init__(self):
        self.heap_ = []

    def heapify_up(self, idx):
        while idx > 0:
            parent = (idx - 1) // 2
            
            if self.heap_[idx].freq < self.heap_[parent].freq:
                self.heap_[idx], self.heap_[parent] = self.heap_[parent], self.heap_[idx]
                idx = parent
            else:
                break

    def heapify_down(self, idx):
        size = len(self.heap_)

        while True:
            left = 2 * idx + 1
            right = 2 * idx + 2
            smallest = idx

            if left < size and self.heap_[left].freq < self.heap_[smallest].freq:
                smallest = left

            if right < size and self.heap_[right].freq < self.heap_[smallest].freq:
                smallest = right

            if smallest != idx:
                self.heap_[idx], self.heap[smallest] = self.heap_[smallest], self.heap_[idx]
                idx = smallest
            else:
                break

    def push(self, node):
        self.heap_.append(node)
        self.heapify_up(len(self.heap_) - 1)

    def pop(self):
        if len(self.heap_) == 0:
            return None

        min_node = self.heap_[0]
        last = self.heap_.pop()

        self.heap_[0] = last
        self.heapify_down(0)

        return min_node
        
    def __getitem__(self, key):
        return self.heap_[key]

    def __len__(self):
        return len(self.heap_)

def Huffman_code(st):
    frequencies = frequency_table(st)
    heap = Heap()

    for char, freq in frequencies.items():
        heap.push(heap, Node(char, freq))

    while len(heap) > 1:
        n1 = heap.pop()
        n2 = heap.pop()

        # ...


'''
(c) Prints the binary encoding of the string st using the Huffman codes produced in part (b).

- Input:
    - A string st (max len 256)
    - A dict codes containing the Huffman code for each character
- Output:   Print the binary-encoded version of st
'''
def Huffman_encode(st, codes):
    pass


'''
(d) Reconstructs the Huffman tree from the list L.

- Input:    A list L of pairs: (character, Huffman code)
- Output:   Return the root of the Huffman tree produced from the List
'''
def Huffman_tree(L):
    pass


'''
(e) Decodes a binary string back to the original text.

- Input:
    - A binary string bst (the encoded text)
    - The Huffman tree
- Output:   Print the decoded string
'''
def Huffman_decode(bst, tree):
    pass






def main():
    test_string = "mississippi"

    freq = frequency_table(test_string)
    


if __name__ == "__main__":
    main()
