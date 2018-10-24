# Create Node class
class Node:
    def __init__(self, data):
        self.val = data
        self.left_node = None
        self.right_node = None

    def insert(self, data):
        # 檢查是否已經有重複的值了
        if self.val == data:
            return False
        # 節點值大於新增值的狀況
        elif self.val > data:
            if self.left_node:
                return self.left_node.insert(data) # 遞迴
            else:
                self.left_node = Node(data)
                return True
        # 節點值小於新增值的狀況
        else:
            if self.right_node:
                return self.right_node.insert(data) # 遞迴
            else:
                self.right_node = Node(data)
                return True


    # def print_tree(self):
    #     print(self.data)

# Create Tree class
class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True
