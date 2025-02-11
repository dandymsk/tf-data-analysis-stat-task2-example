import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 841977 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    n = len(x)
    alpha = 1 - p
    loc = 2 * x.mean() / 50 ** 2
    scale = np.sqrt(4 / (x.mean() ** 2 * n))
    return loc - scale * norm.ppf(1 - alpha / 2), \
           loc - scale * norm.ppf(alpha / 2)
