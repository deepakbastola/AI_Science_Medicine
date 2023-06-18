import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the sequence
n = np.linspace(1, 100, 100)  # 100 terms
sequence = np.sin(n) + (-1)**n / np.sqrt(n)

fig, ax = plt.subplots(figsize=(10,6))
line, = ax.plot(n, sequence, 'o-')
limsup_line, = ax.plot([], [], 'r--')
liminf_line, = ax.plot([], [], 'g--')
ax.set_xlabel('n')
ax.set_ylabel('$x_n$')
ax.grid(True)

def update(frame):
    if frame == 0:
        limsup = liminf = sequence[0]
    else:
        limsup = np.max(sequence[:frame])
        liminf = np.min(sequence[:frame])
    
    line.set_data(n[:frame], sequence[:frame])
    limsup_line.set_data(n[:frame], [limsup]*frame)
    liminf_line.set_data(n[:frame], [liminf]*frame)
    
    ax.relim()
    ax.autoscale_view()
    ax.legend(['Sequence $x_n = \sin(n) + (-1)^n / \sqrt{n}$', 'limsup', 'liminf'])
    
    return line, limsup_line, liminf_line,

ani = animation.FuncAnimation(fig, update, frames=len(n), blit=True)

# Save the animation as a GIF file
ani.save(r'C:\Users\User\Desktop\limsup_liminf.gif', writer='pillow')

plt.show()
