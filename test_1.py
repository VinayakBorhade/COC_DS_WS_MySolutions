# Your code for the 1st query goes here
# Make sure to write the "put" function to create data structure from data base.
# Make sure to write the "get" function to query from data structure
# Refer app.py to see what "put" and 'get" should return


# your implementation of data structure goes here
class minHeap:
        heapList=[]
        heapLength=0
        key=[]
        
        
        def insertKey(self,key):
		
		#print key
		#print key[6]
		self.heapList.append(key)
		#print self.heapList
		#print self.heapList
		i=len(self.heapList)-1
                
		while i>0:
                        if self.heapList[(i)//2][-1]>self.heapList[i][-1]:
                                self.heapList[(i)//2],self.heapList[i]=self.heapList[i],self.heapList[(i)/2]
                        i=i/2
                
                """        
                while (i!=0)and self.heapList[(i-1)//2][6]>self.heapList[i][6]:
                        self.heapList[(i-1)//2],self.heapList[i]=self.heapList[i],self.heapList[(i-1)//2]
                        i=i//2
                self.heapLength+=1                
                """
import pandas as pd

def put():
	data_structure = minHeap()
        df=pd.read_csv("final.csv")
        for index,row in df.iterrows():
                empno,bdate,fname,lname,gender,hdate,sal=row
                data_structure.insertKey([empno,bdate,fname,lname,gender,hdate,sal])

                #fname,lname,sal=row["First Name"],row["Last Name"],row["Salary"]
                #data_structure.insertKey([fname,lname,sal])       
	# code here
	return data_structure

def get(data_structure):
	# query on the data_structure and return data required
	empno,bdate,fname,lname,gender,hdate,sal=data_structure.heapList[0]
	return (data_structure,fname,lname,sal)
