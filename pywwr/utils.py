import importlib.util

def import_from_file(file_path, module_name):
    """
    Import a Python module from a local file.

    Parameters
    ----------
    file_path : str
        The path to the .py file to import.
    module_name : str
        The name to give the imported module.

    Returns
    -------
    module
        The imported Python module.
    
    Examples
    --------
    >>> file_path = "/path/to/module.py"
    >>> module_name = "module"
    >>> module = import_from_file(file_path, module_name)
    >>> module.some_function()
    """
    # Load the module spec
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    # Execute the module
    spec.loader.exec_module(module)
    return module
