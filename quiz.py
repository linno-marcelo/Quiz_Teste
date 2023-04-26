import tkinter as tk
import time

# Define as perguntas e respostas do quiz
perguntas = [
    {
        'pergunta': '1 - Quando tratamos da gestão da cadeia de suprimentos, de modo geral, o mais importante é a gestão dos processos que possibilitem um adequado fluxo ao longo de toda a cadeia logística. De acordo com Fleury, Wanke, Figueiredo 2012,\n p. 42  a gestão da cadeia de suprimentos é uma abordagem sistêmica de razoável complexidade que implica alta interação entre participantes, exigindo a consideração simultânea de diversos trade-off. Com base nessas informações, assinale a única alternativa correta quanto ao conceito de trade-off. \n \n ************************************************************************************************************\n',


        'opcoes': [
            ('(A) Trade-offs significam o resultado das pesquisas de marketing feitas ao longo do ano pela empresa,\n que auxiliamna tomada de decisão da empresa sobre um produto ou serviço.', 'A'),
            ('(B) Significa as estratégias utilizadas pelas empresas para persuadir os seus clientes e consumidores com base nas\n ferramentas do marketing empresarial.', 'B'),
            ('(C) Significa fazer a gestão da cadeia de suprimentos com base na terceirização dos seus principais serviços logísticos\n concentrando-se apenas no que sabe fazer.', 'C'),
            ('(D) Os trade-offs representam a estratégia da empresa para vender mais por meio da correta\n escolha dos canais dedistribuição.', 'D'),
            ('(E) Por trade-offs, entende-se uma situação conflitante que se faz necessário tomar uma decisão,\n uma escolha, entreum determinado bem ou serviço por outro bem ou serviço.', 'E')
        ],
        'resposta': 'E'

    },

    {
        'pergunta': '2 - Podemos afirmar que a cadeia de suprimentos é composta por três elos fundamentais, são eles: Produção, Suprimentos e Distribuição.Sendo assim, marque a opção que conceitue corretamente a Produção. \n \n ************************************************************************************************************\n',
        'opcoes': [
            ('(A) Para que esse abastecimento tenha êxito é necessário que osprincipais fornecedores da empresa, sejam parceiros.', 'A'),
            ('(B) É o elo da cadeia em que  os produtos acabados e outros materiais serão transformados em um produto final.', 'B'),
            ('(C) É o elo da cadeia em que as matérias primas e outros materiais serão transformados em um produto final.', 'C'),
            ('(D) Para que esse abastecimento tenha êxito é necessário que os principais clientes da empresa, sejam parceiros.', 'D'),
            ('(E) Faz a interface direta com os clientes da empresa, podendo ser um distribuidor atacadista, um representante ou, um varejista.', 'E')
        ],
        'resposta': 'C'
    },

    {
        'pergunta': '3 - Com referência às contribuições em software agregadas pela Tecnologia de Informações à Logística, o GPS trouxe benefício a atividade logística de: \n \n ************************************************************************************************************\n',
        'opcoes': [
            ('(A) Armazenagem.', 'A'),
            ('(B) Processamento de pedidos.', 'B'),
            ('(C) Transportes. ', 'C'),
            ('(D)  Suprimentos.', 'D'),
            ('(E)  Produção ', 'E')
        ],
        'resposta': 'C'
    },


    {
        'pergunta': '4 - O pleno desempenho logístico é alcançado através da coordenação das atividades logísticas. O desafio está em gerenciar as Atividades relacionadas, de tal forma orquestrada, com o objetivo\n de oferecer o nível elevado de atendimento aos clientes. Considere as afirmações abaixo. Escolha aquelas que estão relacionadas com a atividade logística denominada ESTOQUES. \n \n ************************************************************************************************************\n',
        'opcoes': [
            ('(A) Representa uma rede de relações de trabalho especializadas em movimentar e posicionar o estoque.', 'A'),
            ('(B) A adaptação de serviços tradicionais às modernas exigências de prestação\n de serviços e de redução de custos fazem parte dos requisitos desta atividade.', 'B'),
            ('(C) Um depósito é considerado, geralmente, um lugar onde são guardados estoques de materiais e de produtos.', 'C'),
            ('(D) São poucas as situações em que empresas tem como manter em níveis tão elevados, em função do risco e do custo total proibitivos.', 'D'),
            ('(E) As exigências de uma distribuição bem sucedida só serão plenamente satisfeitas através da cooperação no âmbito de todo o canal.', 'E')
        ],
        'resposta': 'D'
    },

    {
        'pergunta': '5 - A logística tem como objetivo principal colocar as mercadorias ou serviços no lugar certo, na hora certa, nas condições acertadas com o cliente e sempre ao menor custo possível.\n Com o passar dos tempos, houve uma acentuada evolução em termos conceituais, em que a logística dividiu-se em quatro fases. Dentre as afirmativas abaixo, qual delas está relacionada ao Gerenciamento da Cadeia de Suprimento (Supply Chain Management): \n \n ************************************************************************************************************\n',
        'opcoes': [
            ('(A) Fase em que a logística concentrava todos os seus esforços somente na otimização do sistema de transportes e administração de materiais.', 'A'),
            ('(B) Fase que contempla uma visão sistêmica da empresa, incluindo desde fornecedores até os canais de distribuição.', 'B'),
            ('(C) Fase de amplo uso de alianças estratégicas. ', 'C'),
            ('(D) Fase em que a logística atua na gestão da demanda.', 'D'),
            ('(E) Fase em que a logística passa a atuar de forma sistêmica dentro da organização, além de fazer uso de um sistema integrado de informações.', 'E')
        ],
        'resposta': 'B'
    },

]

# Cria uma função para exibir a pergunta atual


def exibir_pergunta():
    global pergunta_index
    pergunta = perguntas[pergunta_index]
    pergunta_label.configure(text=pergunta['pergunta'])
    for i, opcao in enumerate(pergunta['opcoes']):
        opcoes_radios[i].configure(text=opcao[0], value=opcao[1])

# Cria uma função para exibir o resultado da pergunta


def exibir_resultado(resposta):
    if resposta == perguntas[pergunta_index]['resposta']:
        resultado_label.configure(text='\nACERTÔ, MISERÁVI!')
    else:
        resultado_label.configure(text='\nERRRROOOOOOU!')

# Cria uma função para verificar a resposta e exibir o resultado


def verificar_resposta():
    resposta = opcao_selecionada.get()
    exibir_resultado(resposta)
    opcao_selecionada.set('')  # Limpa a seleção do usuário
    global pergunta_index
    if resposta == perguntas[pergunta_index]['resposta']:
        pergunta_index += 1
        if pergunta_index < len(perguntas):
            exibir_pergunta()
        else:
            pergunta_label.configure(text='Fim do quiz!')
    else:
        # Exibe a mesma pergunta após 2 segundos
        resultado_label.after(2000, exibir_pergunta)


# Cria uma função para reiniciar o jogo


def reiniciar_jogo():
    global pergunta_index
    pergunta_index = 0
    exibir_pergunta()


# Cria a janela principal da interface
janela = tk.Tk()
janela.title('GESTÃO DA CADEIA DE SUPRIMENTOS')
janela.geometry("900x500+0+0")


# Cria as widgets da interface
pergunta_label = tk.Label(janela, text=perguntas, wraplength=600)
pergunta_label.pack()

opcao_selecionada = tk.StringVar()
opcoes_radios = []
for i in range(5):
    opcao = tk.Radiobutton(janela, text='', variable=opcao_selecionada)
    opcoes_radios.append(opcao)
    opcao.pack()

verificar_button = tk.Button(
    janela, text='Responder', command=verificar_resposta)
verificar_button.pack()

reiniciar_button = tk.Button(janela, text='Reiniciar', command=reiniciar_jogo)
reiniciar_button.pack()

resultado_label = tk.Label(janela, text='')
resultado_label.pack()

# Inicia o quiz com a primeira pergunta
pergunta_index = 0
exibir_pergunta()

# Inicia a janela principal
janela.mainloop()
