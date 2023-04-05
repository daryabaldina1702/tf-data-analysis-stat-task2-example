import pandas as pd
import numpy as np
from scipy.stats import norm
from scipy.stats import t

chat_id = 834411281 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
   n = len(x)
   time = 86
   mean_distance = np.mean(x)
   variance = 0.5
   sum_sq_deviation = np.sum((x - mean_distance) ** 2)
   variance_acceleration = (2 * variance * sum_sq_deviation) / ((n - 1) * time ** 2)
   std_error_acceleration = np.sqrt(variance_acceleration)
   t_stat = norm.ppf((1 + p) / 2, n - 1)
   lower_bound = mean_distance - t_stat * std_error_acceleration
   upper_bound = mean_distance + t_stat * std_error_acceleration
   return (lower_bound, upper_bound)
