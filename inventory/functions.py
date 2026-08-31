from inventory.language import language
from rich.panel import Panel
from rich import print
import uuid
from time import sleep
from inventory.data_base import *



#VALIDATING TEXT Ê and Ì for PTBR "Available" and "Conferência"
def corrigir_texto(texto):

    if texto.upper().strip() == 'DISPONIVEL':
        return 'DISPONÍVEL'

    elif texto.upper().strip() == 'CONFERENCIA':
        return 'CONFERÊNCIA'

    return texto.strip().upper()




def item_creation(lang, item):

    create_table()

    while True:

        sleep(0.2)
        print(Panel.fit(language[lang]['ITEM_CREATION']))

        item_name = input(f'\n{language[lang]['ITEM_NAME']}: ').strip().title()

        if item_name == '':
            break

        short_id = uuid.uuid4().hex

        item_batch = input(f'{language[lang]['ITEM_BATCH']}: ')

        if item_batch == '':
            break

        while True:
            item_status = input(f'{language[lang]['ITEM_STATUS']}: ')
            corrected_status = corrigir_texto(item_status)

            if corrected_status not in (language[lang]['AVAILABLE'], language[lang]['BLOCKED'], language[lang]['CHECKING'], 'HOLD'):

                print(f'{language[lang]['INVALID_STATUS']}\n\n{language[lang]['ALL_STATUS']}\n')


            else:
                item_status = corrected_status
                break


        print(f'\n{language[lang]['ITEM_ID']}: {short_id}\n')
        print(f'{language[lang]['SUCCESSFUL_CREATION']}')

        new_item =  item(

            name = item_name,
            idn = short_id,
            batch = item_batch,
            status= item_status,

        )

        insert_item(new_item)


def item_listing(lang):

    sleep(0.2)
    rows = get_all_items()

    if not rows:
        print(language[lang]['NO_REGISTERED_ITEM'])
        return

    for row in rows:
        sleep(0.2)
        print(f'\nID: {row['idn']} | {language[lang]['NAME']}: {row['name']} | {language[lang]['ITEM_STATUS']}: {row['status']}')


def item_editing(lang, item):

    while True:
        sleep(0.2)

        item_listing(lang)

        rows = get_all_items()

        if not rows:
            print(language[lang]['NO_REGISTERED_ITEM'])
            return

        print(Panel.fit(language[lang]['ITEM_EDITING']))

        term = input(f'{language[lang]["SEARCH_ITEM_BY_ID"]}: ').strip()

        if term == '':
            break

        results = search_items(term)

        if not results:

            print(language[lang]['ITEM_NOT_FOUND'])
            continue

        if len(results) == 1:

            row = results[0]

        else:
            
            for r in results:
                print(
                    f'ID: {r["idn"]} | {language[lang]["NAME"]}: {r["name"]} | {language[lang]["ITEM_STATUS"]}: {r["status"]}')

            chosen_idn: str = input(f'{language[lang]["ID_EDITING"]}: ').strip()

            if chosen_idn == '':
                continue

            row = get_item_by_id(chosen_idn)

            if row is None:
                print(language[lang]['ITEM_NOT_FOUND'])
                return

        current_item = item(
            name = row['name'],
            idn = row['idn'],
            batch = row['batch'],
            status = row['status']
        )

        print(current_item)

        new_name = input(f'{language[lang]['NEW_NAME']}: ').strip()
        if new_name:

            current_item.name = new_name.title()

        new_batch = input(f'{language[lang]['NEW_BATCH']}: ').strip()
        if new_batch:

            current_item.batch = new_batch.upper()

        while True:
            new_status = input(f'{language[lang]["NEW_STATUS"]}: ').strip()
            print()

            if new_status:

                try:
                    current_item.status = new_status
                    break

                except ValueError as e:
                    print(str(e))  #Forcing conversion to string before passing through print

            else:
                break

        update_item(current_item)
        print(language[lang]['SUCCESSFUL_UPDATE'])
        break


def validate_option(lang, *options):

    while True:
        option = input('> ').strip().upper()

        if option == '':
            return ''

        if not option:
            print(f'{language[lang]['INVALID_OPTION']}')
            continue

        option = option[0]
        if option in options:
            return option

        print(f'{language[lang]['INVALID_OPTION']}')