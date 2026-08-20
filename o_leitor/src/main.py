import flet as ft
from page_read import read_view

def main(page: ft.Page):

    # handler = lida com eventos
    # "e" = sigla comum para "evento"/"event"
    async def picking_file(e):

        # 1. abrir o seletor;
        # 2. esperar o usuário escolher
        # 3. coloque o resultados em file_selected

        selected_files = await ft.FilePicker().pick_files(allow_multiple=False, allowed_extensions=["pdf"])

        # verifica se há arquivos selecionados
        if selected_files:
            # pega o primeiro item da lista (no caso, o único arquivo selecionado)
            file_selected = selected_files[0]
            # guarda o nome do arquivo direto no objeto 'page' (estado)
            page.selected_filename = file_selected.name
            # muda a rota para /reader
            await page.push_route("/reader")

        # se não tem nada, apenas escreve no terminal que foi cancelado
        else:
            print("Canceled!!!")

    # título da página
    page.title = "O Leitor"

    # função para mudança de rotas/páginas
    def change_route(route):
        # importante para limpar a página antes de receber os novos componentes
        page.views.clear()

        # se for a rota inicial
        if page.route=="/":

            # texto gancho
            text_intro = ft.Text(
                "Selecione seu arquivo PDF:",
                size=20
            )

            # botão para selecionar o arquivo
            btn_add_file =ft.Button(
                content="Escolher PDF",
                icon=ft.Icons.FOLDER_OPEN,
                on_click=picking_file
            )

            page.views.append(
                ft.View(
                    # define a rota
                    route = "/",
                    # adicionandos os componentes na página com ft.Views ao invés do page.add()
                    controls=[
                        ft.AppBar(
                            title=ft.Text("Bem-vindo, leitor!")
                        ),

                        # basicamente movi o ft.Column do final do código (page.add) para o ft.View
                        ft.Column(
                            controls=[text_intro, btn_add_file],

                            expand=True,
                            width=float("inf"),
                            
                            alignment=ft.MainAxisAlignment.CENTER, # Centraliza na vertical
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER
                        )
                    ]
                )
            )

        # se for a rota do leitor
        elif page.route=="/reader":
            page.views.append(
                read_view(page, name_file=page.selected_filename)
            )

        # atualiza a página com os novos elementos
        page.update()

    # coloca a função 'change_route' como navegação de rotas
    page.on_route_change = change_route
    # chama a função para desenhar a tela principal
    # 'page.route' é nossa rota atual
    ## de acordo com a documentação: "current route string"
    change_route(page.route)


# faz o app rodar:
ft.run(main)