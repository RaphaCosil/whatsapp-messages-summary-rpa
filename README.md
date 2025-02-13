# Automação de Envio de Mensagens para Professores

## Descrição
Este projeto tem como objetivo automatizar o processo de comunicação entre alunos e professores sobre atrasos e faltas nas aulas. Atualmente, a coordenadora do curso, Fe Godoy, realiza essa tarefa manualmente todos os dias, repassando as mensagens dos alunos para os professores.

Com o uso do **Selenium** como RPA (Robotic Process Automation), a ferramenta permitirá que esse processo seja realizado de forma automática, reduzindo o esforço manual e garantindo que as mensagens sejam enviadas de maneira rápida e eficiente.

## Tecnologias Utilizadas
- **Python**
- **Selenium**
- **WebDriver** (Chrome ou Firefox)
- **Agendamento de Tarefas (Cronjobs ou Task Scheduler)**

## Funcionalidades
- Captura das mensagens enviadas pelos alunos (via formulário, chatbot ou outro meio de comunicação)
- Processamento e organização das mensagens
- Envio automatizado das mensagens para os professores via e-mail, WhatsApp ou outro canal de comunicação
- Logs das mensagens enviadas para rastreamento

## Como Utilizar
1. **Configuração Inicial:**
   - Instale as dependências do projeto:
     ```bash
     pip install selenium
     ```
   - Configure o WebDriver compatível com o navegador utilizado.

2. **Execução da Automação:**
   - Execute o script principal:
     ```bash
     python main.py
     ```
   - O RPA capturará as mensagens e as enviará automaticamente para os professores.

3. **Agendamento Automático:**
   - Para evitar execuções manuais, configure um **cronjob** (Linux/macOS) ou **Task Scheduler** (Windows) para rodar o script automaticamente.

## Contribuição
Caso queira contribuir para o projeto, siga os passos:
1. Faça um fork do repositório
2. Crie uma branch com sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas alterações (`git commit -m 'Adiciona nova feature'`)
4. Faça um push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## Licença
Este projeto está sob a licença MIT. Sinta-se à vontade para usá-lo e modificá-lo conforme necessário.

