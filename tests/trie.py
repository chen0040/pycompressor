import unittest

from pycompressor.trie import TernarySearchTrie


class TernarySearchTrieUnitTest(unittest.TestCase):

    def test_trie(self):
        trie = TernarySearchTrie()

        trie.put("Hello", "World")
        trie.put("Hi", "There")

        self.assertEqual(trie.size(), 2)
        self.assertFalse(trie.is_empty())

        self.assertEqual(trie.get("Hello"), "World")
        self.assertEqual(trie.get("Hi"), "There")
        self.assertEqual(trie.get("none"), None)

        for i in range(20):
            trie.put(str(i), i)
        for i in range(20):
            self.assertTrue(trie.contains_key(str(i)))
            self.assertEqual(trie.get(str(i)), i)

        self.assertEqual(trie.size(), 22)
        trie.delete("Hi")
        self.assertEqual(trie.size(), 21)
        self.assertFalse(trie.contains_key("Hi"))

        for key in trie.keys():
            print(key)


if __name__ == '__main__':
    unittest.main()
