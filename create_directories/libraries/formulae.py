import os
import time
import datetime
from datetime import date
# プロジェクト由来のモジュール。
from libraries import classes
from libraries import time_edit

def formula_directory_J_is_equal_to_or_below_directory_I(ordered_pair:DirectoryOrderedPair) -> bool: # directory_I < directory_Jをdirectory_I\directory_Jのことと定める。 directory_I, directory_Jのルートディレクトリは一致するという前提。
	return True if (ordered_pair.directory_J.directory_path.find(ordered_pair.directory_I.directory_path) != -1) else False

def formula_directory_J_is_equal_to_directory_I(ordered_pair:DirectoryOrderedPair) -> bool:
	return True if (ordered_pair.directory_J.directory_path == ordered_pair.directory_I.directory_path) else False 	

def formula_directory_J_is_not_directory_I(ordered_pair:DirectoryOrderedPair) -> bool:
	return True if (not (formula_directory_J_is_equal_to_directory_I(ordered_pair))) else False

def formula_directory_J_is_below_directory_I(ordered_pair:DirectoryOrderedPair) -> bool:
	return True if (formula_directory_J_is_equal_to_or_below_directory_I(ordered_pair) and (formula_directory_J_is_not_directory_I(ordered_pair))) else False

def formula_directory_J_is_equal_to_or_below_directory_I_other_type(directory_I_path:str, directory_J_path:str) -> bool:
	return True if (directory_J_path.find(directory_I_path) != -1) else False

def formula_directory_J_is_below_directory_I_other_type(directory_I_path:str, directory_J_path:str) -> bool:
	return True if (formula_directory_J_is_equal_to_or_below_directory_I_other_type(directory_I_path, directory_J_path) and (directory_I_path != directory_J_path)) else False