from colorama import init, Fore, Back, Style

# Ініціалізація бібліотеки
init()

# Використання кольорового тексту
print(Fore.RED + 'Це червоний текст')
print(Back.GREEN + 'Це текст з зеленим фоном')
print(Style.BRIGHT + 'Це яскравий текст' + Style.RESET_ALL)

# Комбінування кольорів та стилів
print(Fore.BLUE + Back.YELLOW + Style.DIM + 'Синій текст з жовтим фоном і слабо освітлений')