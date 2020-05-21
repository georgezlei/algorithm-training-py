# https://github.com/georgezlei/algorithm-training-py
# Author: George Lei
from unittest import TestCase
import algorithm_training as at
import algorithm_training.classic.string_search as s

class StringSearchTest(TestCase):
  def test_brute_force(self):
    self.assertTrue(at.test(s.brute_force, s.test_cases))

  def test_string_find(self):
    self.assertTrue(at.test(s.string_find, s.test_cases))

  def test_kmp(self):
    self.assertTrue(at.test(s.kmp, s.test_cases))