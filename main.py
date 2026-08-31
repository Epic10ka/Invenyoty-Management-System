from inventory.imports import *
from inventory.language import language

create_table()

def main(lang):

    print(Panel.fit(f'[1] {language[lang]['CREATE_ITEM']}\n[2] {language[lang]['EDIT_ITEM']}\n[3] {language[lang]['LIST_ITEMS']}\n\n  [4] {language[lang]['HELP']}', title = language[lang]['MAIN_MENU']))

    option = validate_option(lang, '1', '2', '3', '4')

    match option:

        case '1':
            item_creation(lang, Item)

        case '2':
            pass

        case '3':
            pass

        case '4':
            pass



if __name__ == '__main__':
    main('ptbr')