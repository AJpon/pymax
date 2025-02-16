"""Abstraction layer for PySide2/PySide6 compatibility."""

try:
    import PySide2 as qt
except ImportError:
    import PySide6 as qt

QtWidgets = qt.QtWidgets
QtCore = qt.QtCore
