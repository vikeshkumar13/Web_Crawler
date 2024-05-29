import time
import pandas as pd
import requests
from bs4 import BeautifulSoup


def shiva1():
    name = []
    price = []
    stay_details = []

    url = ('https://www.booking.com/searchresults.en-gb.html?ss=Goa%2C+India&ssne=Shimla&ssne_untouched=Shimla&efdco=1'
           '&label=gen173nr'
           '-1FCAEoggI46AdIM1gEaGyIAQGYAQm4ARfIAQzYAQHoAQH4AQuIAgGoAgO4Aq2dibEGwAIB0gIkZTFmNWU0MjktZWU1OC00YWNiLTg1NjktOWZlNGY1MzlkZjFm2AIG4AIB&sid=9a25ee2684ded45821197dc02786f4d0&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=4127&dest_type=region&checkin=2024-04-25&checkout=2024-04-28&group_adults=2&no_rooms=1&group_children=0')
    HEADERS = ({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US, en;q=0.5'})

    req = requests.get(url, headers=HEADERS)
    time.sleep(4)

    web_content = BeautifulSoup(req.content, 'html.parser')

    hotel_name = web_content.findAll('div', {'class': 'f6431b446c a15b38c233'})
    for i in hotel_name:
        name.append(i.text)
    time.sleep(4)
    hotel_price = web_content.findAll('div', {'class': 'e84eb96b1f a661120d62'})
    for i in hotel_price:
        price.append(i.text)
    time.sleep(4)
    hotel_stay = web_content.findAll('div', {'class': 'abf093bdfe f45d8e4c32'})
    for i in hotel_stay:
        price.append(i.text)
    time.sleep(4)

    data = {'hotel_name': name, 'price': price, 'stay_details': hotel_stay}
    df = pd.DataFrame.from_dict(data, orient='index')
    new_df = df.T
    new_df.to_csv('booking.csv')
    print('done')


#shiva1()

def shiva2():
    from openpyexcel import load_workbook

    filename = 'booking.xlsx'
    wb = load_workbook(filename=filename)
    ws1 = wb['Sheet1']
    ws2 = wb['Sheet2']

    ws1.cell(column=1, row=1, value='name')
    ws2.cell(column=1, row=1, value='roll')

    while True:
        name = input('ENTER NAME->')
        roll = int(input('ENTER ROLL->'))

        ws1.cell(column=1, row=ws1.max_row + 1, value=name)
        ws2.cell(column=1, row=ws2.max_row + 1, value=roll)

        wb.save(filename=filename)

        x = int(input('1->More\n2->exit\nchoose->'))

        if x == 2:
            print('Thank You')
            exit()


#shiva2()

def shiva4():
    from openpyexcel import load_workbook
    filename = 'booking.xlsx'
    wb = load_workbook(filename=filename)
    ws = wb['Sheet2']
    temp = ws.cell(column=1, row=2).value
    temp = temp + 100
    print(temp)
    ws.cell(column=2, row=2, value=temp)
    temp2 = temp * 10
    print(temp2)
    ws.cell(column=3, row=3, value=temp2)
    wb.save(filename=filename)


#shiva4()


def inventory():
    from openpyexcel import load_workbook
    import pandas as pd
    from openpyexcel.styles import PatternFill

    file_name = 'inventory.xlsx'
    wb = load_workbook(filename=file_name)
    ws = wb['Sheet1']

    ws.cell(column=1, row=1, value='Date')
    cell = ws['A1']
    cell.fill = PatternFill(start_color='FF0000', fill_type='solid')
    ws.cell(column=2, row=1, value='Description')
    cell = ws['B1']
    cell.fill = PatternFill(start_color='FF0000', fill_type='solid')
    ws.cell(column=3, row=1, value='Amount')
    cell = ws['C1']
    cell.fill = PatternFill(start_color='FF0000', fill_type='solid')
    ws.cell(column=4, row=1, value='PaymentMode')
    cell = ws['D1']
    cell.fill = PatternFill(start_color='FF0000', fill_type='solid')
    ws.cell(column=5, row=1, value='ModeName')
    cell = ws['E1']
    cell.fill = PatternFill(start_color='FF0000', fill_type='solid')

    while True:

        desc = input('Enter Product Details ->')
        amount = float(input('Enter Amount ->'))

        payment_mode = input('Enter Payment Mode ->')
        if payment_mode == 'cc':
            cell.fill = PatternFill(start_color='FF0000', fill_type='solid')

        mode_name = input('Enter Mode Name ->')

        last_row = ws.max_row + 1

        ws.cell(column=2, row=last_row, value=desc)
        ws.cell(column=3, row=last_row, value=amount)
        ws.cell(column=4, row=last_row, value=payment_mode)
        ws.cell(column=5, row=last_row, value=mode_name)

        wb.save(filename=file_name)
        repeat_var = int(input('1->More\n2->Clear_Cell\n3->Exit\nChoose->'))

        if repeat_var == 2:
            ws.delete_rows(2, 100)
            print('Rows Deleted Successfully')

        elif repeat_var >= 2:
            print('Thank you')
            exit()


#inventory()

def inventory1():
    from openpyexcel import load_workbook
    from openpyexcel.styles import PatternFill

    file_name = 'inventory.xlsx'
    wb = load_workbook(filename=file_name)
    ws = wb['Sheet1']

    ws.cell(column=1, row=1, value='Date')
    cell = ws['A1']
    cell.fill = PatternFill(start_color='FF0000', fill_type='solid')
    ws.cell(column=2, row=1, value='Description')
    cell = ws['B1']
    cell.fill = PatternFill(start_color='FF0000', fill_type='solid')
    ws.cell(column=3, row=1, value='Amount')
    cell = ws['C1']
    cell.fill = PatternFill(start_color='FF0000', fill_type='solid')
    ws.cell(column=4, row=1, value='PaymentMode')
    cell = ws['D1']
    cell.fill = PatternFill(start_color='FF0000', fill_type='solid')
    ws.cell(column=5, row=1, value='ModeName')
    cell = ws['E1']
    cell.fill = PatternFill(start_color='FF0000', fill_type='solid')

    while True:

        menu = int(input('1->Insert\n2->Delete\n3->Exit\nChoose->'))
        last_row = ws.max_row + 1

        if menu == 1:

            desc = input('Enter Product Details ->')
            try:
                amount = float(input('Enter Amount ->'))
            except ValueError:
                print('Enter number only')
                amount = float(input('Enter Amount ->'))

            payment_mode = input('Enter Payment Mode ->')
            print('Payment mode like-CC,Cash,Upi')

            mode_name = input('Enter Mode Name ->')

            ws.cell(column=2, row=last_row, value=desc)
            ws.cell(column=3, row=last_row, value=amount)
            ws.cell(column=4, row=last_row, value=payment_mode)
            ws.cell(column=5, row=last_row, value=mode_name)

            wb.save(filename=file_name)

        elif menu == 2:

            ws.delete_rows(2, 100)
            print('data deleted')
            wb.save(filename=file_name)

        elif menu >= 3:
            exit()


inventory1()
