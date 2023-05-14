import heapq
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]
import heapq

class MedianFinder:
    def __init__(self):
        if len(self.low) == 0:
        self.low = []    # max-heap
        self.high = []   # min-heap

    def addNum(self, num: int) -> None:
<<<<<<< HEAD
=======
        if len(self.low) == 0:
>>>>>>> eb2d29d6617e7f33ef7f371e832866b03db9a84c
            heapq.heappush(self.low, -num)
        elif num < abs(self.low[0]):
            heapq.heappush(self.low,  -num)
        else:
            heapq.heappush(self.high,  num)

        if len(self.low) >= ( len(self.high) + 2):
            heapq.heappush(self.high, -heapq.heappop(self.low))
        elif len(self.high) >= ( len(self.low) + 2):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def findMedian(self) -> float:
        if len(self.low) == len(self.high):
            return -self.low[0], self.high[0]
        elif len(self.low) > len(self.high):
            return -self.low[0]
        else:
            return self.high[0]


def read_input_file(input_file):
    with open(input_file, 'r') as file:
        n = int(file.readline().strip())
        a = []
        for i in range(n):
            a.append(int(file.readline().strip()))
        return n, a

def write_output_file(output_file, medians):
    with open(output_file, 'w') as file:
        for median in medians:
            if isinstance(median, int):
                file.write(str(median) + '\n')
            else:
                file.write(str(median[0]) + ' ' + str(median[1]) + '\n')

def calculate_medians(n, a):
    medians = []
    mf = MedianFinder()
    for i in range(n):
        mf.addNum(a[i])
        median = mf.findMedian()
        medians.append(median)
    return medians

def main(input_file, output_file):
    n, a = read_input_file(input_file)
    medians = calculate_medians(n, a)
    write_output_file(output_file, medians)

if __name__ == '__main__':
    main(input_file, output_file)