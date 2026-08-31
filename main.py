from inventory.imports import *

create_table()

default_lang = 'en'

def language_selection(lang):

    while True:

        print(Panel(f'      [1] {language[lang]['PORTUGUESE']}\n      [2] {language[lang]['ENGLISH']}', title=language[lang]['LANGUAGE_SELECTION_MENU'], width = 30))
        print(f'{language[lang]['SELECT_ONE']}:')

        selection = validate_option(lang,'1', '2').strip()

        if selection == '':
            return lang

        match selection:

            case '1':
                return 'ptbr'

            case '2':
                return 'en'

        return 'en'



def main(lang):

    while True:

        print()
        print(Panel.fit(f'[1] {language[lang]['CREATE_ITEM']}\n[2] {language[lang]['EDIT_ITEM']}\n'
                        f'[3] {language[lang]['LIST_ITEMS']}\n[4] {language[lang]['DELETE_ITEM']}\n[5] {language[lang]['LANGUAGE_SELECTION']}\n\n  [6] {language[lang]['HELP']}', title = language[lang]['MAIN_MENU']))

        option = validate_option(lang, '1', '2', '3', '4', '5', '6')
        if option == '':
            break

        match option:

            case '1':
                item_creation(lang, Item)

            case '2':
                item_editing(lang, Item)

            case '3':
                item_listing(lang)
                input('> ')
                sleep(0.2)

            case '4':
                item_deleting(lang, Item)

            case '5':
                lang = language_selection(lang)

            case '6':

                while True:
                    print(Panel(f'- {language[lang]['BLANK_ENTER']}\n\n- {language[lang]['AUTO_SAVING']}\n\n    -{language[lang]['MADE_BY_FORTES']}', title = f'[blue]{language[lang]['HELP_MENU']}[/]', width = 50))
                    input('> ')
                    sleep(0.4)
                    print('\n\n\n\n\n\n\n\n\n')
                    break


if __name__ == '__main__':

    while True:

        main(default_lang)

        break