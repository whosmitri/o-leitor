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


def read_view(page: ft.Page, name_file, bytes_file) -> ft.View:

    # abre o arquivo no pdfium
    pdf = pdfium.PdfDocument(bytes_file)

    # define o número da página atual (sempre começa em 0)
    page.current_page_index = 0
    # número total de páginas
    total_pages = len(pdf)

    # imagem da página atual do PDF
    page_image = ft.Image(src=get_page_image(pdf_document=pdf, page_number=page.current_page_index), fit=ft.BoxFit.COVER)

    # texto que mostra a página atual em relação ao documento inteiro
    page_counter_text = ft.Text(f"{page.current_page_index + 1}/{total_pages}")

    # cria objeto Share
    # é meio uma "ponte" entre o Flet e o SO
    share = ft.Share()

    async def go_back(e):
        await page.push_route("/")

    def page_back(e):
        if (page.current_page_index==0):
            return
        # atualiza o índice da página
        page.current_page_index -= 1
        
        # aualiza a imagem
        page_image.src = get_page_image(pdf_document=pdf, page_number=page.current_page_index)
        
        # atualiza o texto contador
        page_counter_text.value = f"{page.current_page_index + 1}/{total_pages}"
        
        # redesenha/atualiza a tela no flet
        page.update()

    def page_next(e):
        if (page.current_page_index==(total_pages-1)):
            return

        # atualiza o índice da página
        page.current_page_index += 1
        
        # aualiza a imagem
        page_image.src = get_page_image(pdf_document=pdf, page_number=page.current_page_index)
        
        # atualiza o texto contador
        page_counter_text.value = f"{page.current_page_index + 1}/{total_pages}"
        
        # redesenha/atualiza a tela no flet
        page.update()

    async def share_pdf(e):
        # cria o objeto ShareFile, indicando o arquivo que deve ser compartilhado e seu nome
        file = ft.ShareFile.from_bytes(data=bytes_file, name=name_file)

        # chama a função de compartilhar arquivo
        # Flet informa o SO que quer compartilhar o arquivo
        # SO abre o menu nativo
        # usuário escolhe opção ou cancela
        # o resultado indicando qual app foi escolhido ou se foi cancelado volta para o Flet ('result')
        # await espera o usuário escolher/clicar, sem travar a interface
        result = await share.share_files(
            [file],
            text="Sharing a file from memory"
        )

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
                ),
                actions=[
                    ft.IconButton(
                        ft.Icons.SHARE,
                        on_click=share_pdf
                    )
                ]
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