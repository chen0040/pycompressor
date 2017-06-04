import unittest

from pycompressor.queue import Queue


class QueueUnitTest(unittest.TestCase):

    def test_queue(self):
        queue = Queue()
        queue.enqueue(100)
        queue.enqueue(200)
        for i in range(20):
            queue.enqueue(i)

        self.assertEqual(queue.size(), 22)
        self.assertFalse(queue.is_empty())

        self.assertEqual(queue.dequeue(), 100)
        self.assertEqual(queue.dequeue(), 200)

        for i in range(20):
            self.assertEqual(queue.dequeue(), i)

        self.assertEqual(queue.size(), 0)
        self.assertTrue(queue.is_empty())


if __name__ == '__main__':
    unittest.main()
