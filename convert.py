def pdf_to_book_page(pdf_page):
    pdf_reference = 219
    book_reference = 93
    book_page = pdf_page - (pdf_page - pdf_reference) * ((book_reference - 1) / (pdf_reference - 1))
    return round(book_page)  # Rounding to the nearest whole number

# Example usage:
pdf_page_number = int(input("Enter the PDF page number: "))
book_page_number = pdf_to_book_page(pdf_page_number)
print(f"PDF Page {pdf_page_number} corresponds to Book Page {book_page_number}")
