# Data

The dataset is stored in this directory:

| File | Role |
|------|------|
| `p1_swansf.csv` | Training |
| `p2_swansf.csv` | Validation |
| `p3_swansf.csv` | Test |

Use these files as given. Do **not** invent your own train / validation / test splits.

## Columns (18)

Features:

- `TOTUSJH_median`, `TOTBSQ_median`, `TOTPOT_median`
- `TOTUSJH_min`, `TOTBSQ_min`, `TOTPOT_min`
- `TOTUSJH_max`, `TOTBSQ_max`, `TOTPOT_max`
- `TOTUSJH_std`, `TOTBSQ_std`, `TOTPOT_std`
- `TOTUSJH_last_value`, `TOTBSQ_last_value`, `TOTPOT_last_value`

Metadata / label:

- `label`: This contains the targests (1: flaring, 0: non-flaring)
- `start`: This contains the start-time of the events. Please do not use this in your models.
- `end`: This contains the end-time of the events. Please do not use this in your models.

Class imbalance is expected; how you handle it is specified in your project materials.
