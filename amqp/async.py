from __future__ import absolute_import

_current_loop = None


def get_event_loop():
    return _current_loop


def set_event_loop(loop):
    global _current_loop
    _current_loop = loop
    return loop
