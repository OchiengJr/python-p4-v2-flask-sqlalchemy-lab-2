#!/usr/bin/env python3

def pytest_itemcollected(item):
    """
    This hook function modifies the `nodeid` attribute of each collected test item.
    It combines the class-level and method-level docstrings (or names if docstrings are missing)
    to create a more descriptive test ID.
    """
    # Get the class object of the test case
    par = item.parent.obj
    # Get the method/function object of the test case
    node = item.obj
    
    # Get the class-level docstring or class name if docstring is missing
    pref = par.__doc__.strip() if par.__doc__ else par.__name__
    # Get the method-level docstring or method name if docstring is missing
    suf = node.__doc__.strip() if node.__doc__ else node.__name__
    
    # Combine the class-level and method-level descriptions
    if pref or suf:
        item._nodeid = ' '.join((pref, suf))

    # Ensure the nodeid is a string
    item._nodeid = str(item._nodeid)

