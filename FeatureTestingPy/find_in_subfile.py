"""
auth = jxy17258@gmail.com
Link = www.jichen-info.com

"""

import os

pwd1 = os.path.abspath('.')

for f in os.listdir(pwd1):
    if os.path.isdir(f):
        print(os.path.dirname(f))
        for f1 in os.listdir(f):
            pass
    else :
        if os.path.split():
            pass

