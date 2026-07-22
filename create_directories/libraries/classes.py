import os
import time
import datetime
from datetime import date
# プロジェクト由来のモジュール。
from libraries import time_edit
from libraries import sets
from libraries import formulae

class Directory():
	"""	
	ディレクトリに関する情報を管理するクラス。
	"""
	def __init__(self, dir_name:str = None, dir_where:str = None, root_dir_path:str = None, tree_mode:bool = False, directory_id:int = None):	
		# Info As Directory
		self.dir_name = dir_name
		self.dir_where = dir_where
		self.dir_path = None
		self.is_tree_node = False
		if (tree_mode == True):
			self.is_tree_node = True
		else:
			pass
		self.directory_id = directory_id

		# Info As Tree Node
		self.root_dir_path = root_dir_path
		self.set_for_calculate_rank = SetOfDirectories()
		self.set_for_calculation = set()
		self.rank = None # (基礎論の文脈における)typeで決定することが可能。	
		self.height = None
		self.dir_name_related_and_rank_minus_1:Directory = None
		self.dir_or_dirs_related_and_rank_plus_1:SetOfDirectories = SetOfDirectories()
		self.node_id = None

	def show_directory_info(self):
		print("DIR NUM: " + (str)(self.directory_id))
		print("DIR NAME: " + self.dir_name)
		print("DIR WHERE: " + self.dir_where)
		print("DIR PATH: " + self.dir_path)
		print("IS TREE NODE: " + self.is_tree_node) 
		print("DIR ID: " + self.directory_id)
		if (self.is_tree_node == False):
			print("TREE_NODE: " + self.is_tree_node)
		else:
			pass
			print("------ Info As Tree Node ------")
			print("HEIGHT: " + (str)(self.height))
			print("RANK: " + (str)(self.rank))
			print("DIR_NAME_RELATED_AND_RANK_MINUS_1: " + (str)(self.dir_related_and_rank_minus_1))
			print("DIR ROOT DIR PATH: " + (str)(self.root_dir_path))
			print("DIR RELATED AND RANK MINUS 1: " + (str)(self.dir_related_and_rank_minus_1))
			print("DIR OR DIRS RELATED AND RANK PLUS 1: " + (str)(self.dir_or_dirs_related_and_rank_plus_1))
			print("NODE ID: " + (str)(self.node_id))

	def set_dir_path(self): # 一度だけ呼び出せるようにする。
		self.dir_path = self.dir_where + "\\" + self.dir_name

	def set_root_dir_path(self, root_dir_path:str):
		self.root_dir_path = root_dir_path

	def calculate_rank(self, set_of_directory_ordered_pairs:SetOfDirectoryOrderedPairs): # Every node has its rank, one and only.
		if (self.is_tree_node == False):
			pass
		else:
			self.set_for_calculate_rank = sets.is_related_with_certain_directory(formulae.formula_directory_J_is_below_directory_I_other_type, self, set_of_directory_ordered_pairs, True) # 予め、正しく計算されている。
			if ((self.set_for_calculate_rank.mutable_set) <= set()):
				self.rank = 0
			else:
				for directory in self.set_for_calculate_rank.mutable_set:
					if (directory.rank == None):
						directory.calculate_rank(set_of_directory_ordered_pairs)
					self.set_for_calculation.add((int)(directory.rank + 1))
				self.rank = max(self.set_for_calculation)
	
	def calculate_height_of_element(self, set_of_directory_ordered_pairs:SetOfDirectoryOrderedPairs): # rankでheightを定義。
		if (self.rank == None):
			self.calculate_rank(set_of_directory_ordered_pairs)
		self.height = self.rank

	def set_dir_related_and_rank_minus_1(self, set_of_directory_ordered_pairs:SetOfDirectoryOrderedPairs):
		if (self.rank == None):
			self.calculate_rank(set_of_directory_ordered_pairs)
		if (self.rank == 0):
			self.dir_related_and_rank_minus_1 = None
		elif (self.rank > 0):
			self.dir_related_and_rank_minus_1 = calculate_directory_of_max_rank(self.set_for_calculate_rank.mutable_set)
		else:
			pass
	
	def is_directory_tree_node(self):
		return True if (self.is_tree_node == True) else False

	def calculate_directory_of_max_rank(self, set_of_directories:SetOfDirectories):
		if (self.is_tree_node == False):
			print("NOT TREE")
		else:
			directory_of_max_rank = Directory()
			for directory in set_of_directories:
				if ((directory_of_max_rank != set() and directory_of_max_rank.rank < directory.rank) or (directory_of_max_rank.rank < directory.rank)):
					directory_of_max_rank = directory
			return directory

	def set_dir_related_and_rank_plus_1(self, set_of_directories:SetOfDirectories, set_of_directory_ordered_pairs:SetOfDirectoryOrderedPairs):
		if (self.rank == None):
			self.calculate_rank(set_of_directory_ordered_pairs)
		for directory in set_of_directories:
			if (directory.mutable_set.rank == self.mutable_set.rank + 1):
				self.dir_or_dirs_related_and_rank_plus_1.append(directory)

	def set_tree_info(self):
		self.set_dir_path()
		self.set_root_dir_path()
		self.calculate_rank()
		self.calculate_height_of_element()
		self.set_dir_related_and_rank_minus_1()
		self.dir_or_dirs_related_and_rank_plus_1()

class NormalSet():
	"""
	本プログラムで扱う集合を表現するクラス
	"""
	def __init__(self):
		self.mutable_set = set()
		self.frozenset = set()
		self.frozen:bool = False

	def add_element(self, element:Set):
		if (self.frozen == True):
			pass
		else:
			self.mutable_set.add(element)
	
	def create_frozenset(self):
		if (self.frozen == False):
			self.frozenset = frozenset(self.mutable_set)
			self.frozen = True
		else:
			pass

	def remove_element(self, element:Set):
		if (self.frozen == True):
			pass
		else:
			self.mutable_set.discard(element)

class SetOfDirectories(NormalSet):
	"""
	ディレクトリの集合を表現するクラス
	"""
	def show(self):
		if (directory.directory_id != None for directory in self.mutable_set):
			for directory in self.mutable_set:
				directory.set_dir_path()
				print("DIRNAME: " + directory.dir_name + ", DIRPATH: " + directory.dir_path)
		else:
			for directory in self.mutable_set:
				directory.set_dir_path()
				print("DIRNAME: " + directory.dir_name + ", DIRPATH: " + directory.dir_path)

class TreeOfDirectories(SetOfDirectories):
	"""
	SetOfDirectoriesクラスと実質同様なクラス。
	"""
	def show(self):
		print(self.mutable_set)

class OrderedPair(NormalSet):
	"""
	順序対を表現するクラス。
	"""
	def __init__(self, element_I:Set, element_J:Set):
		self.element_I = element_I
		self.element_J = element_J
		self.mutable_set = { frozenset([self.element_I]), frozenset([self.element_I, self.element_J]) }
		self.ordered_pair:frozenset = frozenset([frozenset([self.element_I]), frozenset([self.element_I, self.element_J])])

class DirectoryOrderedPair(OrderedPair):
	"""
	ディレクトリに関する順序対を表現するクラス。
	"""
	def __init__(self, dir_I:Directory, dir_J:Directory):
		self.element_I = dir_I
		self.element_J = dir_J
		self.dir_I = dir_I
		self.dir_J = dir_J
		self.mutable_set = { frozenset([self.element_I]), frozenset([self.element_I, self.element_J]) }
		self.ordered_pair:frozenset = frozenset([frozenset([self.dir_I]), frozenset([self.dir_I, self.dir_J])])

class SetOfOrderedPairs(NormalSet):
	"""
	順序対の集合を定義するクラス。
	"""
	def show_ordered_pairs(self):
		for ordered_pair in self.mutable_set:
			print("OREDERED_PAIR: " + "< " + ordered_pair.element_I + ", " + ordered_pair.element_J + " >")

class SetOfDirectoryOrderedPairs(SetOfOrderedPairs): 
	"""
	ディレクトリに関する順序対の集合を定義するクラス。
	"""
	def show_ordered_pairs(self, set_representation = False):
		if (set_representation == True):
			print("{ ", end=" ")
			c = 0
			for ordered_pair in self.mutable_set:
				c += 1
				print("〈 " + "\"" + ordered_pair.dir_I.dir_name + "\"" + ", " + "\"" + ordered_pair.dir_J.dir_name + "\"" + " 〉", end=" ")
				if (0 <= c and c < len(self.mutable_set)):
					print(", ", end=" ")
				elif (c == len(self.mutable_set)):
					print("", end=" ")
				else:
					print("", end=" ")
			print(" }")
		else:	
			for ordered_pair in self.mutable_set:
				print("ORDERED_PAIR_OF_DIRECTORIES: " + "〈 " + "\"" + ordered_pair.dir_I.dir_name + "\"" + ", " + "\"" + ordered_pair.dir_J.dir_name + "\"" + " 〉")

class Tree():
	"""
	木構造を表現するクラス。集合と半順序の対として定義されているように、単なるディレクトリの集合等ではないことに注意する。
	"""
	def __init__(self, set_of_elements:NormalSet, relation:Set, relation_formula:function):
		self.set_of_elements:NormalSet = set_of_elements # set of directories等である。
		self.relation:SetOfDirectoryOrderedPairs = relation # set of directory orde
		self.relation_formula:function = None
		self.height_of_tree:int = None
		self.formula:function = None
		self.levels_of_tree:SetOfOrderedPairs = SetOfOrderedPairs()

	def calculate_level_alpha_of_tree(self, ordinal_number:int):
		if (ordinal_number >= 0): # self.level_of_tree[(str)(ordinal_number)] == None
			level_alpha_of_tree = NormalSet()
			for element in set_of_elements:
				if (element.rank == alpha):
					level_alpha_of_tree.mutable_set.add_element(element)
		self.levels_of_tree.add_element(OrderedPair(ordinal_number, level_alpha_of_tree)) # alpha毎に定まるため、ordinal_numberを情報として持たせることが正しい。

	def calculate_all_level_of_tree(self):
		for ordinal_number in range(len(self.set_of_directories)):
			calculate_level_alpha_of_tree(ordinal_number)

	def calculate_height_of_tree(self):
		min_value = len(self.set_of_directories)
		for ordinal_number in range(len(self.set_of_directories)):
			if (self.levels_of_tree.mutable_set.element_I == set() and ordinal_number < min_value):
				min_value = ordinal_number
		self.height_of_tree = min_value