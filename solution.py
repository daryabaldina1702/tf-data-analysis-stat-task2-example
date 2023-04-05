import pandas as pd
import numpy as np
from scipy.stats import norm
from scipy.stats import t

chat_id = 834411281 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
   n = len(x)
   mean = np.mean(x)
   std_error = np.std(x, ddof=1) / np.sqrt(n)  # стандартная ошибка среднего
   t_val = t.ppf(1 - p / 2, n - 1)  # t-значение
   left = mean - t_val * std_error
   right = mean + t_val * std_error
   return (left, right)
