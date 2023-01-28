from abc import ABC, abstractmethod



class Button(ABC):
    @abstractmethod
    def new_file(self):
        pass
    @abstractmethod
    def delete_file(self):
        pass
    @abstractmethod
    def new_diretocry(self):
        pass
    @abstractmethod
    def delete_directory(self):
        pass

class LinuxButton(Button):
    def new_file(self):
        return "Stworzono nowy plik LINUX"
    def delete_file(self):
        return "Usunieto plik LINUX"
    def new_diretocry(self):
        return "Stworzono folder LINUX"
    def delete_directory(self):
        return "Usunieto folder LINUX"


class WindowsButton(Button):
    def new_file(self):
        return "Stworzono nowy plik WINDOWS"
    def delete_file(self):
        return "Usunieto plik WINDOWS"
    def new_diretocry(self):
        return "Stworzono folder WINDOWS"
    def delete_directory(self):
        return "Usunieto folder WINDOWS"



class CLIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass


class LinuxFactory(CLIFactory):
    def create_button(self):
        return LinuxButton()


class WindowsFactory(CLIFactory):
    def create_button(self):
        return WindowsButton()


if __name__ == "__main__":
    system = 0
    while True:
        print("1. WINDOWS")
        print("2. LINUKS")
        system = input("Wybierz system >> ")
        if system == "1":
            factory = WindowsFactory()
            button = factory.create_button()
            break
        elif system == "2":
            factory = LinuxFactory()
            button = factory.create_button()
            break
    
    while True:
        print("1. Stworz plik")
        print("2. Usun plik")
        print("3. Stworz folder")
        print("4. Usun folder")
        print("5. Wyjdz")
        choice = input("Wybor >> ")

        if choice == "1":
            print(button.new_file())
        elif choice == "2":
            print(button.delete_file())
        elif choice == "3":
            print(button.new_diretocry())
        elif choice == "4":
            print(button.delete_directory())
        elif choice == "5":
            break
            