
def tets_(test):
    import time
    time_fomat = "%Y-%m-%d-%H:%M:%S"
    def echo_(*args,**kwargs):
        print(time.strftime(time_fomat,time.localtime())+"<---运维测试demo---><==========>调用接口<==========>[INFO]:'{fund}()'".format(fund=test.__name__))
        return tets_(*args,**kwargs)
    return echo_

class Message:
    @tets_
    def v1_debus(self):
        print("输出web调用-01")
