# sida-cs228

## Installation

```bash
pip install sida-cs228
```

## Usage

```python
import sida-cs228 as cs228
data = ... # shape (5,4,6,n)
std_data = cs228.standardization.do(data)
```

```python
import sida-cs228 as cs228
data = ... # shape (5,4,6,n)
cs228.show(data[:,:,:,0], view_point="front", scale="unit") # show the first hand
```
