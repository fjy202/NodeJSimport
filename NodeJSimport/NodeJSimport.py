import js2py
import sys
import os
from importlib._bootstrap import ModuleSpec
class module_wrapper(type(sys)):
    def __init__(self, obj, loader,name,spec):
        self.__object=obj
        self.__package__=self
        self.__loader__=loader
        self.__name__=name
        self.__spec__=spec
    def __getattr__(self, attr):
        return self.__object.__getattr__(attr)
        
def find(name,path):
    if not name:
        return path+"/__init__.js"
    if os.path.isfile(path+"/"+name[0]+".js"):
        return path+"/"+name[0]+".js"
    elif os.path.isdir(path+"/"+name[0]):
        return find(name[1:],path+"/"+name[0])
    else:
        return None
class NJSFinder:
    def find_spec(self,fullname,path=None,a=None):
        fname=fullname.split(".")
        for path in sys.path:
            x=find(fname,path)
            if x!=None:
                spec=ModuleSpec(fullname,None,origin=x)
                obj=NJSLoader(x,spec)
                spec.loader=obj
                return spec
        return None
class NJSLoader:
    def __init__(self,path,spec):
        self.path=path
        self.spec=spec
    def load_module(self,fullname):
        env=js2py.EvalJs({},True)
        with open(self.path) as f:
            env.execute(f.read())
        mod=module_wrapper(env,type(self),fullname,self.spec)
        sys.modules[fullname]=mod
        return mod
inst=NJSFinder()
def install():
    sys.meta_path.append(inst)
def uninstall():
    sys.meta_path.remove(inst)