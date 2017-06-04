import unittest

from pycompressor.huffman import HuffmanCompressor


class HuffmanCompressionUnitTest(unittest.TestCase):

    def test_huffman_binary(self):
        huffman = HuffmanCompressor()
        text = 'Hello World'
        bit_stream = huffman.compress_to_binary(text)
        self.assertFalse(bit_stream.is_empty())
        print(bit_stream.size())
        decompressed = huffman.decompress_from_binary(bit_stream)
        print(decompressed)
        self.assertEqual(text, decompressed)

    def text_huffman_string(self):
        huffman = HuffmanCompressor()
        text = 'Hello World'


if __name__ == '__main__':
    unittest.main()
