# sida-cs228

## Installation

```bash
pip install sida-cs228
```

## Usage

### Moving the data of the hands to make them standardized

```python
import sida.cs228.standardize as std
data = ... # shape (5,4,6,n)
std_data = std.do(data)
```

### Show one hand, or save it as a file

```python
from sida.cs228.show import show_hand
data = ... # shape (5,4,6,n)
show_hand(data[:,:,:,0], view_point="front", scale="unit") # show the first hand
show_hand(data[:,:,:,1], view_point="side", scale="fit", fname="hand1.png") # save the side view of the second hand to a png file
```

## Standardizing steps

The shape of the argument `data` should be: `(5,4,6,n)`, where `n` can be any integer.

The meaning of the shape is: `5` fingers, `4` bones, `6` coordinates, `n` hands.

The result of `do` function will satisfy those conditions:

```bash
(1) the base of index finger on the origin,

(2) the tip of the metacarpal bone of the index finger will on the point (0,1,0),

(3) the tip of the metacarpal bone of the baby finger will also on the x-y plane,

(4) the tip of the metacarpal bone of the thumb will be on the +z side.
```
