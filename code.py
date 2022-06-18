import PySimpleGUI as sg

#controll_col =
image_col = sg.Column([[sg.Image('test.png')]])

layout = [
    [image_col]
]

window = sg.Window('Image Editor', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()