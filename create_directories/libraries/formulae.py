import os
import time
import datetime
from datetime import date
# プロジェクト由来のモジュール。
from libraries import classes
from libraries import time_edit

def formula_directory_J_is_equal_to_or_below_directory_I(ordered_pair:DirectoryOrderedPair) -> bool: # dir_I < dir_Jをdir_I\dir_Jのことと定める。 dir_I, dir_Jのルートディレクトリは一致するという前提。
	return True if (ordered_pair.dir_J.dir_path.find(ordered_pair.dir_I.dir_path) != -1) else False

def formula_directory_J_is_equal_to_directory_I(ordered_pair:DirectoryOrderedPair) -> bool:
	return True if (ordered_pair.dir_J.dir_path == ordered_pair.dir_I.dir_path) else False 	

def formula_directory_J_is_not_directory_I(ordered_pair:DirectoryOrderedPair) -> bool:
	return True if (not (formula_directory_J_is_equal_to_directory_I(ordered_pair))) else False

def formula_directory_J_is_below_directory_I(ordered_pair:DirectoryOrderedPair) -> bool:
	return True if (formula_directory_J_is_equal_to_or_below_directory_I(ordered_pair) and (formula_directory_J_is_not_directory_I(ordered_pair))) else False

def formula_directory_J_is_equal_to_or_below_directory_I_other_type(dir_I_path:str, dir_J_path:str) -> bool:
	return True if (dir_J_path.find(dir_I_path) != -1) else False

def formula_directory_J_is_below_directory_I_other_type(dir_I_path:str, dir_J_path:str) -> bool:
	return True if (formula_directory_J_is_equal_to_or_below_directory_I_other_type(dir_I_path, dir_J_path) and (dir_I_path != dir_J_path)) else False