import os
import time
import datetime
from datetime import date
# プロジェクト由来のモジュール。
from libraries import classes 
from libraries import time_edit
from libraries import formulae

def create_directories_on_specific_time(given_t:datetime, directory_name:str, dir_related_and_rank_minus_1:str) -> None:
	"""
	特定の時間にディレクトリを1つ以上作成することができる関数。
	"""
	while True:
		current_t = datetime.datetime.now()
		if (time_edit.if_equal_time(current_t, given_t)):		
			create_directories(directory_name, dir_related_and_rank_minus_1)
			break
		else:
			print("Not Now: ")
			time.sleep(1)
		pass

def create_directories(dir_name:str, dir_related_and_rank_minus_1:str) -> None:
	"""
	ディレクトリを１つ以上作成する関数。
	"""
	current_wd = os.getcwd()
	if ((dir_related_and_rank_minus_1 == current_wd)):
		path_of_dir:str = dir_name
	else:
		path_of_dir:str = dir_related_and_rank_minus_1 + "\\" + dir_name
	os.makedirs(path_of_dir, exist_ok=True)
	print("DIRNAME: " + dir_name + ", DIRPATH: " + dir_related_and_rank_minus_1) # print("DIRECTORIE(S) ARE CREATED !!!: ")

def create_directory_info(directory_info_dict_list:list, directory_id:int, if_create:bool = True, tree_mode:bool = True, is_root_directory = False) -> dict:
	"""
	ディレクトリに関する情報を辞書型で作成する関数。
	"""
	directory_info_dict = { 'directory_name': None, 'directory_where': None, 'directory_path': None }
	directory_info_dict['directory_id'] = directory_id
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

	else:
		directory_info_dict['directory_name'] = input("作成するディレクトリ名称を入力してください。: ")
		print(directory_info_dict['directory_name'])
		if (is_root_directory == True):
			root_dir_where = input("ルートディレクトリを置く場所のPATHを入力: ")
			directory_info_dict['directory_where'] = root_dir_where
			directory_info_dict['directory_path'] = directory_info_dict['directory_where'] + '\\' + directory_info_dict['directory_name']
			directory_info_dict['tree_mode'] = None
			directory_info_dict['root_dir_path'] = None
		else:
			print("作成するディレクトリを配下する場所のパスを選択するために以下からIDを一つ入力してください。")
			if (directory_info_dict_list != []):
				for directory_info in directory_info_dict_list:
					print("ID: ", (str)(directory_info['directory_id']) + ", DIR NAME: " + directory_info['directory_name'] + ", DIR_PATH: " + directory_info['directory_path'])
			print("")
			chosen_id:int = (int)(input("IDを入力: "))
			# 簡単に説明すれば、tree_modeがTrueの場合はルートディレクトリの下にあるかどうかを確認する。
			if (chosen_id < 0 or len(directory_info_dict_list) <= chosen_id):
				print("そのようなIDは存在しません。")
			else:
				for directory_info_i in directory_info_dict_list:
					if (chosen_id == directory_info_i['directory_id']):
						directory_info_dict['directory_where'] = directory_info_i['directory_path']
						directory_info_dict['directory_path'] = directory_info_dict['directory_where'] + '\\' + directory_info_dict['directory_name']
						directory_info_dict['tree_mode'] = None
						directory_info_dict['root_dir_path'] = None					
			if ((directory_info_dict_list != []) and (not(formulae.formula_directory_J_is_equal_to_or_below_directory_I_other_type(directory_info_dict_list[0]['directory_where'], directory_info_dict['directory_where'])))):
				print("作成するディレクトリを配下する場所のパスは、既に一つ以上のディレクトリを指定している場合、作成予定のディレクトリ全てを下に持つディレクトリを持っている必要があります。")

	if (is_root_directory == True):
		directory_info_dict['root_dir_path'] = directory_info_dict['directory_path']
	if (is_root_directory == False and tree_mode == True):
		directory_info_dict['root_dir_path'] = None # 既存のもの（既に他で決定されている。）
	if (tree_mode == True):
		directory_info_dict['tree_mode'] = True
	if (is_root_directory == True):
		directory_info_dict['is_root_directory'] = True
		directory_info_dict['directory_id'] = 0
	else:
		directory_info_dict['is_root_directory'] = False
	return directory_info_dict

def create_root_directory_info(directory_info_dict_list:list) -> list:
	# ルートとなるディレクトリを指定する。
	while True:
		if_create_root_directory = input("木構造上にディレクトリを作成します。ルートとなるディレクトリとなるディレクトリを作成しますか？ 作成しない場合は、既存のディレクトリから選択することになります。　[ Y/N ]: ")
		if (if_create_root_directory == "Y"):
			root_directory_info_dict = create_directory_info(directory_info_dict_list, 0, True, True, True)
			break
		elif (if_create_root_directory == "N"):
			root_directory_info_dict = create_directory_info(directory_info_dict_list, 0, False, True, True)
			break
		else:
			print("入力が正しくありません。")
			pass
	return root_directory_info_dict

"""
def create_tree_info(directory_info_dict_list:list):

"""