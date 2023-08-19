import time
import numpy as np
import unittest

class Timer(object):
    num = 0
    
    def __init__(self):
        Timer.num += 1
        if Timer.num > 20:
            raise ValueError('同时存在太多实例对象')
        self.times = []
        self.start()
    
    def __del__(self):
        Timer.num -= 1

    def start(self):
        self.tik = time.time()
    
    def stop(self):
        self.times.append(time.time() - self.tik)
        return self.times[-1]
    
    def avg(self):
        return sum(self.times) / len(self.times)
    
    def sum(self):
        return sum(self.times)
    
    def cumsum(self):
        return np.array(self.times).cumsum().tolist()


class TimerTest(unittest.TestCase):
    def test_timer(self):
        timers = []
        for i in range(10):
            timer = Timer()
            timers.append(timer)
            time.sleep(1)
            self.assertIsInstance(timer.stop(), float)
            self.assertIsInstance(Timer.num, int)

    def test_avg(self):
        timer = Timer()
        timer.start()
        time.sleep(1)
        timer.stop()
        self.assertAlmostEqual(timer.avg(), 1, delta = 0.01)

    def test_sum(self):
        timer = Timer()
        timer.start()
        time.sleep(1)
        timer.stop()
        self.assertAlmostEqual(timer.sum(), 1, delta=0.01)

    def test_cumsum(self):
        timer = Timer()
        timer.start()
        time.sleep(1)
        timer.stop()
        self.assertAlmostEqual(timer.cumsum()[0], 1, delta=0.01)

if __name__ == '__main__':
    unittest.main()
    