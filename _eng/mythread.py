import threading
from time import sleep

class myThread (threading.Thread):
    name = ""
    threadsToWait = []
    func = None
    args = ()
    kwargs = {}

    def __init__(self, name, functorun, threadstowait = [], argstouse = (), kwargstouse = {}):
        threading.Thread.__init__(self)
        self.func = functorun
        self.name = name
        self.threadsToWait = threadstowait
        self.args = argstouse
        self.kwargs = kwargstouse

    def run(self):

        # print("thread "+self.name+" start")
        if (len(self.threadsToWait)!= 0):
            for t in self.threadsToWait:
                t.join()
            # print("thread "+self.name+" stops waiting")
        else:
            pass
            # print("Nothing to wait")
        self.func(*self.args, **self.kwargs)
        # print("thread " +self.name+ " end" )
