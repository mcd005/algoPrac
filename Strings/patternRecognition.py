# For an input string like: "bcdefbcbebc|abcdebcfgsdf|cbdbesfbcy|1bcdef23423bc32"
# and a given pattern like: "bc"
# count how many times that pattern occurs in each of the substrings seperated by |
# Return the answer in the form : A|B|C|D|E 
# where A, B, C, D are the counts in that slice 
# and E = A + B + C + D

# Time complexity     O(n)
# Space complexity    O(n)

import re

def patternRecog(blob, pattern):
    slices = blob.split("|")
    output = []
    total = 0
    for slce in slices:
        numInSlice = slce.count(pattern)
        total += numInSlice
        output.append(str(numInSlice))
        output.append("|")

    output.append(str(total))
    return "".join(output)

def doSomething(blobs, pattern):

        if not pattern:
            validPattern = 0
        else:
            validPattern = 1

        output = []
        total = 0
        for blob in blobs:
            numInSlice = len(re.findall('(?={})'.format(pattern)))
            total += numInSlice
            output.append(str(numInSlice * validPattern))
            output.append("|")

        output.append(str(total * validPattern))
        return "".join(output)


    # occurrences = [m.start() for m in re.finditer(pattern, blob)]
    # slices = [m.start() for m in re.finditer("\|", blob)] + [len(blob) - 1]
    #
    # j = 0
    # slice_count, total = 0, 0
    # output = []
    # for i in range(len(slices)):
    #     while occurrences[j] < slices[i]:
    #         j += 1
    #         slice_count += 1
    #         total += 1
    #     output.append(str(slice_count))
    #     output.append("|")
    #     slice_count = 0
    #
    # output.append(str(total))
    # return "".join(output)

print(patternRecog("bcdefbcbebc|abcdebcfgsdf|cbdbesfbcy|1bcdef23423bc32", "b"))
