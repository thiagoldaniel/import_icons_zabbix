# import_icons_zabbix
Importação Massiva de Icones para o Zabbix.

Importe rapidamente icones em formato PNG presentes em um diretorio para o zabbix de forma facil e segura.

Testado no Zabbix 7.

# Procedimento de Instalação
pip install zabbix-api

Antes: gere um API token em Administração → Tokens de API e copie.

Ajuste a variavel API_TOKEN com o Token Criado.

    API_TOKEN = "aaaaabbbbbcccccddddd"     # Gere no frontend

Defina o diretorio onde estarão armazenados os icones em formato png. Podem ser inclusive colocados em subpastas.

    ICON_DIR  = r"/tool/icones"                  # Pasta raiz


# Procedimento de Execução

Execute o comando abaixo para que o programa se execute e proceda com a importação de todos os icones presentes no diretorio e subdiretorios definido.

python3 importa_icones.py



