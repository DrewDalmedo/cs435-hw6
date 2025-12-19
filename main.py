'''
(a) Constructs and prints a frequency table for all characteres in the string st.

- Input:    A string st (max len 256)
- Output:   Print each character in st together with the number of times it appears
'''
def frequency_table(st):
    frequencies = {char: st.count(char) for char in st}
    print(frequencies)

    # also return frequencies for use with other parts
    return frequencies


'''
(b) Builds a Huffman tree from the input string and generates the Huffman code for each character. Print the code assigned to each character.

- Input:    A string st (max len 256)
- Output:   Print each character along with its Huffman code
'''
def Huffman_code(st):
    pass


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
    test_string = "water water everywhere but not a drop to drink"

    freq = frequency_table(test_string)
    


if __name__ == "__main__":
    main()
