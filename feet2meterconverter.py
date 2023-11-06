import PySimpleGUI as sg

feet_label = sg.Text('Enter Feet: ')
feet_ip = sg.Input(key='feet')
inches_label = sg.Text('Enter Inches:')
inches_ip = sg.Input(key='inches')
button=sg.Button('Convert',key='convert')
meter_label = sg.Text(key='meter')

window = sg.Window('Converter',layout=[[feet_label,feet_ip],
                                       [inches_label,inches_ip],
                                       [button,meter_label]])

while True:
    event,values= window.read()
    print(event,values)
    match event:
        case 'convert':
            feet= float(values['feet'] if values['feet'] else 0)
            print(feet)
            inches = float(values['inches'] if values['inches'] else 0)
            meters = .0254 * (12*feet + inches)
            window['meter'].update(value=f"{meters} m")

        case sg.WIN_CLOSED:
            break


window.close()