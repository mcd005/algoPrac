# https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        output = []
        tables = {}
        foods = set()

        for order in orders:
            tableNo = int(order[1])
            food = order[2]
            if tableNo not in tables:
                tables[tableNo] = {food: 1}
            else:
                if food not in tables[tableNo]:
                    tables[tableNo][food] = 1
                else:
                    tables[tableNo][food] += 1

            if food not in foods:
                foods.add(food)

        output.append(["Table"] + sorted(list(foods)))

        for table in sorted(tables.items()):
            newRow = [str(table[0])] + ["0"] * len(foods)
            for j in range(1, len(foods) + 1):
                if output[0][j] in table[1]:
                    newRow[j] = str(table[1][output[0][j]])
            output.append(newRow)

        return output



