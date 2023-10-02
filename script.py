from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyautogui
import pandas
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from twilio.rest import Client

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com')
# path = '\\\\storage-server\\invoices\\'
path = input("Enter PATH: ")
time.sleep(3)
excel_data = pandas.read_excel('invoice details.xlsx', sheet_name='invoices')
count = 0

for column in excel_data['Shop'].tolist():
    whatsapp_message = 'Hi Dear Customer, This is YOUR_COMPANY_NAME *{} {}* is the amount of invoice number *{}* that you purchased today in our store. Thank you!'.format(excel_data['Amount'][count],excel_data['Currency'][count],excel_data['InvoiceNumber'][count])
    try:
        # contact number selection
        search_box = WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.CLASS_NAME, '_2vDPL')))
        search_box.click()

        pyautogui.write(str(excel_data['Phone'][count]), interval=0)

        pyautogui.hotkey('enter')

        # attach selection
        attach_button = WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.CLASS_NAME, '_1OT67')))
        attach_button.click()

        # documents selection
        attach_document = WebDriverWait(driver, 35).until(EC.element_to_be_clickable((By.CLASS_NAME, '_2UNQo')))
        attach_document.click()

        # select file
        time.sleep(1)
        pyautogui.write(path+ '\\' + str(excel_data['InvoiceNumber'][count])+'.pdf')
        pyautogui.press('enter')

        # close attachment selection
        WebDriverWait(driver, 35).until(EC.element_to_be_clickable((By.CLASS_NAME, 'aft2yglh')))

        # write message
        pyautogui.write(whatsapp_message)

        # send button selection
        send_button = WebDriverWait(driver, 35).until(EC.element_to_be_clickable((By.CLASS_NAME, '_3wFFT')))
        send_button.click()
        time.sleep(1)
        try:
            pyautogui.press('esc')
        except Exception as e:
            print(e)
        break
    except Exception as e:
        time.sleep(1)
        try:
            pyautogui.press('esc')
        except Exception as e:
            print(e)

    count = count + 1
    time.sleep(1)
    # break

input("End")