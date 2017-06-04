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

    def test_huffman_string(self):
        huffman = HuffmanCompressor()
        original = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been ' \
                   'the industry standard dummy text ever since the 1500s, when an unknown printer took a galley ' \
                   'of type and scrambled it to make a type specimen book. It has survived not only five centuries, ' \
                   'but also the leap into electronic typesetting, remaining essentially unchanged. It was ' \
                   'popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, ' \
                   'and more recently with desktop publishing software like Aldus PageMaker including versions of ' \
                   'Lorem Ipsum.'
        print('before compression: ' + original)
        print('length: ' + str(len(original)))
        compressed = huffman.compress_to_string(original)
        print('after compression: ' + compressed)
        print('length: ' + str(len(compressed)))
        decompressed = huffman.decompress_from_string(compressed)
        print('after decompression: ' + decompressed)
        print('length: ' + str(len(decompressed)))
        self.assertEqual(original, decompressed)


if __name__ == '__main__':
    unittest.main()
