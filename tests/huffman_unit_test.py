import unittest

from pycompressor.huffman import HuffmanCompressor


class HuffmanCompressionUnitTest(unittest.TestCase):

    def test_huffman(self):
        huffman = HuffmanCompressor()
        text = 'Hello World'
        bit_stream = huffman.compress_to_binary(text)
        self.assertFalse(bit_stream.is_empty())
        print(bit_stream.size())


if __name__ == '__main__':
    unittest.main()
