import mraa
import rotary_encoder as renc


class EncoderEC11:
    def __init__(self):
        self._enc = None
        self.old_position = 0

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
    def __init__(self):
        pass

    def encode(self, pin):
        self._pin = pin
        self.pin = mraa.Gpio(pin)
        self.pin.dir(mraa.DIR_IN)

    @property
    def n_pin(self):
        return self._pin

    def isr(self):
        self.pin.isr(mraa.EDGE_RISING, self.b_routine, self.n_pin)

    @staticmethod
    def b_routine(gpio):
        print(gpio)
