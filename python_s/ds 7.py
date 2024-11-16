import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

def checker(function):

    def checker( *args, **kwargs):
        try:
            result = function(*args, **kwargs)
        except Exception as exc:
            print(Fore.RED + f"We have problem {exc}")
        else:
            print(Fore.GREEN+ f"No problem. Result - {result}")
    return checker

@checker
def calculate(expression):
    return eval(expression)

#вписати числа
calculate("23 + 10")