#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 20:23:08 2020

@author: fardeenmeeran
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 14:16:16 2020

@author: fardeenmeeran
"""
from pygame import mixer
from subprocess import Popen, PIPE
pipe = Popen("pmset -g ps", shell=True, stdout=PIPE).stdout
output = pipe.read().decode('utf-8')
print(output)
while "Battery Power" in output:
    pipe2 = Popen("pmset -g ps", shell=True, stdout=PIPE).stdout
    output2 = pipe2.read().decode('utf-8')
    if "AC Power" in output2 :
        mixer.init()
        mixer.music.load('/Users/fardeenmeeran/Desktop/xyz.mp3')
        mixer.music.play()
        break
    
    
