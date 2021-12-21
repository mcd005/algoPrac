# https://leetcode.com/problems/invalid-transactions
# Version 2 - From LC. A nested dictionary
# Time complexity         O(n)
# Space complexity         O(n)
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        tran = defaultdict(dict)
        invalid = []
        # Construct a dict that looks like {timestamp: { person_name: set(city_names}}
        for transaction in transactions:
            name, time, amount, city = transaction.split(',')
            time = int(time)
            if name not in tran[time]:
                tran[time][name] = {city}
            else:
                tran[time][name].add(city)
        # Then iterate through the transactions again
        for transaction in transactions:
            name, time, amount, city = transaction.split(',')
            time = int(time)
            # Check for validity based on first constraint
            if int(amount) > 1000:
                invalid.append(transaction)
                continue
            # Then check if there are any other transactions that occured within 60 mins of given transaction
            for inv_time in range(time-60, time+61):
                if inv_time not in tran:
                    continue
                # ... and make sure they have the same name
                if name not in tran[inv_time]:
                    continue
                trans_by_name_at_time = tran[inv_time][name]
                # check if transactions were done in a different city
                if city not in trans_by_name_at_time or len(trans_by_name_at_time) > 1:
                    invalid.append(transaction)
                    break

        return invalid

# Version 1 - Use a dict that looks like {name_of_person: transactions_that_person_made}
# Then for each new transaction, iterate over the other transactions of that person to see if it was invalid based on time and city
# Time complexity         O(n^2)
# Space complexity         O(n)
from collections import defaultdict
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid_transactions = set()

        transactions_per_person = defaultdict(lambda: [])
        for idx, transaction in enumerate(transactions):
            name, time, amount, city = transaction.split(",")
            time, amount = int(time), int(amount)
            if amount > 1000:
                invalid_transactions.add(idx)
            for idx_old, time_old, city_old in transactions_per_person[name]:
                if abs(time_old - time) <= 60 and city != city_old:
                    invalid_transactions.add(idx)
                    invalid_transactions.add(idx_old)
            transactions_per_person[name].append((idx, time, city))

        return [transactions[i] for i in invalid_transactions]