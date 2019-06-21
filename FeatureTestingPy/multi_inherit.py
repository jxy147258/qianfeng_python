# -*- coding: utf-8 -*-

class flyable(object):
    def fly(self):
        print('I can fly')

class runnable(object):
    def run(self):
        print('i can run')
    def fly(self):
        print('I can\'t fly')

class dog(flyable,runnable):
    def run(self):
        print('dog can run')

dog1=dog()
dog1.run()

dog1.fly()
#import os
#
#print(help(os.access))