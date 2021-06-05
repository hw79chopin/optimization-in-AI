class Binary_Search_Tree:
    def __init__(self):
        self.root=None

    def insert(self,data):
        self.root=self._insert(self.root,data)
        return self.root is not None
    
    def _insert(self,node,val):
        if node is None:
            node=Node(val)
        else:
            if val<=node.data:
                node.left=self._insert(node.left,val)
            else:
                node.right=self._insert(node.right,val)
        return node
    
    def find(self,key):
        return self._find(self.root,key)
    
    def _find(self,node,key):
        if node is None or node.data==key:
            return node is not None
        elif key<node.data:
            return self._find(node.left,key)
        else:
            return self._find(node.right,key)
    
    def delete(self,key):
        self.root,deleted=self._delete(self.root,key)
        return deleted
    
    def _delete(self,node,key):
        if node is None:
            return node,False
        deleted=False
        if key==node.data:
            deleted=True
            if node.left and node.right:
                parent,child=node,node.right
                while child.left is not None:
                    parent,child=child,child.left
                child.left=node.left
                if parent!=node:
                    parent.left=child.right
                    child.right=node.right
                node=child
            elif node.left or node.right:
                node=node.left or node.right
            else:
                node=None
        elif key<node.data:
            node.left,deleted=self._delete(node.left,key)
        else:
            node.right,deleted=self._delete(node.right,key)
        return node,deleted    

class Node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None