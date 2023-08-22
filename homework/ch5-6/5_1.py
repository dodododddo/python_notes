import logging
from functools import reduce
logging.getLogger().setLevel(logging.INFO)

def agg(l:list, mode = 'median'):
    viable_modes = ['median', 'mean', 'max', 'majority']
    if not l or not isinstance(l, list):
        logging.error('仅支持非空列表')
        return None
    if mode not in viable_modes:
        logging.error('不支持该模式')
        return None
    if mode == 'median':
        l = sorted(l)
        length = len(l)
        if length % 2:
            return l[length // 2]
        else:
            return (l[length // 2] + l[length // 2 + 1]) / 2
    if mode == 'mean':
        return reduce(lambda x, y: x + y, l) / len(l)
    if mode == 'max':
        return max(l)
    if mode == 'majority':
        return max(l, key=l.count)
    

if __name__ == '__main__':
    
    l = [3,3,5,8,6]
    median = agg(l)
    mean = agg(l,'mean')
    maximum = agg(l, 'max')
    majority = agg(l, 'majority')
    _ = agg(l, 'balabala')
    _ = agg([])
    
    logging.info(f'median = {median}, mean = {mean}, maximum = {maximum}, majority = {majority}')