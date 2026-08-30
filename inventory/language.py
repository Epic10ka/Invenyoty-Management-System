white = '\033[1;97m'
green = '\033[1;92m'
red = '\033[1;91m'
yellow = '\033[1;93m'
blue = '\033[1;94m'


language = {

    'ptbr': {


        #ITEMS
        'ITEMS': 'ITENS',
        'NAME': 'NOME',

        #NAME
        'NAME_SUCCESSFUL_CHANGE': 'NOME ALTERADO COM [\033[1;92mSUCESSO\033[m]',

        #ID
        'ID_SUCCESSFUL_CHANGE': 'ID ALTERADO COM [\033[1;92mSUCESSO\033[m]',

        #BATCH
        'BATCH_SUCCESSFUL_CHANGE': 'BATCH ALTERADO COM [\033[1;92mSUCESSO\033[m]',

        #STATUS
        'STATUS_SUCCESSFUL_CHANGE': 'STATUS ALTERADO COM [\033[1;92mSUCESSO\033[m]',


        'AVAILABLE': 'DISPONÍVEL',
        'BLOCKED': 'BLOQUEADO',
        'CHECKING': 'CONFERÊNCIA',


        #ERRORS
        'INVALID_NUMBER': f'{red}ERRO\033[m NÚMERO INVÁLIDO',
        'INVALID_STATUS': f'{red}ERRO\033[m STATUS INVÁLIDO',
        'ALL_STATUS': f' {white}STATUS SELECIONÁVEIS: {green}DISPONÍVEL\033[1;97m | {red}BLOQUEADO\033[1;97m | {yellow}HOLD\033[1;97m | {blue}CONFERÊNCIA\033[m '
    }
}