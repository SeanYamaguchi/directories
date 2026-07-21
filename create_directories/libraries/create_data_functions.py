import os
import time
import datetime
from datetime import date
# プロジェクトフォルダーから。
from libraries import classes 
from libraries import time_edit
from libraries import formulae

def sort_set(given_set:set):
	if (type(given_set) == SetOfOrderedPairs):
		min_value, min_directory, list_of_element = len(given_set), None, []
		for iterator in range(len(given_set)):
			for ordered_pair in given_set:
				if (ordered_pair.element_I < min_value):
					min_value, min_directory = ordered_pair.element_I, ordered_pair.element_J
			min_ordered_pair = OrderedPair(min_value, min_directory)
			given_set.remove_element(min_ordered_pair)
			list_of_element.append(min_ordered_pair)
		return list_of_element

def create_dirs_on_specific_time(given_t:datetime, directory_name, dir_related_and_rank_minus_1) -> None:
	while True:
		current_t = datetime.datetime.now()
		if (time_edit.if_equal_time(current_t, given_t)):		
			create_directories(directory_name, dir_related_and_rank_minus_1)
			break
		else:
			print("Not Now: ")
			time.sleep(1)
		pass

def create_directories(dir_name:str, dir_related_and_rank_minus_1:str):
	current_wd = os.getcwd()
	if ((dir_related_and_rank_minus_1 == current_wd)):
		path_of_dir:str = dir_name
	else:
		path_of_dir:str = dir_related_and_rank_minus_1 + "\\" + dir_name
	os.makedirs(path_of_dir, exist_ok=True)
	print("DIRECTORY NAME: " + dir_name + ", PATH: " + dir_related_and_rank_minus_1) # print("DIRECTORIE(S) ARE CREATED !!!: ")

def create_directory_info(directory_info_dict_list:list, if_create:bool = True, tree_mode:bool = True, is_root_directory = False) -> dict:
	directory_info_dict = { 'directory_name': None, 'directory_where': None, 'directory_path': None }
	if (if_create == False):
		directory_info_dict['directory_path'] = input("選択するディレクトリのパスを入力してください。")
		dir_segments = directory_info_dict['directory_path'].split('\\')
		if (dir_segments[-1] == ''):
			directory_info_dict['directory_name'] = dir_segments[-2]
			directory_info_dict['directory_where'] = directory_info_dict['directory_path'].strip('\\')
			directory_info_dict['directory_where'] = directory_info_dict['directory_path'].strip(directory_info_dict['directory_name'])
			directory_info_dict['directory_where'] = directory_info_dict['directory_path'].strip('\\')
		else:
			directory_info_dict['directory_name'] = dir_segments[-1]
			directory_info_dict['directory_where'] = directory_info_dict['directory_path'].strip(directory_info_dict['directory_name'])
			directory_info_dict['directory_where'] = directory_info_dict['directory_where'].strip('\\')
		# print("ROOT DIRECTORY: ")
		# print(directory_info_dict['directory_name'])
		# print(directory_info_dict['directory_where'])
		# print(directory_info_dict['directory_path'])
	else:
		directory_info_dict['directory_name'] = input("作成するディレクトリ名称を入力してください。: ")
		current_working_dir = os.getcwd()
		print("作成するディレクトリを配下する場所のパスを指定してください。標準は{}。".format(current_working_dir))
		if (directory_info_dict_list != []):
			for directory_info in directory_info_dict_list:
				print("DIR NAME: " + directory_info['directory_name'] + ", DIR_PATH: " + directory_info['directory_path'])
		print("")
		directory_info_dict['directory_where'] = input("標準でいい場合は、そのままエンターキーを押してください。: ")
		# 簡単に説明すれば、tree_modeがTrueの場合はルートディレクトリの下にあるかどうかを確認する。
		if ((directory_info_dict_list != []) and (not(formulae.formula_directory_J_is_equal_to_or_below_directory_I_other_type(directory_info_dict_list[0]['directory_where'], directory_info_dict['directory_where'])))):
			print("作成するディレクトリを配下する場所のパスは、既に一つ以上のディレクトリを指定している場合、作成予定のディレクトリ全てを下に持つディレクトリを持っている必要があります。")
		if ((directory_info_dict['directory_where'] == current_working_dir) or (directory_info_dict['directory_where'] == "")):
			directory_info_dict['directory_where'] = current_working_dir
			directory_info_dict['directory_path'] = current_working_dir + "\\" + directory_info_dict['directory_name']
			directory_info_dict['tree_mode'] = None
			directory_info_dict['root_dir_path'] = None
		else:
			directory_info_dict['directory_path'] = directory_info_dict['directory_where'] + '\\' + directory_info_dict['directory_name']
			directory_info_dict['tree_mode'] = None
			directory_info_dict['root_dir_path'] = None
	if (is_root_directory == True):
		directory_info_dict['root_dir_path'] = directory_info_dict['directory_path']
	if (is_root_directory == False and tree_mode == True):
		directory_info_dict['root_dir_path'] = None # 既存のもの（既に他で決定されている。）
	if (tree_mode == True):
		directory_info_dict['tree_mode'] = True
	if (is_root_directory == True):
		directory_info_dict['is_root_directory'] = True
	else:
		directory_info_dict['is_root_directory'] = False
	return directory_info_dict

### def create_tree_info(directory_info_dict_list:list): ###

def print_hyphen(directory:Directory):
	print_str = ''
	if (directory.dir_path == None):
		directory.get_dir_path()
	for symbol in range(len(directory.dir_name + directory.dir_path)):
		print_str += '-'
	print(print_str)