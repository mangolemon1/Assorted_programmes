class Median:

    def __init__(self, numbers):
        self.numbers = []
        self.count = 0

    def count_objects_list(self):
        count = self.count
        for objects in self.numbers:
            count += 1

    def calculate_median(self, count):
        self.count_objects_list()
        if (count % 2) == 2:
            print(self.numbers[((count / 2) + (count / 2 + 1)) / 2])
        else:
            print(self.numbers[(count / 2) + 0.5])

my_median = Median([1, 2, 3])
my_median.calculate_median(my_median.count)


    