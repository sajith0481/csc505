def convert_to_words(num):
    """Converts a numeric value to words for check writing."""
    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", 
             "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    
    if num == 0:
        return "Zero"
    
    if num < 10:
        return ones[num]
    
    if num < 20:
        return teens[num - 10]
    
    if num < 100:
        return tens[num // 10] + (" " + ones[num % 10] if num % 10 != 0 else "")
    
    if num < 1000:
        return ones[num // 100] + " Hundred" + (" " + convert_to_words(num % 100) if num % 100 != 0 else "")
    
    if num < 1000000:
        return convert_to_words(num // 1000) + " Thousand" + (" " + convert_to_words(num % 1000) if num % 1000 != 0 else "")
    
    return "Number too large to convert"

def check_writer(amount):
    """Main function to convert a numeric dollar amount into words."""
    try:
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
        
        dollars = int(amount)
        cents = round((amount - dollars) * 100)
        
        dollars_in_words = convert_to_words(dollars)
        cents_in_words = convert_to_words(cents) if cents > 0 else "Zero"
        
        return f"{dollars_in_words} Dollars and {cents_in_words} Cents"
    except Exception as e:
        return f"Error: {str(e)}"

# Test the program
if __name__ == "__main__":
    amount = float(input("Enter the numeric dollar amount: "))
    print(check_writer(amount))
