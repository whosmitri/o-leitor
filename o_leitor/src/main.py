import flet as ft
from page_read import read_view
from home import home_view

THEMES = {
    "light": {
        "primary": "#463F3A",
        "on_primary": "#F4F3EE",
        "secondary": "#8A817C",
        "on_secondary": "#F4F3EE",
        "tertiary": "#E0AFA0",
        "on_tertiary": "#463F3A",
        "surface": "#F4F3EE",
        "on_surface": "#463F3A",
        "outline": "#BCB8B1",
    },
    "dark": {
        "primary": "#F4F3EE",
        "on_primary": "#463F3A",
        "secondary": "#BCB8B1",
        "on_secondary": "#F4F3EE",
        "tertiary": "#E0AFA0",
        "on_tertiary": "#463F3A",
        "surface": "#463F3A",
        "on_surface": "#F4F3EE",
        "outline": "#BCB8B1",
    }
}

def main(page: ft.Page):

    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(**THEMES["light"]),

        button_theme=ft.ButtonTheme(
            style=ft.ButtonStyle(
                bgcolor=THEMES["light"]["tertiary"],
                color=THEMES["light"]["on_tertiary"],
            )
        ),

        text_theme=ft.TextTheme(
            body_medium=ft.TextStyle(color=THEMES["light"]["on_surface"]),
            title_medium=ft.TextStyle(color=THEMES["light"]["secondary"]),
            title_large=ft.TextStyle(color=THEMES["light"]["secondary"], weight=ft.FontWeight.BOLD),
            headline_small=ft.TextStyle(color=THEMES["light"]["secondary"], weight=ft.FontWeight.BOLD),
        ),

        appbar_theme=ft.AppBarTheme(
            shape=ft.RoundedRectangleBorder(radius=12),
        ),
    )

    page.dark_theme = ft.Theme(
        color_scheme=ft.ColorScheme(**THEMES["dark"]),

        button_theme=ft.ButtonTheme(
            style=ft.ButtonStyle(
                bgcolor=THEMES["dark"]["tertiary"],
                color=THEMES["dark"]["on_tertiary"],
            )
        ),

        text_theme=ft.TextTheme(
            body_medium=ft.TextStyle(color=THEMES["dark"]["on_surface"]),
            title_medium=ft.TextStyle(color=THEMES["dark"]["on_surface"]),
        ),

        appbar_theme=ft.AppBarTheme(
            shape=ft.RoundedRectangleBorder(radius=12),
        ),
    )

    page.theme_mode = ft.ThemeMode.SYSTEM

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
                read_view(page, name_file=page.selected_filename, bytes_file=page.selected_file_bytes)
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