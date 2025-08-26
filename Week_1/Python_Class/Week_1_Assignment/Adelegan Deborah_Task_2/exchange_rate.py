#  Nigerian Currency Converter (Very Advanced)
#   - Ask for:
#     - Amount in Naira (float)
#     - Exchange rate to US Dollars (float)
#     - Exchange rate to British Pounds (float)
# - Convert and print results with thousands separators and currency symbols, neatly aligned in a table-like format using escape sequences.


naira = float(input("Please enter your amount in naira: "))
dollar = float(input("How much is the current exchange from naira to dollar?: "))
pounds = float(input("How much is the current exchange from naira to pounds?: "))
converted_naira = naira * dollar
converted_pounds = naira * pounds
print()
print(f"\t\t\tCURRENCY CONVERSION\nNaira:\t\t      {naira}\n\n:      {dollar} kW/hr\n\nYour total bill is:   {dollar} in Naira")















































































































