from resolver import Resolver


resolve = Resolver()
resolve('sixty-north.com')
resolve.__call__('baidu.com')


# from timeit import timeit
# timeit(setup="from __main__ import resolve", stmt="resolve('google.com')",number=1)
# print("{:f}".format(_))
