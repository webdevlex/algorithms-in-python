from abc import ABC, abstractmethod


# Command Interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


# Receiver
class Light:
    def on(self):
        print("Light is on.")

    def off(self):
        print("Light is off.")


# Concrete Commands
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()


class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.off()


# Invoker
class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        self.command.execute()


# Client code
def main():
    light = Light()
    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)

    remote = RemoteControl()

    remote.set_command(light_on)
    remote.press_button()  # Output: "Light is on."

    remote.set_command(light_off)
    remote.press_button()  # Output: "Light is off."


if __name__ == "__main__":
    main()
