import os
import time
import datetime
from datetime import date
# プロジェクト由来のモジュール。
from libraries import classes
from libraries import time_edit
from libraries import formulae, sets, create_data_functions

def main() -> None:
	while True:
		commandline_input = input("入力待ち: ")
		if commandline_input == 'later':
			print("プログラムを終了します。")
			break
		elif commandline_input == 'create_dirs_on_specific_time':
			directory_info_dict_list = []
			given_datetime = time_edit.input_time_today()
			directory_info_dict = create_data_functions.create_directory_info(directory_info_dict_list)
			create_data_functions.create_dirs_on_specific_time(given_datetime, directory_info_dict['directory_name'], directory_info_dict['directory_where'])
		elif commandline_input == 'create_dirs':
			directory_info_dict_list = []
			directory_info_dict = create_data_functions.create_directory_info(directory_info_dict_list)	
			create_data_functions.create_directories(directory_info_dict['directory_name'], directory_info_dict['directory_where'])
		elif commandline_input == 'create_multiple_directories':
			file_or_directory_input = input("Tree構造状にディレクトリを作成しますか？ T/F: ")
			if (file_or_directory_input == "T"): # tree構造状にディレクトリを作成する。
				directory_tree = classes.SetOfDirectories()
				directory_info_dict_list = []
				# ルートディレクトリを指定する。
				if_create_root_directory = input("ルートディレクトリとなるディレクトリを作成しますか？ 作成しない場合は、既存のディレクトリから選択することになります。　T/F: ")
				if (if_create_root_directory == "T"):
					root_directory_info_dict = create_data_functions.create_directory_info(directory_info_dict_list, True, True, True)
				else:
					root_directory_info_dict = create_data_functions.create_directory_info(directory_info_dict_list, False, True, True)
				directory_info_dict_list.append(root_directory_info_dict)

				c=0
				while True:
					directory_info_dict = create_data_functions.create_directory_info(directory_info_dict_list, True)
					directory_info_dict_list.append(directory_info_dict)
					directory_tree.add_element(classes.Directory(directory_info_dict['directory_name'], directory_info_dict['directory_where'], directory_info_dict['root_dir_path'], directory_info_dict['tree_mode'], c))
					
					if_show = input("現状作成予定のディレクトリ情報表示しますか？ T/F: ")
					if (if_show	== "T"):
						directory_tree.show()

					if_more = input("さらにディレクトリを作成しますか？ T/F: ")
					if (if_more == "T"):
						c += 1
					else:
						break
				
				set_of_directories = classes.SetOfDirectories()
				for directory_info in directory_info_dict_list:
					directory = classes.Directory(directory_info['directory_name'], directory_info['directory_where'], directory_info['root_dir_path'], directory_info['tree_mode'])
					directory.set_dir_path()
					set_of_directories.add_element(directory)

				set_of_directory_ordered_pairs = sets.create_set_of_ordered_pairs_from_set_of_directories(set_of_directories.mutable_set)				
				relation = sets.create_relation(formulae.formula_directory_J_is_equal_to_or_below_directory_I, set_of_directory_ordered_pairs)
				relation.show_ordered_pairs(True)

				print("\n")
				for directory in set_of_directories.mutable_set:
					directory.calculate_rank(set_of_directory_ordered_pairs)
					print("DIRNAME: " + directory.dir_name + ", RANK" + (str)(directory.rank))
					print("SET FOR CALCULATION: " + (str)(directory.set_for_calculation) + "\n")

				given_datetime = time_edit.input_time_today()
				for directory_info_dict in directory_info_dict_list:
					create_data_functions.create_dirs_on_specific_time(given_datetime, directory_info_dict['directory_name'], directory_info_dict['directory_where'])