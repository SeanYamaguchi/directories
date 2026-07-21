import os
import time
import datetime
from datetime import date
# プロジェクトフォルダー
from libraries import classes

from libraries import time_edit

# ディレクトリの集合からその順序対全体の集合を構成する関数。 -- create関数。
def create_set_of_ordered_pairs_from_set_of_directories(set_of_directories:SetOfDirectories) -> SetOfDirectoryOrderedPairs:
	new_set_of_directory_ordered_pairs:SetOfDirectoryOrderedPairs = classes.SetOfDirectoryOrderedPairs()
	for I in set_of_directories: # setだからiterableではない。
		for J in set_of_directories:
			new_ordered_pair = classes.DirectoryOrderedPair(I, J)
			new_set_of_directory_ordered_pairs.add_element(new_ordered_pair)
	new_set_of_directory_ordered_pairs.create_frozenset()
	return new_set_of_directory_ordered_pairs

# 順序対の集合から関係を構成する関数。 -- create関数。 適当な論理式(formula)を満たす部分集合を定義できるようにする。
def create_relation(relation_method:formula, set_of_ordered_pairs:SetOfDirectoryOrderedPairs) -> SetOfDirectoryOrderedPairs: # 高階関数
	set_of_related_ordered_pairs = classes.SetOfDirectoryOrderedPairs()
	for i in set_of_ordered_pairs.mutable_set:
		# print(i.mutable_set)
		# print("PATH I" + i.dir_I.dir_path)
		# print("PATH J" + i.dir_J.dir_path)
		# print(relation_method(i))
		if (relation_method(i)):
			set_of_related_ordered_pairs.add_element(i)
		else:
			pass
	return set_of_related_ordered_pairs

# 特定のディレクトリとディレクトリのsetのそれぞれの要素を比較する関数。
def is_related_with_certain_directory(relation_method:function, directory:Directory, set_of_directory_ordered_pairs:SetOfDirectoryOrderedPairs, return_elements:bool = False) -> SetOfDirectoryOrderedPairs: # 高階関数
	set_of_related_ordered_pairs = classes.SetOfDirectoryOrderedPairs()
	set_of_related_atomic_elements = classes.SetOfDirectories()
	for ordered_pair in set_of_directory_ordered_pairs.mutable_set:
		if(relation_method(ordered_pair.dir_I.dir_path, directory.dir_path)): 
			related_ordered_pair = classes.DirectoryOrderedPair(ordered_pair.dir_I, directory)
			set_of_related_atomic_elements.add_element(ordered_pair.dir_I)
			set_of_related_ordered_pairs.add_element(related_ordered_pair)
	if (return_elements == False):
		return set_of_related_ordered_pairs
	else:
		return set_of_related_atomic_elements