import js2py
import sys
import os
def find(name,path):
    if not name:
        return path+"/__init__.js"
    if os.isfile(path+"/"+name[0]+".js"):
        return path+"/"+name[0]+".js"
    elif os.isdir(path+"/"+name[0]):
        return find(name[1:],path+"/"+name[0])
    else:
        return None
class NJSFinder:
    def find_module(self,fullname,path=None):
        fname=fullname.split(".")
        for path in sys.path:
            x=find(fname,path)
            if x!=None:
                return NJSLoader(x)
        return None
class NJSLoader:
    def __init__(self,path):
        self.path=path
    def load_module(self,fullname):
        env=js2py.EvalJs({},True)
        env.execute(open(self.path).read())
        return env