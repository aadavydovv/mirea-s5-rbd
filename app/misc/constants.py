from enum import Enum

BUTTON_BG = '#767777'
BUTTON_HEIGHT = 4
BUTTON_WIDTH = 9

BG = '#434444'
FG = '#FFFFFF'
LEFT_MOUSE_BUTTON = "<Button-1>"
PAD_X = 16
PAD_Y = 16

FONT_SIZE_DEFAULT = 12


class QueryModes(Enum):
    GET = 'get'
    EDIT = 'edit'
    GET_PRIMARY_KEY = 'get_pk'


class ResultModes(Enum):
    SINGLE = 'single',
    ENTRY_LIST = 'entry_list'


class ValuesWindowModes(Enum):
    EDIT = 'edit'
    ADD = 'add'
