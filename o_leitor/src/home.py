import flet as ft

def home_view(page: ft.Page):
    # handler = lida com eventos
    # "e" = sigla comum para "evento"/"event"
    async def picking_file(e):

        # 1. abrir o seletor;
        # 2. esperar o usuário escolher
        # 3. coloque o resultados em file_selected

        selected_files = await ft.FilePicker().pick_files(
            allow_multiple=False, # seleciona apenas UM PDF
            allowed_extensions=["pdf"], # selecionas apenas PDF
            with_data=True # recebe bytes
        )

        # verifica se há arquivos selecionados
        if selected_files:
            # pega o primeiro item da lista (no caso, o único arquivo selecionado)
            file_selected = selected_files[0]
            # guarda o nome do arquivo direto no objeto 'page' (estado)
            page.selected_filename = file_selected.name
            # guarda os bytes do arquivo ao invés do path
            page.selected_file_bytes = file_selected.bytes

            # muda a rota para /reader
            await page.push_route("/reader")

        # se não tem nada, apenas escreve no terminal que foi cancelado
        else:
            print("Canceled!!!")

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

    return ft.View(
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