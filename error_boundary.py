import PySimpleGUI as view


def check_valid_int_response(response, max_value):
    try:
        response = int(response)
        if response > max_value or response < 1 :
            raise Exception()
        return True
    except ValueError:
        layout = [
            [view.Text('Ops, Você deve informar um número')],
            [view.Ok()]
        ]
        window = view.Window('Aviso').Layout(layout)
        button = window.Read()
        window.close()
        return False
    except Exception:
        layout = [
            [view.Text('O número deve estar entre [1 e {max}]'.format(max = max_value))],
            [view.Ok()]
        ]
        window = view.Window('Aviso').Layout(layout)
        button = window.Read()
        window.close()
        return False

def check_valid_string_response(response):
    while True:
        try:
            if len(response.strip()) == 0 :
                raise Exception()
            return response
        except Exception:
            layout = [
                [view.Text('Ops, Você deve informar um nome')],
                [view.Ok()]
            ]
            window = view.Window('Aviso').Layout(layout)
            button = window.Read()
            window.close()
            return False
