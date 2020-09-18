class Solution:
    def numberOfSteps (self, num: int) -> int:
        digits = f'{num:b}'
        MSB = len(digits)
        steps = MSB
        for i in range(1,MSB):
            #print(digits[i])
            if digits[i] == '1':
                steps += 1
        return steps
      
#Formula is (position of MSB + number of ones the follow it)
