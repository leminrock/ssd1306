import mraa


class EncoderEC11:
    def __init__(self):
        self._enc = None

    @property
    def enc(self):
        return self._enc

    def encode(self, p1, p2):
        self.pin1 = mraa.Gpio(p1)
        self.pin2 = mraa.Gpio(p2)
        self.pin1.dir(mraa.DIR_IN)
        self.pin2.dir(mraa.DIR_IN)
        self._enc = renc.RotaryEncoder(
            self.pin1, self.pin2, renc.LATCHMODE['FOUR3'])

    def tick(self):
        self._enc.tick()

    def isr(self, func):
        self.pin1.isr(mraa.EDGE_BOTH, rotary_routine, self.pin1)
        self.pin2.isr(mraa.EDGE_BOTH, rotary_routine, self.pin2)


def rotary_routine(gpio):
