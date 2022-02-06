import unittest

def generate_n_van_eck_terms(n):
    # 0 0 1 0 2 0 2 2 1 6 0 ... etc
    seen = {} # {int: greatest idx at which int can be found at}
    terms = []
    val, next = 0, 0
    for i in range(n):
        terms.append(val)
        if val in seen:
            next = i - seen[val]
        else:
            next = 0
        seen[val] = i 
        val = next
        
    return terms

class TestVanEck(unittest.TestCase):
    def test_van_eck_for_given_n(self):
        sequence = generate_n_van_eck_terms(60000)
        self.assertTrue(self.is_valid_van_eck_seq(sequence))

    def is_valid_van_eck_seq(self, sequence):
        n = len(sequence)
        for term_no in range(n):
            if (term_no == 0 and sequence[term_no] != 0) or (sequence[term_no - 1 - sequence[term_no]] != sequence[term_no - 1]):
                return False
        return True


if __name__ == "__main__":
    unittest.main()