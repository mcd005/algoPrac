import calendar

class Solution:
    def __init__(self):
        self.month_map = {month: f'{str(index):0>2}' for index, month in enumerate(calendar.month_abbr) if month}

    def reformatDate(self, date: str) -> str:
        date_split = date.split()
        date_split[0] = f'{date_split[0][:-2]:0>2}'
        date_split[1] = self.month_map[date_split[1]]
        return "-".join(reversed(date_split))
