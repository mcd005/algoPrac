class SnapshotArray:

    def __init__(self, length: int):
        pass

    def set(self, index: int, val: int) -> None:
        pass

    def snap(self) -> int:
        pass

    def get(self, index: int, snap_id: int) -> int:
        pass

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)

'''
Naive
We have a standard array
We do set operations as you would usually
When snap is called we save the array, storing it in an array of arrays
When get is called we lookup in the 2D array
Quite expensive in terms of memory O(n * m) n is array and n is number of snaps

When we call get we ask 

If set has not been called on this index since the 


'''