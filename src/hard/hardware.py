import mraa
from hard import rotary_encoder as renc
from soft import rock_logger as log


class EncoderEC11:
    def __init__(self, pin1, pin2):
        self._enc = None
        self.old_position = 0
        self.encode(pin1, pin2)

    @property
    def enc(self):
        return self._enc

    @property
    def direction(self):
        return self._enc.get_direction()

    @property
    def position(self):
        return self._enc.get_position()

    def encode(self, p1, p2):
        self.pin1 = mraa.Gpio(p1)
        self.pin2 = mraa.Gpio(p2)
        self.pin1.dir(mraa.DIR_IN)
        self.pin2.dir(mraa.DIR_IN)
        self._enc = renc.RotaryEncoder(
            self.pin1, self.pin2, renc.LATCHMODE['FOUR3'])

    def tick(self):
        self._enc.tick()

    def isr(self):
        self.pin1.isr(mraa.EDGE_BOTH, self.routine, self._enc)
        self.pin2.isr(mraa.EDGE_BOTH, self.routine, self._enc)

    def refresh(self):
        self.tick()
        new_pos = self.position

        if self.old_position != new_pos:
            self.old_position = new_pos
            return self.direction

        return None

    @staticmethod
    def routine(args):
        args.tick()


class RockButton:
    def __init__(self, pin):
        self.encode(pin)

    def encode(self, pin):
        self._pin = pin
        self.button = mraa.Gpio(pin)
        self.button.dir(mraa.DIR_IN)
        log.INFO(f"{self.button}")

    @property
    def n_pin(self):
        return self._pin

    def isr(self, routine, arg):
        self.button.isr(mraa.EDGE_RISING, routine, arg)
