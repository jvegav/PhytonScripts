import sys
import webbrowser

urls = {
    "work" : ['https://web.whatsapp.com/','https://github.com/', 'https://francais.lingolia.com/fr/grammaire'],
    "personal" : ['https://www.youtube.com/']
}

def open_webpages(urls):
    for url in urls:
        print(url)
        webbrowser.open(url)


if __name__ == '__main__':
    set_name =  sys.argv[1]
    direcciones = urls[set_name]
    open_webpages(direcciones)