from abc import ABC, abstractmethod


# Handler Interface
class Handler(ABC):
    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle_request(self, request):
        pass


# Concrete Handlers
class ConcreteHandler1(Handler):
    def set_next(self, handler):
        self.next_handler = handler

    def handle_request(self, request):
        if request == "Type1":
            print("ConcreteHandler1 handles Type1 request.")
        elif self.next_handler:
            self.next_handler.handle_request(request)


class ConcreteHandler2(Handler):
    def set_next(self, handler):
        self.next_handler = handler

    def handle_request(self, request):
        if request == "Type2":
            print("ConcreteHandler2 handles Type2 request.")
        elif self.next_handler:
            self.next_handler.handle_request(request)


# Client code
def main():
    handler1 = ConcreteHandler1()
    handler2 = ConcreteHandler2()

    handler1.set_next(handler2)

    handler1.handle_request("Type1")
    handler1.handle_request("Type2")
    handler1.handle_request("Type3")


if __name__ == "__main__":
    main()
