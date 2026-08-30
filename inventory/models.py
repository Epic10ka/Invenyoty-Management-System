from language import language


#VALIDATING TEXT ACCCENTS Ê and Ì for PTBR "Available" and "Conferência"
def corrigir_texto(texto):

    if texto.upper() == 'DISPONIVEL':
        return 'DISPONÍVEL'

    elif texto.upper() == 'CONFERENCIA':
        return 'CONFERÊNCIA'

    return texto


class Item:

    def __init__(self, name:str, idn:int, batch:str, status:str, lang = 'ptbr'):

        """
        :param name: Product/Item name
        :param idn: Identification Number
        :param batch: Batch number
        :param status: Product/Item Status --> Available | Blocked | Hold | Checking
        """

        self._name = name
        self._idn = idn
        self._batch = batch
        self.__status = status
        self.lang = lang

    # -RETURNING A MORE VISIBLE CLASS ATTRIBUTES
    def __str__(self):
        return f'--------------------------\nITEM: {self._name}\nID NUMBER: {self._idn}\nBATCH: {self._batch}\nSATUS: {self.__status}\n--------------------------'


    # -GETTERS AND SETTERS

    @property
    def name(self):
        return self._name


    @name.setter
    def name(self, new_name):

        print(f'{language[self.lang]['NAME_SUCCESSFUL_CHANGE']}')
        self._name = new_name.strip().upper()


    @property
    def id_number(self):
        return self._idn


    @id_number.setter
    def id_number(self, new_number):

        try:
            new_number = int(new_number)
            print(f'{language[self.lang]['ID_SUCCESSFUL_CHANGE']}')
            self._idn = new_number


        except ValueError as e:
            print(f'{language[self.lang]['INVALID_NUMBER']} | {e}')


    @property
    def batch(self):
        return self._batch


    @batch.setter
    def batch(self, new_batch):

        print(f'{language[self.lang]['BATCH_SUCCESSFUL_CHANGE']}')
        self._batch = new_batch


    @property
    def status(self):
        return self.__status


    @status.setter
    def status(self, new_status):

        new_status = corrigir_texto(new_status)

        print(new_status)

        if new_status not in (language[self.lang]['AVAILABLE'], language[self.lang]['BLOCKED'], language[self.lang]['CHECKING'], 'HOLD'):

            print(f'{language[self.lang]['INVALID_STATUS']} [{language[self.lang]['ALL_STATUS']}]')


        else:

            print(f'{language[self.lang]['STATUS_SUCCESSFUL_CHANGE']}')
            self.__status = new_status



testing = Item('Whey Protein Powder', 2468, 'CC059265A', 'AVAILABLE')


print(testing)