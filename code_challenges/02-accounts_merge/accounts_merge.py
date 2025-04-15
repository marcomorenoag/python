# Problem: https://leetcode.com/problems/accounts-merge/description/

import logging
from typing import List

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(funcName)s - %(message)s",
)


class Solution:
    def __init__(self):
        """
        {
            'johnsmith@mail.com': ['john_newyork@mail.com', 'john00@mail.com'],
            'john_newyork@mail.com': ['johnsmith@mail.com'],
            'john00@mail.com': ['johnsmith@mail.com'],
            'mary@mail.com': [],
            'johnnybravo@mail.com': []
        }
        """
        self.__adjacent_list = dict()

        """
        {'johnsmith@mail.com', 'mary@mail.com', 'johnnybravo@mail.com'}
        """
        self.__visited_nodes = set()

    def __DFS(self, merged_account: List[str], email: str) -> None:
        self.__visited_nodes.add(email)
        merged_account.append(email)

        if email not in self.__adjacent_list:
            return

        for neighbor in self.__adjacent_list[email]:
            if neighbor in self.__visited_nodes:
                continue
            self.__DFS(merged_account, neighbor)

    def __buildGraphAdjacentList(self, accounts: List[List[str]]) -> None:
        for account in accounts:
            # Centre of the Graph Star https://en.wikipedia.org/wiki/Star_(graph_theory)
            first_email = account[1]
            total_emails = len(account)

            for idx in range(2, total_emails):
                email = account[idx]

                # Build vertex from centre (first_email) to the current email
                # # if first_email not in self.__adjacent_list:
                # #     self.__adjacent_list[first_email] = []
                # # self.__adjacent_list[first_email].append(email)
                self.__adjacent_list.setdefault(first_email, []).append(email)

                # Build vertex from the current email to centre (first_email). Due to it's a Undirected Graph
                # # if email not in self.__adjacent_list:
                # #     self.__adjacent_list[email] = []
                # # self.__adjacent_list[email].append(first_email)
                self.__adjacent_list.setdefault(email, []).append(first_email)

    def accounts_merge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Build Graph adjacent list
        self.__buildGraphAdjacentList(accounts)

        # Go over DFS
        merged_accounts: List[List[str]] = []
        for account in accounts:
            name = account[0]
            first_email = account[1]
            if first_email in self.__visited_nodes:
                continue

            merged_account: List[str] = [name]
            self.__DFS(merged_account, first_email)
            merged_account[1:] = sorted(merged_account[1:])

            merged_accounts.append(merged_account)

        # Return result
        return merged_accounts


if __name__ == "__main__":
    input = [
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["Mary", "mary@mail.com"],
        ["John", "johnnybravo@mail.com"],
    ]
    solution = Solution()
    merged_accounts = solution.accounts_merge(input)
    logging.info(f"merged_accounts: {merged_accounts}")
