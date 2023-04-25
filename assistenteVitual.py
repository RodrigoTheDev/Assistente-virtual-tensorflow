import funcoes as fc
import exec_test as exe


# variáveis de comandos
DICT_COMMANDS = {'como você está': fc.comoestou, 'hora': fc.tempo, 'data': fc.data, 'dia é hoje': fc.data, 'navegador': fc.navegador, 'melhor time': fc.melhortime, 'modo texto': fc.textMode, 'modo fala': fc.textMode, 'quem é você': fc.quemsoueu, 'finalizar': fc.endapp, 'finaliza': fc.endapp, 'finalize': fc.endapp, 'desligar': fc.endapp, 'apresentação': fc.apresentacao, 'spotify': fc.spotify, 'dormir': fc.awake, 'dormi': fc.awake, 'novo apelido': fc.novoapelido, 'quais apelidos': fc.listarApelidos, 'que apelidos': fc.listarApelidos, 'novo nome': fc.novonome, 'wikipedia' : fc.wikipedia}

AWAKE_COMMANDS = ['bacaxinho', 'abacaxi', 'cachinho', 'cachimbo', 'ximbinha',
                  'maluco', 'acorda porra', 'zé ruela', 'cabeça de lata']

KEYWORDS = list(DICT_COMMANDS.keys())

if __name__ == "__main__":

    # loop principal
    while True:

        print('Aguardando chamada...')
        # aguardando chamada
        comando = fc.recebeInput()
        if fc.chamou(AWAKE_COMMANDS, comando):
            fc.saudacao()
            fc.awake()

        # ao chamar
        while fc.acordado:
            print("Escutando...")

            # recebendo o input
            comando = fc.recebeInput()

            emocao = exe.analisarFrase(comando)
            
            #interpretando as emoções
            if emocao == "alegria":
                fc.falar("Parece que você está bem feliz hoje né")
            elif emocao == "tristeza":
                fc.falar("Não fique triste, estou aqui para te ajudar!")
            elif emocao == "raiva":
                fc.falar("Não precisa ter raiva de mim, posso de ajudar com o que precisar")



            if fc.searchKey(DICT_COMMANDS, KEYWORDS, comando) != -1:
                # executando a função
                DICT_COMMANDS[KEYWORDS[fc.searchKey(
                    DICT_COMMANDS, KEYWORDS, comando)]]()
                
            elif 'youtube' in comando:
                fc.youtube(comando)
            elif 'google' in comando:
                fc.google(comando)
            elif 'como fala' in comando:
                fc.tradutor(comando)
            else:
                fc.openia(comando)
            

