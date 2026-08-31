from inventory.imports import *

create_table()

def main(lang):

    while True:

        print()
        print(Panel.fit(f'[1] {language[lang]['CREATE_ITEM']}\n[2] {language[lang]['EDIT_ITEM']}\n[3] {language[lang]['LIST_ITEMS']}\n\n  [4] {language[lang]['HELP']}', title = language[lang]['MAIN_MENU']))

        option = validate_option(lang, '1', '2', '3', '4')
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

                while True:
                    print(Panel(f'- {language[lang]['BLANK_ENTER']}\n\n- {language[lang]['AUTO_SAVING']}', title = f'[blue]{language[lang]['HELP_MENU']}[/]', width = 50))
                    input('> ')
                    sleep(0.4)
                    print('\n\n\n\n\n\n\n\n\n')
                    break


if __name__ == '__main__':

    while True:

        main('ptbr')

        break