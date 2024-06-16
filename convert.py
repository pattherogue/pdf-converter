# Function to convert PDF page number to book page number
def convert_to_book_page(pdf_page_number):
    # Given formula: ( (pdf_page_number) * 93 ) / 219
    book_page_number = (pdf_page_number * 93) / 219
    return int(book_page_number)  # Convert to integer for whole page numbers

# Main function to interact with user input
def main():
    # Input from user
    pdf_page_number = int(input("Enter PDF page number: "))
    
    # Calculate corresponding book page number
    book_page_number = convert_to_book_page(pdf_page_number)
    
    # Output the result
    print(f"The corresponding page in the book is: {book_page_number}")

# Entry point of the script
if __name__ == "__main__":
    main()
