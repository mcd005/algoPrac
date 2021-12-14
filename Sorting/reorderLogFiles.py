# Version 1 - Using list.sort() with a key
# When we do key=lamdba x: ( f1(x), f2(x), f3(x) )
# We first try to sort in ascending order the keys produced from f1(x)
# If two elements from f1(x) producing the same key, we leave them in their existing order
# We then try to sort them based on the keys produced by f2(x)
# If again the keys are the same we try to sort by f3(x)
# And so on

# So for this problem the ordering is done as follows
# digitLogSortKey will return 0 for letter logs and (idx from original logs + 1) for a digit log
#   all the digit logs will be at then end of the array with their existing order and all the letter logs will be at the start of the array
#   because all the letter logs will have a key of 0 from this function, we move to the next function that produces a key
# getLogContents will return the content of the log as a key. By default Python sorts these lexicographically, as we wanted
#   if we have the same content we move to the next function that produces a key
# getLogId will return the Id of the log as a key. By default Python sorts these lexicographically, as we wanted

# Time complexity       O(n + nlogn)
# Space complexity       O(n)
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_log_ordering = {log : idx for idx, log in enumerate(logs) if self.is_digit_log(log)}
        logs.sort(key=lambda log: (self.digit_log_sort_key(log, digit_log_ordering), self.get_log_contents(log), self.get_log_id(log)))
        return logs

    @staticmethod
    def is_digit_log(log):
        return log[log.find(" ") + 1].isdigit()

    @staticmethod
    def get_log_contents(log):
        return log[log.find(" ") + 1:]

    @staticmethod
    def get_log_id(log):
        return log[:log.find(" ") ]

    @classmethod
    def digit_log_sort_key(cls, log, digit_log_ordering):
        if cls.is_digit_log(log):
            return digit_log_ordering[log] + 1
        return 0