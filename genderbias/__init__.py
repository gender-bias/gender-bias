#!/usr/bin/env python3

import os  # To find the directories
import importlib  # To import those directories as modules
import inspect  # To find Detector-derived classes

from .document import Document


def scanned_detectors():
    """
    Get a list of all detectors available in the genderbias package.

    This is most commonly used to get a list of all detectors when none are
    specified on the commandline.

    """

    _dir = os.path.dirname(__file__)
    exclude_dirs = ("__pycache__",)

    all_full_module_paths = [os.path.join(_dir, entry) for entry in os.listdir(_dir)]
    module_paths = [
        path
        for path in all_full_module_paths
        if os.path.isdir(path) and os.path.basename(path) not in exclude_dirs
    ]
    module_path_to_module = {
        path: importlib.import_module("." + os.path.basename(path), "genderbias")
        for path in module_paths
    }
    return [
        (module_path, class_name, cls)
        for module_path, module in module_path_to_module.items()
        for class_name, cls in inspect.getmembers(module, inspect.isclass)
        if "Detector" in str(cls.__bases__)
    ]


_scanned_detectors = scanned_detectors()
ALL_SCANNED_DETECTORS = {class_name: cls for _, class_name, cls in _scanned_detectors}
