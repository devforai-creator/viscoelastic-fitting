import numpy as np

data = np.loadtxt(
    "viscoelastic_test.csv",
    delimiter=",",
    skiprows=1
)

time_values = data[:, 0]
x_values = data[:, 1]
F_values = data[:, 2]
k_true = 200.00 
c_true = 30.00
## estimate_kx_only.py 참조
r_squared_kx_only = 0.77688

print(f"Loaded {len(time_values)} rows")

x_dot = np.gradient(x_values, time_values)

design_matrix = np.column_stack((x_values, x_dot))

k_estimated, c_estimated = np.linalg.lstsq(design_matrix, F_values, rcond=None)[0]

k_error = k_estimated - k_true 
c_error = c_estimated - c_true

k_relative_error = k_error / k_true * 100
c_relative_error = c_error / c_true * 100

F_fitted = k_estimated * x_values + c_estimated * x_dot
residual_full = F_values - F_fitted

ss_res_full = np.sum(residual_full ** 2)
ss_tot_full = np.sum((F_values - np.mean(F_values)) ** 2)

r_squared_full = 1 - ss_res_full/ss_tot_full

print(f"Estimated_k: {k_estimated:.2f} N/m (true k: {k_true:.2f} N/m)")
print(f"Estimated_c: {c_estimated:.2f} N*s/m (true c: {c_true:.2f} N*s/m)")

print(f"k_error: {k_error:.6f} N/m ({k_relative_error:.6f} %)")
print(f"c_error: {c_error:.6f} N*s/m ({c_relative_error:.6f} %)")

print(f"R^2: {r_squared_full:.5f} (F = kx only: {r_squared_kx_only:.5f})")