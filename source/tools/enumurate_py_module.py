import inspect

def enumerate_import(module_name):
    try:
        module = __import__(module_name)
        print(f"Module structure for {module_name}:")
        print(inspect.getmodule(module).__file__)
        print(inspect.getdoc(module))
        print(inspect.getcomments(module))
        print(inspect.getmembers(module))
    except ImportError:
        print(f"Module {module_name} not found.")

inputmodule = input("Enter a module name to enumerate: ")
enumerate_import(inputmodule)
input("Press enter to exit...")
