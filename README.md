# Automação de Envio de Mensagens 

Este projeto tem como objetivo automatizar a comunicação sobre atrasos e faltas de alunos, reduzindo o esforço manual da coordenação e garantindo rapidez no envio das mensagens para os professores.

## Tecnologias Utilizadas

- Python
- Selenium
- WebDriver (Chrome)
- Agendamento de Tarefas (Cronjobs ou Task Scheduler)

## Funcionalidades

- Captura de mensagens enviadas pelos alunos via WhatsApp
- Processamento e filtragem das mensagens
- Envio automatizado das mensagens para os professores
- Envio de confirmação no grupo de origem

## Requisitos

- Python 3.x
- Google Chrome instalado
- WebDriver para Chrome (gerenciado automaticamente pelo `webdriver-manager`)
- Bibliotecas necessárias:
    
    `selenium`
    
    `webdriver-manager`
    

## Instalação

1. Clone o repositório:
    
    ```
    git clone https://github.com/seuusuario/whatsapp-automation.git
    cd whatsapp-automation
    ```
    
2. Instale as dependências:
    
    ```
    pip install -r requirements.txt
    ```
    

## Configuração

Edite as variáveis no código conforme necessário:

```python
  group_origin = "Grupo 2"
  group_destination = "Grupo Destino"
  message = "Esses alunos faltaram ou chegarão atrasados"
  reference = "Ok! Já avisei os professores"
  filter = ["3", "3°"]

```

## Execução

Execute o script com:

```
python script.py

```

## Como funciona

1. O script abre o WhatsApp Web no navegador
2. O usuário escaneia o QR Code
3. O script coleta, filtra e processa as mensagens
4. As mensagens filtradas são enviadas para o grupo de destino
5. O script envia uma mensagem de confirmação no grupo de origem
6. O WhatsApp Web é fechado automaticamente

## Observações

- O WhatsApp Web pode detectar automação e restringir o uso
- Ajuste os tempos de espera (`time.sleep()`) conforme necessário
