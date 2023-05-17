import time

import openpyxl as openpyxl
import pandas as pandas
import xlwings as xlwings

# import pywhatkit as pyw
# from keyboard import press
# pyw.sendwhatmsg_to_group_instantly("9Lk1FauDkeB7qzQiZZlFIC", "This is auto-generated message ! Please Ignore", 10, False)
# # pyw.sendwhatmsg("+12269294244", "This is auto-generated message", 18, 28,  15, True)
# press('enter')
# time.sleep(5.0)
# press('Cmd+w')

dataframe1 = xlwings.Book('salah-time.xlsx').sheets("Sheet1")
print(dataframe1)