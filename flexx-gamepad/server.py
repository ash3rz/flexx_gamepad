from flexx import flx
from client import GamepadClient
from button_mapping import button_mapping
import pygame
import asyncio
import os
import json

# Dummy video to effectively make pygame run headless
os.environ["SDL_VIDEODRIVER"] = "dummy"

# Read config file
with open("config.json") as json_config_file:
    config = json.load(json_config_file)


class GamepadServer(flx.PyWidget):
    def init(self):
        self.gamepad_connected = False
        with flx.VBox(title='Gamepad Test'):
            self.gamepad = GamepadClient()
            self.start = flx.Button(text='Start')
            self.stop = flx.Button(text='Stop')

    @flx.reaction('stop.pointer_down')
    def _stop_gamepad(self, *events):
        self.gamepad_connected = False
        self.gamepad.status(False)
        pygame.quit()

    @flx.reaction('start.pointer_down')
    def _check_gamepad(self, *events):
        pygame.init()
        num_joysticks = pygame.joystick.get_count()
        if num_joysticks < 1:
            self.gamepad_connected = False
            self.gamepad.status(False)
        else:
            self.gamepad_connected = True
            self.gamepad.status(True)
            joystick = pygame.joystick.Joystick(0)
            joystick.init()
            while self.gamepad_connected:
                self.read_gamepad()

    def read_gamepad(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.gamepad_connected = False
                self.gamepad.status(False)
            elif event.type == pygame.JOYBUTTONDOWN:
                self.gamepad.button_update(event.button, True)
            elif event.type == pygame.JOYBUTTONUP:
                self.gamepad.button_update(event.button, False)
            elif event.type == pygame.JOYAXISMOTION:
                if event.axis == button_mapping("left_joystick_x"):
                    self.gamepad.axis_update("stick left", "x", event.value)
                if event.axis == button_mapping("left_joystick_y"):
                    self.gamepad.axis_update("stick left", "y", event.value)
                if event.axis == button_mapping("right_joystick_x"):
                    self.gamepad.axis_update("stick right", "x", event.value)
                if event.axis == button_mapping("right_joystick_y"):
                    self.gamepad.axis_update("stick right", "y", event.value)
            elif event.type == pygame.JOYHATMOTION:
                [x, y] = event.value
                if x == 0:
                    self.gamepad.button_update("left", False)
                    self.gamepad.button_update("right", False)
                if x == -1:
                    self.gamepad.button_update("left", True)
                if x == 1:
                    self.gamepad.button_update("right", True)
                if y == 0:
                    self.gamepad.button_update("up", False)
                    self.gamepad.button_update("down", False)
                if y == -1:
                    self.gamepad.button_update("down", True)
                if y == 1:
                    self.gamepad.button_update("up", True)


if __name__ == '__main__':
    a = flx.App(GamepadServer)
    a.serve()
    flx.create_server(host='0.0.0.0', port=config["port"], loop=asyncio.new_event_loop())
    flx.start()