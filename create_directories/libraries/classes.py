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
	def __init__(self, directory_name:str, directory_where:str, root_directory_path:str = None, tree_mode:bool = False, directory_id:int = None):	
		# Info As Directory
		self.__directory_name = directory_name
		self.__directory_where = directory_where
		self.__directory_path = self.__directory_where + "\\" + self.__directory_name
		self.__is_tree_node = False
		if (tree_mode == True):
			self.__is_tree_node = True
		else:
			pass
		self.__directory_id = directory_id
		# Info As Tree Node
		self.__root_directory_path = root_directory_path
		self.__set_for_calculate_rank = SetOfDirectories()
		self.__set_for_calculation = set()
		self.__rank = None # (基礎論の文脈における)typeで決定することが可能。	
		self.__height = None
		self.__directory_name_related_and_rank_minus_1:Directory = None
		self.__dir_or_dirs_related_and_rank_plus_1:SetOfDirectories = SetOfDirectories()

	def show_directory_info(self) -> None:
		print("DIRNUM: " + (str)(self.directory_id))
		print("DIRNAME: " + self.__directory_name)
		print("DIRWHERE: " + self.__directory_where)
		print("DIRPATH: " + self.__directory_path)
		print("IS TREE NODE: " + self.__is_tree_node) 
		print("DIRID: " + self.__directory_id)
		if (self.__is_tree_node == False):
			print("TREE_NODE: " + self.__is_tree_node)
		else:
			pass
			print("------ Info As Tree Node ------")
			print("RANK: " + (str)(self.__rank))
			print("HEIGHT: " + (str)(self.__height))
			print("DIR NAME RELATED AND RANK MINUS 1: " + (str)(self.__dir_related_and_rank_minus_1))
			print("DIR ROOT DIR PATH: " + (str)(self.__root_directory_path))
			print("DIR RELATED AND RANK MINUS 1: " + (str)(self.__dir_related_and_rank_minus_1))
			print("DIR OR DIRS RELATED AND RANK PLUS 1: " + (str)(self.__dir_or_dirs_related_and_rank_plus_1))

	@property
	def directory_name(self) -> str:
		return self.__directory_name

	@directory_name.setter
	def directory_name(self, directory_name:str) -> None:
		self.__directory_name = directory_name

	@property
	def directory_where(self) -> str:
		return self.__directory_where

	@directory_where.setter
	def directory_where(self, directory_where:str) -> None:
		self.__directory_where = directory_where

	@property
	def directory_path(self) -> str:
		return self.__directory_path

	def calculate_directory_path(self) -> None:
		self.__directory_path = self.__directory_where + "\\" + self.__directory_name

	@property
	def is_tree_node(self) -> bool:
		return self.__is_tree_node

	@is_tree_node.setter
	def is_tree_node(self, is_tree_node:bool) -> None:
		self.__is_tree_node = is_tree_node

	@property
	def directory_id(self) -> int:
		return self.__directory_id

	def is_directory_tree_node(self) -> bool:
		return True if (self.__is_tree_node == True) else False
	
	@property
	def root_directory_path(self) -> str:
		return self.__root_directory_path
	
	@root_directory_path.setter
	def root_directory_path(self, root_directory_path:str) -> None:
		self.__root_directory_path = root_directory_path

	@property
	def set_for_calculation_rank(self) -> SetOfDirectories:
		return self.__set_for_calculation_rank
	
	@property
	def set_for_calculation(self) -> set:
		return self. __set_for_calculation

	@property
	def rank(self) -> int:
		return self.__rank
	
	def calculate_rank(self, set_of_directory_ordered_pairs:SetOfDirectoryOrderedPairs) -> None: # Every node has its rank, one and only.
		if (self.__is_tree_node == False):
			pass
		else:
			self.__set_for_calculate_rank = sets.is_related_with_certain_directory(formulae.formula_directory_J_is_below_directory_I_other_type, self, set_of_directory_ordered_pairs, True) # 予め、正しく計算されている。
			if ((self.__set_for_calculate_rank.mutable_set) <= set()):
				self.__rank = 0
			else:
				for directory in self.__set_for_calculate_rank.mutable_set:
					if (directory.rank == None):
						directory.calculate_rank(set_of_directory_ordered_pairs)
					self.__set_for_calculation.add((int)(directory.rank + 1))
				self.__rank = max(self.__set_for_calculation)

	@property
	def height(self) -> int:
		return self.__height
	
	def calculate_height_of_element(self, set_of_directory_ordered_pairs:SetOfDirectoryOrderedPairs) -> None: 
		"""
		ノードのheightを定義する関数。rankでheightを定義している。
		"""
		if (self.__rank == None):
			self.calculate_rank(set_of_directory_ordered_pairs)
		self.__height = self.__rank

	@property
	def dir_related_and_rank_minus_1(self) -> Directory:
		return self.__dir_related_and_rank_minus_1

	def calculate_dir_related_and_rank_minus_1(self, set_of_directory_ordered_pairs:SetOfDirectoryOrderedPairs) -> None:
		if (self.__rank == None):
			self.calculate_rank(set_of_directory_ordered_pairs)
		if (self.__rank == 0):
			self.__dir_related_and_rank_minus_1 = None
		elif (self.__rank > 0):
			self.__dir_related_and_rank_minus_1 = calculate_directory_of_max_rank(self.__set_for_calculate_rank.mutable_set)
		else:
			pass

	def calculate_directory_of_max_rank(self, set_of_directories:SetOfDirectories) -> Directory:
		if (self.__is_tree_node == False):
			print("NOT TREE")
		else:
			directory_of_max_rank = Directory()
			for directory in set_of_directories:
				if ((directory_of_max_rank != set() and directory_of_max_rank.rank < directory.rank) or (directory_of_max_rank.rank < directory.rank)):
					directory_of_max_rank = directory
			return directory

	def calculate_dir_or_dirs_related_and_rank_plus_1(self, set_of_directories:SetOfDirectories, set_of_directory_ordered_pairs:SetOfDirectoryOrderedPairs) -> None:
		if (self.__rank == None):
			self.calculate_rank(set_of_directory_ordered_pairs)
		for directory in set_of_directories:
			if (directory.mutable_set.rank == self.__mutable_set.rank + 1): # ここおかしい。
				self.__dir_or_dirs_related_and_rank_plus_1.append(directory)

	def calculate_tree_info(self) -> None:
		self.calculate_directory_path()
		self.calculate_rank()
		self.calculate_height_of_element()
		self.calculate_dir_related_and_rank_minus_1()
		self.calculate_dir_or_dirs_related_and_rank_plus_1()

class NormalSet():
	"""
	本プログラムで扱う集合を表現するクラス
	"""
	def __init__(self) -> None:
		self.__mutable_set = set()
		self.__frozenset = set()
		self.__frozen:bool = False

	def add_element(self, element) -> None:
		if (self.__frozen == True):
			pass
		else:
			self.__mutable_set.add(element)
	
	def create_frozenset(self) -> None:
		if (self.__frozen == False):
			self.__frozenset = frozenset(self.__mutable_set)
			self.__frozen = True
		else:
			pass

	def remove_element(self, element) -> None:
		if (self.frozen == True):
			pass
		else:
			self.__mutable_set.discard(element)

class SetOfDirectories(NormalSet):
	"""
	ディレクトリの集合を表現するクラス
	"""
	def show(self) -> None:
		if (directory.directory_id != None for directory in self.__mutable_set):
			for directory in self.__mutable_set:
				directory.set_directory_path()
				print("DIRNAME: " + directory.directory_name + ", DIRPATH: " + directory.directory_path)
		else:
			for directory in self.__mutable_set:
				directory.set_directory_path()
				print("DIRNAME: " + directory.directory_name + ", DIRPATH: " + directory.directory_path)

	def show_with_directory_id(self) -> None:
		if (directory.directory_id != None for directory in self.__mutable_set):
			for directory in self.__mutable_set:
				directory.calculate_directory_path()
				print("ID: " + (str)(directory.directory_id) + ", DIRNAME: " + directory.directory_name + ", DIRPATH: " + directory.directory_path)
		else:
			for directory in self.__mutable_set:
				directory.set_directory_path()
				print("ID: " + (str)(directory.directory_id) + ", DIRNAME: " + directory.directory_name + ", DIRPATH: " + directory.directory_path)

class TreeOfDirectories(SetOfDirectories):
	"""
	SetOfDirectoriesクラスと実質同様なクラス。
	"""
	def show(self) -> None:
		print(self.__mutable_set)

class OrderedPair(NormalSet):
	"""
	順序対を表現するクラス。
	"""
	def __init__(self, element_I, element_J) -> None:
		self.element_I = element_I
		self.element_J = element_J
		self.__mutable_set = { frozenset([self.element_I]), frozenset([self.element_I, self.element_J]) }
		self.ordered_pair:frozenset = frozenset([frozenset([self.element_I]), frozenset([self.element_I, self.element_J])])

class DirectoryOrderedPair(OrderedPair):
	"""
	ディレクトリに関する順序対を表現するクラス。
	"""
	def __init__(self, dir_I:Directory, dir_J:Directory) -> None:
		self.element_I = dir_I
		self.element_J = dir_J
		self.dir_I = dir_I
		self.dir_J = dir_J
		self.__mutable_set = { frozenset([self.element_I]), frozenset([self.element_I, self.element_J]) }
		self.ordered_pair:frozenset = frozenset([frozenset([self.dir_I]), frozenset([self.dir_I, self.dir_J])])

class SetOfOrderedPairs(NormalSet):
	"""
	順序対の集合を定義するクラス。
	"""
	def show_ordered_pairs(self) -> None:
		for ordered_pair in self.__mutable_set:
			print("OREDERED PAIR: " + "< " + ordered_pair.element_I + ", " + ordered_pair.element_J + " >")

class SetOfDirectoryOrderedPairs(SetOfOrderedPairs): 
	"""
	ディレクトリに関する順序対の集合を定義するクラス。
	"""
	def show_ordered_pairs(self, set_representation = False) -> None:
		if (set_representation == True):
			print("{ ", end=" ")
			c = 0
			for ordered_pair in self.__mutable_set:
				c += 1
				print("〈 " + "\"" + ordered_pair.dir_I.directory_name + "\"" + ", " + "\"" + ordered_pair.dir_J.directory_name + "\"" + " 〉", end=" ")
				if (0 <= c and c < len(self.__mutable_set)):
					print(", ", end=" ")
				elif (c == len(self.__mutable_set)):
					print("", end=" ")
				else:
					print("", end=" ")
			print(" }")
		else:	
			for ordered_pair in self.__mutable_set:
				print("ORDERED PAIR OF DIRECTORIES: " + "〈 " + "\"" + ordered_pair.dir_I.directory_name + "\"" + ", " + "\"" + ordered_pair.dir_J.directory_name + "\"" + " 〉")

class Tree():
	"""
	木構造を表現するクラス。集合と半順序の対として定義されているように、単なるディレクトリの集合等ではないことに注意する。
	"""
	def __init__(self, set_of_elements:NormalSet, relation:Set, relation_formula:function) -> None:
		self.set_of_elements:NormalSet = set_of_elements # set of directories等である。
		self.relation:SetOfDirectoryOrderedPairs = relation # set of directory orde
		self.relation_formula:function = None
		self.height_of_tree:int = None
		self.formula:function = None
		self.levels_of_tree:SetOfOrderedPairs = SetOfOrderedPairs()

	def calculate_level_alpha_of_tree(self, ordinal_number:int) -> None:
		if (ordinal_number >= 0): # self.level_of_tree[(str)(ordinal_number)] == None
			level_alpha_of_tree = NormalSet()
			for element in set_of_elements:
				if (element.rank == alpha):
					level_alpha_of_tree.mutable_set.add_element(element)
		self.levels_of_tree.add_element(OrderedPair(ordinal_number, level_alpha_of_tree)) # alpha毎に定まるため、ordinal_numberを情報として持たせることが正しい。

	def calculate_all_level_of_tree(self) -> None:
		for ordinal_number in range(len(self.set_of_directories)):
			calculate_level_alpha_of_tree(ordinal_number)

	def calculate_height_of_tree(self) -> None:
		min_value = len(self.set_of_directories)
		for ordinal_number in range(len(self.set_of_directories)):
			if (self.levels_of_tree.mutable_set.element_I == set() and ordinal_number < min_value):
				min_value = ordinal_number
		self.height_of_tree = min_value