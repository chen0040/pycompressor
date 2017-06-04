import unittest

from pycompressor.priority_queue import MinPQ


class MinPQUnitTest(unittest.TestCase):

    def test_pq(self):
        pq = MinPQ()
        pq.enqueue(100)
        pq.enqueue(200)
        for i in range(20):
            pq.enqueue(19 - i)

        self.assertEqual(pq.size(), 22)
        self.assertFalse(pq.is_empty())

        for i in range(20):
            self.assertEqual(pq.del_min(), i)
        self.assertEqual(pq.del_min(), 100)
        self.assertEqual(pq.del_min(), 200)
        self.assertTrue(pq.is_empty())

    def test_max_pq(self):
        pq = MinPQ(compare=lambda x, y: y - x)
        pq.enqueue(100)
        pq.enqueue(200)
        for i in range(20):
            pq.enqueue(19 - i)

        self.assertEqual(pq.size(), 22)
        self.assertFalse(pq.is_empty())

        self.assertEqual(pq.del_min(), 200)
        self.assertEqual(pq.del_min(), 100)
        for i in range(20):
            self.assertEqual(pq.del_min(), 19 - i)

        self.assertTrue(pq.is_empty())


if __name__ == '__main__':
    unittest.main()