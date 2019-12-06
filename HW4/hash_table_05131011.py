#待更新
from Crypto.Hash import MD5

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.pre = None
class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
      
    def add(self, key:int)->None:
        idx=key%self.capacity
        node=self.data[idx]
        while node:
            if node.val==key:
                return
            node=node.next
        new_node=ListNode(key)
        new_node.next=self.data[idx]
        self.data[idx]=new_node
    def remove(self, key:int)->None:
        idx=key%self.capacity
        node=self.data[idx]
        if node and node.val==key:
            self.data[idx]==node.next
            return
        pre=None

    def contains(self, key):
       pass
