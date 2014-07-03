# -*- coding: UTF-8 -*-

from PyQt4.QtCore import *
import collections

threads = []


class Thread(QThread):
    global threads
    ACTION_SETATTR = 0
    ACTION_CALL    = 1
    ACTION_GETLIST = 2
    ACTION_GETDICT = 3
    def __init__(self, func):
        QThread.__init__(self)

        self.thr_func = func
        self.thr_stopFlag = False
        self.connect(self, SIGNAL('fromMainThread(PyQt_PyObject, PyQt_PyObject)'),
                     self._fromMainThread, Qt.QueuedConnection)
        self.connect(self, SIGNAL('fromMainThreadBlocking(PyQt_PyObject, PyQt_PyObject)'),
                     self._fromMainThread, Qt.BlockingQueuedConnection)
        self.connect(self, SIGNAL('finished()'), self._removeThread)

    def run(self):
        self.thr_func(self, *self.thr_args)

    def __call__(self, instance, *args, **kwargs):
        self.thr_instance = instance
        self.thr_args = args

        if kwargs.get('thr_start'):
            self.start()

    def __getattr__(self, name):
        if name.startswith('thr_'):
            return self.__dict__[name]

        attr = self.thr_instance.__getattribute__(name)
        if callable(attr):
            self.thr_lastCallFunc = self.thr_instance.__class__.__dict__[name]
            return self._callFunc
        elif type(attr) in (list, dict):
            self.emit(SIGNAL('fromMainThreadBlocking(PyQt_PyObject, PyQt_PyObject)'),
                      self.ACTION_GETLIST if type(attr) == list else self.ACTION_GETDICT,
                      name)
            return self.thr_result
        elif isinstance(attr, collections.Hashable):
            return attr
        else:
            raise(TypeError('unhashable type: %s' % type(attr).__name__))

    def __setattr__(self, name, value):
        if name.startswith('thr_'):
            self.__dict__[name] = value
        else:
            self.thr_instance.__setattr__(name, value)
            self.emit(SIGNAL('fromMainThreadBlocking(PyQt_PyObject, PyQt_PyObject)'), self.ACTION_SETATTR, (name, value))

    def _callFunc(self, *args, **kwargs):
        method = kwargs.get('thr_method')
        if not method:
            return self.thr_lastCallFunc(self, *args)
        if method == 'q':
            self.emit(SIGNAL('fromMainThread(PyQt_PyObject, PyQt_PyObject)'),
                      self.ACTION_CALL, (self.thr_lastCallFunc, args))
            return
        if method == 'b':
            self.emit(SIGNAL('fromMainThreadBlocking(PyQt_PyObject, PyQt_PyObject)'),
                      self.ACTION_CALL, (self.thr_lastCallFunc, args))
            return self.thr_result

    def _fromMainThread(self, action, value):
        if action == self.ACTION_SETATTR:
            self.thr_instance.__setattr__(*value)
        elif action == self.ACTION_CALL:
            func, arg = value
            self.thr_result = func(self.thr_instance, *arg)
        elif action == self.ACTION_GETLIST:
            self.thr_result = self.thr_instance.__getattribute__(value)[:]
        elif action == self.ACTION_GETDICT:
            self.thr_result = self.thr_instance.__getattribute__(value).copy()

    def thr_stop(self):
        self.disconnect(self, SIGNAL('fromMainThread(PyQt_PyObject, PyQt_PyObject)'), self._fromMainThread)
        self.disconnect(self, SIGNAL('fromMainThreadBlocking(PyQt_PyObject, PyQt_PyObject)'), self._fromMainThread)
        self.thr_stopFlag = True

    def _removeThread(self):
        threads.remove(self)

def SimpleThread(func):
    """Simple thread decorator

Exmaple:
class Foo(QLabel):
    def __init__(self, parent = None):
        QLabel.__init__(self, parent)
        self.setFixedSize(320, 240)
        self.digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

    @SimpleThread
    def bar(self, primaryText):
        rows = []
        digits = self.digits
        for item in digits:
            rows.append('%s: %s' % (primaryText, item))
            self.setText('\n'.join(rows), thr_method = 'b')
            sleep(0.5)
            
    def setText(self, text):
        QLabel.setText(self, text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    foo = Foo()
    foo.show()
    foo.bar('From thread', thr_start = True)
    app.exec_()"""

    def wrapper(*args, **kwargs):
        global threads
        thread = Thread(func)
        thread(*args, **kwargs)
        threads.append(thread)
        return thread
    return wrapper

def closeThreads():
    """Close all threads"""
    for thread in threads:
        thread.thr_stop()
    for thread in threads:
        thread.wait()

def terminateThreads():
    for thread in threads[:]:
        thread.terminate()