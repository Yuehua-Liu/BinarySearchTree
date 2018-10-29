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

    # 找最大值
    def print_max(self):
        if self.right_node:
            return self.right_node.print_max()
        else:
            return self.val

    # 找最小值
    def print_min(self):
        if self.left_node:
            return self.left_node.print_min()
        else:
            return self.val

    # 計算 node 數
    def count_node_num(self, node_num):
        node_num += 1
        if self.left_node:
            print('算了一次左')
            return self.left_node.count_node_num(node_num)
        if self.right_node:
            print('算了一次右')
            return self.right_node.count_node_num(node_num)
        return node_num

    # 計算 internal node 數
    def count_internal_num(self, internal_num):
        internal_num += 1
        if not self.left_node or self.right_node:
            return internal_num - 1
        if self.left_node:
            return self.left_node.count_internal_num(internal_num)
        if self.right_node:
            return self.right_node.count_internal_num(internal_num)
        return internal_num
# ///////////////////////////////////////////////////////////////////////
    # 計算樹的 height
    def count_height(self):
        if self.left_node is None and self.right_node is None:
            return 1
        lh = self.left_node.count_height()
        rh = self.left_node.count_height()

        if lh > rh:
            return lh + 1
        elif rh > lh:
            return rh + 1
        else:  # 相等情況
            return lh + 1
# /////////////////////////////////////////////////////////////////////////
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

    # Delete
    # def delete(self, del_val):
    #
    #     if self.val == del_val:
    #         # case_1 : 刪除的值沒有任何child
    #         if self.left_node is None and self.right_node is None:
    #             self = None
    #         # case_2-1 : 刪除的值有一個child(left)
    #         if self.left_node and self.right_node is None:
    #             self = self.left_node
    #         # case_2-2 : 刪除的值有一個child(right)
    #         if self.left_node is None and self.right_node:
    #             self = self.right_node
    #         # case_3 : 刪除的值有兩個child (未完成)
    #         if self.left_node and self.right_node:
    #
    #     # 如果該node不是要刪除的值，跳下一個
    #     elif self.val > del_val:
    #         return self.left_node.delete(del_val)
    #     else:
    #         return self.right_node.delete(del_val)


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

    # Delete num
    def delete(self, del_val):
        if self.root:
            # step 1: 檢查值是否存在
            if not self.root.find(del_val):
                return print('The number you wanna delete is not exit!')
            # step 2: 確認值存在，則進行刪除
            else:
                if self.root.val == del_val:
                    # case_1 : 刪除的值沒有任何child
                    if self.root.left_node is None and self.root.right_node is None:
                        self.root = None
                        return print(self.preorder() + '\n' + self.preorder())
                    # case_2-1 : 刪除的值有一個child(left)
                    if self.root.left_node and self.root.right_node is None:
                        self.root = self.root.left_node
                        return print(self.preorder() + '\n' + self.preorder())
                    # case_2-2 : 刪除的值有一個child(right)
                    if self.root.left_node is None and self.root.right_node:
                        self.root = self.root.right_node
                        return print(self.preorder() + '\n' + self.preorder())
# **********************************************************************************************
                    # case_3 : 刪除的值有兩個child (未完成)
                    if self.root.left_node and self.root.right_node:
                        clone_tree = self
                        # 結果一變數設定:
                        del_nodeparent_1 = self.root
                        del_node_1 = self.root.left_node
                        # 結果二變數設定:
                        del_nodeparent_2 = clone_tree.root
                        del_node_2 = clone_tree.root.right_node

                        # 處理結果一:
                        while del_node_1:
                            del_nodeparent_1 = del_node_1
                            del_node_1 = del_node_1.right_node
                        self.root.val = del_nodeparent_1.val
                        # 最後一個數值要變None
                        del_nodeparent_1.right_node = None

                        # 處理結果二:
                        while del_node_2:
                            del_nodeparent_2 = del_node_2
                            del_node_2 = del_node_2.left_node
                        clone_tree.root.val = del_nodeparent_2.val
                        # 最後一個數值要變None
                        del_nodeparent_2.left_node = None

                        # 印出兩種可能結果:
                        return print(self.preorder() + '\n' + clone_tree.preorder())

                # 如果該node不是要刪除的值，跳下一個
                elif self.root.val > del_val:
                    return self.root.left_node.delete(del_val) # 這邊轉換可能有問題***********************
                else:
                    return self.root.right_node.delete(del_val)
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

# output_4:height
print(new_tree.count_height())

# # output_5:印出這棵樹現在共有幾個 node
# print(new_tree.count_node_num())
# # output_6:印出這棵樹現在共有幾個 internal node
# print(new_tree.count_internal_num())
# # output_7:印出樹中最大值
# print(new_tree.find_max())
# # output_8:印出樹中最小值
# print(new_tree.find_min())
# # output_9:刪除一個數 Y 後, 印出兩種答案的 pre-order traversal (先印出左子樹最大再印出右子樹最小，如果只有一種答案則答案印兩次)
# new_tree.delete(num_Y)
