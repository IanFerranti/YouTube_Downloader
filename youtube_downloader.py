from pytubefix import YouTube
from moviepy.editor import AudioFileClip
import os

def download_video(url, format_choice):
    try:
        yt = YouTube(url)
        stream = None

        # Obtém o diretório de trabalho atual
        download_path = os.path.join(os.getcwd(), "downloads")

        # Cria o diretório de downloads se não existir
        if not os.path.exists(download_path):
            os.makedirs(download_path)

        if format_choice == "mp4":
            stream = yt.streams.get_highest_resolution()
            file_path = os.path.join(download_path, yt.title + ".mp4")
            stream.download(download_path)
            print(f"O vídeo foi baixado com sucesso! Salvo em {file_path}")

        elif format_choice == "mp3":
            stream = yt.streams.filter(only_audio=True).first()
            out_file = os.path.join(download_path, yt.title + ".mp4")
            file_path = os.path.join(download_path, yt.title + '.mp3')
            stream.download(download_path)

            # Converter para MP3
            audio_clip = AudioFileClip(out_file)
            audio_clip.write_audiofile(file_path)
            audio_clip.close()
            os.remove(out_file)  # Remove o arquivo .mp4
            print(f"O áudio foi baixado e convertido para mp3! Salvo em {file_path}")

        print("Download e conversão concluídos!")

    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

if __name__ == "__main__":
    url = input("Insira a URL do vídeo: ")
    format_choice = input("Escolha o formato (mp4 ou mp3): ")
    if format_choice in ["mp4", "mp3"]:
        download_video(url, format_choice)
    else:
        print("Formato inválido. Escolha entre mp4 e mp3.")