import io
import base64

import flet as ft
import pypdfium2 as pdfium

def get_page_image(pdf_document, page_number):

    # pega a primeira página
    pdf_page = pdf_document[page_number]

    # renderiza a imagem em alta resolução (scale=2)
    image_page = pdf_page.render(scale=2).to_pil()

    # precisa enviar a imagem pro flet
    # guardar na memória RAM é mais leve do que salvar e deletar vários arquivos do disco
    # 'io' cria os arquivos virtuais para salvar no buffer
    # o flet só recebe texto
    # base64 = transforma a imagem em uma string

    # cria o buffer na memória RAM
    buffer = io.BytesIO()

    # salva a imagem no buffer
    image_page.save(buffer, format="PNG")

    # pega os bytes salvo no buffer
    img_bytes = buffer.getvalue()

    # transforma em texto utf-8 base64 para o flet
    img_base64 = base64.b64encode(img_bytes).decode("utf-8")

    # retorna o texto (imagem)
    return img_base64


def read_view(page: ft.Page, name_file, path_file) -> ft.View:

    # abre o arquivo no pdfium
    pdf = pdfium.PdfDocument(path_file)

    # define o número da página atual (sempre começa em 0)
    page.current_page_index = 0
    # número total de páginas
    total_pages = len(pdf)

    # imagem da página atual do PDF
    page_image = ft.Image(src=get_page_image(pdf_document=pdf, page_number=page.current_page_index), fit=ft.BoxFit.COVER)

    # texto que mostra a página atual em relação ao documento inteiro
    page_counter_text = ft.Text(f"{page.current_page_index + 1}/{total_pages}")

    async def go_back(e):
        await page.push_route("/")

    def page_back(e):
        # atualiza o índice da página
        page.current_page_index -= 1
        
        # aualiza a imagem
        page_image.src = get_page_image(pdf_document=pdf, page_number=page.current_page_index)
        
        # atualiza o texto contador
        page_counter_text.value = f"{page.current_page_index + 1}/{total_pages}"
        
        # redesenha/atualiza a tela no flet
        page.update()

    def page_next(e):
        # atualiza o índice da página
        page.current_page_index += 1
        
        # aualiza a imagem
        page_image.src = get_page_image(pdf_document=pdf, page_number=page.current_page_index)
        
        # atualiza o texto contador
        page_counter_text.value = f"{page.current_page_index + 1}/{total_pages}"
        
        # redesenha/atualiza a tela no flet
        page.update()

    # ft.View = tela completa
    return ft.View(
        # atualiza a rota para "/reader"
        route = "/reader",

        controls=[
            # AppBar
            ft.AppBar(
                title=ft.Text(name_file, size=18),
                leading=ft.IconButton(
                    icon=ft.Icons.ARROW_BACK,
                    # volta para o início
                    on_click=go_back
                )
            ),

            # conteúdo do página
            # ft.Container embrulha o ft.Text, permitindo maior manipulação do espaço
            ft.Container(
                page_image,
                expand=True,
                alignment=ft.Alignment(0, 0)
            ),

            ft.Row(
                controls=[
                    # botão de volat
                    ft.IconButton(
                        icon=ft.Icons.CHEVRON_LEFT,
                        on_click=page_back
                    ),

                    # texto contador
                    page_counter_text,

                    # botão de avançar    
                    ft.IconButton(
                        icon=ft.Icons.CHEVRON_RIGHT,
                        on_click=page_next
                    )
                ],

                alignment=ft.MainAxisAlignment.CENTER                
            )
        ]
    )