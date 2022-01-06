# https://leetcode.com/problems/count-unhappy-friends/
# Time complexity           O(n^2)
# Space complexity          O(n^2)
class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        # rank[i][j] is how person i rates person j
        rank = [[n for j in range(n)] for i in range(n)]

        for person_no, preference_list in enumerate(preferences):
            for pref_no, other_person in enumerate(preference_list):
                rank[person_no][other_person] = pref_no
            
        paired_with = {}
        for x, y in pairs:
            paired_with[x] = y
            paired_with[y] = x

        unhappy_people = set()
        for x, y in pairs:
            if x not in unhappy_people and rank[x][y] != 0:
                for u, u_rank in enumerate(rank[x]):
                    if u_rank < rank[x][y] and rank[u][x] < rank[u][paired_with[u]]:
                        unhappy_people.add(x)
                        unhappy_people.add(u)
                        break

            if y not in unhappy_people and rank[y][x] != 0:
                for v, v_rank in enumerate(rank[y]):
                    if v_rank <  rank[y][x] and rank[v][y] < rank[v][paired_with[v]]:
                        unhappy_people.add(y)
                        unhappy_people.add(v)
                        break
        
        return len(unhappy_people)

# Iterate over pairs, expanding each as person 1 and person 2
# Look at all the people that person 1 would prefer to be paired with
# If those people would prefer to be paired with person1 over the person they are currently paired with
#   then increment the count
# We need a way of answering "Who would they rather be with than x?" in O(1)
# What we could is create a dict that looks like 
# {person_1 : {person2 : people_person1 would rather be with than person 2}}
# Would result in an O(n^3) solution though

# Rank matrix
# My current plan is to iterate over the pairs
# Then for each person in the pair - O(n)
# Look at all the people they rate more than the person they are paired with - O(n)
# At see if that person would prefer to be with them - O(1)
# Unhappy friends come in pairs which allows us to reduce search space