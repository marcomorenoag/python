import unittest

from accounts_merge import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    # def tearDown(self):
    #     return super().tearDown()

    def test_only_two_common_accounts(self):
        input = [
            ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
            ["John", "johnsmith@mail.com", "john00@mail.com"],
            ["Mary", "mary@mail.com"],
            ["John", "johnnybravo@mail.com"],
        ]
        merged_accounts = self.solution.accounts_merge(input)
        self.assertIsNotNone(merged_accounts)
        self.assertEqual(len(merged_accounts), 3)

        self.assertEqual(len(merged_accounts[0]), 4)
        self.assertEqual(merged_accounts[0][0], "John")
        self.assertEqual(merged_accounts[0][1], "john00@mail.com")

        self.assertEqual(len(merged_accounts[1]), 2)
        self.assertEqual(merged_accounts[1][0], "Mary")
        self.assertEqual(merged_accounts[1][1], "mary@mail.com")

        self.assertEqual(len(merged_accounts[2]), 2)
        self.assertEqual(merged_accounts[2][0], "John")
        self.assertEqual(merged_accounts[2][1], "johnnybravo@mail.com")


if __name__ == "__main__":
    unittest.main()
