from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.add_argument("--disable-blink-features=AutomationControlled")

group_origin = "Grupo 2"
group_destination = "Grupo Destino"
message = "Esses alunos faltaram ou chegarão atrasados"
reference = "Ok! Já avisei os professores"
filter = ["3", "3°"]

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://web.whatsapp.com")
input("Scan the QR Code in WhatsApp Web and press Enter...")

def open_conversation(contact_name):
    search_box = driver.find_element(By.XPATH, "//div[@contenteditable='true']")
    search_box.clear()
    search_box.send_keys(contact_name)
    time.sleep(2)
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)
            
def get_all_messages():
    all_msgs = []
    msg_elements = driver.find_elements(By.XPATH, "//div[contains(@class, 'message-in') or contains(@class, 'message-out')]")

    for msg in msg_elements:
        try:
            text = msg.find_element(By.XPATH, ".//span[contains(@class, 'selectable-text')]").text.strip()
            all_msgs.append(text)
        except:
            continue

    return all_msgs

def get_messages_after_reference(messages, reference):
    if reference in messages:
        inverted_position = messages[::-1].index(reference)
        last_index = len(messages) - 1 - inverted_position
        return messages[last_index + 1:]
    else:
        return []

def filter_messages(messages, filters):
        return [msg for msg in messages if any(f in msg for f in filters)]

def format_messages_as_list(messages):
    if not messages:
        return None

    formatted_message = ""
    for i in messages:
        formatted_message += f"• {i} "        

    return formatted_message

def send_message(destination, message):
    open_conversation(destination)
    try:
        input_box = driver.find_element(By.XPATH, "//div[@contenteditable='true' and @data-tab='10']")
        input_box.send_keys(message)
        time.sleep(1)
        input_box.send_keys(Keys.RETURN)
        time.sleep(1)
        print(f"Message sent successfully to {destination}!")
    except Exception as e:
        print(f"Error sending message to {destination}: {e}")

def open_new_whatsapp_tab_and_send_message(group_name, message, collected_messages):
    driver.execute_script("window.open('https://web.whatsapp.com');")
    time.sleep(15)
    
    driver.switch_to.window(driver.window_handles[-1])

    open_conversation(group_name)
    send_message(group_name, message)
    send_message(group_name, collected_messages)

def close_whatsapp_and_browser():
    driver.quit()
    print("WhatsApp Web and browser closed successfully.")

def main():
    open_conversation(group_origin)

    collected_messages = get_all_messages()
    print(collected_messages)

    if not collected_messages:
        print("No new messages found after the last reference!")
        driver.quit()
        exit()

    print(f"{len(collected_messages)} new messages captured.")

    collected_messages = get_messages_after_reference(collected_messages, reference)

    collected_messages = filter_messages(collected_messages, filter)

    collected_messages = format_messages_as_list(collected_messages)
    
    print(f"Filtered messages: {collected_messages}")

    if not collected_messages:
        print("No new messages found after the filter!")
        driver.quit()
        exit()

    print(collected_messages)

    send_message(group_origin, reference)

    open_new_whatsapp_tab_and_send_message(group_destination, message, collected_messages)

    close_whatsapp_and_browser()
        
if __name__ == "__main__":
    main()