from inventory.language import language
from inventory.functions import corrigir_texto



class Item:

    def __init__(self, name:str, idn:str, batch:str, status:str):

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

    # -RETURNING A MORE READABLE __str__ REPRESENTATION
    def __str__(self):
        return f'--------------------------\nITEM: {self._name}\nID NUMBER: {self._idn}\nBATCH: {self._batch}\nSTATUS: {self.__status}\n--------------------------'


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


        #CHECKING IF USER IS SETTING A SYSTEM STATUS, IN EACH LANGUAGE.

        if new_status not in (language[self.lang]['AVAILABLE'], language[self.lang]['BLOCKED'], language[self.lang]['CHECKING'], 'HOLD'):

            print(f'{language[self.lang]['INVALID_STATUS']} [{language[self.lang]['ALL_STATUS']}]')


        else:

            print(f'{language[self.lang]['STATUS_SUCCESSFUL_CHANGE']}')
            self.__status = new_status




    #Turning attributes into a dictionary
    def to_dict(self):

        """
        Turns the vehicle save into a dictionary to make it savable in JSON
        """

        return {

            'item_name': self._name,
            'item_id': self._idn,
            'item_batch': self._batch,
            'item_status': self.__status,
        }