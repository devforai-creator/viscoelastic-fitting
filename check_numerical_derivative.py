import numpy as np

data = np.loadtxt(
    "viscoelastic_test.csv",
    delimiter=",",
    skiprows=1
)

time_values = data[:, 0]
x_values = data[:, 1]
F_values = data[:, 2]

print(f"Loaded {len(time_values)} rows")

amplitude = 0.03
period = 2.0

x_dot_numerical = np.gradient(x_values, time_values)
x_dot_analytic = amplitude * (np.pi / period) * np.cos(np.pi * time_values / period)
absolute_errors = np.abs(x_dot_numerical - x_dot_analytic)

print(f"x_dot numerical (t=0.00): {x_dot_numerical[0]:.6f} analytic: {x_dot_analytic[0]:.6f}")
print(f"x_dot numerical (t=1.00): {x_dot_numerical[50]:.6f} analytic: {x_dot_analytic[50]:.6f}")
print(f"Max absolute error: {np.max(absolute_errors):.6f}")
print(f"Mean absolute error: {np.mean(absolute_errors):.6f}")