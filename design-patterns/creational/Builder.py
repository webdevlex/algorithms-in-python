class Computer:
    def __init__(self, cpu, gpu, ram, storage, case):
        self.cpu = cpu
        self.gpu = gpu
        self.ram = ram
        self.storage = storage
        self.case = case

    def __str__(self):
        return f"Computer: CPU={self.cpu}, GPU={self.gpu}, RAM={self.ram}, Storage={self.storage}, Case={self.case}"


class ComputerBuilder:
    def __init__(self):
        self.computer = None

    def create_computer(self):
        self.computer = Computer("", "", "", "", "")

    def set_cpu(self, cpu):
        self.computer.cpu = cpu

    def set_gpu(self, gpu):
        self.computer.gpu = gpu

    def set_ram(self, ram):
        self.computer.ram = ram

    def set_storage(self, storage):
        self.computer.storage = storage

    def set_case(self, case):
        self.computer.case = case

    def get_computer(self):
        return self.computer


# Director
class ComputerDirector:
    def __init__(self, builder):
        self.builder = builder

    def build_gaming_pc(self):
        self.builder.create_computer()
        self.builder.set_cpu("Intel i9")
        self.builder.set_gpu("NVIDIA RTX 3080")
        self.builder.set_ram("32GB")
        self.builder.set_storage("1TB SSD")
        self.builder.set_case("Gaming Case")

    def build_workstation(self):
        self.builder.create_computer()
        self.builder.set_cpu("AMD Ryzen 9")
        self.builder.set_gpu("NVIDIA Quadro RTX 4000")
        self.builder.set_ram("64GB")
        self.builder.set_storage("2TB NVMe SSD")
        self.builder.set_case("Professional Case")


# Client code
builder = ComputerBuilder()
director = ComputerDirector(builder)

director.build_gaming_pc()
gaming_pc = builder.get_computer()
print(gaming_pc)

director.build_workstation()
workstation = builder.get_computer()
print(workstation)
