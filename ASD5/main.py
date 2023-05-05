import heapq
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]
import heapq

class MedianFinder:
    def __init__(self):
        self.low = []    # max-heap
        self.high = []   # min-heap

    def addNum(self, num: int) -> None:
        if len(self.low) == len(self.high):
            heapq.heappush(self.high, -heapq.heappushpop(self.low, -num))
        else:
            heapq.heappush(self.low, -heapq.heappushpop(self.high, num))

    def findMedian(self) -> float:
        if len(self.low) == len(self.high):
            return (self.high[0] - self.low[0]) / 2.0
        else:
            return float(self.high[0])

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
        if i % 2 == 0:
            median = abs(int(mf.findMedian()))
        else:
            median = (abs(int(mf.low[0])), abs(int(mf.high[0])))
        medians.append(median)
    return medians

def main(input_file, output_file):
    n, a = read_input_file(input_file)
    medians = calculate_medians(n, a)
    write_output_file(output_file, medians)

if __name__ == '__main__':
    main(input_file, output_file)
