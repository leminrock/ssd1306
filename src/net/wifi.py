#!/usr/bin/env python3

import nmcli


def _scan():
    return nmcli.device.wifi()


def get_names():
    ssids = _scan()
    names = [(x.in_use, x.ssid, x.signal) for x in ssids]
    return names


def format_names(names):
    TOTAL = 47
    strings = []

    for in_use, ssid, signal in names:
        if in_use:
            pre = ' * '
        else:
            pre = '   '
        length = len(ssid)
        strings.append(pre + ssid + str(signal).rjust(TOTAL - length))

    return strings


class SSID:
    def __init__(self, name):
        self._name = name
        self._password = None

    @property
    def password(self):
        return '*' * len(self._password)

    @password.setter
    def password(self, password):
        self._password = password


class ScanList:
    def __init__(self):
        self.scan_list = []

    def append_ssid(self, ssid):
        self.scan_list.append(ssid)

    def extend(self, ssids):
        self.scan_list.extend(ssids)
