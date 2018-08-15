
import os
import sys

print (os.path.abspath(__file__))

print (os.path.dirname(os.path.abspath(__file__)))

print (os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


print(sys.path)

from conf import settings

settings.options()

from modes import main

main.hello()