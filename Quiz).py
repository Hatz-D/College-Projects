import random

pontuacao = 0
qst_acertadas = 0
streak = 0
streak_max = 0
pergunta = 1
frases_acerto = ['Muito bem! :)', 'Você está quase lá! >.<', 'Você está fera! owo', 'Parabéns! ♥', 'Você consegue!', 'Tenho certeza que você vai acertar a próxima também!']
frases_erro = ['Você está quase lá! ^-^', 'Você consegue!', 'Tenho certeza que você vai acertar a próxima! ;)']
alternativas = ['A', 'B', 'C', 'D', 'E']
gabarito_d = {'1': 'D',
            '2': 'A',
            '3': 'B',
            '4': 'A',
            '5': 'D',
            '6': 'E',
            '7': 'A',
            '8': 'D',
            '9': 'B',
            '10': 'C'}

perguntas = [
    'Qual é a proposta do modelo de governo do presidente João Goulart, também conhecido como Jango, considerada como o\nestopim para a tomada do governo pelos militares em 1964?',
    'Qual foi a posição dos Estados Unidos da América frente à ascensão de uma ditadura no contexto pós Segunda Guerra Mundial?',
    'Por qual motivo a Ditadura Militar de 1964 também é conhecida como Ditadura Civil-Militar de 1964?',
    'Como ficaram conhecidos os decretos sancionados no regime ditatorial de 1964 que garantiam aos militares extensos\npoderes e a sua permanência no poder?',
    'Como se davam as votações para as eleições de representantes políticos durante o regime ditatorial?',
    'Dentre os governos dos militares que governaram o Brasil entre 1964 e 1985, qual dos nomes a seguir se destacou por\npromulgar o AI 5 e estar no poder no período mais repressivo e violento do regime militar, ganhando, inclusive, a designação de “anos de chumbo”?',
    'Quais acontecimentos ficaram conhecidos como o “milagre econômico” durante o regime militar brasileiro de 1964?',
    'Qual dos acontecimentos abaixo pode ser relacionado à Política do Pão e Circo como medida de manutenção do governo\natravés da satisfação das massas?',
    'Qual foi a importância da cultura durante o período da Ditadura Civil-Militar de 1964?',
    'De qual maneira o período da Ditadura Civil-Militar de 1964 foi encerrado no Brasil?'
]

respostas = [['A - Conservadorismo econômico', 'B - Aspirações comunistas', 'C - Plano real', 'D - Reforma agrária', 'E - Promulgação da CLT'],
             ['A - Apoio e suporte', 'B - Repúdio, porém sem intervenção', 'C - Intervieram fortemente e tentaram restabelecer a democracia', 'D - Aplicaram sanções econômicas no Brasil', 'E - Aplicaram o embargo econômico no Brasil'],
             ['A - Pois o povo brasileiro, uniformemente, opôs-se veemente ao golpe', 'B - Pois parte considerável da população apoiou o golpe e a manutenção da ditadura', 'C - Pelo fato de parcela civil da população ter sido contra o golpe de estado', 'D - Porque o primeiro governante do período ditatorial foi um civil: Castello Branco', 'E - Nenhum dos itens acima'],
             ['A - Atos Institucionais', 'B - Emendas constitucionais', 'C - Códigos de Hamurabi', 'D - Medidas provisórias', 'E - Atos internacionais'],
             ['A - Eleições diretas através do multipartidarismo', 'B - Eleições indiretas através do multipartidarismo', 'C - Eleições diretas através do bipartidarismo', 'D - Eleições indiretas através do bipartidarismo', 'E - Eleições indiretas através do monopartidarismo'],
             ['A - Ernesto Geisel', 'B - Castello Branco', 'C - Emílio Médici', 'D - João Figueiredo', 'E - Artur de Costa e Silva'],
             ['A - Alto crescimento do PIB e investimentos em infraestrutura através de empréstimos, o que deixou uma dívida externa imensa nos anos seguintes', 'B - Crescimento econômico e diminuição da concentração de renda mesmo em anos posteriores ao término do regime militar', 'C - Alto crescimento do PIB e investimentos em infraestrutura, o que elevou o Brasil à uma das superpotências da época, concorrendo\ncom USA e URSS na Guerra Fria', 'D - Diminuição da concentração de renda e quitação de todas as dívidas externas geradas no período pré ditatorial ', 'E - Alto crescimento econômico e quitação das dívidas externas geradas em governos anteriores dentro do regime militar'],
             ['A - Retomada do direito da liberdade de expressão no Governo Médici', 'B - Promulgação do voto direto e do multipartidarismo no Governo de Costa e Silva', 'C - Anúncio da união do Brasil com os EUA em um conflito armado contra a URSS', 'D - Investimentos em propagandas ufanistas pró governo somadas com a conquista do tricampeonato mundial de futebol pela seleção brasileira', 'E - Promulgação da Lei da Anistia no governo de Ernesto Geisel'],
             ['A - Houve um período de grande enaltecimento da música popular brasileira, que, através de movimentos como o Tropicalismo, passou a\nrejeitar quaisquer formatos de arte estrangeira em território nacional durante o governo ditatorial', 'B - Diversos artistas, como Chico Buarque e Vinícius de Moraes, utilizaram da música e outros meios de expressão para manifestar a\nsua opinião política e criticar o governo ditatorial através de metáforas, servindo como uma forma de protesto', 'C - Houve um período de intensa importação de arte e música estrangeira em território nacional, sendo o movimento do Tropicalismo\num de seus principais representantes, descartando quaisquer vestígios da cultura nacional nas novas composições', 'D - Diversos artistas, como Chico Buarque e Vinícius de Moraes, utilizaram da música e outros meios de expressão para enaltecer os\nmilitares e realizar a manutenção do governo ditatorial vigente', 'E - A cultura e as artes não desempenharam papel algum na construção da identidade cultural brasileira no período do regime\nditatorial tendo em vista que as produções eram censuradas'],
             ['A - Através da forte mobilização social,que resultou em uma revolução orquestrada pelos membros das camadas mais baixas da sociedade', 'B - Através da eleição direta de Tancredo Neves para a presidência do Brasil', 'C - Os governos de Geisel e Figueiredo representaram uma lenta transição do regime ditatorial para a abertura política através da\nrevogação dos Atos Institucionais e da promulgação da Lei da Anistia', 'D - Através de sanções e embargos estabelecidos no Brasil pela URSS para o fim da ditadura em território nacional', 'E - Através das fortes demandas e pressões por parte de membros da elite brasileira para o fim da ditadura militar'],
             ]

explicacoes = [['Resposta incorreta!\n\nAs propostas do governo de Jango eram altamente liberais, conhecidas como Reformas de Base. Dentre elas, a que se\ndestacou como a mais polêmica entre os membros da elite brasileira foi a reforma agrária, que garantia uma redistribuição\nde terras de forma mais igualitária entre a população',
                'Resposta incorreta!\n\nAs propostas do governo de Jango eram liberais, e não comunistas. Dentre elas, a que se destacou como a mais polêmica\nentre os membros da elite brasileira foi a reforma agrária, que garantia uma redistribuição de terras de forma mais\nigualitária entre a população',
                'Resposta incorreta!\n\nO plano real foi um conjunto de reformas econômicas implementadas no Brasil na década de 90. As propostas principais\ndo governo de Jango ficaram conhecidas como Reformas de Base, dentre as quais se destacou a reforma agrária como a\nmais polêmica entre os membros da elite brasileira, que garantia uma redistribuição de terras de forma mais igualitária entre a população',
                'Resposta correta!\n\nAs propostas principais do governo de Jango ficaram conhecidas como Reformas de Base, dentre as quais se destacou a\nreforma agrária como a mais polêmica entre os membros da elite brasileira, que garantia uma redistribuição de terras\nde forma mais igualitária entre a população',
                'Resposta incorreta!\n\nA CLT foi promulgada em 1943 pelo presidente Getúlio Vargas, durante o período do Estado Novo. As propostas principais\ndo governo de Jango ficaram conhecidas como Reformas de Base, dentre as quais se destacou a reforma agrária como a\nmais polêmica entre os membros da elite brasileira, que garantia uma redistribuição de terras de forma mais igualitária entre a população'],
               ['Resposta correta!\n\nOs Estados Unidos da América apoiaram fortemente a implementação de uma ditadura militar no Brasil, principalmente após\no surgimento de movimentos liberais na América Latina, como a Revolução Cubana. Em meio ao contexto de Guerra Fria,\nos EUA temiam que uma ascensão socialista acontecesse próximo de seu território',
                'Resposta incorreta!\n\nOs Estados Unidos da América apoiaram fortemente a implementação de uma ditadura militar no Brasil, principalmente após\no surgimento de movimentos liberais na América Latina, como a Revolução Cubana. Em meio ao contexto de Guerra Fria,\nos EUA temiam que uma ascensão socialista acontecesse próximo de seu território',
                'Resposta incorreta!\n\nOs Estados Unidos da América apoiaram fortemente a implementação de uma ditadura militar no Brasil, principalmente após\no surgimento de movimentos liberais na América Latina, como a Revolução Cubana. Em meio ao contexto de Guerra Fria,\nos EUA temiam que uma ascensão socialista acontecesse próximo de seu território',
                'Resposta incorreta!\n\nOs Estados Unidos da América apoiaram fortemente a implementação de uma ditadura militar no Brasil, principalmente após\no surgimento de movimentos liberais na América Latina, como a Revolução Cubana. Em meio ao contexto de Guerra Fria,\nos EUA temiam que uma ascensão socialista acontecesse próximo de seu território, portanto, sanção econômica alguma foi aplicada ao Brasil',
                'Resposta incorreta!\n\nOs Estados Unidos da América apoiaram fortemente a implementação de uma ditadura militar no Brasil, principalmente após\no surgimento de movimentos liberais na América Latina, como a Revolução Cubana. Em meio ao contexto de Guerra Fria,\nos EUA temiam que uma ascensão socialista acontecesse próximo de seu território, portanto, embargo econômico algum foi implementado no Brasil'],
               ['Resposta incorreta!\n\nPor mais que parcelas da população brasileira tenham se oposto ao golpe de estado aplicado, certas camadas da sociedade,\nprincipalmente das elites brasileiras, apoiaram a tomada do poder pelos militares em 1964 por serem altamente\nconservadoras e contra as propostas de Reformas de Base de João Goulart',
                'Resposta correta!\n\nO termo Ditadura Civil-Militar é amplamente utilizado pois as camadas da elite brasileira, altamente conservadoras, eram\ncontra as propostas de Reformas de Base de João Goulart, isto é, apoiaram a tomada do poder pelos militares em 1964.\nAdemais, certas parcelas das massas, alienadas em relação ao contexto vivido, também ofereceram o seu apoio aos militares',
                'Resposta incorreta!\n\nPor mais que parcelas da população brasileira tenham se oposto ao golpe de estado aplicado, certas camadas da sociedade,\nprincipalmente das elites brasileiras, apoiaram a tomada do poder pelos militares em 1964 por serem altamente\nconservadoras e contra as propostas de Reformas de Base de João Goulart',
                'Resposta incorreta!\n\nO primeiro governante do período ditatorial de 1964 foi o militar Castello Branco, e não um civil. O termo Ditadura\nCivil-Militar é amplamente utilizado pois as camadas da elite brasileira, altamente conservadoras, eram contra as propostas\nde Reformas de Base de João Goulart, isto é, apoiaram a tomada do poder pelos militares em 1964',
                'Resposta incorreta!\n\nO termo Ditadura Civil-Militar é amplamente utilizado pois as camadas da elite brasileira, altamente conservadoras, eram\ncontra as propostas de Reformas de Base de João Goulart, isto é, apoiaram a tomada do poder pelos militares em 1964.\nAdemais, certas parcelas das massas, alienadas em relação ao contexto vivido, também ofereceram o seu apoio aos militares'],
               ['Resposta correta!\n\nOs Atos Institucionais foram decretos oficiais promulgados pelos militares para realizar a manutenção de seu poder no governo,\ndecretos os quais os garantiam amplos poderes e limitavam os direitos da população. Dentre os AIs, o mais temeroso\nficou conhecido como AI 5, que, dentre inúmeras transgressões às liberdades individuais da sociedade, cassava mandatos e proibia manifestações',
                'Resposta incorreta!\n\nEmendas constitucionais são dispositivos para a alteração do texto constitucional de forma democrática. Os Atos Institucionais\nforam decretos oficiais promulgados pelos militares para realizar a manutenção de seu poder no governo, decretos\nos quais os garantiam amplos poderes e limitavam os direitos da população',
                'Resposta incorreta!\n\nO Código de Hamurabi foi o primeiro código de leis da História, de origem na Mesopotâmia. Os Atos Institucionais, por outro\nlado, foram decretos oficiais promulgados pelos militares para realizar a manutenção de seu poder no governo,\ndecretos os quais os garantiam amplos poderes e limitavam os direitos da população',
                'Resposta incorreta!\n\nOs Atos Institucionais foram decretos oficiais promulgados pelos militares para realizar a manutenção de seu poder no governo,\ndecretos os quais os garantiam amplos poderes e limitavam os direitos da população',
                'Resposta incorreta!\n\nOs Atos Institucionais foram decretos oficiais promulgados pelos militares para realizar a manutenção de seu poder no governo,\ndecretos os quais os garantiam amplos poderes e limitavam os direitos da população'],
               ['Resposta incorreta!\n\nO direito ao voto direto foi revogado com a promulgação do primeiro Ato Institucional, cabendo ao Congresso Nacional eleger os\npróximos governantes, enquanto o multipartidarismo foi proibído com o AI 2',
                'Resposta incorreta!\n\nO multipartidarismo foi proibido com a promulgação do segundo Ato Institucional',
                'Resposta incorreta!\n\nO direito ao voto direto foi revogado com a promulgação do primeiro Ato Institucional, cabendo ao Congresso Nacional eleger os\npróximos governantes',
                'Resposta correta!\n\nO exercício ao voto foi limitado com a promulgação do primeiro Ato Institucional, cabendo ao Congresso Nacional eleger os próximos\ngovernantes. Já com a promulgação do AI 2, todos os partidos políticos foram fechados, adotando-se o bipartidarismo\npolítico entre a Aliança Renovadora Nacional (ARENA) e o Movimento Democrático Brasileiro (MDB)',
                'Resposta incorreta!\n\nO bipartidarismo foi implementado com a promulgação do segundo Ato Institucional, polarizando a política entre a Aliança\nRenovadora Nacional (ARENA) e o Movimento Democrático Brasileiro (MDB). É notório mencionar que, embora um partido\ndemocrático tenha existido durante o regime militar, as suas ações eram amplamente restringidas, servindo somente como\num partido de fachada para conter revoltas'],
               ['Resposta incorreta!\n\nO período do governo de Costa e Silva ficou conhecido por ter uma grande repressão, violência e transgressões aos direitos\nhumanos e civis, principalmente após a promulgação do AI 5, que fechou o Congresso Nacional por um tempo e decretou\nestado de sítio no Brasil, limitando ainda mais os direitos da população e expandindo os poderes dos militares',
                'Resposta incorreta!\n\nO período do governo de Costa e Silva ficou conhecido por ter uma grande repressão, violência e transgressões aos direitos\nhumanos e civis, principalmente após a promulgação do AI 5, que fechou o Congresso Nacional por um tempo e decretou\nestado de sítio no Brasil, limitando ainda mais os direitos da população e expandindo os poderes dos militares',
                'Resposta incorreta!\n\nPor mais que o governo de Médici tenha sido tão violento e repressivo quanto o de Costa e Silva, não foi esse o nome do\ngovernante que promulgou o AI 5 que fechou o Congresso Nacional por um tempo e decretou estado de sítio no Brasil, limitando\nainda mais os direitos da população e expandindo os poderes dos militares',
                'Resposta incorreta!\n\nO período do governo de Costa e Silva ficou conhecido por ter uma grande repressão, violência e transgressões aos direitos\nhumanos e civis, principalmente após a promulgação do AI 5, que fechou o Congresso Nacional por um tempo e decretou estado\nde sítio no Brasil, limitando ainda mais os direitos da população e expandindo os poderes dos militares',
                'Resposta correta!\n\nO período do governo de Costa e Silva ficou conhecido por ter uma grande repressão, violência e transgressões aos direitos\nhumanos e civis, principalmente após a promulgação do AI 5, que fechou o Congresso Nacional por um tempo e decretou estado de\nsítio no Brasil, limitando ainda mais os direitos da população e expandindo os poderes dos militares'],
               ['Resposta correta!\n\nNo governo de Médici diversas medidas tomadas, dentre elas a restrição do crédito, a contenção dos salários e o aumento das\ntarifas do setor público, provocaram grandes mudanças econômicas no Brasil, o que aumentou o seu PIB consideravelmente na época.\nNo entanto, tal “milagre” resultou na criação de uma dívida externa imensa para o país, o que,\nconsequentemente, criou uma dependência brasileira por empréstimos externos',
                'Resposta incorreta!\n\nPor mais que tenha havido um grande crescimento na economia brasileira na época, a concentração de renda aumentou infinitamente\nmesmo nos anos posteriores ao término do regime militar, assim como as dívidas externas geradas pelo acúmulo de empréstimos estrangeiros',
                'Resposta incorreta!\n\nPor mais que a economia brasileira tenha apresentado um crescimento considerável na época, esse desenvolvimento não levou o\nBrasil a disputar a hegemonia mundial com USA e URSS na Guerra Fria. O que ocorreu de fato foi um aumento na concentração de\nrenda e nas dívidas externas brasileiras geradas pelo acúmulo de empréstimos estrangeiros',
                'Resposta incorreta!\n\nHouve um imenso aumento na concentração de renda no Brasil e um grande acúmulo de dívidas externas geradas por empréstimos\nestrangeiros, independentemente do crescimento econômico observado pelo aumento do PIB nacional',
                'Resposta incorreta!\n\nHouve um grande acúmulo de dívidas externas geradas por empréstimos estrangeiros na época, independentemente do crescimento\neconômico observado pelo aumento do PIB nacional'],
               ['Resposta incorreta!\n\nO Governo Médici ficou conhecido como um dos períodos mais repressivos da Ditadura Civil-Militar de 1964. Durante esse período,\ninúmeras propagandas ufanistas eram transmitidas à população como forma de enaltecimento do país e da forma de governo\nvigente, dentre elas as campanhas “Brasil, ame-o ou deixo-o” e “Ninguém mais segura esse país”. Ademais, a satisfação\ngerada pela conquista da seleção brasileira do tricampeonato de futebol contribuiu para a efetivação da Política de Pão e Circo vigente',
                'Resposta incorreta!\n\nTanto o voto direto quanto o multipartidarismo foram proibidos com a promulgação dos Atos Institucionais primeiro e segundo,\nrespectivamente, durante o governo de Castello Branco. Durante o regime militar de 1964 inúmeras propagandas ufanistas eram\ntransmitidas à população como forma de enaltecimento do país e da forma de governo vigente, dentre elas as campanhas\n“Brasil, ame-o ou deixo-o” e “Ninguém mais segura esse país”. Ademais, a satisfação gerada pela conquista da seleção\nbrasileira do tricampeonato de futebol contribuiu para a efetivação da Política de Pão e Circo vigente',
                'Resposta incorreta!\n\nO Brasil não entrou em conflitos armados contra a URSS. Durante o regime militar de 1964 inúmeras propagandas ufanistas eram\ntransmitidas à população como forma de enaltecimento do país e da forma de governo vigente, dentre elas as campanhas “Brasil,\name-o ou deixo-o” e “Ninguém mais segura esse país”. Ademais, a satisfação gerada pela conquista da seleção brasileira\ndo tricampeonato de futebol contribuiu para a efetivação da Política de Pão e Circo vigente',
                'Resposta correta!\n\nDurante o regime militar de 1964 inúmeras propagandas ufanistas eram transmitidas à população como forma de enaltecimento do país\ne da forma de governo vigente, dentre elas as campanhas “Brasil, ame-o ou deixo-o” e “Ninguém mais segura esse país”.\nAdemais, a satisfação gerada pela conquista da seleção brasileira do tricampeonato de futebol contribuiu para a efetivação\nda Política de Pão e Circo vigente',
                'Resposta incorreta!\n\nA Lei da Anistia foi promulgada durante o governo de Figueiredo, e não de Geisel. Durante o regime militar de 1964 inúmeras\npropagandas ufanistas eram transmitidas à população como forma de enaltecimento do país e da forma de governo vigente, dentre\nelas as campanhas “Brasil, ame-o ou deixo-o” e “Ninguém mais segura esse país”. Ademais, a satisfação gerada pela\nconquista da seleção brasileira do tricampeonato de futebol contribuiu para a efetivação da Política de Pão e Circo vigente'],
               ['Resposta incorreta!\n\nO movimento Tropicalismo prezava a junção da cultura nacional com a cultura estrangeira. Apesar de ser mais uma das manchas\nna história brasileira, a Ditadura Civil Militar serviu fortemente para a construção de uma identidade cultural brasileira com\na contribuição de artistas como Tom Jobim e Chico Buarque, que criticaram a forma de governo vigente através de\nmetáforas em suas composições',
                'Resposta correta!\n\nApesar de ser mais uma das manchas na história brasileira, a Ditadura Civil Militar serviu fortemente para a construção de uma\nidentidade cultural brasileira com a contribuição de artistas como Tom Jobim e Chico Buarque, que criticaram a forma de governo\nvigente através de metáforas em suas composições. Ademais, o movimento do Tropicalismo fomentou, também, a construção\ndessa identidade através da mesclagem na música nacional com a internacional',
                'Resposta incorreta!\n\nO movimento Tropicalismo prezava a junção da cultura nacional com a cultura estrangeira. Apesar de ser mais uma das manchas na\nhistória brasileira, a Ditadura Civil Militar serviu fortemente para a construção de uma identidade cultural brasileira\ncom a contribuição de artistas como Tom Jobim e Chico Buarque, que criticaram a forma de governo vigente através de\nmetáforas em suas composições',
                'Resposta incorreta!\n\nApesar de ser mais uma das manchas na história brasileira, a Ditadura Civil Militar serviu fortemente para a construção de uma\nidentidade cultural brasileira com a contribuição de artistas como Tom Jobim e Chico Buarque, que criticaram a forma de\ngoverno vigente através de metáforas em suas composições',
                'Resposta incorreta!\n\nApesar de ser mais uma das manchas na história brasileira, a Ditadura Civil Militar serviu fortemente para a construção de uma\nidentidade cultural brasileira com a contribuição de artistas como Tom Jobim e Chico Buarque, que criticaram a forma de\ngoverno vigente através de metáforas em suas composições. Ademais, o movimento do Tropicalismo fomentou, também, a construção\ndessa identidade através da mesclagem na música nacional com a internacional'],
               ['Resposta incorreta!\n\nO fim do regime militar no Brasil não teve seu término através de uma revolução, mas sim por meio de uma lenta e gradual transição\nde um regime totalitário para o início de uma abertura política com a revogação de medidas como o AI 5 e a promulgação\nda Lei da Anistia nos governos de Geisel e Figueiredo, respectivamente',
                'Resposta incorreta!\n\nA eleição de Tancredo Neves para presidência do Brasil se deu de forma indireta, sendo que as eleições seguintes passaram a ser\ndiretas novamente. Com o início do governo de Geisel houve uma lenta e gradual transição de um regime totalitário para o\ninício de uma abertura política com a revogação de medidas como o AI 5 e a promulgação da Lei da Anistia. Tal rumo foi\nseguido pelo seu sucessor político, Figueiredo, que efetivamente colocou fim ao período ditatorial após seus 6 anos de mandato',
                'Resposta correta!\n\nCom o início do governo de Geisel houve uma lenta e gradual transição de um regime totalitário para o início de uma abertura política\ncom a revogação de medidas como o AI 5 e a promulgação da Lei da Anistia. Tal rumo foi seguido pelo seu sucessor político,\nFigueiredo, que efetivamente colocou fim ao período ditatorial após seus 6 anos de mandato',
                'Resposta incorreta!\n\nNão houveram sanções e nem embargos aplicados ao Brasil pela URSS para o fim da ditadura em território nacional. Com o início do\ngoverno de Geisel houve uma lenta e gradual transição de um regime totalitário para o início de uma abertura política com\na revogação de medidas como o AI 5 e a promulgação da Lei da Anistia. Tal rumo foi seguido pelo seu sucessor político,\nFigueiredo, que efetivamente colocou fim ao período ditatorial após seus 6 anos de mandato',
                'Resposta incorreta!\n\nMuitas das camadas da elite brasileira prezavam pela manutenção da ditadura militar justamente pelo aumento da concentração fundiária\ne por temerem uma nova tentativa de reforma agrária. Com o início do governo de Geisel houve uma lenta e gradual\ntransição de um regime totalitário para o início de uma abertura política com a revogação de medidas como o AI 5 e a promulgação\nda Lei da Anistia. Tal rumo foi seguido pelo seu sucessor político, Figueiredo, que efetivamente colocou\nfim ao período ditatorial após seus 6 anos de mandato'],
              ]


def main():
    nome = ''
    print('Olá! Seja bem-vindo(a) ao quiz da Ditadura Civil-Militar de 1964!')
    print('Este é um projeto desenvolvido por alunos do primeiro semestre do curso de ciência da computação do Mackenzie!')
    print('Para começar, digite o seu nome')
    while len(nome) == 0:
        nome = input('\nNome: ')
        nome = nome.capitalize()
    print('\nOlá, {0}! Logo embaixo você vai encontrar as regras de pontuação do quiz:'.format(nome))
    regras()
    questoes()
    print('----------------------------------------')
    print('Você terminou o quiz! Confira os seus resultados abaixo e o gabarito das questões:')
    print('')
    gabarito()
    rank()
    print('\nObrigado por jogar, {}! Até a próxima!'.format(nome))


def questoes():
    global qst_acertadas
    global pontuacao
    global streak
    global streak_max
    global pergunta
    resposta = ''

    for i in perguntas:    #Loop para printar as perguntas
        print('----------------------------------------')
        print('Pergunta ' + str(pergunta) + ')')
        print(i)

        for j in respostas[pergunta - 1]:    #Loop para printar as alternativas de cada pergunta
            resposta = ''
            print(j)

        while resposta not in alternativas:
            resposta = (input('\nDigite a sua resposta: ')).upper()
            if resposta not in alternativas:
                print('Digite uma opção válida! (A/B/C/D/E)')

        checagem(resposta)
        pergunta += 1


def checagem(resposta):
    global qst_acertadas
    global pontuacao
    global streak_max
    global streak
    global pergunta
    contadors = 0
    aux = 5

    for g in explicacoes[pergunta - 1]:   #Loop para definir um index para a resposta do usuário e printar um comentário sobre essa resposta
        if resposta == 'A':
            aux = 0

        elif resposta == 'B':
            aux = 1

        elif resposta == 'C':
            aux = 2

        elif resposta == 'D':
            aux = 3

        elif resposta == 'E':
            aux = 4

        if contadors == aux:   #Eventualmente chegará a essa igualdade
            print('\n', g, sep='')

        contadors += 1

    if resposta == gabarito_d[str(pergunta)]:
        print('')
        print(random.choice(frases_acerto))
        qst_acertadas += 1
        pontuacao += 7

        if streak == 1:
            pontuacao += 1

        elif streak == 2:
            pontuacao += 2

        elif streak >= 3:
            pontuacao += 3

        streak += 1

        if streak > streak_max:
            streak_max = streak

    else:
        print('')
        print(random.choice(frases_erro))
        streak = 0


def regras():
    print('\n1 - Haverá um sistema de pontuação no quiz baseado no número de questões acertadas e na sequência de acertos')
    print('2 - Quanto mais questões acertadas em sequência, maior será a sua pontuação')
    print('3 - A bonificação do streak tem um limite máximo de 3 questões acertadas em sequência')
    print('4 - Responder incorretamente às questões reseta o streak e, por consequência, a bonificação')
    print('5 - Caso não saiba a resposta de alguma pergunta, não pesquise na internet: há a explicação de cada alternativa\nao longo do jogo')
    print('6 - Divirta-se aprendendo história!')


def gabarito():
    print('Gabarito:')
    for i, j in gabarito_d.items():
        print(i,':', j)


def rank():
    global qst_acertadas
    global pontuacao
    global streak_max
    estrelas = ''
    ranking = ''

    if qst_acertadas < 2:
        estrelas = '☆☆☆☆☆'

    elif qst_acertadas < 4:
        estrelas = '★☆☆☆☆'

    elif qst_acertadas < 6:
        estrelas = '★★☆☆☆'

    elif qst_acertadas < 8:
        estrelas = '★★★☆☆'

    elif qst_acertadas < 10:
        estrelas = '★★★★☆'

    elif qst_acertadas == 10:
        estrelas = '★★★★★'

    if pontuacao / 18.8 < 1:
        ranking = 'D'

    elif pontuacao / 18.8 < 2:
        ranking = 'C'

    elif pontuacao / 18.8 < 3:
        ranking = 'B'

    elif pontuacao / 18.8 < 4:
        ranking = 'A'

    elif pontuacao / 18.8 <= 5:
        ranking = 'S'

    print('\nQuestões acertadas: ' + str(qst_acertadas) + '/10 - ' + estrelas)
    print('Pontuação total atingida: ', str(pontuacao) + '/94 - Rank ' + ranking)
    print('Maior sequência de acertos:', streak_max)


main()