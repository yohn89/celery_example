#encoding:utf-8
import gevent
from tasks import add
import sys


def do(n=10000):
    """
    异步执行1w个add任务

    """

    for i in xrange(0, n):
        res = add.apply_async([i, 0])
        sys.stdout.write('\r{}:{}%,{},{}'.format(n, 100 * i/n, i, res.id))
        sys.stdout.flush()

    sys.stdout.write('\n done!')


if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser()

    parser.add_option("-n","--num", action="store", dest="num",
                      default=1, help="how many tasks you want to do?", type='int')


    options,args = parser.parse_args()
    do(options.num)


