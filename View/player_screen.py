import PySimpleGUI as view


class PlayerScreen:
    def __init__(self):
        pass

    def check_valid_int_response(self, string, max_value):
        while True:
            try:
                response = int(input(string))
                if response > max_value :
                    raise Exception()
                return response
            except ValueError:
                print("\nOps, Você deve informar um número")
            except Exception:
                print("\nO número deve estar entre [0 e {max}]".format(max = max_value))

    def get_data(self):

        layout = [
            [view.Text('Informe a matrícula do jogador:')],
            [view.InputText()],
            [view.Text('Informe o número do jogador:')],
            [view.InputText()],
            [view.Submit()]
        ]
        window = view.Window('Jogador').Layout(layout)
        button, values = window.Read()
        window.close()

        return int(values[0]), int(values[1])
