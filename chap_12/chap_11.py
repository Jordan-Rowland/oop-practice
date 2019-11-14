import unittest


def average(seq):
    return sum(seq) / len(seq)


class TestAverage(unittest.TestCase):
    def test_zero(self):
        self.assertRaises(ZeroDivisionError, average, [])

    @unittest.skip("Testing the skip decorator")
    def test_with_zero(self):
        with self.assertRaises(ZeroDivisionError):
            average([])

    def test_falsey(self):
        self.assertFalse(0)

    def test_truthy(self):
        self.assertTrue('string')


class CheckNumbers(unittest.TestCase):
    def test_int_float(self):
        self.assertEqual(1, 1.0)

    @unittest.expectedFailure
    def test_str_float(self):
        """Supposed to fail."""
        self.assertEqual(1, "1")


# from stats import StatsList
# 
# 
# class TestValidInputs(unittest.TestCase):
#     def setUp(self):
#         self.stats = StatsList([1, 2, 2, 3, 3, 4, ])
# 
#     def test_mean(self):
#         self.assertEqual(self.stats.mean(), 2.5)
# 
#     def test_median(self):
#         self.assertEqual(self.stats.median(), 2.5)
#         self.stats.append(4)
#         self.assertEqual(self.stats.median(), 3)
# 
#     def test_mode(self):
#         self.assertEqual(self.stats.mode(), [2, 3])
#         self.stats.remove(2)
#         self.assertEqual(self.stats.mode(), [3])
# 





if __name__ == "__main__":
    unittest.main()
