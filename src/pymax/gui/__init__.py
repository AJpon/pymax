from pymxs import runtime as rt
from .qt import QtWidgets


def get_main_window() -> QtWidgets.QMainWindow:
    """Get the main 3ds Max window."""
    return QtWidgets.QWidget.find(rt.windows.getMAXHWND())
