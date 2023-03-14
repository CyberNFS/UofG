import tkinter as tk
import requests


class CurrencyConverter:
    """This class is used to retrieve exchange rate information from an API and perform currency conversions."""

    def __init__(self, url):
        # Get exchange rate data from an API and store in self.currencies.
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount):
        # Check for validity
        if from_currency not in self.currencies or to_currency not in self.currencies:
            raise ValueError('Invalid currency codes')

        # Convert amount from from_currency to to_currency
        converted_amount = amount / \
            self.currencies[from_currency] * self.currencies[to_currency]
        return round(converted_amount, 4)


class App:

    def __init__(self, master):
        # Create an instance with exchange rate data from API
        self.currency_converter = CurrencyConverter(
            'https://api.exchangerate-api.com/v4/latest/USD')
        # Main application window
        master.title('Currency Converter')
        master.geometry('400x200')

        # Currency signs dictionary
        self.currency_signs = {'USD': '$', 'EUR': '€',
                               'GBP': '£', 'CNY': '¥', 'PLN': 'zł', 'HUF': 'Ft'}

        # From currency input
        self.from_label = tk.Label(
            master, text='From Currency:', font=('Arial', 14))
        self.from_label.grid(column=0, row=0)
        self.from_var = tk.StringVar()
        self.from_var.set('GBP')
        self.from_option = tk.OptionMenu(
            master, self.from_var, 'USD', 'EUR', 'GBP', 'CNY', 'PLN', 'HUF')
        self.from_option.grid(column=1, row=0)

        # To currency input
        self.to_label = tk.Label(
            master, text='To Currency:', font=('Arial', 14))
        self.to_label.grid(column=0, row=1)
        self.to_var = tk.StringVar()
        self.to_var.set('EUR')
        self.to_option = tk.OptionMenu(
            master, self.to_var, 'USD', 'EUR', 'GBP', 'CNY', 'PLN', 'HUF')
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
        # Get currency values
        from_currency = self.from_var.get()
        to_currency = self.to_var.get()

        # Exceptions
        try:
            # Get input value
            amount = float(self.amount_entry.get())
            # Convert the input amount
            converted_amount = self.currency_converter.convert(
                from_currency, to_currency, amount)
            # Get the currency sign
            currency_sign = self.currency_signs.get(to_currency, '')
            # Special Cases
            if to_currency in ['PLN', 'HUF']:
                converted_amount = f'{converted_amount:.2f}{currency_sign}'
            else:
                converted_amount = f'{currency_sign}{converted_amount:.2f}'
            # Configure the output (with the converted_amount and currency_sign) - f'string
            self.converted_label.config(text=converted_amount)

        except ValueError:
            # Handle invalid input value
            self.converted_label.config(
                text='Unexpected input value.\nPlease only use digits as input.')


root = tk.Tk()
app = App(root)
root.mainloop()
