# whatsapp-bulk-messages-with-document-file

It is a python script that sends WhatsApp messages automatically from the WhatsApp web application with documents like pdf, images, video, etc.

## Contact me over Telegram: https://t.me/inforkgodara

## Important Note
* This repo is only for the educational purpose not meant for commercial uses.

## Prerequisites

In order to run the python script, your system must have the following programs/packages installed and the contact number should be saved in your phone as well as documents file also needed to be kept with the same name that is in excel sheet.
* Python 3.11.5: Download it from https://www.python.org/downloads
* Chrome v79: Download it from https://chrome.google.com
* Pandas : Run in command prompt **pip install pandas**
* Xlrd : Run in command prompt **pip install xlrd**
* Selenium: Run in command prompt **pip install selenium** 
* Web Driver: Run in command prompt **pip install webdriver_manager**
* Openpyxl: Run in command prompt **pip install openpyxl**

## Approach
* First need to clone this respiratory.
* Generate documents and paste into invoices directory.
* Run python script script.py using py script.py in the terminal.
* The script opens WhatsApp web using chrome.
* User needs to scan QR code from his/her phone.
* Enter in path where invoices saved. This can be fixed in code as a one time task.
* The search the phone number in search bar and send message with document file from excel sheet.
* Once all the message will be sent chrome driver will wait to enter again in order to close browser.

## Legal
* This code is in no way affiliated with, authorized, maintained, sponsored or endorsed by WhatsApp or any of its affiliates or subsidiaries. This is an independent and unofficial software. Use at your own risk. Commercial use of this code/repo is strictly prohibited.

## Code
```
# Program to send bulk messages through WhatsApp web from an excel sheet with documents file like pdf, images, video, etc.
# Author @inforkgodara

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyautogui
import pandas
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
```
Note: The script may not work in case if the HTML of web WhatsApp is changed. So in order to make it work you need to update the class whenever whatsapp changes the its HTML.
