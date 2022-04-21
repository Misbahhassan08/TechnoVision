price=100000
is_goodcredit=True
if is_goodcredit:
    downpayment=0.1*price
else:
    downpayment=0.2*price
print(f'Down Payment: ${downpayment}')
