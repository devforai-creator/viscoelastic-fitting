import numpy as np

k_true = 200.0
c_true = 30.0
amplitude = 0.03
period = 2.0

time_values = np.linspace(
    0.0,
    period,
    101
)

x_values = amplitude * np.sin(np.pi * time_values / period)

x_dot_values = amplitude * (np.pi / period) * np.cos(np.pi * time_values / period)

F_values = k_true * x_values + c_true * x_dot_values

rng = np.random.default_rng(42)
F_values = F_values + rng.normal(0.0, 0.02, F_values.shape)

table = np.column_stack(
    (time_values, x_values, F_values)
)

np.savetxt(
    "viscoelastic_test.csv",
    table,
    delimiter=",",
    header="time_s, displacement_m, force_N",
    comments="",
    fmt="%.10f"
)

print("Saved viscoelastic_test.csv")
print(f"True k: {k_true:.2f} N/m, True c: {c_true:.2f} N*s/m")