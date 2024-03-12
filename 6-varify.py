from glitch_ctrl import GlitchController, TriggerConfiguration
from dut import DuT

class Verify:
    def __init__(self):
        self.offset = 2240
        self.width = 14

        self.dut = DuT()
        self.dut.reset()

        self.glitcher = GlitchController()
        self.glitcher.reset()
        self.edge = TriggerConfiguration.TRIGGER_EXTERNAL_RISING_EDGE
    
    def trigger(self):
        self.glitcher.trigger_on = self.edge

if __name__ == "__main__":
    veri = Verify()
    veri.trigger()
    veri.dut.authorize(b"1234567890123456789012345678901234567890123456789012345678901234")
    print(f"status: {veri.dut.authorized}")


