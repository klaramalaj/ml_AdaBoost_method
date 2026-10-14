"""Shared skill scores for solar flare classification: TSS and HSS."""

import numpy as np
from sklearn.metrics import confusion_matrix


def tss(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """True Skill Statistic (Hanssen–Kuipers discriminant).

    TSS = TP / (TP + FN) - FP / (FP + TN)

    Assumes binary labels ``{0, 1}`` with ``1`` as the positive (flare) class.
    Ranges from -1 to 1 (1 is perfect). Returns ``nan`` if a denominator is zero.
    """
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred, labels=[0, 1]).ravel()
    denom_pos = tp + fn
    denom_neg = fp + tn
    if denom_pos == 0 or denom_neg == 0:
        return float("nan")
    return tp / denom_pos - fp / denom_neg


def hss(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """Heidke Skill Score.

    HSS = 2 * (TP * TN - FP * FN)
          / ((TP + FN) * (FN + TN) + (TP + FP) * (FP + TN))

    Assumes binary labels ``{0, 1}`` with ``1`` as the positive (flare) class.
    Ranges from -inf to 1 (1 is perfect; 0 is no skill vs chance).
    Returns ``nan`` if the denominator is zero.
    """
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred, labels=[0, 1]).ravel()
    numerator = 2 * (tp * tn - fp * fn)
    denominator = (tp + fn) * (fn + tn) + (tp + fp) * (fp + tn)
    if denominator == 0:
        return float("nan")
    return numerator / denominator
