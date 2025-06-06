import PySimpleGUI as sg

sg.theme("Black")


label1 = sg.Text("Enter feet:")
input1 = sg.Input(key="feet")

label2 = sg.Text("Enter inches")
input2 = sg.Input(key="inches")

convert_button = sg.Button("Convert")
exit_button = sg.Button("Exit")

output = sg.Text("", key="output")

window = sg.Window("Convertor",
                   layout=[[label1, input1],
                           [label2, input2],
                           [convert_button, exit_button, output]])

#print(event, values)
while True:
    event, values = window.read()
    match event:
        case 'Convert':
            try:
                feet = float(values["feet"])
                inches = float(values["inches"])
                calculate = (feet * 0.3048) + (inches * 0.0254)
                window["output"].update(value=calculate)
            except ValueError:
                sg.popup("Wprowadz poprawne liczby!")
        case 'Exit':
            break
        case sg.WIN_CLOSED:
            break


window.close()