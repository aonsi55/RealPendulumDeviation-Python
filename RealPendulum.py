import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the parameters for the pendulum
g = 9.81  # acceleration due to gravity, in m/s^2
l = 0.45  # length of the pendulum, in meters
theta0 = np.radians(30)  # initial angle (30 degrees), converted to radians
omega0 = 0.0  # initial angular velocity, in rad/s

# Define the equations of motion for the real pendulum
def real_pendulum_equations(t, y):
    theta, omega = y
    dtheta_dt = omega
    domega_dt = - (g / l) * np.sin(theta)
    return [dtheta_dt, domega_dt]

# Define the equations of motion for the simple pendulum using small angle approximation
def simple_pendulum_equations(t, y):
    theta, omega = y
    dtheta_dt = omega
    domega_dt = - (g / l) * theta
    return [dtheta_dt, domega_dt]

# Initial conditions
y0 = [theta0, omega0]

# Time span for the simulation
t_span = (0, 10)  # simulate for 10 seconds
t_eval = np.linspace(t_span[0], t_span[1], 500)  # reduce the number of frames

# Solve the differential equations
solution_real = solve_ivp(real_pendulum_equations, t_span, y0, t_eval=t_eval)
solution_simple = solve_ivp(simple_pendulum_equations, t_span, y0, t_eval=t_eval)

# Extract the results
theta_real = solution_real.y[0]
theta_simple = solution_simple.y[0]
t = solution_real.t

# Set up the figure and axis for the animation
fig, ax = plt.subplots()
ax.set_xlim(-l - 0.1, l + 0.1)
ax.set_ylim(-l - 0.1, l + 0.1)
ax.set_aspect('equal')
line_real, = ax.plot([], [], 'o-', lw=2, color='blue', label='Real Pendulum')
line_simple, = ax.plot([], [], 'o-', lw=2, color='red', label='Simple Pendulum')
ax.legend()

# Initialize the animation
def init():
    line_real.set_data([], [])
    line_simple.set_data([], [])
    return line_real, line_simple

# Update the animation at each frame
def update(frame):
    x_real = l * np.sin(theta_real[frame])
    y_real = -l * np.cos(theta_real[frame])
    line_real.set_data([0, x_real], [0, y_real])

    x_simple = l * np.sin(theta_simple[frame])
    y_simple = -l * np.cos(theta_simple[frame])
    line_simple.set_data([0, x_simple], [0, y_simple])

    return line_real, line_simple

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True, interval=20)

# Save the animation as a GIF
ani.save('double_pendulum.gif', writer='pillow', fps=20)

# Show the animation
plt.show()
