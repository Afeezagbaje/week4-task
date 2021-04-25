import unittest
from src.chart import *


class TestBarChat(unittest.TestCase):
    def setUp(self):
        self.x_axis = ['Python', 'Number', 'Game', 'Users', 'Night', 'Longer', 'Javascript']
        self.y_axis = [3, 2, 2, 1, 1, 1, 1]
        self.bar = BarChart(self.x_axis, self.y_axis)

    def test_plot(self):
        self.assertIsNotNone(self.bar.plot)


class TestPieChat(unittest.TestCase):
    def setUp(self):
        self.data_label = ['Python', 'Number', 'Game', 'Users', 'Night', 'Longer', 'Javascript']
        self.data = [3, 2, 2, 1, 1, 1, 1]
        self.pie = BarChart(self.data, self.data_label)

    def test_plot(self):
        self.assertIsNotNone(self.pie.plot)


if __name__ == '__main__':
    unittest.main()
