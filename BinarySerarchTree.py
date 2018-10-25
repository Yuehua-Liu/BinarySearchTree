# Create Node class
class Node:
    def __init__(self, data):
        self.val = data
        self.left_node = None
        self.right_node = None

    # 插入新值
    def insert(self, data):
        # 檢查是否已經有重複的值了
        if self.val == data:
            return False
        # 節點值大於新增值的狀況
        elif self.val > data:
            if self.left_node:
                return self.left_node.insert(data)  # 遞迴
            else:
                self.left_node = Node(data)
                return True
        # 節點值小於新增值的狀況
        else:
            if self.right_node:
                return self.right_node.insert(data)  # 遞迴
            else:
                self.right_node = Node(data)
                return True

    # 尋找值
    def find(self, data):
        if self.val == data:
            return True
        elif self.val > data:
            if self.left_node:
                return self.find(data)
            else:
                return False
        else:
            if self.right_node:
                return self.find(data)
            else:
                return False

    # 找最大值
    def print_max(self):
        if self.right_node:
            return self.right_node.print_max()
        else:
            return print(self.val)

    # 找最小值
    def print_min(self):
        if self.left_node:
            return self.left_node.print_min()
        else:
            return print(self.val)

    # 計算 node 數
    def count_node_num(self, node_num):
        node_num += 1
        if self.left_node:
            return self.left_node.count_node_num(node_num)
        if self.right_node:
            return self.right_node.count_node_num(node_num)
        return node_num

    # 計算 internal node 數
    def count_internal_num(self, internal_num):
        internal_num += 1
        if not self.left_node or self.right_node:
            return internal_num -1
        if self.left_node:
            return self.left_node.count_internal_num(internal_num)
        if self.right_node:
            return self.right_node.count_internal_num(internal_num)
        return internal_num

    # 計算樹的 height


    # Preorder
    def preorder(self, order_list):
        order_list.append(self.val)

        if self.left_node:
            return self.left_node.inorder(order_list)

        if self.right_node:
            return self.right_node.inorder(order_list)
        return order_list

    # Inorder
    def inorder(self, order_list):
        if self.left_node:
            return self.left_node.inorder(order_list)

        order_list.append(self.val)

        if self.right_node:
            return self.right_node.inorder(order_list)
        return order_list

    # Postorder
    def order(self, order_list):
        if self.left_node:
            return self.left_node.inorder(order_list)

        if self.right_node:
            return self.right_node.inorder(order_list)

        order_list.append(self.val)
        return order_list


# Create Tree class
class Tree:
    # 初始化
    def __init__(self):
        self.root = None

    # 插入新值
    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    # 尋找值
    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    # 找最大
    def find_max(self):
        if self.root:
            return self.root.print_max()
        else:
            return False

    # 找最小
    def find_min(self):
        if self.root:
            return self.root.print_min()
        else:
            return False

    # 計算樹的 Node 數
    def count_node_num(self):
        node_num = 0
        if self.root:
            return self.root.count_node_num(node_num)
        else:
            return print('There is no node exist...')

    # 計算樹的 internal Node 數
    def count_internal_num(self):
        internal_num = 0
        if self.root:
            return self.root.count_internal_num(internal_num)
        else:
            return False

    # 計算樹的高
    def count_height(self):


    # Preorder
    def preorder(self):
        list = []
        if self.root:
            print('Preorder：' + self.root.preorder(list))
        else:
            return False

    # Inorder
    def inorder(self):
        list = []
        if self.root:
            print('Inorder：' + self.root.inorder(list))
        else:
            return False

    # Postorder
    def postorder(self):
        list = []
        if self.root:
            print('Postorder：' + self.root.postorder(list))
        else:
            return False
