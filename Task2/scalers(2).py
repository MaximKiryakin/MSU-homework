import numpy as np


class MinMaxScaler:
    def fit(self, data):
        self.min = np.min(data, axis=0)
        self.max = np.max(data, axis=0)

    def transform(self, data):
        return (data - self.min)/(self.max - self.min)


class StandardScaler:
    def fit(self, data):
        self.mean = np.mean(data, axis=0)
        self.std = np.std(data, axis=0)

    def transform(self, data):
        return (data - self.mean)/self.std
