# ML 4340 / 5340 — Final Project

Skeleton repository for the course final project. Each student works on **one** method below. The goal is to understand the method (theory) and apply it to **solar flare prediction** using the shared train / validation / test CSVs.

This repo provides structure only. You implement the investigation, supporting scripts, and write-up.

## Projects (one per student)

| Folder | Method |
|--------|--------|
| [`projects/01_decision_trees`](projects/01_decision_trees/) | Decision Trees / Random Forests |
| [`projects/02_svm`](projects/02_svm/) | Support Vector Machines |
| [`projects/03_adaboost`](projects/03_adaboost/) | AdaBoost |
| [`projects/04_gradient_boosting`](projects/04_gradient_boosting/) | Gradient Boosting |
| [`projects/05_mlp`](projects/05_mlp/) | Multilayer Perceptron (MLP) |
| [`projects/06_gaussian_processes`](projects/06_gaussian_processes/) | Gaussian Processes |

See [`projects/README.md`](projects/README.md) for objectives, milestones, and rubric.

## Per-project layout

Each assigned folder contains:

- `README.md` — short description of your task
- `theory_and_experiments.ipynb` — your presentation notebook (theory + experiment front-end)

Put reusable code (data loading, preprocessing, training helpers, metrics, etc.) in `.py` scripts and call them from the notebook. Shared utilities live under [`common/`](common/).

## Data

Place the instructor-provided files under [`data/`](data/):

- `train.csv`
- `validation.csv`
- `test.csv`

Do **not** invent your own train/validation/test split. Use the provided CSVs as given.

