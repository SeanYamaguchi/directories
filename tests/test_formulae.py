import unittest
import sys
import os

# プロジェクトフォルダーよりインポート。
upper_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(upper_directory, 'create_directories'))
from libraries import classes, create_data_functions, formulae, sets

directory_root = classes.Directory('directory_root', 'directory_root_where', 'directory_root_where\\directory_root', True, 0)
directory_root.set_dir_path()

directory_M = classes.Directory('directory_M', 'directory_root_where\\directory_root', 'directory_root_where\\directory_root', True, 1)
directory_M.set_dir_path()

directory_N = classes.Directory('directory_N', 'directory_root_where\\directory_root\\directory_M', 'directory_root_where\\directory_root', True, 2)
directory_N.set_dir_path()

ordered_pair_directory_M_comma_directory_N = classes.DirectoryOrderedPair(directory_M, directory_N)
ordered_pair_directory_N_comma_directory_M = classes.DirectoryOrderedPair(directory_N, directory_M)

ordered_pair_directory_root_comma_directory_M = classes.DirectoryOrderedPair(directory_root, directory_M)
ordered_pair_directory_M_comma_directory_root = classes.DirectoryOrderedPair(directory_M, directory_root)

ordered_pair_directory_root_comma_directory_N = classes.DirectoryOrderedPair(directory_root, directory_N)
ordered_pair_directory_N_comma_directory_root = classes.DirectoryOrderedPair(directory_N, directory_root)

ordered_pair_directory_M_comma_directory_M = classes.DirectoryOrderedPair(directory_M, directory_M)
ordered_pair_directory_N_comma_directory_N = classes.DirectoryOrderedPair(directory_N, directory_N)
ordered_pair_directory_root_comma_directory_root = classes.DirectoryOrderedPair(directory_root, directory_root)

class TestFormulaDirectoryJIsEqualToOrBelowDirectoryI(unittest.TestCase):
	def test_directory_M_is_equal_to_or_below_directory_N(self):
		self.assertEqual(formulae.formula_directory_J_is_equal_to_or_below_directory_I(ordered_pair_directory_M_comma_directory_N), True)

	def test_directory_M_is_equal_to_or_below_directory_M(self):
		self.assertEqual(formulae.formula_directory_J_is_equal_to_or_below_directory_I(ordered_pair_directory_M_comma_directory_M), True)

	def test_directory_N_is_neither_equal_to_nor_below_directory_M(self):
		self.assertEqual(formulae.formula_directory_J_is_equal_to_or_below_directory_I(ordered_pair_directory_N_comma_directory_M), False)

class TestFormulaDirectoryJIsEqualToDirectoryI(unittest.TestCase):
	def test_directory_M_is_equal_to_directory_M(self):
		self.assertEqual(formulae.formula_directory_J_is_equal_to_directory_I(ordered_pair_directory_M_comma_directory_M), True)

	def test_directory_N_is_equal_to_directory_N(self):
		self.assertEqual(formulae.formula_directory_J_is_equal_to_directory_I(ordered_pair_directory_N_comma_directory_N), True)

	def test_directory_root_is_equal_to_directory_root(self):
		self.assertEqual(formulae.formula_directory_J_is_equal_to_directory_I(ordered_pair_directory_root_comma_directory_root), True)

	def test_directory_root_is_not_equal_to_directory_M(self):
		self.assertEqual(formulae.formula_directory_J_is_equal_to_directory_I(ordered_pair_directory_root_comma_directory_M), False)

	def test_directory_M_is_not_equal_to_directory_root(self):
		self.assertEqual(formulae.formula_directory_J_is_equal_to_directory_I(ordered_pair_directory_M_comma_directory_root), False)

class TestFormulaDirectoryJIsNotDirectoryI(unittest.TestCase):
	def test_directory_M_is_equal_to_directory_M(self):
		self.assertEqual(formulae.formula_directory_J_is_not_directory_I(ordered_pair_directory_M_comma_directory_M), False)

	def test_directory_N_is_equal_to_directory_N(self):
		self.assertEqual(formulae.formula_directory_J_is_not_directory_I(ordered_pair_directory_N_comma_directory_N), False)

	def test_directory_root_is_equal_to_directory_root(self):
		self.assertEqual(formulae.formula_directory_J_is_not_directory_I(ordered_pair_directory_root_comma_directory_root), False)

	def test_directory_root_is_not_directory_M(self):
		self.assertEqual(formulae.formula_directory_J_is_not_directory_I(ordered_pair_directory_root_comma_directory_M), True)

	def test_directory_M_is_not_directory_root(self):
		self.assertEqual(formulae.formula_directory_J_is_not_directory_I(ordered_pair_directory_M_comma_directory_root), True)

class TestFormulaDirectoryJIsBelowDirectoryI(unittest.TestCase):
	def test_directory_M_is_below_directory_N(self):
		self.assertEqual(formulae.formula_directory_J_is_below_directory_I(ordered_pair_directory_M_comma_directory_N), True)

	def test_directory_M_is_not_below_directory_M(self):
		self.assertEqual(formulae.formula_directory_J_is_below_directory_I(ordered_pair_directory_M_comma_directory_M), False)

	def test_directory_N_is_not_below_directory_M(self):
		self.assertEqual(formulae.formula_directory_J_is_below_directory_I(ordered_pair_directory_N_comma_directory_M), False)

unittest.main(argv=['first-arg-is-ignored'], exit=False)