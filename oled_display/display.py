import math
import time
import random
import os.path
from demo_opts import get_device
from luma.core.render import canvas
from PIL import Image, ImageFont

class CB650F_Display:
    def __init__(self, device):
        self.device = device

        font_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'fonts', 'HelveticaNeue.ttf'))

        self.font_10 = ImageFont.truetype(font_path, 10)
        self.font_48 = ImageFont.truetype(font_path, 48)

        self.gears = ['-', 'N', 'K', '1', '2', '3', '4', '5', '6']

        self.ect = 100
        self.iat = 100
        self.map = 100
        self.tps = 100
        self.gear = 'N'
        self.rpm = 0
        self.speed = 0
        self.battery_voltage = 12
        self.engine_running = False

        self.time = 0

        self.background = {
            'red': 0,
            'green': 0,
            'blue': 0
        }

        self.txt_ect = 'ECT {0} C'
        self.txt_iat = 'IAT {0} C'
        self.txt_map = 'MAP {0}kPa'
        self.txt_tps = 'TPS {0}%'
        self.txt_batt = 'Batt {0}V'
        self.txt_rpm = '{0} RPM'
        self.txt_gear = '{0}'

    def render(self):
        if self.time % 10 == 0:
            self.gear = random.choice(self.gears)

        self.rpm += math.floor(random.random()*100-50)
        if self.rpm < 1500:
            self.rpm = 1500

        if self.rpm > 11000:
            self.rpm = 11000

        self.time += 1;

        with canvas(self.device, dither=False) as ctx:
            self.renderBackground(ctx, 'rgb({0},{1},{2})'.format(self.background['red'], self.background['green'], self.background['blue']))
            self.renderCenteredText(ctx, self.font_10, self.txt_ect.format(self.ect), 0, 'white')
            self.renderCenteredText(ctx, self.font_10, self.txt_iat.format(self.iat), 10, 'white')
            self.renderCenteredText(ctx, self.font_10, self.txt_map.format(self.map), 20, 'white')
            self.renderCenteredText(ctx, self.font_10, self.txt_tps.format(self.tps), 30, 'white')
            self.renderCenteredText(ctx, self.font_10, self.txt_batt.format(self.battery_voltage), 40, 'white')
            # self.renderCenteredText(ctx, self.font_10, self.txt_rpm.format(self.rpm), 40, 'white')
            self.renderCenteredText(ctx, self.font_48, self.txt_gear.format(self.gear), 44, 'white')

    def renderCenteredText(self, ctx, font, text, y, fill):
        size = ctx.textsize(text, font=font)
        x = (self.device.width - size[0]) // 2
        ctx.text((x, y), text=text, fill=fill, font=font)

    def renderBackground(self, ctx, fill):
        ctx.rectangle((0, 0, device.width, device.height), fill=fill)

def main():
    display = CB650F_Display(device)
    while True:
        display.render()
        time.sleep(0.1)

if __name__ == "__main__":
    try:
        device = get_device()
        main()
    except KeyboardInterrupt:
        pass
