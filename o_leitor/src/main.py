import flet as ft

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
            file_selected = selected_files[0]
            print(file_selected.path)
            print(file_selected.name)
        # se não tem nada, apenas escreve no terminal que foi cancelado
        else:
            print("Canceled!!!")

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
        content="Escolher PDF",
        icon=ft.Icons.FOLDER_OPEN,
        on_click=picking_file
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