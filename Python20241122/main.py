TYPE_OS = 1

class DialogWindows:
    name_class = "DialogWindows"

class DialogLinux:
    name_class = "DialogLinux"

class Dialog:
    def __new__(cls, *args, **kwargs):
        obj = None

        if TYPE_OS == 1:
            obj = super().__new__(DialogWindows)
        else:
            obj = super().__new__(DialogLinux)

        obj.name = args[0]

        return obj

dialog = Dialog('First Dialog')
print(dialog.name_class, dialog.name, sep="\n")