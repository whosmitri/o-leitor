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
* PyMuPDF

## Criar o APK
Para rodar o comando `build`, é necessário estar dentro do diretório `o_leitor`.

```bash
flet build apk -v
```

Para instalar no celular Android com `adb` e pelo Windows:

```bash
adb install '.\build\apk\O Leitor.apk'
```