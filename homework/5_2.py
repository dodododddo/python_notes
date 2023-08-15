from functools import reduce
import logging

def outstand(*args)->(float, list):
    '''
    输入任意个参数，返回其平均值与高于其平均值的元素组成的列表
    '''
    if not len(args):
        logging.error('参数数量小于1')
        return None, None
    avg = reduce(lambda x, y: x + y, args) / len(args)
    res = list(filter(lambda x: x > avg, args))
    # res = [arg for arg in args if arg > avg]
    return avg, res


if __name__ == '__main__':
    avg, res = outstand(1, 2, 3, 4, 5)
    print(f'avg = {avg}, res = {res}')
    _, _ = outstand()
    