import pandas as pd
import numpy as np
from scipy.stats import t

chat_id = 834411281 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    n = len(x)
    time = 86
    alpha = 1 - p
    a = np.abs(2 * x / time**2 + 0.5 - np.random.exponential(1, n))
    mean = np.mean(a) #среднее выборки
    s = np.std(a, ddof=1)
    SE = s / np.sqrt(n)
    t_value = t.ppf(1 - alpha/ 2, n - 1)
    lower_bound = mean - t_value * SE
    upper_bound = mean + t_value * SE
    return (lower_bound, upper_bound)
