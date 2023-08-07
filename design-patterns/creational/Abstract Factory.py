from abc import ABC, abstractmethod


# Abstract Product A
class Button(ABC):
    @abstractmethod
    def paint(self):
        pass


# Concrete Product A1
class WindowsButton(Button):
    def paint(self):
        return "Rendering a Windows button"


# Concrete Product A2
class MacOSButton(Button):
    def paint(self):
        return "Rendering a MacOS button"


# Abstract Product B
class Checkbox(ABC):
    @abstractmethod
    def paint(self):
        pass


# Concrete Product B1
class WindowsCheckbox(Checkbox):
    def paint(self):
        return "Rendering a Windows checkbox"


# Concrete Product B2
class MacOSCheckbox(Checkbox):
    def paint(self):
        return "Rendering a MacOS checkbox"


# Abstract Factory
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


# Concrete Factory 1
class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()


# Concrete Factory 2
class MacOSFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacOSButton()

    def create_checkbox(self) -> Checkbox:
        return MacOSCheckbox()


# Client code
def create_ui(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    return button.paint(), checkbox.paint()


# Usage
windows_factory = WindowsFactory()
macos_factory = MacOSFactory()

windows_ui = create_ui(windows_factory)
macos_ui = create_ui(macos_factory)

print(windows_ui)
print(macos_ui)
