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
		print("[ 0.0 ] : create a directory ...... TYPE 0.0")
		print("[ 0.1 ] : create a directory on specific time ...... TYPE 0.1")
		print("[  1  ] : create multiple directories ...... TYPE 1")
		commandline_input = input("入力待ち: ")

		if commandline_input == 'later':
			print("プログラムを終了します。")
			break
		
		elif (commandline_input == 'create_a_directory_on_specific_time') or (commandline_input == '0.1'):
			"""
			ディレクトリを特定の時間に作成できるモード。
			"""
			directory_info_dict_list = []
			given_datetime = time_edit.input_time_today()
			directory_info_dict = create_data_functions.create_directory_info(directory_info_dict_list, 0)
			create_data_functions.create_directories_on_specific_time(given_datetime, directory_info_dict['directory_name'], directory_info_dict['directory_where'])
		
		elif (commandline_input == 'create_a_directory') or (commandline_input == '0.0'):
			"""
			指定したディレクトリを作成できるモード。
			"""
			directory_info_dict_list = []
			directory_info_dict = create_data_functions.create_directory_info(directory_info_dict_list, 0)	
			create_data_functions.create_directories(directory_info_dict['directory_name'], directory_info_dict['directory_where'])
		
		elif (commandline_input == 'create_multiple_directories') or (commandline_input == '1'):
			"""
			木構造にそって指定した1つ以上のディレクトリを特定の時間に作成できるモード。
			"""
			directory_tree = classes.SetOfDirectories()
			directory_info_dict_list = []
	
			root_directory_info_dict = create_data_functions.create_root_directory_info(directory_info_dict_list)
			directory_info_dict_list.append(root_directory_info_dict)
			
			c=1
			while True:
				directory_info_dict = create_data_functions.create_directory_info(directory_info_dict_list, c, True)
				directory_info_dict_list.append(directory_info_dict)
				directory_tree.add_element(classes.Directory(directory_info_dict['directory_name'], directory_info_dict['directory_where'], directory_info_dict['root_dir_path'], directory_info_dict['tree_mode'], directory_info_dict['directory_id']))
				
				if_show = input("現状作成予定のルートディレクトリ以外のディレクトリの情報表示しますか？ [ Y/N ]: ")
				if (if_show	== "Y"):
					directory_tree.show_with_directory_id()

				if_more = input("さらにディレクトリを作成しますか？ [ Y/N ]: ")
				if (if_more == "Y"):
					c += 1
				else:
					break
			
			set_of_directories = classes.SetOfDirectories()
			for directory_info in directory_info_dict_list:
				directory = classes.Directory(directory_info['directory_name'], directory_info['directory_where'], directory_info['root_dir_path'], directory_info['tree_mode'])
				directory.set_directory_path()
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
				create_data_functions.create_directories_on_specific_time(given_datetime, directory_info_dict['directory_name'], directory_info_dict['directory_where'])