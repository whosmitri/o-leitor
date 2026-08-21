import flet as ft

def read_view(page: ft.Page, name_file) -> ft.View:
    async def go_back(e):
        await page.push_route("/")

    # ft.View = tela completa
    return ft.View(
        # atualiza a rota para "/reader"
        route = "/reader",

        controls=[
            # AppBar
            ft.AppBar(
                title=ft.Text(name_file),
                leading=ft.IconButton(
                    icon=ft.Icons.ARROW_BACK,
                    # volta para o início
                    on_click=go_back
                )
            ),

            # conteúdo do página
            # ft.Container embrulha o ft.Text, permitindo maior manipulação do espaço
            ft.Container(
                content=ft.Text("Visualizar o PDF aqui", size=20),
                alignment=ft.alignment.center
            )
        ]
    )