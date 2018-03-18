# Your code for the 1st query goes here
# Make sure to write the "put" function to create data structure from data base.
# Make sure to write the "get" function to query from data structure
# Refer app.py to see what "put" and 'get" should return


# your implementation of data structure goes here
import pandas as pd

class Node:
        def __init__(self,key):
                self.left=None
                self.right=None
                self.rightThread=False
                self._key=key #Dictionary input

class Tree:
        def __init__(self):
                self.Root=None

        def insert(self,node):
                if self.Root is None:
                        self.Root=node
                        return
                
                cur=self.Root
                prev=None
                while cur is not None:
                        #print "inside insert while", cur._key['Employee No']
                        prev=cur
                        if cur._key['Salary']>node._key['Salary']:
                                cur=cur.left
                        else:
                                if cur.rightThread==True:
                                        break
                                else:
                                        cur=cur.right
                if prev._key['Salary']>node._key['Salary']:
                        node.right=prev
                        node.rightThread=True
                        prev.left=node
                else:
                        if prev.rightThread==True:
                                node.right=prev.right
                                node.rightThread=True
                        prev.right=node
                        prev.rightThread=False
					

def leftmost(root):
        if root is None:
                return None
        while root.left is not None:
                root=root.left
        return root

def printInOrder(root):
        if root is None:
                return
        
        cur=leftmost(root)
        result_list=[]
        while cur is not None:
                result_list.append(cur._key)
                if cur.rightThread==True:
                        cur=cur.right
                else:
                        cur=leftmost(cur.right)
        return result_list

def put():
	data_structure = Tree()
	df=pd.read_csv("final.csv")
	count=0
        for index,row in df.iterrows():
                #empno,bdate,fname,lname,gender,hdate,sal=row["Employee No"],row["Birth Date"],row["First Name"],row["Last Name"],row["Gender"],row["Hire Date"],row["Salary"]
		node=Node(row)
                data_structure.insert(node)
	return data_structure

def get(data_structure):
        #result_list=printInOrder(data_structure.Root)
        #return_list=[]
        #for elem in result_list:
        #       llist=[elem.empno,elem.bdate,elem.fname,elem.lname,elem.gender,elem.hdate,elem.sal]
        #       return_list.append(llist)
	# query on the data_structure and return data required
	return printInOrder(data_structure.Root)

#def main():
#        ds = put()
#        row_list = get(ds)
#        print len(row_list)
#if __name__ == '__main__':
#        main()

