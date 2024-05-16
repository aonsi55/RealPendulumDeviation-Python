# RealPendulumDeviation-Python
In this code we are trying to stimulate the motion of a real Pendulum without using small angle approximatiton.

First we proceed by stating the force acting on the pendulum strings, and the direction of those forces, and by applying equation of motions, we derive the required equation that should be solved to represent a real pendulum. So far, this equation can represent the position of the bob through any time interval $t$, but yet this is not absolutely real pendulum, where we are not accounting for air resistance. But however, this still a good insights for understanding the deviation between a simple pendulum (small angle approximation) and a real pendulum.

It must be noted that a polar coordinates is used to approach this problem, as it makes it much easier to focus on a single parameter $\theta$, rather than the $x$ and $y$ coordinates.

# Equation of Motion for a Real Pendulum Using Polar Coordinates

To describe the motion of a real pendulum using polar coordinates, we consider a simple pendulum consisting of a mass $m$ attached to a string of length $l$ that swings under the influence of gravity. The equation is derived in terms of the angular displacement $\theta$.

## Assumptions and Setup

- **Pendulum Length** $l$: The length of the string is constant.
- **Mass** $m$: The mass at the end of the string.
- **Gravity** $g$: The acceleration due to gravity.
- **Angular Displacement** $\theta$: The angle the pendulum makes with the vertical.

## Coordinate System

In polar coordinates, the position of the mass can be described by:
- Radial distance $r = l$ (constant).
- Angular position $\theta$.

## Forces on the Pendulum

- **Tension** $T$ in the string, acting along the length of the string (radial direction).
- **Gravitational Force** $mg$, acting vertically downward.

## Components of Forces

To find the forces in polar coordinates, we resolve the gravitational force into radial and tangential components relative to the pendulum’s motion.

- **Radial Component**: $-mg \cos\theta$
- **Tangential Component**: $-mg \sin\theta$

## Equations of Motion

Using Newton's second law in polar coordinates:

### Radial Direction

In the radial direction, the centripetal force required for circular motion is provided by the tension $T$ and the radial component of gravity:
$$T - mg \cos\theta = m\left( -\frac{d^2r}{dt^2} + r\left(\frac{d\theta}{dt}\right)^2 \right)$$

Since $r = l$ is constant:
$$\frac{d^2r}{dt^2} = 0$$
$$T = mg \cos\theta + ml \left( \frac{d\theta}{dt} \right)^2$$

### Tangential Direction

In the tangential direction, the tangential component of gravity causes angular acceleration:
$$-mg \sin\theta = m l \frac{d^2\theta}{dt^2}$$

## Simplifying the Tangential Equation

Rearrange to solve for the angular acceleration:
$$\frac{d^2\theta}{dt^2} + \frac{g}{l} \sin\theta = 0$$

This is the nonlinear differential equation describing the motion of a simple pendulum.

## Small Angle Approximation

For small angular displacements $\theta \approx 0$, $\sin\theta \approx \theta$. The equation simplifies to:
$$\frac{d^2\theta}{dt^2} + \frac{g}{l} \theta = 0$$

This is the equation of a simple harmonic oscillator with the general solution:
$$\theta(t) = \theta_0 \cos\left( \sqrt{\frac{g}{l}} t + \phi \right)$$

where $\theta_0$ is the maximum angular displacement and $\phi$ is the phase constant determined by initial conditions.

## Full Nonlinear Equation

For larger angles where the small angle approximation does not hold, the equation:
$$\frac{d^2\theta}{dt^2} + \frac{g}{l} \sin\theta = 0$$
must be solved, which typically requires numerical methods or more advanced analytical techniques such as elliptic integrals.

## Conclusion

The motion of a real pendulum using polar coordinates is governed by:
$$\frac{d^2\theta}{dt^2} + \frac{g}{l} \sin\theta = 0$$

This second-order nonlinear differential equation describes the angular motion of the pendulum and is foundational in understanding the dynamics of pendular systems in both simple and complex contexts.

And at the end we show the graphics, which show the difference between the real pendulum and simple pendulum, 


