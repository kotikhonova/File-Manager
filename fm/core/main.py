import os

from runner import Runner

if __name__ == '__main__':
    runner = Runner()
    runner.parse_conf()
    runner.run()
