from datetime import datetime
from random import randint

# main point - is to provide one place (class) to manipulate with chain
# of functionalities (classes). This should reduce complexity
# for using by consumer.


class Invoice:

    def __init__(self, customer):
        self.timestamp = datetime.now()
        self.number = self.generate_number()
        self.lines = []
        self.total, self.tax = 0, 0
        self.customer = customer

    def save(self):
        print('Invoice was saved in persistent storage')

    def send_to_printer(self):
        print('Invoice was sent to printer')

    def add_line(self, inoice_line):
        self.lines.append(inoice_line)
        self.calculate()

    def remove_line(self, line_item):
        try:
            self.lines.remove(line_item)
        except ValueError as e:
            print(
                f'Could not remove {line_item} because there is no such '
                f'item in the invoice'
            )

    def calculate(self):
        self.total = sum(x.total * x.amount for x in self.lines)
        self.tax = sum(x.total * x.tax_rate for x in self.lines)

    def generate_number(self):
        return f"{self.timestamp}{randint(1,1000)}"


class InvoiceLine:

    @classmethod
    def fetch(cls, line_item):
        print(f'Get InvoiceLine {line_item}  from persistent storage')
        return cls()

    def save(self):
        print('InvoiceLine was saved in persistent storage')


class Receipt:
    def __init__(self, invoice, payment_type):
        self.invoice = invoice
        self.customer = invoice.customer
        self.payment_type = payment_type

    @classmethod
    def fetch(cls, receipt):
        print(f'Get Receipt {receipt}  from persistent storage')
        return cls()

    def save(self):
        print('Receipt was saved in persistent storage')


class Item:

    def __init__(self):
        self.amount_in_stock = 0

    @classmethod
    def fetch(cls, item_barcode):
        print(f'Get Item {item_barcode} from persistent storage')
        return cls()

    def save(self):
        print('Item was saved in persistent storage')


class Customer:

    @classmethod
    def fetch(cls, customer_code):
        print(f'Get Customer {customer_code} from persistent storage')
        return cls()

    def save(self):
        print('Customer was saved in persistent storage')


class LoyaltyAccount:

    @classmethod
    def fetch(cls, customer):
        print(f'Get LoyaltyAccount {customer} from persistent storage')
        return cls()

    def save(self):
        print('LoyaltyAccount was saved in persistent storage')

    def calculate(self, invoice):
        print(f'Loyalty points was calculated for invoice {invoice}')


class SaleFacade:

    @staticmethod
    def make_invoice(customer_id):
        return Invoice(Customer.fetch(customer_id))

    @staticmethod
    def make_customer():
        return Customer()

    @staticmethod
    def make_item():
        return Item()

    @staticmethod
    def make_invoice_line():
        return InvoiceLine()

    @staticmethod
    def make_receipt(invoice, payment_type):
        return Receipt(invoice, payment_type)

    @staticmethod
    def make_loyalty_account():
        return LoyaltyAccount()

    @staticmethod
    def fetch_customer(customer_code):
        return Customer.fetch(customer_code)

    @staticmethod
    def fetch_item(item_barcode):
        return Item.fetch(item_barcode)

    @staticmethod
    def fetch_invoice_line(line_item_id):
        return InvoiceLine.fetch(line_item_id)

    @staticmethod
    def fetch_receipts(receipt_id):
        return Receipt.fetch(receipt_id)

    @staticmethod
    def fetch_loyalty_account(invoice_id):
        return LoyaltyAccount.fetch(invoice_id)

    def add_item(self, invoice, item_barcode, amount_purchased):
        item = self.fetch_item(item_barcode)
        item.amount_in_stock -= amount_purchased
        item.save()
        invoice_line = self.fetch_invoice_line(item)
        invoice.add_line(invoice_line)

    def finalize(self, invoice):
        invoice.calculate()
        invoice.save()

        loyalty_account = self.fetch_loyalty_account(invoice.customer)
        loyalty_account.calculate(invoice)
        loyalty_account.save()

    def generate_receipt(self, invoice, payment_type):
        receipt = self.make_receipt(invoice, payment_type)
        receipt.save()


def sales_processor(customer_id, item_dict_list, payment_type):
    invoice = SaleFacade.make_invoice(customer_id)

    sales = SaleFacade()
    for item_dict in item_dict_list:
        sales.add_item(invoice, item_dict["barcode"],
                       item_dict["amount_purchased"])
    sales.finalize(invoice)
    sales.generate_receipt(invoice, payment_type)
