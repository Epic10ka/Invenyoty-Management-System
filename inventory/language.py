white = '\033[1;97m'
green = '\033[1;92m'
red = '\033[1;91m'
yellow = '\033[1;93m'
blue = '\033[1;94m'


language = {

    'ptbr': {


        #MENU
        'MAIN_MENU': 'MENU PRINCIPAL',
        'CREATE_ITEM': 'CRIAR ITEM',
        'EDIT_ITEM': 'EDITAR ITEM',
        'LIST_ITEMS': 'LISTAR ITENS',
        'SEARCH_ITEM_BY_ID': 'PROCURAR ITEM POR ID',
        'HELP': 'AJUDA',

        #ITEMS
        'ITEMS': 'ITENS',
        'NAME': 'NOME',
        'ITEM_CREATION': 'CRIAÇÃO DE ITEM',
        'SUCCESSFUL_CREATION': f'{white}ITEM CRIADO COM [{green}SUCESSO{white}]',
        'SUCCESSFUL_UPDATE': f'{white}ITEM ATUALIZADO COM [{green}SUCESSO{white}]',
        'ITEM_EDITING': 'EDIÇÃO DE ITEM',

        #NAME
        'ITEM_NAME': 'NOME DO ITEM',
        'NAME_SUCCESSFUL_CHANGE': f'{white}NOME ALTERADO COM [{green}SUCESSO{white}]',
        'NEW_NAME': 'NOVO NOME (ENTER EM BRANCO PARA MANTER) ',

        #ID
        'ITEM_ID': 'ID DO ITEM',
        'ID_SUCCESSFUL_CHANGE': f'{white}ID ALTERADO COM [{green}SUCESSO{white}]',
        'ID_EDITING': 'Digite o ID do item que deseja editar',

        #BATCH
        'ITEM_BATCH': 'LOTE DO ITEM',
        'BATCH_SUCCESSFUL_CHANGE': f'{white}BATCH ALTERADO COM [{green}SUCESSO{white}]',
        'NEW_BATCH': 'NOVO LOTE (ENTER EM BRANCO PARA MANTER) ',

        #STATUS
        'ITEM_STATUS': 'STATUS DO ITEM',
        'STATUS_SUCCESSFUL_CHANGE': f'{white}STATUS ALTERADO COM [{green}SUCESSO{white}]',
        'NEW_STATUS': 'NOVO STATUS (ENTER EM BRANCO PARA MANTER) ',


        'AVAILABLE': 'DISPONÍVEL',
        'BLOCKED': 'BLOQUEADO',
        'CHECKING': 'CONFERÊNCIA',


        #ERRORS
        'ITEM_NOT_FOUND': f'{white}[{red}ERRO{white}] ITEM NÃO ENCONTRADO',
        'INVALID_OPTION': f'{white}[{red}ERRO{white}] OPÇÃO INVÁLIDA',
        'INVALID_NUMBER': f'{white}[{red}ERRO{white}] NÚMERO INVÁLIDO',
        'INVALID_STATUS': f'{white}[{red}ERRO{white}] STATUS INVÁLIDO',
        'ALL_STATUS': f'{white}STATUS SELECIONÁVEIS: \n\n{green}DISPONÍVEL\033[1;97m\n{red}BLOQUEADO\033[1;97m\n{yellow}HOLD\033[1;97m\n{blue}CONFERÊNCIA{white}',
        'NO_REGISTERED_ITEM': f'{white}[{red}ERRO{white}] NENHUM ITEM CADASTRADO',
    }
}