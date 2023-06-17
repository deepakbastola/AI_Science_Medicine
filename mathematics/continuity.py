import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.style as style

# Define the function
def f(x):
    return x**2

# Choose the point of interest
a = 2.0

# Calculate the function value at a
fa = f(a)

# Generate x values
x = np.linspace(a - 1, a + 1, 400)
y = f(x)

fig, ax = plt.subplots()

# Set figure size
fig.set_size_inches(6, 8)

# Label the axes
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Plot the function
line, = ax.plot(x, y)

# Initial delta and epsilon
delta = [1]
epsilon = [0.04]

# Plot the point at 'a'
point, = ax.plot(a, fa, 'ro')

# Delta lines
d_line1, = ax.plot([a - delta[0], a - delta[0]], [fa - epsilon[0], fa + epsilon[0]], 'r--')
d_line2, = ax.plot([a + delta[0], a + delta[0]], [fa - epsilon[0], fa + epsilon[0]], 'r--')

# Epsilon lines
e_line1, = ax.plot([a - delta[0], a + delta[0]], [fa - epsilon[0], fa - epsilon[0]], 'g--')
e_line2, = ax.plot([a - delta[0], a + delta[0]], [fa + epsilon[0], fa + epsilon[0]], 'g--')

# Annotations for values
delta_text = ax.text(0.02, 0.9, '', transform=ax.transAxes)
epsilon_text = ax.text(0.02, 0.85, '', transform=ax.transAxes)

# Annotations for lines
delta_line_text = ax.text(a - delta[0]/2, fa + epsilon[0]/2, '$\delta$', color='red')
epsilon_line_text = ax.text(a + delta[0]/2, fa - epsilon[0]/2, '$\epsilon$', color='green')

# Epsilon-delta definition of a continuous function
definition_text = ax.annotate(r'For any $\epsilon > 0$, there exists $\delta > 0$ such that'
                              '\n$|f(x) - f(a)| < \epsilon$ whenever $0 < |x - a| < \delta$',
                              xy=(0.5, 0.92), xycoords='axes fraction',
                              ha='center', va='top', fontsize=10, bbox=dict(boxstyle='round', fc='white'))

# Add your name in the header
header_text = ax.text(0.5, 1.10, 'Basic Characteristic of Continuous Function f(x) = x^2, x ∈ [1, 3]\nby Deepak Bastola',
                      transform=ax.transAxes, ha='center', va='top', fontsize=12)

def animate(i):
    # Update delta and epsilon values
    if delta[0] > 0.01:
        delta[0] -= 0.01
    else:
        delta[0] = 1.0

    # Limit epsilon to a maximum value of 2
    if epsilon[0] < 2:
        epsilon[0] += 0.01

    # Update x values
    x = np.linspace(a - delta[0], a + delta[0], 400)
    y = f(x)

    # Update the function
    line.set_data(x, y)

    # Update delta lines with sinusoidal motion
    d_line1.set_data([a - delta[0] * np.sin(i / 10), a - delta[0] * np.sin(i / 10)], [fa - epsilon[0], fa + epsilon[0]])
    d_line2.set_data([a + delta[0] * np.sin(i / 10), a + delta[0] * np.sin(i / 10)], [fa - epsilon[0], fa + epsilon[0]])

    # Update epsilon lines
    e_line1.set_data([a - delta[0], a + delta[0]], [fa - epsilon[0], fa - epsilon[0]])
    e_line2.set_data([a - delta[0], a + delta[0]], [fa + epsilon[0], fa + epsilon[0]])

    # Update annotations
    delta_text.set_text(r'$\delta$ = %.2f' % delta[0])
    epsilon_text.set_text(r'$\epsilon$ = %.2f' % epsilon[0])
    
    # Update line annotations
    delta_line_text.set_position((a - delta[0] * np.sin(i / 10)/2, fa + epsilon[0]/2))
    epsilon_line_text.set_position((a + delta[0] * np.sin(i / 10)/2, fa - epsilon[0]/2))

    return line, point, d_line1, d_line2, e_line1, e_line2, delta_text, epsilon_text, delta_line_text, epsilon_line_text, definition_text

# Set the new animation style
style.use('fast')

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=200, blit=True)

# Adjust the plot layout to make room for the definition text
plt.subplots_adjust(top=0.85)

# Save the animation as a GIF file
# ani.save(r'C:\Users\dbastola2022\Desktop\animation.gif', writer='pillow')

plt.show()
