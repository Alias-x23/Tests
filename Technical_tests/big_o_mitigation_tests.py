import unittest
import pandas as pd
from big_o_mitigation import Problem1, Problem2


class Testing(unittest.TestCase):
    def test_prob_1a_pass(self):
        data = [198, 37, 2000, 14, 20]
        expected_result = {"value_a": 2000, "value_b": 20, "multiply": (2000*20)}
        func_result = Problem1.find_two(data)
        self.assertEqual(func_result, expected_result)

    def test_prob_1a_fail(self):
        data = [198, 37, 2001, 14, 20]
        expected_result = {"error": "Couldn't find any working values"}
        func_result = Problem1.find_two(data)
        self.assertEqual(func_result, expected_result)

    def test_prob_1b_pass(self):
        data = [198, 37, 2000, 14, 19, 1]
        expected_result = {"value_a": 2000, "value_b": 19, "value_c": 1, "multiply": (2000*19*1)}
        func_result = Problem1.find_three(data)
        self.assertEqual(func_result, expected_result)

    def test_prob_1b_fail(self):
        data = [198, 37, 2000, 14, 20, 1]
        expected_result = {"error": "Couldn't find any working values"}
        func_result = Problem1.find_three(data)
        self.assertEqual(func_result, expected_result)

    def test_prob_2a_pass(self):
        data_row = [{0: "1-2", 1: "b", 2: "abcde"}]
        data = pd.DataFrame(data_row)
        expected_result = 1
        func_result = Problem2.str_count(data)
        self.assertEqual(func_result, expected_result)

    def test_prob_2a_none(self):
        data_row = [{0: "1-2", 1: "b", 2: "acde"}]
        data = pd.DataFrame(data_row)
        expected_result = 0
        func_result = Problem2.str_count(data)
        self.assertEqual(func_result, expected_result)

    def test_prob_2b_pass(self):
        data_row = [{0: "1-2", 1: "b", 2: "abcde"}]
        data = pd.DataFrame(data_row)
        expected_result = 1
        func_result = Problem2.position_count(data)
        self.assertEqual(func_result, expected_result)

    def test_prob_2b_fail_none(self):
        data_row = [{0: "1-2", 1: "b", 2: "accde"}]
        data = pd.DataFrame(data_row)
        expected_result = 0
        func_result = Problem2.position_count(data)
        self.assertEqual(func_result, expected_result)

    def test_prob_2b_fail_none_alt(self):
        data_row = [{0: "1-2", 1: "b", 2: "acbbb"}]
        data = pd.DataFrame(data_row)
        expected_result = 0
        func_result = Problem2.position_count(data)
        self.assertEqual(func_result, expected_result)

    def test_prob_2b_fail_double(self):
        data_row = [{0: "1-2", 1: "b", 2: "bbcde"}]
        data = pd.DataFrame(data_row)
        expected_result = 0
        func_result = Problem2.position_count(data)
        self.assertEqual(func_result, expected_result)


if __name__ == '__main__':
    unittest.main()
