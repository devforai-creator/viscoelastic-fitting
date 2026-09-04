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

k_estimated, intercept = np.polyfit(
    x_values, 
    F_values, 
    1
)

F_fitted = k_estimated * x_values + intercept

residuals = F_values - F_fitted

ss_res = np.sum(residuals ** 2)

ss_tot = np.sum(
    (F_values - np.mean(F_values)) ** 2
)

r_squared = 1 - ss_res / ss_tot

print(f"Estimated k = {k_estimated:.2f} N/m (true k: 200.00N/m)")
print(f"Intercept = {intercept:.3f} N")
print(f"R^2 = {r_squared:.5f}")