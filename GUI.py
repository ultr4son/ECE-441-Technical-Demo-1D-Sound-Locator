import PySimpleGUI as sg

DRAW_GRID = "DRAW_GRID"
WINDOW_TITLE = "Wow"
def open_window():
    layout = [
        [sg.Canvas(key=DRAW_GRID)]
    ]
    window = sg.Window(WINDOW_TITLE,layout = layout, size=(500, 500))
    return window
