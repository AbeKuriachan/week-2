
import numpy as np

rng = np.random.default_rng(1313)

# ── Task 1: Generate dataset (50, 24, 3) ─────────────────────────────────
temp     = rng.uniform(15, 45,  (50, 24))
humidity = rng.uniform(20, 95,  (50, 24))
battery  = rng.uniform(10, 100, (50, 24))
data = np.stack([temp, humidity, battery], axis=2)   # (50, 24, 3)
print("Dataset shape:", data.shape)


# ── Task 2: Alert sensors — temp > 40C OR humidity > 90% in any hour ─────
alert_mask    = (data[:, :, 0] > 40) | (data[:, :, 1] > 90)  # (50, 24) bool
alert_sensors = np.where(alert_mask.any(axis=1))[0]           # reduce over hours
print(f"Alert sensors: {alert_sensors.tolist()[:8]} ... ({len(alert_sensors)} total)")


# ── Task 3: Per-sensor daily averages (axis=1 → collapse hours) ──────────
daily_avg = data.mean(axis=1)   # (50, 3)
print("Daily avg shape:", daily_avg.shape)
print("Sample (sensor 0): temp={:.1f}C  hum={:.1f}%  bat={:.1f}%".format(*daily_avg[0]))


# ── Task 4: Hottest hour — mean across sensors then argmax ───────────────
hourly_temp = data[:, :, 0].mean(axis=0)   # (24,) mean over 50 sensors
hottest_hour = hourly_temp.argmax()
print(f"Hottest hour: {hottest_hour} ({hottest_hour}:00)")


# ── Task 5: Battery drain (first hour − last hour), flag > 50% ───────────
battery_drain  = data[:, 0, 2] - data[:, -1, 2]   # (50,)
critical_drain = np.where(battery_drain > 50)[0]
print(f"Critical battery drain sensors (>50%): {critical_drain.tolist()}")


# ── Task 6: Min-max normalise per metric using broadcasting ──────────────
col_min  = data.min(axis=(0, 1))   # (3,) global min per metric
col_max  = data.max(axis=(0, 1))   # (3,) global max per metric
norm     = (data - col_min) / (col_max - col_min)
# col_min/col_max shape (3,) broadcasts against (50, 24, 3)
print(f"Normalised range: [{norm.min():.4f}, {norm.max():.4f}]")


# ── Task 7: Save daily averages to CSV ───────────────────────────────────
np.savetxt(
    "sensor_summary.csv",
    daily_avg,
    delimiter=",",
    header="temperature,humidity,battery",
    comments=""
)
print("Saved: sensor_summary.csv — 50 rows × 3 columns")
