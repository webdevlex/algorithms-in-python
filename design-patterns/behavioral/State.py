from abc import ABC, abstractmethod


# Context (Phone)
class Phone:
    def __init__(self):
        self.state = OffState()

    def change_state(self, state):
        self.state = state

    def press_power_button(self):
        self.state.press_power_button(self)

    def press_volume_up(self):
        self.state.press_volume_up(self)

    def press_volume_down(self):
        self.state.press_volume_down(self)


# State (Abstract)
class PhoneState(ABC):
    @abstractmethod
    def press_power_button(self, phone):
        pass

    @abstractmethod
    def press_volume_up(self, phone):
        pass

    @abstractmethod
    def press_volume_down(self, phone):
        pass


# Concrete States
class OffState(PhoneState):
    def press_power_button(self, phone):
        print("Turning the phone on.")
        phone.change_state(OnState())

    def press_volume_up(self, phone):
        print("Phone is off. Cannot adjust volume.")

    def press_volume_down(self, phone):
        print("Phone is off. Cannot adjust volume.")


class OnState(PhoneState):
    def press_power_button(self, phone):
        print("Turning the phone off.")
        phone.change_state(OffState())

    def press_volume_up(self, phone):
        print("Increasing volume.")

    def press_volume_down(self, phone):
        print("Decreasing volume.")


# Client code
def main():
    phone = Phone()

    phone.press_volume_up()  # Output: Phone is off. Cannot adjust volume.

    phone.press_power_button()  # Output: Turning the phone on.
    phone.press_volume_up()  # Output: Increasing volume.
    phone.press_volume_down()  # Output: Decreasing volume.
    phone.press_power_button()  # Output: Turning the phone off.


if __name__ == "__main__":
    main()
