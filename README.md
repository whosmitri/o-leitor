# O Leitor
um app que lê PDFs

---

## MVP (Minimum Viable Product)
1. Abrir app
2. Tela básica com botão para selecionar o arquivo
3. Mostrar pdf

## Ferramentas:
* Python
* Flet
* pypdfium2

## Criar o APK
Para rodar o comando `build`, é necessário estar dentro do diretório `o_leitor`.

No momento só funciona com o argumento `--android-legacy-packaging` no comando `build`:

```bash
flet build apk --android-legacy-packaging -v
```