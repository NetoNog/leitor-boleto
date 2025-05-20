import cv2
import tkinter as tk
from tkinter import filedialog
from pyzbar.pyzbar import decode

def escolher_arquivo():
    """Abre uma janela para selecionar um arquivo de imagem."""
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal
    arquivo = filedialog.askopenfilename(title="Selecione o boleto", filetypes=[("Imagens", "*.jpg;*.png;*.jpeg")])
    return arquivo

def ler_codigo_de_barras(imagem_boleto):
    """Lê e retorna apenas o código de barras da imagem."""
    if not imagem_boleto:
        return "Nenhum arquivo selecionado."

    imagem = cv2.imread(imagem_boleto)
    codigos_de_barra = decode(imagem)
    
    for codigo in codigos_de_barra:
        return codigo.data.decode('utf-8')  # Retorna apenas o primeiro código encontrado
    
    return "Código de barras não encontrado."

if __name__ == "__main__":
    caminho_imagem = escolher_arquivo()
    codigo_barras = ler_codigo_de_barras(caminho_imagem)
    print(f"Código de Barras: {codigo_barras}")
