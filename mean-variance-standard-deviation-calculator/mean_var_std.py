import numpy as np

def calculate(li):
    if len(li) < 9:
        raise ValueError("List must contain nine numbers.")
    else:
        arr = np.array(li, dtype='int')
        arr = arr.reshape(3,3)
        mean0, mean1, mean_flattened = arr.mean(axis=0), arr.mean(axis=1), arr.mean()
        variance0, variance1, variance_flattened = arr.var(axis=0), arr.var(axis=1), arr.var()
        sd0, sd1, sd_flattened = arr.std(axis=0), arr.std(axis=1), arr.std()
        max0, max1, max_flattened = arr.max(axis=0), arr.max(axis=1), arr.max()
        min0, min1, min_flattened = arr.min(axis=0), arr.min(axis=1), arr.min()
        sum0, sum1, sum_flattened = arr.sum(axis=0), arr.sum(axis=1), arr.sum()
        calculations = {
        }
        calculations['mean'] = [list(mean0), list(mean1), mean_flattened]
        calculations['variance'] = [list(variance0), list(variance1), variance_flattened]
        calculations['standard deviation'] = [list(sd0), list(sd1), sd_flattened]
        calculations['max'] = [list(max0), list(max1), max_flattened]
        calculations['min'] = [list(min0), list(min1), min_flattened]
        calculations['sum'] = [list(sum0), list(sum1), sum_flattened]
        return calculations