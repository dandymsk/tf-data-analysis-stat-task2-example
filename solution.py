import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 841977 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    n = len(x)
    lambda_hat = x.sum() / (n * 46)
    alpha = 1 - p
    loc = x.mean()
    scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
    return lambda_hat
