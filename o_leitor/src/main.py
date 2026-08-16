import flet as ft

def main(page: ft.Page):
    # título da página
    page.title = "O Leitor"

    # centralizando as coisas
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER

    # boas-vindas simples
    page.appbar = ft.AppBar(
        title=ft.Text("Bem-vindo, leitor!")
    )

    # texto gancho
    text_intro = ft.Text(
        "Selecione seu arquivo PDF:",
        size=20
    )

    # botão para selecionar o arquivo
    btn_add_file =ft.Button(
        "Escolher PDF",
        icon=ft.Icons.FOLDER_OPEN
    )

    # adicionandos os componentes na página
    page.add(
        ft.Column(
            controls=[text_intro, btn_add_file],

            alignment=ft.MainAxisAlignment.CENTER, # Centraliza na vertical
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

# faz o app rodar:
ft.run(main)