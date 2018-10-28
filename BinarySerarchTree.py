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


    # Pre-order
    def preorder(self, order_list):
        order_list.append(self.val)

        if self.left_node:
            return self.left_node.inorder(order_list)

        if self.right_node:
            return self.right_node.inorder(order_list)
        return order_list

    # In-order
    def inorder(self, order_list):
        if self.left_node:
            return self.left_node.inorder(order_list)

        order_list.append(self.val)

        if self.right_node:
            return self.right_node.inorder(order_list)
        return order_list

    # Post-order
    def order(self, order_list):
        if self.left_node:
            return self.left_node.inorder(order_list)

        if self.right_node:
            return self.right_node.inorder(order_list)

        order_list.append(self.val)
        return order_list

    # Show mirror
    def mirror(self):
        if self.left_node:
            return self.left_node.mirror()
        if self.right_node:
            return self.right_node.mirror()
        temp = self.left_node
        self.left_node = self.right_node
        self.right_node = temp

    # Delete
    def delete(self, del_val):

        if self.val == del_val:
        # case_1 : 刪除的值沒有任何child
            if self.left_node is None and self.right_node is None:
                self = None
        # case_2-1 : 刪除的值有一個child(left)
            if self.left_node is not None and self.right_node is None:
                self = self.left_node
        # case_2-2 : 刪除的值有一個child(right)
            if self.left_node is None and self.right_node is not None:
                self = self.right_node
        # case_3 : 刪除的值有兩個child (未完成)
            if self.left_node is not None and self.right_node is not None:
                
        elif self.val > del_val:
            return self.left_node.delete(del_val)
        else:
            return self.right_node.delete(del_val)


# Create Tree class
class Tree:
    # 初始化
    def __init__(self):
        self.root = None

    # 插入新值 insert
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

    # 找最大 find the max num
    def find_max(self):
        if self.root:
            return self.root.print_max()
        else:
            return False

    # 找最小 find the min num
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


    # Pre-order
    def preorder(self):
        order_list = []
        if self.root:
            print('Pre-order：' + self.root.preorder(order_list))
        else:
            return False

    # In-order
    def inorder(self):
        order_list = []
        if self.root:
            print('In-order：' + self.root.inorder(order_list))
        else:
            return False

    # Post-order
    def postorder(self):
        order_list = []
        if self.root:
            print('Post-order：' + self.root.postorder(order_list))
        else:
            return False


    # Show mirror
    def mirror(self):
        if self.root:
            tree_mirror = self
            tree_mirror.root.mirror()
            print('Mirror in post-order：', tree_mirror.postorder())
        else:
            return False

    # Delete num
    def delete(self, del_val):
        if self.root:
            # step 1: 檢查值是否存在
            if not self.root.find(del_val):
                return print('The number you wanna delete is not exit!')
            # step 2: 確認值存在，則進行刪除
            else:
                self.root.delete(del_val)
                return
