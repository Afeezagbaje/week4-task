from matplotlib import pyplot as plt


class IChart:
    def plot(self):
        raise NotImplementedError


class BarChart(IChart):
    """This class models bar chart plotter"""
    def __init__(self, x_axis, y_axis):
        self.x_axis = x_axis
        self.y_axis = y_axis

    def plot(self):
        plt.bar(self.x_axis, self.y_axis)
        plt.xlabel('Words')
        plt.ylabel('Number of Appearance')
        return plt.show()


class PieChart(IChart):
    """This class models pie chart plotter"""
    def __init__(self, data, data_label):
        self.data = data
        self.data_label = data_label

    def plot(self):
        plt.pie(self.data, labels=self.data_label, shadow=True,
                wedgeprops={'edgecolor': 'black'}, autopct='%1.1f%%')
        plt.show()

