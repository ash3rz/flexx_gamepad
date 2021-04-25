from flexx import flx
from client import GamepadClient
from button_mapping import button_mapping
import pygame
import asyncio
import os
import json
import sys

# Dummy video to effectively make pygame run headless
os.environ["SDL_VIDEODRIVER"] = "dummy"

# Read config file
with open("config.json") as json_config_file:
    config = json.load(json_config_file)


class GamepadServer(flx.PyWidget):
    def init(self):
        with flx.HBox():
            self.gamepad = GamepadClient()
        # This needs to be in a callback fn because Flexx waits for the init
        # call to complete before making the server available
        asyncio.get_event_loop().call_later(1, self.handle_gamepad_start)

    def handle_gamepad_disconnect(self):
        pygame.quit()
        self.gamepad.connected(False)
        self.handle_gamepad_start()

    def handle_gamepad_start(self):
        pygame.init()
        num_joysticks = pygame.joystick.get_count()

        if num_joysticks > 0:
            self.gamepad.connected(True)
            joystick = pygame.joystick.Joystick(0)
            joystick.init()
            while pygame.get_init() and pygame.joystick.get_count() > 0:
                self.read_gamepad()

        self.handle_gamepad_disconnect()

    def read_gamepad(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.handle_gamepad_disconnect()

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


if __name__ == '__main__':
    a = flx.App(GamepadServer)
    a.serve()
    flx.create_server(host='0.0.0.0', port=config["port"], loop=asyncio.new_event_loop())
    flx.start()
