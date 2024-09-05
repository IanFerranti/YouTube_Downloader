# YouTube Downloader
Este projeto é uma ferramenta para baixar vídeos do YouTube e convertê-los em diferentes formatos (MP4 ou MP3) diretamente do Google Colab.

## Funcionalidades

- **Download de Vídeos**: Baixa vídeos do YouTube no formato MP4.
- **Conversão para MP3**: Converte o áudio do vídeo em um arquivo MP3.
- **Interface Simples**: Interface interativa no Google Colab para facilitar o uso.

## Como Usar

1. **Clone o Repositório**

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio

2. **Instale as Dependências**

  No Google Colab, execute as seguintes células para instalar as bibliotecas necessárias:

  ```bash
  !pip install pytubefix moviepy ipywidgets
  ```

3. **Execute o Código**

  Copie e cole o seguinte código em uma célula do Google Colab e execute-a:

  ```python
  import ipywidgets as widgets
from IPython.display import display
from pytubefix import YouTube
from moviepy.editor import AudioFileClip
import os
from google.colab import files

def download_video(url, format_choice):
    try:
        yt = YouTube(url)
        stream = None
        download_path = "/content"
        
        if format_choice == "MP4":
            stream = yt.streams.get_highest_resolution()
            file_path = os.path.join(download_path, yt.title + ".mp4")
            stream.download(download_path)
            print("O vídeo foi baixado com sucesso!")
            files.download(file_path)
        
        elif format_choice == "MP3":
            stream = yt.streams.filter(only_audio=True).first()
            out_file = os.path.join(download_path, yt.title + ".mp4")
            file_path = os.path.join(download_path, yt.title + '.mp3')
            stream.download(download_path)
            
            # Converter para MP3
            audio_clip = AudioFileClip(out_file)
            audio_clip.write_audiofile(file_path)
            audio_clip.close()
            os.remove(out_file)  # Remove o arquivo .mp4
            print("O áudio foi baixado e convertido para MP3!")
            files.download(file_path)
        
        # Limpeza dos arquivos temporários
        for file in os.listdir(download_path):
            file_path = os.path.join(download_path, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
        
    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

def on_button_click(b):
    url = url_text.value
    format_choice = format_dropdown.value
    if format_choice in ["MP4", "MP3"]:
        download_video(url, format_choice)
    else:
        print("Formato inválido. Escolha entre MP4 e MP3.")

# Criar widgets
url_text = widgets.Text(
    description='URL:',
    placeholder='Insira a URL do vídeo',
    layout=widgets.Layout(width='80%')
)

format_dropdown = widgets.Dropdown(
    options=['MP4', 'MP3'],
    value='MP4',
    description='Formato:',
    layout=widgets.Layout(width='50%')
)

download_button = widgets.Button(
    description='Baixar',
    button_style='success',
)

download_button.on_click(on_button_click)

# Exibir widgets
display(url_text, format_dropdown, download_button)
```
