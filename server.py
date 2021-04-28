import asyncio
import json
import os

import pygame
from flexx import flx

from button_mapping import button_mapping
from client import GamepadClient

# Dummy video to effectively make pygame run headless
os.environ["SDL_VIDEODRIVER"] = "dummy"

flexx_port = 3000

# Read config file
if os.path.isfile("config.json"):
    with open("config.json") as json_config_file:
        config = json.load(json_config_file)
        flexx_port = config["port"]


class GamepadServer(flx.PyWidget):
    def init(self):
        with flx.HBox():
            self.gamepad = GamepadClient()

        self.done = False
        # This needs to be in a callback fn because Flexx waits for the init
        # call to complete before making the server available
        asyncio.get_event_loop().call_later(1, self.handle_gamepad_start)

    def read_gamepad_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True

            elif event.type == pygame.JOYBUTTONDOWN:
                self.gamepad.button_update(event.button, True)

            elif event.type == pygame.JOYBUTTONUP:
                self.gamepad.button_update(event.button, False)

            elif event.type == pygame.JOYAXISMOTION:
                axis_map = button_mapping("axis")
                if event.axis in axis_map:
                    [name, axis] = axis_map[event.axis]
                    if axis:
                        self.gamepad.axis_update(name, axis, event.value)
                    else:
                        self.gamepad.button_render(name, True if event.value > 0 else False)

            elif event.type == pygame.JOYHATMOTION:
                [x, y] = event.value
                if x == 0:
                    self.gamepad.button_update("left", False)
                    self.gamepad.button_update("right", False)
                else:
                    self.gamepad.button_update("left" if x == -1 else "right", True)
                if y == 0:
                    self.gamepad.button_update("up", False)
                    self.gamepad.button_update("down", False)
                else:
                    self.gamepad.button_update("down" if y == -1 else "up", True)

    def handle_gamepad_start(self):
        pygame.init()
        pygame.joystick.init()

        # The order in which these are executed (read events, then get the number of joysticks,
        # then init joystick) seems illogical, but also seems to be necessary
        # This is the same order from pygame's joystick sample code:
        # https://www.pygame.org/docs/ref/joystick.html
        while not self.done:
            self.read_gamepad_events()

            num_joysticks = pygame.joystick.get_count()

            if num_joysticks > 0:
                self.gamepad.connected(True)
            else:
                self.gamepad.connected(False)
            for i in range(num_joysticks):
                joystick = pygame.joystick.Joystick(i)
                joystick.init()
        pygame.quit()


if __name__ == '__main__':
    flx.App(GamepadServer).serve()
    flx.create_server(host='0.0.0.0', port=3000)
    flx.run()
