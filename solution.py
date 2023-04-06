import numpy as np
from scipy.stats import gamma

chat_id = 834411281

def solution(p: float, x: np.array) -> tuple:
    left = 2 / 86 ** 2 * (gamma.ppf((1 - p) / 2, x.size) / x.size + x.mean() - 1 / 2)
    right = 2 / 86 ** 2 * (gamma.ppf((1 + p) / 2, x.size) / x.size + x.mean() - 1 / 2)
    return left, right
