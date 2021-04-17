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

# Time complexity       O(n*m) where n is the number of words in wordlist and m in the lenght of the words
# Space complexity      O(n)
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
            for j in range(m):
                if current_word[j] == reference_word[j]:
                    current_num_matches += 1
                arr_of_counters[j][current_word[j]] -= 1
            if current_num_matches == target_num_matches:
                new_word_list.append(current_word)
            else:
                self.remove_word_from_arr_of_counters(current_word, arr_of_counters)

        return new_word_list

    def remove_word_from_arr_of_counters(self, word, arr_of_counters):
        for i, char in enumerate(word):
            arr_of_counters[i][char] -= 1

# Version 2 - A slightly more concise way of implementing the aprroach from V1
class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        # keep track of candidates
        candidates = {word: 0 for word in wordlist}
        
        # update scores of words related to our guess
        def update_score(word, guess, guess_score):
            for i in range(len(word)):
                if word[i] == guess[i]:
                    if guess_score == 0:
                        del candidates[word]
                        return
                    candidates[word] += 1
        
        # search for candidate with the highest score
        attempts = 0
        while len(candidates) > 0 and attempts < 10:
            _, guess = min([(-score, word) for word, score in candidates.items()])
            guess_score = master.guess(guess)
            if guess_score == len(guess):
                return
            del candidates[guess]
            for candidate in list(candidates.keys()):
                update_score(candidate, guess, guess_score)
            attempts += 1

# Version 3 - Apply no heuristic to which guess is next. Just randomly pick a word 
# and eliminate using matching
class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        
        def match(word, guessword):
            ctr = 0
            for i in range(6):
                if word[i] == guessword[i]:
                    ctr += 1
            return ctr
            
        i = 0
        while i < 10:
            guessword = random.choice(wordlist)
            value = master.guess(guessword)
            if value != 6:
                wordlist = [word for word in wordlist if match(word, guessword) == value]
            else:
                break
            i += 1