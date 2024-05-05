from glitch_ctrl import GlitchController
from glitch_ctrl import TriggerConfiguration
from time import sleep
import time
from random import randint

from dut import DuT
from time import sleep
import time

dut = DuT()
dut.reset()
glitcher = GlitchController()
edge = TriggerConfiguration.TRIGGER_EXTERNAL_FALLING_EDGE

while True:
    for i in range(56,100):
        for j in range(60,66):    
            glitcher.reset()
            glitcher.pulse_offset = i
            glitcher.pulse_width = j
            glitcher.trigger_on = edge
            sum = dut.read_sum()
            print(f" width:{j} offset:{i} sum:{sum}")               



