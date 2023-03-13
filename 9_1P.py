import tkinter as tk
import requests


class CurrencyConverter:

    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        if from_currency != 'USD':
            amount = amount / self.currencies[from_currency]
        amount = round(amount * self.currencies[to_currency], 4)
        return amount


class App:

    def __init__(self, master):
        self.currency_converter = CurrencyConverter(
            'https://api.exchangerate-api.com/v4/latest/USD')
        master.title('Currency Converter')
        master.geometry('400x200')

        # Currency signs dictionary
        self.currency_signs = {'USD': '$', 'EUR': '€', 'GBP': '£', 'CNY': '¥'}

        # From currency input
        self.from_label = tk.Label(
            master, text='From Currency:', font=('Arial', 14))
        self.from_label.grid(column=0, row=0)
        self.from_var = tk.StringVar()
        self.from_var.set('USD')
        self.from_option = tk.OptionMenu(
            master, self.from_var, 'USD', 'EUR', 'GBP', 'CNY')
        self.from_option.grid(column=1, row=0)

        # To currency input
        self.to_label = tk.Label(
            master, text='To Currency:', font=('Arial', 14))
        self.to_label.grid(column=0, row=1)
        self.to_var = tk.StringVar()
        self.to_var.set('EUR')
        self.to_option = tk.OptionMenu(
            master, self.to_var, 'USD', 'EUR', 'GBP', 'CNY')
        self.to_option.grid(column=1, row=1)

        # Amount input
        self.amount_label = tk.Label(
            master, text='Amount:', font=('Arial', 14))
        self.amount_label.grid(column=0, row=2)
        self.amount_entry = tk.Entry(master, font=('Arial', 14))
        self.amount_entry.grid(column=1, row=2)

        # Conversion output
        self.converted_label = tk.Label(master, text='', font=('Arial', 14))
        self.converted_label.grid(column=1, row=3)

        # Convert button
        self.convert_button = tk.Button(
            master, text='Convert', font=('Arial', 14), command=self.convert)
        self.convert_button.grid(column=0, row=3)

    def convert(self):
        from_currency = self.from_var.get()
        to_currency = self.to_var.get()
        amount = float(self.amount_entry.get())
        converted_amount = self.currency_converter.convert(
            from_currency, to_currency, amount)
        currency_sign = self.currency_signs.get(to_currency, '')
        self.converted_label.config(
            text=f'{currency_sign}{converted_amount:.2f}')


root = tk.Tk()
app = App(root)
root.mainloop()
