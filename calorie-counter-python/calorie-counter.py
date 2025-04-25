# Calourie Counter - O seu Aplicativos para contar suas calorias

    # Criar uma página de bem-vindo e quero continuar;
    
    # Após clicar no botão irá abrir um pop-up pedindo para inserir o nome e as calorias diárias;
    
    # Após enviar os dados, será redirecionado para uma outra janela para contar as calorias;

        # Titulo: Insira suas calorias
        # Fieldtext: números de calorias
        # Selecionar a refeição
        # Adicionar as calorias a refeição

    # As calorias serão separadas por 5 refeições

        # Café da manhâ;
        # Lanche da manhã;      
        # Almoço;
        # Café da tarde;
        # Jantar;
        # Ceia.
    
    # Após irá calcular o total de calorias e exibir a diferença sobre o valor de calores desejados, ou o aumento;
    
    # Melhorias Futuras
        
    # Fazer um gráfico comparando o total de calorias entre as refeições.
    
    # Collor Pattern
        
        # Bege - #F0EAD2
        # Verde Claro - #DDE5B6
        # Verde Militar - #ADC178
        # Marrom Claro - #A98467
        # Marrom - #6C584C

# Biblioteca Flet - Front-End

import flet as ft

# Função principal
def principal(pagina):
    
    # Função iniciar_app
    def iniciar_app(evento):
        pagina.dialog = janela
        janela.open = True
        pagina.update()
    
    # Função entrar_app
    def entrar_app(evento):
        pagina.remove(titulo_principal)
        pagina.remove(subtitulo_principal)
        pagina.remove(botao_iniciar)
        janela_continuar.open = False
        pagina.add(titulo_contador)
        pagina.add(refeicao_dropdown)
        pagina.update()
        nome_usuario_dado = nome_usuario.value
        meta_calorias_dado = meta_calorias.value
        print(nome_usuario_dado)
        print(meta_calorias_dado)

    # Função continuar_janela

    def continuar_janela(evento):
        janela.open = False
        pagina.dialog = janela_continuar
        janela_continuar.open = True
        pagina.update()

    # Página Inicial

    # Variáveis
    pagina.title = "Calorie Counter"
    titulo_principal = ft.Text("Calorie Counter")
    subtitulo_principal = ft.Text("O seu Aplicativos para contar suas calorias")
    botao_iniciar = ft.ElevatedButton("Começe aqui", on_click=iniciar_app)
    
    pagina.add(titulo_principal)
    pagina.add(subtitulo_principal)
    pagina.add(botao_iniciar)

    # Janela

    # Variáveis
    
    titulo_janela = ft.Text("Bem-vindo ao Calorie Counter")
    titulo_continuar = ft.Text("Estamos quase lá")
    nome_usuario = ft.TextField(label="Coloque seu nome")
    meta_calorias = ft.TextField(label="Digite sua meta de calorias")
    botao_continuar = ft.ElevatedButton("Continuar com calorias",on_click=continuar_janela)
    botao_app = ft.ElevatedButton("Calcular calorias",on_click=entrar_app)
    

    janela = ft.AlertDialog(
            title=titulo_janela,
            content=nome_usuario,
            actions=[botao_continuar]
        )
    
    janela_continuar = ft.AlertDialog(
            title=titulo_continuar,
            content=meta_calorias,
            actions=[botao_app]
        )
    
    # Aplicativo Contador

    # Variáveis

    titulo_contador = ft.Text("Insira seus dados calóricos", size=40)
    subtitulo_contador = print(nome_usuario)
    calorias = ft.TextField(label="Digite as calorias de sua refeição")
    refeicao_dropdown = ft.Dropdown(
        label="Refeições",
        width=200,
        options=[
            ft.dropdown.Option("Café da Manhã"),
            ft.dropdown.Option("Lanche"),
            ft.dropdown.Option("Almoço"),
            ft.dropdown.Option("Lanche da Tarde"),
            ft.dropdown.Option("Jantar"),
            ft.dropdown.Option("Ceia"),
            ft.dropdown.Option("Outros")
        ]
    )


# Inicializar o aplicativo

ft.app(principal)