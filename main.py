from PIL import Image, ImageDraw, ImageFont
from datetime import date

background = Image.open('download.jpg')
foreground = Image.open('foreground.jpg')

cordenada = (192,46)
nome = 'Nome: Carlos Alberto Ribas Jr'
nascimento = 'Nascimento: 12/10/1998' 
cpf = 'Cpf: 358.435.843-75'
profissao = 'Profissao: Desenvolvedor'
especialidade = 'Especialidade: Fazer bosta'

data = date.today().strftime('%d/%m/%Y')

imagem = Image.open(r'testePython.jpg')
caminho_font = r"C:Windows\Fonts\ARIALN.TTF"
font = ImageFont.truetype(caminho_font, 24)

rgb_preto = (0,0,0)
desenho = ImageDraw.Draw(imagem)
desenho.text((301, 148), nome, font=font, fill=rgb_preto)
desenho.text((301, 191), nascimento, font=font, fill=rgb_preto)
desenho.text((301, 225), cpf, font=font, fill=rgb_preto)
desenho.text((301, 264), profissao, font=font, fill=rgb_preto)
desenho.text((301, 301), especialidade, font=font, fill=rgb_preto)

imagem.save(f'teste.png')
