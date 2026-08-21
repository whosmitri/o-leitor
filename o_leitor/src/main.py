import flet as ft
from page_read import read_view
from home import home_view

def main(page: ft.Page):

    # título da página
    page.title = "O Leitor"

    # função para mudança de rotas/páginas
    def change_route(route):
        # importante para limpar a página antes de receber os novos componentes
        # limpa todo empilhamento de páginas do Flet
        page.views.clear()

        # se for a rota inicial
        if page.route=="/":
            page.views.append(
                home_view(page)
            )
            
        # se for a rota do leitor
        elif page.route=="/reader":
            page.views.append(
                read_view(page, name_file=page.selected_filename, path_file=page.selected_file_path)
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