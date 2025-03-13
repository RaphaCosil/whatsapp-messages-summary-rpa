# Message Sending Automation

This project aims to automate communication about student delays and absences, reducing the manual effort of coordination and ensuring fast message delivery to teachers.

## Technologies

- Python  
- Selenium  
- WebDriver (Chrome)  
- Task Scheduling (Cronjobs or Task Scheduler)  

## Features

- Captures messages sent by students via WhatsApp  
- Processes and filters messages  
- Automatically sends messages to teachers  
- Sends a confirmation message in the original group  

## Requirements

- Python 3.x  
- Google Chrome installed  
- WebDriver for Chrome (automatically managed by `webdriver-manager`)  
- Required libraries:  

  `selenium`  

  `webdriver-manager`  

## Installation

1. Clone the repository:  

    ```
    git clone https://github.com/youruser/whatsapp-automation.git
    cd whatsapp-automation
    ```

2. Install dependencies:  

    ```
    pip install -r requirements.txt
    ```

## Configuration

Edit the variables in the code as needed:

```python
  group_origin = "Grupo 2"
  group_destination = "Grupo Destino"
  message = "Esses alunos faltaram ou chegarão atrasados"
  reference = "Ok! Já avisei os professores"
  filter = ["3", "3°"]
```

## Execution

Run the script with:

```
python script.py
```

## How It Works

1. The script opens WhatsApp Web in the browser  
2. The user scans the QR Code  
3. The script collects, filters, and processes messages  
4. The filtered messages are sent to the destination group  
5. The script sends a confirmation message in the original group  
6. WhatsApp Web is automatically closed  

## Notes

- WhatsApp Web may detect automation and restrict usage  
- Adjust wait times (`time.sleep()`) as needed  
