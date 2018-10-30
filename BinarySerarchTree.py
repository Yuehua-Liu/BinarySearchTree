# Create Node class
class Node:
    def __init__(self, data):
        self.val = data
        self.left_node = None
        self.right_node = None

    # 插入新值(OK)
    def insert(self, data):
        # 檢查是否已經有重複的值了
        if self.val == int(data):
            return False
        # 節點值大於新增值的狀況
        elif self.val > int(data):
            if self.left_node:
                return self.left_node.insert(int(data))  # 遞迴
            else:
                self.left_node = Node(int(data))
                return True
        # 節點值小於新增值的狀況
        elif self.val < int(data):
            if self.right_node:
                return self.right_node.insert(int(data))  # 遞迴
            else:
                self.right_node = Node(int(data))
                return True

    # 尋找值(OK)
    def find(self, data):
        if self.val == data:
            return True
        elif self.val > data:
            if self.left_node:
                return self.left_node.find(data)
            else:
                return False
        else:
            if self.right_node:
                return self.right_node.find(data)
            else:
                return False

    # 找最大值(OK)
    def print_max(self):
        if self.right_node:
            return self.right_node.print_max()
        else:
            return self.val

    # 找最小值(OK)
    def print_min(self):
        if self.left_node:
            return self.left_node.print_min()
        else:
            return self.val

    # 計算 node 數(OK)
    def count_node_num(self, node_num):
        if self.left_node:
            node_num += 1
            node_num = self.left_node.count_node_num(node_num)
        if self.right_node:
            node_num += 1
            node_num = self.right_node.count_node_num(node_num)
        return node_num

    # 計算 internal node 數(OK)
    def count_internal_num(self, internal_num):
        internal_num += 1
        if self.left_node is None and self.right_node is None:
            return internal_num - 1
        if self.left_node:
            internal_num = self.left_node.count_internal_num(internal_num)
        if self.right_node:
            internal_num = self.right_node.count_internal_num(internal_num)
        return internal_num

    # 計算樹的 height(OK)
    def count_height(self):
        if self.left_node is None and self.right_node is None:
            return 1
        if self.left_node is None and self.right_node:
            return self.right_node.count_height() + 1
        if self.left_node and self.right_node is None:
            return self.left_node.count_height() + 1
        if self.left_node and self.right_node:
            lh = self.left_node.count_height()
            rh = self.right_node.count_height()
            if lh > rh:
                return lh + 1
            elif rh > lh:
                return rh + 1
            else:  # 相等情況
                return lh + 1

    # Pre-order(修)
    def preorder(self, order_list):
        order_list.append(self.val)
        if self.left_node:
            self.left_node.preorder(order_list)

        if self.right_node:
            self.right_node.preorder(order_list)
        return order_list

    # In-order(修)
    def inorder(self, order_list):
        if self.left_node:
            self.left_node.inorder(order_list)

        order_list.append(self.val)

        if self.right_node:
            self.right_node.inorder(order_list)
        return order_list

    # Post-order(修)
    def postorder(self, order_list):
        if self.left_node:
            self.left_node.postorder(order_list)

        if self.right_node:
            self.right_node.postorder(order_list)

        order_list.append(self.val)
        return order_list

    # Show mirror(OK)
    def mirror(self):
        if self.left_node:
            self.left_node.mirror()
        if self.right_node:
            self.right_node.mirror()
        temp = self.left_node
        self.left_node = self.right_node
        self.right_node = temp

    # Delete(OK)
    def delete(self, del_val, check_num):
        if self.val == del_val:
            # case_1 : 刪除的值沒有任何child
            if self.left_node is None and self.right_node is None:
                self = None
            # case_2-1 : 刪除的值有一個child(left)
            elif self.right_node is None and self.left_node:
                self = self.left_node
            # case_2-2 : 刪除的值有一個child(right)
            elif self.left_node is None and self.right_node:
                self = self.right_node
            # case 3 : 刪除的值有兩個children
            elif self.left_node and self.right_node:
                # 作法一:把左邊最大放上來
                if check_num == 1:
                    target_parent_node = self
                    target_node = self.left_node
                    while target_node.right_node:
                        target_parent_node = target_node
                        target_node = target_node.right_node
                    self.val = target_node.val
                    # self.left_node.delete(target_node.val)
                    # 把換過來的原node刪除
                    if target_node.left_node:
                        if target_parent_node.val < target_node.left_node.val:
                            target_parent_node.right_node = target_node.left_node
                        else:
                            target_parent_node.left_node = target_node.left_node
                    else:
                        target_parent_node.right_node = None

                # 作法二:把右邊最小放上來
                elif check_num == 2:
                    target_parent_node = self
                    target_node = self.right_node
                    while target_node.left_node:
                        target_parent_node = target_node
                        target_node = target_node.left_node
                    self.val = target_node.val
                    # self.left_node.delete(target_node.val)
                    # 把換過來的原node刪除
                    if target_node.right_node:
                        if target_parent_node.val < target_node.right_node.val:
                            target_parent_node.right_node = target_node.right_node
                        else:
                            target_parent_node.left_node = target_node.right_node
                    else:
                        target_parent_node.right_node = None

        # 如果該node不是要刪除的值，跳下一個
        elif self.val > del_val:
            self.left_node.delete(del_val, check_num)
        elif self.val < del_val:
            self.right_node.delete(del_val, check_num)


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

    # 找最大 find the max num(OK)
    def find_max(self):
        if self.root:
            return self.root.print_max()
        else:
            return False

    # 找最小 find the min num(OK)
    def find_min(self):
        if self.root:
            return self.root.print_min()
        else:
            return False

    # 計算樹的 Node 數(OK)
    def count_node_num(self):
        node_num = 1
        if self.root:
            return self.root.count_node_num(node_num)
        else:
            return print('There is no node exist...')

    # 計算樹的 internal Node 數(OK)
    def count_internal_num(self):
        internal_num = 0
        if self.root:
            return self.root.count_internal_num(internal_num)
        else:
            return False

    # 計算樹的高(OK)
    def count_height(self):
        if self.root:
            return self.root.count_height()
        else:
            return False

    # Pre-order(修)
    def preorder(self):
        order_list = []
        if self.root:
            print('Pre-order：' + " ".join(str(e) for e in self.root.preorder(order_list)))
        else:
            return False

    # In-order(OK)
    def inorder(self):
        order_list = []
        if self.root:
            print('In-order：' + " ".join(str(e) for e in self.root.inorder(order_list)))
        else:
            return False

    # Post-order(OK)
    def postorder(self):
        order_list = []
        if self.root:
            print('Post-order：' + " ".join(str(e) for e in self.root.postorder(order_list)))
        else:
            return False

    # Show mirror(OK)
    def mirror(self):
        if self.root:
            tree_mirror = self
            tree_mirror.root.mirror()
            return tree_mirror
        else:
            return False

    # Delete num(OK)
    def delete(self, del_val):
        if self.root:
            # step 1: 檢查值是否存在
            if not self.root.find(del_val):
                return False
            # step 2: 確認值存在，則進行刪除
            else:
                # 複製一個樹，拿來ｐｒｉｎｔ第二個結果用
                clone_tree = Tree()
                for data in node_val:
                    clone_tree.insert(int(data))
                clone_tree.insert(num_X)
                # 進行刪除
                self.root.delete(del_val, 1)
                self.preorder()

                clone_tree.root.delete(del_val, 2)
                clone_tree.preorder()


# ***********************************************************************************************


# 初始值設定(使用者介面):
node_num = input('輸入node數:')
node_val = input('輸入各node值(分隔請以空白表示):').split(' ', int(node_num)-1)
num_X = input('輸入數值X:')
num_Y = input('輸入數值Y:')

# 建立樹
new_tree = Tree()
for data in node_val:
    new_tree.insert(int(data))

# output_1:樹的postorder (OK)
new_tree.postorder()

# output_2:印出將這棵樹的 mirror 的 post-order traversal(OK)
new_tree.mirror().postorder()
new_tree.mirror()

# output_3:增加一個數 X 後, 印出 pre-order traversal(OK)
new_tree.insert(num_X)
new_tree.preorder()

# output_4:height(OK)
print(new_tree.count_height())

# output_5:印出這棵樹現在共有幾個 node(OK)
print(new_tree.count_node_num())

# output_6:印出這棵樹現在共有幾個 internal node(OK)
print(new_tree.count_internal_num())

# output_7:印出樹中最大值(OK)
print(new_tree.find_max())

# output_8:印出樹中最小值(OK)
print(new_tree.find_min())

# output_9:刪除一個數 Y 後, 印出兩種答案的 pre-order traversal (先印出左子樹最大再印出右子樹最小，如果只有一種答案則答案印兩次)(OK)
new_tree.delete(int(num_Y))
