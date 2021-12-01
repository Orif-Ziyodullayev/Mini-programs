from translate import Translator
from termcolor import colored
from pyfiglet import Figlet
f = Figlet(font='slant')
print(colored(f.renderText('Interpreter'),'yellow'))
translator = Translator(from_lang='eng',to_lang='ru')
while True:
    result = input(colored('Enter a word: ','yellow'))
    result1 = translator.translate(result)
    print(colored(result.title(),'red'),'-',colored(result1.title(),'blue'))