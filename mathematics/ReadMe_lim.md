# Limit Superior and Limit Inferior Animation

This Python script generates an animated visualization of the limit superior and limit inferior of a sequence using Matplotlib. The sequence used in this example is defined as:

```
x_n = sin(n) + (-1)^n / sqrt(n)
```

## Getting Started

To run this script, you need to have the following dependencies installed:

- NumPy
- Matplotlib

You can install these dependencies using the following command:

```
pip install numpy matplotlib
```

## Usage

1. Import the necessary libraries:
```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
```

2. Define the sequence:
```python
n = np.linspace(1, 100, 100)  # 100 terms
sequence = np.sin(n) + (-1)**n / np.sqrt(n)
```

3. Create the figure and axes:
```python
fig, ax = plt.subplots(figsize=(10, 6))
```

4. Plot the sequence:
```python
line, = ax.plot(n, sequence, 'o-')
```

5. Define the limit superior and limit inferior lines:
```python
limsup_line, = ax.plot([], [], 'r--')
liminf_line, = ax.plot([], [], 'g--')
```

6. Set the labels for the axes and enable grid:
```python
ax.set_xlabel('n')
ax.set_ylabel('$x_n$')
ax.grid(True)
```

7. Define the `update` function to update the plot for each frame of the animation.

8. Create the animation:
```python
ani = animation.FuncAnimation(fig, update, frames=len(n), blit=True)
```

9. Display the animation:
```python
plt.show()
```

## Saving the Animation

To save the animation as a GIF file, uncomment the following code:

```python
# ani.save('limsup_liminf.gif', writer='pillow')
```

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvement, please feel free to open an issue or submit a pull request in the repository.


## Acknowledgments

- This script was created for educational purposes and demonstrates the concept of limit superior and limit inferior.
- Thanks to [Matplotlib](https://matplotlib.org/) for providing the animation functionality.
