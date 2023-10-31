import PySimpleGUI as sg

title = 'Convert'
layout = [
    # [sg.Text('Text', enable_events=True, key='-text-'), sg.Spin(['item1', 'item2'],)],
    # [sg.Button('Button', key='-button1-')],
    # [sg.Input(key='-input-')],
    # [sg.Text('Test'), sg.Button('Test Button', key='-button2-')]
    [sg.Input(key='input'), sg.Spin(['km to mile', 'kg to pound', 'sec to min'], key='units'), sg.Button('Convert', key='btn_convert')],
    [sg.Text('Output', key='output')]
]

window = sg.Window(title, layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'btn_convert':
        input_value = values['input']
        unit = values['units']
        if input_value.isnumeric():
            match unit:
                case 'km to mile':
                    output = round(float(input_value) * 0.6214, 2)
                    output_str = f'{input_value}km are {output} miles'
                case 'kg to pound':
                    output = 
            window['output'].update(output_str)


window.close()

