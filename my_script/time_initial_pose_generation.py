import os
import time
from functools import wraps

def timethis(func):
    """
    Decorator that reports the execution time.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, (end-start)/60)
        return result
    return wrapper

@timethis
def protac_invent():
    cmd = 'python /data/baiqing/PycharmProjects/Reinvent-master-3.2/input.py initial_pose_generate.json'
    os.system(cmd)
    print()

if __name__ == '__main__':
    base_dir = '/data/baiqing/PycharmProjects/Reinvent-master-3.2/result/LINK_invent'

    name_list = ['5T35',
                 '6BN7',
                 '6BOY',
                 '6HAY',
                 '6HR2',
                 '6W7O',
                 '6ZHC',
                 '7JTO',
                 '7JTP',
                 '7KHH',
                 '7Q2J',
                 'BRD9',
                 'BTK',
                 'BAF']

    for name in name_list:
        print(name)
        work_dir = os.path.join(base_dir, name)
        os.chdir(work_dir)
        protac_invent()
