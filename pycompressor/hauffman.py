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

    def is_leave(self):
        return self.left is None and self.right is None


class HauffmanCompressor(object):

    def __init__(self):
        pass
