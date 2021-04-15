# https://leetcode.com/problems/guess-the-word/
#  Work out what the count is for each letter in each position
#  Then go through and calculate a similiarity score for each word
#  Keep track of the least similiar word
#  Guess the least similar word
#       You pick a word and it gives you n matches. This word is now your reference
#       You iterate through the rest of the words. They have to match exactly n characters with your reference
#       If they don't you discard them
#  As you are discarding update the counts
#  Repeat until you've elimated all possible words except the secret
# Time complexity       O(n*m) where n is the number of words in wordlist and 
class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        arr_of_counters = self.get_count(wordlist)
        for i in range(10):
            most_unique = self.find_most_unique_word(wordlist, arr_of_counters)
            num_match = master.guess(most_unique)
            if num_match == 6: return
            wordlist = self.eliminate_non_matches(num_match, wordlist, arr_of_counters, most_unique)

    def get_count(self, wordlist):
        n , m = len(wordlist), 6
        output = [collections.defaultdict(lambda: 0) for _ in range(m)]
        for i in range(n):
            current_word = wordlist[i]
            for j in range(m):
                output[j][current_word[j]] += 1
        return output

    def find_most_unique_word(self, wordlist, arr_of_counters):
        n , m = len(wordlist), 6
        min_similarity_score = n * m 
        result = wordlist[0]
        for i in range(n):
            current_word = wordlist[i]
            similiarityScore = 0
            for j in range(m):
                similiarityScore += arr_of_counters[j][current_word[j]]
            if similiarityScore < min_similarity_score:
                min_similarity_score = similiarityScore
                result = wordlist[i]
        return result

    def eliminate_non_matches(self, target_num_matches, wordlist, arr_of_counters, reference_word):
        n , m = len(wordlist), 6
        new_word_list = []
        for i in range(n):
            current_word = wordlist[i]
            current_num_matches = 0
            old_arr_of_counters = arr_of_counters.copy()
            for j in range(m):
                if current_word[j] == reference_word[j]:
                    current_num_matches += 1
                arr_of_counters[j][current_word[j]] -= 1
            if current_num_matches == target_num_matches:
                new_word_list.append(current_word)
                arr_of_counters = old_arr_of_counters
        return new_word_list
