# -*- coding: utf-8 -*-
import sida.cs228.standardize as std
import numpy as np
import pickle

def test_help():
    std.help()

def test_do():
    data = np.random.rand(5,4,6,1)
    data = std.do(data)

def test_true_data():
    with open("test/test_data/Liu_train2.p", "rb") as f:
        data = pickle.load(f)
    data = std.do(data)

def test_true_data_1():
    with open("test/test_data/Liu_train2.p", "rb") as f:
        data = pickle.load(f)
    data = std.do(data)
    # If want to write new result for future comparison:
    # with open("test/test_data/Liu_train2_std.p", "wb") as f:
    #     pickle.dump(data, f)
    with open("test/test_data/Liu_train2_std.p", "rb") as f:
        data_1 = pickle.load(f)
    assert np.array_equal(data, data_1)

if __name__ == "__main__":
    test_true_data_1()