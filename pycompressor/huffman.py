from pycompressor.priority_queue import MinPQ
from pycompressor.queue import Queue
from pycompressor.trie import TernarySearchTrie


class Node(object):
    left = None
    right = None
    key = None
    freq = 0

    def __init__(self, key=None, freq=None, left=None, right=None):
        if key is not None:
            self.key = key
        if freq is not None:
            self.freq = freq
        if left is not None:
            self.left = left
        if right is not None:
            self.right = right

    def is_leaf(self):
        return self.left is None and self.right is None


def char_at(text, i):
    if len(text) - 1 < i:
        return -1
    return ord(text[i])


def write_char(char, bit_stream):
    for i in range(8):
        bit = char % 2
        bit_stream.enqueue(bit)
        char = char // 2


def read_char(bit_stream):
    a = [0] * 8
    for i in range(8):
        a[i] = bit_stream.dequeue()

    char = 0
    for i in range(7, -1, -1):
        char = char * 2 + a[i]
    return char


class HuffmanCompressor(object):
    def compress_to_binary(self, text):
        trie = self.build_trie(text)
        bit_stream = Queue()
        code = {}
        self.build_code(trie, '', code)
        self.write_trie(trie, bit_stream)
        self.write_text(code, text, bit_stream)
        return bit_stream

    def write_text(self, code, text, bit_stream):
        for i in range(len(text)):
            cc = code[char_at(text, i)]
            for j in range(len(cc)):
                if cc[j] == '0':
                    bit_stream.enqueue(0)
                elif cc[j] == '1':
                    bit_stream.enqueue(1)


    def build_code(self, x, prefix, code):
        if x.is_leaf():
            code[x.key] = prefix
            return
        self.build_code(x.left, prefix + '0', code)
        self.build_code(x.right, prefix + '1', code)

    def build_trie(self, text):
        search_trie = dict()
        for i in range(len(text)):
            c = char_at(text, i)
            if c in search_trie:
                search_trie[c].freq += 1
            else:
                node = Node(key=c, freq=1)
                search_trie[c] = node

        pq = MinPQ(lambda x, y: x.freq - y.freq)
        for node in search_trie.values():
            pq.enqueue(node)

        while pq.size() > 1:
            node1 = pq.del_min()
            node2 = pq.del_min()
            freq = node1.freq + node2.freq
            node = Node(freq=freq, left=node1, right=node2)
            pq.enqueue(node)

        return pq.del_min()

    def write_trie(self, x, bit_stream):
        if x is None:
            return
        if x.is_leaf():
            bit_stream.enqueue(1)
            write_char(x.key, bit_stream)
            return

        bit_stream.enqueue(0)
        self.write_trie(x.left, bit_stream)
        self.write_trie(x.right, bit_stream)
