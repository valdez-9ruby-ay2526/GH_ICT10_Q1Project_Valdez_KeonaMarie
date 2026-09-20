# Receipt and SKU Generator - Coffee Shop!
from js import document

# Creates the receipt when the Make Order button is clicked
def create_order(event):
    # Stores customer's name
    customer = document.getElementById("customer").value

    # Establishes subtotal at zero
    subtotal = 0.0

    # Adds the price of all selected items
    if document.getElementById("item1").checked:
        subtotal += float(document.getElementById("item1").value)

    if document.getElementById("item2").checked:
        subtotal += float(document.getElementById("item2").value)

    if document.getElementById("item3").checked:
        subtotal += float(document.getElementById("item3").value)

    if document.getElementById("item4").checked:
        subtotal += float(document.getElementById("item4").value)

    if document.getElementById("item5").checked:
        subtotal += float(document.getElementById("item5").value)

    # Calculates the 12% VAT
    vat = subtotal * 0.12

    # Calculates the final total
    total = subtotal + vat

    # Displays the customer name
    document.getElementById(
        "customer_name"
    ).innerText = customer

    # Displays the subtotal
    document.getElementById(
        "subtotal"
    ).innerText = f"{subtotal:.2f}"

    # Displays VAT
    document.getElementById(
        "vat"
    ).innerText = f"{vat:.2f}"

    # Displays the final total
    document.getElementById(
        "total"
    ).innerText = f"{total:.2f}"

    # Makes receipt visible
    document.getElementById(
        "receipt"
    ).style.display = "block"

# SKU Generator
def generate_sku(event):
    # Gets the category put by user
    category = document.getElementById("category").value

    # Gets prod. name put by the user
    product = document.getElementById("product").value

    # Gets stock quantity
    stock = document.getElementById("stock").value

    # Removes spaces and converts text to uppercase
    category = category.replace(" ", "").upper()
    product = product.replace(" ", "").upper()

    # Takes first 3 characters of the category
    category_code = category[:3]

    # Takes first 3 characters of the product
    product_code = product[:3]

    # Combines category, product, and stock
    sku = category_code + product_code + stock

    # Displays generated SKU
    document.getElementById(
        "sku"
    ).innerText = sku