"""Python project testing an oe-template usability and convenience."""

from .constants import MODULES_TO_INSTRUMENT
from .utils.boot import boot

boot(modules_to_instrument=MODULES_TO_INSTRUMENT)
