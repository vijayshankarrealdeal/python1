class MergeSort(object):
    def __init__(self,array):
        self.array = array
    def merge(self):
        if len(self.array) > 1:
            m = len(self.array)//2
            left = self.array[:m]
            right = self.array[m:]

            leftsorted = MergeSort(left)
            leftsorted.merge()
            rightsorted = MergeSort(right)
            rightsorted.merge()
            i = 0
            j = 0
            k = 0
            while  i < len(left) and j < len(right):
                if left[i] < right[j]:
                    self.array[k] = left[i]
                    i += 1
                else:
                    self.array[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                self.array[k] = left[i]
                i += 1
                k += 1
            while  j < len(right):
                self.array[k] = right[j]
                j += 1
                k += 1     

k = MergeSort([12,4,68,2,4364,1,34])
k.merge()
print(k.array)           
