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
No momento só funciona com o argumento `--android-legacy-packaging` no comando `build`:

```bash
flet build apk --android-legacy-packaging -v"
```