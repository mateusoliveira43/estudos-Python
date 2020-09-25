import os
import fnmatch

# https://ffmpeg.org/ffmpeg.html

comando_ffmpeg = r'C:\Users\Mateus\Documents\ProjetosPYTHON\ffmpeg\ffmpeg.exe'

codec_video = '-c:v libx264'
crf = '-crf 23'
preset = '-preset ultrafast'
codec_audio = '-c:a aac'
bitrate_audio = '-b:a 320k'
debug = '-ss 00:00:00 -to 00:00:00'  # Ajustar para o tamanho do vídeo hh:mm:ss
acelerar_video = '-filter:v "setpts=0.25*PTS"'
sem_audio = '-an'

caminho_origem = r'C:\Users\Mateus\Videos'

for raiz, pastas, arquivos in os.walk(caminho_origem):
    for arquivo in arquivos:
        if fnmatch.fnmatch(arquivo, '*.mp4'):
            caminho_completo = os.path.join(raiz, arquivo)
            nome_arquivo, ext_arquivo = os.path.splitext(caminho_completo)
            # caminho_legenda = nome_arquivo + '.srt'
            #
            # if os.path.isfile(caminho_legenda):
            #     input_legenda = f'-i "{caminho_legenda}"'
            #     map_legenda = '-c:s srt -map v:0 -map a -map 1:0'
            # else:
            #     input_legenda = ''
            #     map_legenda = ''

            arquivo_saida = f'{nome_arquivo}_NOVO{ext_arquivo}'

            # comando = f'{comando_ffmpeg} -i "{caminho_completo}"{input_legenda} ' \
            #           f'{codec_video} {crf} {preset} {codec_audio} {bitrate_audio} ' \
            #           f'{debug} {map_legenda} "{arquivo_saida}"'
            comando = f'{comando_ffmpeg} -i "{caminho_completo}" {acelerar_video} ' \
                      f'{debug} {sem_audio} "{arquivo_saida}"'
            # comando = f'{comando_ffmpeg} -i "{caminho_completo}" ' \
            #           f'{debug} {sem_audio} "{arquivo_saida}"'
            # print(comando)
            os.system(comando)