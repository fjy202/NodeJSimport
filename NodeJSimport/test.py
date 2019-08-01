import unittest,js2py.internals.simplex
import NodeJSimport,importlib
import sys
class testjsimport(unittest.TestCase):
    def test_install(self):
        NodeJSimport.install()
        import testjs
        del testjs
    def test_jsrunthrow(self):
        import testjs
        with self.assertRaises(js2py.internals.simplex.JsException):
            testjs.test_throw()
    def test_jsrun(self):
        import testjs
        self.assertEqual(testjs.test_run(),"running")
    def test_uninstall(self):
        NodeJSimport.uninstall()
        del sys.modules["testjs"]
        try:
            import testjs
        except ModuleNotFoundError:
            pass
        else:
            self.fail()