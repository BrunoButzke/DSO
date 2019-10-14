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
        registration = self.check_valid_int_response("\nInforme a matrícula do jogador: ", 99999999)
        number = self.check_valid_int_response("\nInforme o número do jogador: ", 100)
        return registration, number
