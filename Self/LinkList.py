class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        print("haha")

class SingleLinkList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_at_tail(self, *item):
        for node in item:
            if not isinstance(node,Node):
                node = Node(node)
            
            if self.head is None and self.tail is None:
                self.head = node
                self.tail = node
            else:
                self.tail.next = node
                self.tail = node

    def output(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def delete(self,* node):
        for data in node:
            #删除头结点的场景
            if data == self.head.data:
                self.head = self.head.next
                break

            current = self.head
            pre = self.head
            
            while current is not None:
                if current.data == data:
                    pre.next = current.next
                    break
                else:
                    pre = current
                    current = current.next

    def find(self,value):
        current = self.head

        while current is not None:
            if current.data == value:
                return current
            else:
                current = current.next

if __name__ == "__main__":
    linkList1 = SingleLinkList();
    linkList1.insert_at_tail( 4, 5, 6, 7, 8, 9);
    linkList1.output();
    linkList1.delete(5)
    linkList1.output();

    print(linkList1.find(7).data)