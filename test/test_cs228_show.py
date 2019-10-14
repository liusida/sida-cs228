from sida.cs228.show import show_hand
import pickle

def test_show():
    with open("test/test_data/Liu_train2_std.p", "rb") as f:
        data = pickle.load(f)
    show_hand(data[:,:,:,0], view_point="front", scale="unit", fname="test/test_data/Liu_train2_std_front.png")
    show_hand(data[:,:,:,0], view_point="side", scale="unit", fname="test/test_data/Liu_train2_std_side.png")

if __name__ == "__main__":
    test_show()

