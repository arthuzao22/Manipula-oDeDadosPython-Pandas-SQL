import pandas as pd

# Dados fornecidos

dados = {
    'Setor A': {
        'Canil 1': ['Duke', 'Digo b5', 'Omega', 'Peluda', 'Feliz', 'Banzé', 'Marley', 'Marshal', 'Salsicha',
                    'Princesa'],
        'Canil 2': ['Flor', 'Violeta', 'Rosa', 'Alecrim (bravinha)', 'Dolynho', 'Preta', 'Amarelinha', 'Like'],
        'Canil 3': ['Vovô Geraldo'],
        'Canil 4': ['Polar'],
        'Canil 5': ['Aberto'],
        'Canil 6': ['Pirata Pit bull'],
        'Canil 7': ['Hocckie', 'Felícia'],
        'Canil 8': ['Lampião', 'Maria bonita'],
        'Canil 9': ['Cher', 'Boiadeiro'],
        'Canil 10': ['Preta pretita'],
        'Canil 11': ['Amarela', 'Theo autista', 'Lisa (orelhuda caramelo)', 'Max (preto e branco)'],
        'Canil 12': ['Jurandi filhote', 'Amarelo pequeno filhote', 'Debi peluda', 'Dona Gertrudes', 'Amarela filhote',
                     'Pretinha filhote', 'Moana preta e amarela'],
        'Canil 13': ['Rico', 'Jack', 'Lala', 'Berenice', 'Euros'],
        'Canil 14': [],
        'Canil 15': [],
        'Canil 16': [],
        'Canil 17': ['Delícia Pit bull'],
        'Canil 18': ['Magnólia e dona'],
        'Canil 19': ['Nina pescoço', '5 filhotes'],
        'Canil 20': ['Luna'],
        'Canil 21': ['Tenório'],
    },
    'Setor B': {
        'Filhoteiro 1 Canil 1': ['Diane', 'Pitanguinha', 'Docinho', 'Florzinha', 'Thor (amarelo)', 'Terra (caramelo)',
                                 'Clei', 'Maggie'],
        'Filhoteiro 2 Canil 2': ['Trigresa', 'Trigada', 'Íris (preto cega)', 'Cristóvão', 'Lulinha',
                                 'Fufu (preta com detalhes branco)', 'Pirata', 'Vovó (preto e amarelo velha)',
                                 'Boneca (peluda)', 'Bolsonaro'],
        'Canil 3': ['Mel', 'Maradona'],
        'Canil 4': ['Melissa', 'Bauboa'],
        'Canil 5': ['Maria Flor', 'Maria rosa', 'Mari floco'],
        'Canil 6': ['Guerreiro'],
        'Canil 7': ['Pretao'],
        'Canil 8': ['Pluto', 'Elenico', 'Amarela', 'Amarelinha'],
        'Canil 9': ['Orelhinha', 'Shek', 'Sheila', 'Rex'],
        'Canil 10': ['Bolt (preto e amarelo)', 'Vovó Nina', 'Daly', 'Daisy', 'Libra preto e amarelo'],
        'Canil 11': ['Chasy', 'Ruble'],
        'Canil 12': ['Fox', 'Paulinha', 'Pintinha', '2 machos', 'Amarelão'],
        'Canil 13': ['Isadora'],
        'Canil 14': ['Aberto'],
    },
    'Setor C': {
        'Canil 1': ['Dona Gertrudes', 'Dona Geralda', 'Dona Genoveva', 'Lindinha', 'Tigrão',
                    'Lele (preta do rosto amarela)', 'Morceguinha'],
        'Canil 2': ['Zaza', 'Belo', 'Mel'],
        'Canil 3': ['Beto'],
        'Canil 4': ['Estrela', '2 filhotes macho'],
        'Canil 5': ['Lina', '2 filhotes macho'],
        'Canil 6': ['Pulginha'],
        'Canil 7': ['Marley', 'Tigresa', 'Pingo', 'Pretinha'],
        'Canil 8': [],
        'Canil 9': ['Capivara', 'Benji'],
        'Canil 10': ['Capuccino', 'Café'],
        'Canil 11': ['Maggie', '9 filhotes'],
        'Canil 12': ['Athena', 'Bebezao'],
        'Canil 14 (Geriatria)': ['Dona Jurema Amarela velha', 'Gaia', 'Sr Mário Preto e amarelo',
                                'Dona Josefina preta e amarela meio branca', 'Tritão (preto e marrom)',
                                'Pata mansa', 'Dona neide (preta amarrotada)', 'Alfredo', 'Kira',
                                'Rosinha (preta coleira rosa)', 'Pele', 'Tia da bolinha',
                                'Dona Solzinho amarela com preto velha', 'Dona Olga 2', 'Ofélia',
                                'Tigrada', 'Dona Gertrudes (deitada no pote preta e amarela)',
                                'Mickey', 'Shrek (preto velho)'],
        'Canil 16': ['Tra tra'],
        'Canil 17': ['Eros'],
        'Canil 18': ['Morena'],
        'Canil 19': ['Pico'],
    },
    'Setor D': {
        'Canil 1': ['China', 'Trufao', 'Tsunami'],
        'Canil 2': ['Ivan'],
        'Canil 3': ['Pepa'],
        'Canil 4 (Filhoteiro)': [],
        'Canil 5': ['4 pretos', '1 macho'],
        'Canil 6': ['Gael', 'Gilda'],
        'Canil 7': ['Leôncio', 'Leônidas'],
        'Canil 8': ['Madruga'],
        'Canil 9': ['Cane'],
        'Canil 10': ['Mumuzinho'],
        'Canil 11': ['Morgana preta', 'Manuel', 'Judite'],
        'Canil 12': ['Kiko'],
        'Canil 13': ['Lessi', 'Laurinho', 'Joãozinho'],
        'Canil 14': ['SKY'],
        'Canil 15': ['Bolinha'],
        'Canil 16': ['Rex'],
        'Canil 17': ['Gorila', 'Mane', 'Filomena', 'Álvaro', 'Adão preto pequeno',
                     'Amaro amarelo bravo', 'Ludovico preto e amarelo'],
    },
    'Setor E': {
        'Baia 1': ['Condi'],
        'Baia 2': ['Adriano', 'Japiassu', 'Dan', 'Mauro'],
        'Baia 3': ['Lore'],
        'Baia 4': ['Tiaozinho'],
        'Baia 5': ['Marley'],
        'Baia 6': ['Mike'],
        'Baia 7': ['Bee', 'Arthur', 'Sarah', 'Carioquinho', 'Bojuda', 'Jerry',
                   'Nike (preto e amarelo)', 'Ana marrom e preto (pula)', 'Pirata (preto e branco)',
                   'Zoid (Preto e branco macho um olho de cada cor)', 'Vovô (Amarelo macho)', 'Veludo',
                   'Catarina (caramelo peludo)', 'Vecto (preto e amarelo gordinho)', 'Preto velho',
                   'Sr Ruan (preto e amarelo)'],
    },
    'Setor F': {
        'Baia 1': ['Dentinho', 'Carioquinha', 'Nego da uf', 'Malevolo', 'Raposinha', 'Lindona',
                   'Tigresa', 'Tigrada', 'Ipiranga', 'Leitosa (amarela grande)'],
        'Baia 2': ['Marley'],
        'Baia 3': ['Big ed', 'Rose'],
        'Baia 4 (parte de cima)': ['Doçura amarela pequena', 'Josefina (fica na parte do telhado)',
                                  'Zeus (amarelo grande)', 'Pinto marrom'],
    },
    'Setor G': ['Gatil', 'Amora', 'Zoid nc', 'Perninha (macho)', 'Galã (preto e branco peludo grande)',
                'Garfield', 'Cinza (macho)', 'Jorgina (tigrada)', 'Pintura (tricolor rabo curto) nova',
                'Zulu (preto peludo) nc', 'Amarelão', 'Coringa (preto e branco dos olhos amarelo)',
                'Delícia (preta e branca mãezinha)', 'Sem noção', 'Frajola menino nc', 'Pintada 3 cores menina',
                'Tigrada mansa menina', 'Tigrado bipolar', 'Milk mãezinha', 'Frajola 2 bipolar menino nc',
                'Tigrada mansa menina', 'Preta e branca menina', 'Pinguinha preta menina', 'Menino branco e preto',
                'Acizentada menina', 'Menino amarelo e branco', 'Siamês peluda', 'Cinza bravo',
                'Peluda tigrada menina bipolar', 'Tigrada com preto e amarelo menina', 'Preto e branco menina',
                'Amarelão nc', 'Tortinha preto e branco bravo menino nc', 'Amarela pequena menina',
                'Cinza peludo menina', 'Cinzinha mansa menina', 'Siamês menino', 'Pretinha peluda menina brava',
                'Amarelo russo menino nc', 'Pertinho peludo menino nc', 'Tricolor menina', 'Siamês brava menina',
                'Amarelo pescoço menino', 'Preto e branco menino bravo. Nc', 'Pirata cinza menina',
                'Branco e preto menino', 'Gatuxo branco', 'Mãezinha tigrada peluda nc', 'Alerquina brava'],
        'Setor H': [
        'Parte de trás',
        'Rubi',
        'Kaká',
        'SKY',
        'Pite',
        'Pretinha',
        'Tigresa',
        'Olhinho preto da pata torta',
        'Marta',
        'Sr Zé preto magro',
        'Sorriso',
        'Patinha',
        'Leitão',
        'Ovelho',
        'Biscoito',
        'Bolinha',
        'Vovô azul'
    ],
    'Setor I': [
        'Parte de frente',
        'Sarah',
        'Deco',
        'Pão de queijo',
        'Ricardinho',
        'Mãe da bolinha dona neide',
        'Tutu',
        'Daniel',
        'Zé mane',
        'Raposo',
        'Tais',
        'B4',
        'Laranjinho',
        'Milady',
        'Tonho (bege claro)',
        'Pipoca (cachorra chata que pula na Patrícia)',
        'Capitão olhinho',
        'Pietra (mãezinha)',
        'Leitoa',
        'Caca (velha que comia carniça)',
        'Billy',
        'Dona',
        'Íris(preta e amarela)',
        'Piromaníaco',
        'Dona caco',
        'Safira preta',
        'Torreões',
        'Tadinha',
        'Amora (caramelo)',
        'Bolinha (amarela claro orelhuda)',
        'Bolota (amarela clara orelhuda)',
        'Ze mane',
        'Beijinho (preta)',
        'Sol',
        'Lua',
        'Xerife',
        'Amarelão (bipolar)',
        'Zé (amarelo claro bipolar)',
        'Baby alive',
        'Baby liz'
    ]
}


def salvar_em_excel(dados, nome_arquivo='PIEX_canil.xlsx'):
    # Lista para armazenar os dados de todos os canis
    lista_dados = []

    # Iterar sobre os setores e canis
    for setor, setor_dados in dados.items():
        if isinstance(setor_dados, dict):  # Se o setor tem um dicionário de canis
            for canil, animais in setor_dados.items():
                for animal in animais:
                    lista_dados.append({'Setor': setor, 'Canil': canil, 'Nome': animal})
        elif isinstance(setor_dados, list):  # Se o setor tem uma lista direta de animais
            for animal in setor_dados:
                lista_dados.append({'Setor': setor, 'Canil': '', 'Nome': animal})

    # Criar um DataFrame a partir da lista
    df = pd.DataFrame(lista_dados)

    # Salvar o DataFrame em uma única aba do arquivo Excel
    df.to_excel(nome_arquivo, sheet_name='Todos_Animais', index=False)

    print(f"Dados salvos com sucesso em {nome_arquivo}")

# Exemplo de uso da função
salvar_em_excel(dados)

