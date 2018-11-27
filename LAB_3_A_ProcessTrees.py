"""
@author Rocorral
ID: 80416750
Instructor: David Aguirre
TA: Saha, Manoj Pravakar
Assignment:Lab 3-A - AVL,RBT, word Embeddings
Last Modification: 11/4/2018
Program Purpose: The purpose of this program is to practice and note the
difference in computation times of insertion and retrieval between AVL
Trees and Red Black Trees. We are provided with a word embedding file and 
are required to insert each word and its embedding vector into a tree. 
After the insertions we must retrieved words based on pairs read from another
file and compute the similarity. This is followed by computations of tree size
and file output with word lists generated from the tree.
"""
import AVL
import RBT
import math

def read_f_into_AVL(file):
	"""Recieves glove file with embedings location as a string
	constructs an AVL tree using nodes with the word as one parameter 
	and the 50 floting point vectors in an array as another.
	"""
	CurAVL = AVL.AVLTree()
	forAVL = open(file,'r+',encoding="UTF-8")
	for line in forAVL:
		a = line.split()
		#Direguards "words" in file that do not begin witch characters from the alphabet
		if (a[0] >= 'A' and a[0] <= 'Z') or (a[0] >='a' and a[0] <= 'z'):
					## did you think about using a is char() for the line above
			CurAVL.insert(AVL.Node( a[0] , a[1:(len(a))]))
	return CurAVL

def read_f_into_RBT(file):
	"""Recieves glove file with embeddings location as a string 
	constructs a Red Black tree using nodes with the word as one parameter 
	and the 50 floting point vectors in an array as another.
	"""
	CurRBT = RBT.RedBlackTree()
	forRBT = open(file,'r+', encoding="UTF-8")
	for line in forRBT:
		a = line.split()
		#Direguards "words" in file that do not begin witch characters from the alphabet
		if (a[0] >= 'A' and a[0] <= 'Z') or (a[0] >='a' and a[0] <= 'z'):
			CurRBT.insert_node(RBT.RBTNode(a[0], a[1:(len(a))],None))
	return CurRBT

def computeSimilarity(tree,file2):
	"""Recieves a tree root and a file of word pairs.
	The sin similarity is derived from the vectors associated with the words
	by retrieving them from the tree and computing the values using the 
	function described in our lab 
	"""
	forComparison = open(file2, 'r+', encoding="UTF-8")
	for line in forComparison:
		dotProduct = 0
		denoma = 0
		denomb = 0
		b = line.split()
		w0 = tree.search(b[0])#word 1 from pair
		w1 = tree.search(b[1])#word 2
		for i in range(len(w0.vector)):
			dotProduct = dotProduct + (float(w0.vector[i])*float(w1.vector[i]))
			denoma = denoma + float(w0.vector[i])*float(w0.vector[i])
			denomb = denomb + float(w1.vector[i])*float(w1.vector[i])
		denom = math.sqrt(denoma)*math.sqrt(denomb)
		similarity = dotProduct/denom
		print(w0.key ," ",w1.key, "    similarity: " , similarity )

def user_selection_IF():
	"""User Interface
	the origin of calls to the definitions requested by the lab the user is
	to input values for tree type and depth to print.
	"""
	file = "glove.6B.50d.txt"       #file with embeddings
	file2 ="Apendix-word-List.txt"  #file with words to compare
	menu = True                    
	while menu:
		try:
			print("would you like to USE \n1:AVL(Adelson-Velskii and Landis Tree)\n2:RBT(Red Black Tree)\n3:Exit")
			selection =input()
			print("your selection is:", selection)
			
			if selection == '1':
				"""process using AVL"""
				print("reading file into AVL......")
				tree = read_f_into_AVL(file)
				print("computing similarities of word pairs in", file2)
				computeSimilarity(tree,file2)
				print("Number of Nodes in tree: ",get_numb_nodes(tree.root))
				height =get_tree_height(tree.root)
				print("Tree height: ",height)

				print("generating file with all nodes in ascending order....")
				ascend_file =  open('ascendingwords.txt','a',encoding = "UTF-8")
				gen_ascending_order(tree.root, ascend_file)
				ascend_file.close()
				print("file complete!")
				correct_depth =False
				d = (-1)
				while correct_depth == False:
					try:
						print("enter a depth between 0 and ",height)
						d = input()
						if (int(d) < 0 or int(d) > height):
							raise OSError("wrong input")
						else:
							correct_depth = True
					except OSError as err:	#catches input error for range
						print("------>",d)
						print("is not a valid input....")
					except ValueError as err:	#catches input error for input type.
						print("------>",d)
						print("is not even a Number....")

				print("generating file with all nodes at depth ",d," in ascending order.....")
				depth_file = open('words_at_depth_in_inassending_order.txt','a',encoding = "UTF-8")
				gen_depth_file(tree.root,int(d),depth_file)
				depth_file.close()
				print("file complete")
				print("all tasks complete\n exiting...")
				menu = False

			if selection == '2':
				"""process using Red Black Tree"""
				print("reading file into RBT......")
				tree = read_f_into_RBT(file)
				print("computing similarities of word pairs in using a Red Black Tree", file2)
				computeSimilarity(tree,file2)
				print("Number of Nodes in tree: ",get_numb_nodes(tree.root))
				height =get_tree_height(tree.root)
				print("Tree height: ",height)
				print("generating file with all nodes in ascending order....")
				ascend_file =  open('ascendingwords.txt','a',encoding = "UTF-8")
				gen_ascending_order(tree.root, ascend_file)
				ascend_file.close()
				print("file complete!")
				correct_depth =False
				d = (-1)
				while correct_depth == False:
					try:
						print("enter a depth between 0 and ",height)
						d = input()
						if (int(d) < 0 or int(d)>height):
							raise OSError("wrong input")
						else:
							correct_depth = True
					except OSError as err:
						print("------>",d)
						print("is not a valid input....")
					except ValueError as err:
						print("------>",d)
						print("is not even a Number....")

				print("generating file with all nodes at depth ",d," in ascending order.....")
				depth_file = open('words_at_depth_in_inassending_order.txt','a',encoding = "UTF-8")
				gen_depth_file(tree.root,int(d),depth_file)
				depth_file.close()
				print("file complete")
				print("all tasks complete exiting...")
				menu = False

			if selection == '3':
				print("exiting")
				menu =False	

		except OSError as err:
			print("OS error: {0}".format(err))
			print("the options are 1,2 or 3.... try again")	
		except ValueError as err:
			print("------>",selection)
			print("is not even a Number....")

	

def get_numb_nodes(t):
	"""geven a tree root computes the number of nodes in a tree recursivly"""
	count = 1
	if t.left != None:
		count = count + get_numb_nodes(t.left)
	if t.right != None:
		count = count + get_numb_nodes(t.right)
	return count

def get_tree_height(t):
	"""given a tree roo computes the tree height recursivly"""
	if t is  None:
		return 0
	return 1 + (max(get_tree_height(t.right),get_tree_height(t.left)))


def gen_ascending_order(t,file):
	"""given a tree root and a file to write in to generates file with all words in ascending order """
	if t is None:
		return
	gen_ascending_order(t.left,file)
	file.write("\n" + t.key)
	gen_ascending_order(t.right,file)
	return

def gen_depth_file(t,d,file):
	"""given a tree root a user defined depth and a file
	tgenerates a file with all words at the depth in ascending order
	"""
	if t is None:
		return
	gen_depth_file(t.left,d-1,file)
	if d == 0:
		file.write("\n" + t.key)
		return
	gen_depth_file(t.right,d-1,file)
	return	

#----------Main-----------

user_selection_IF()
