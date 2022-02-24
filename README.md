# ssd1306

## Notes on using ssd1306 oled display on rockpis

Activate I2C protocol modifying file `/boot/uEnv.txt`. In that file adding these lines:

```bash
overlay_prefix=rockchip
rootfstype=ext4
```

and adding to the key `overlays` the following value:

`rk3308-i2c1`

entire line will appear as:

```bash
overlays=rk3308-console-on-uart0  rk3308-i2c1
```

Install dependencies dependencies (probably as `sudo`):

```bash
pip3 install Adafruit-Blinka 
pip3 install adafruit-circuitpython-ssd1306
pip3 install Pillow
```

Oled ssd1306 has 4 pin: GND, VCC, SDA, SCL, connect it to rockpis following this table:

| rockpis | ssd1306 |
| ------- | ------- |
| 1       | 3.3V    |
| 3       | SCL     |
| 5       | SDA     |
| 6       | GND     |