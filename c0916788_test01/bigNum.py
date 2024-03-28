# importing the double linked list
from dblyLnkdLst import DblyLnkdLst

class BigNum:
    def __init__(self, value = '0'):
        # validating the value for the string type
        if not isinstance(value , str):
            raise Exception("Value must be of string type")
        self.digits = DblyLnkdLst() #creating doubly linked list object
        self.sign = '+' # sign variable holds either + or -

        # checking the sign from the value
        if (value[0] == '-'):
            self.sign = '-'
            value = value[1:] # striping the value excluding the sign
        for digit in reversed(value):
            # adding to the linked list
            self.digits.addLast(int(digit))
        # self.digits.display()

    # addition of the magic methods like add, subtract, mul and div
    def __add__(self, other):
        
        # incorporating the sign
        # if both numbers are negative, then perform addition and return with - sign
        # if(self.sign == '-' and other.sign == '-'):
        #     result = self + other
        if self.sign == '-':
            result = other - self
        elif other.sign == '-':
            result = self - other
        else: # if both numbers are positive perform addition
            result = BigNum() # creating a new BigNum object to hold the result
            carry = 0
            pointer1 = self.digits.head
            pointer2 = other.digits.head

            while pointer1 or pointer2 or carry:
                # digit1 and digit2 holds the data of pointer1 and pointer2 if present otherwise it hold 0
                digit1 = pointer1.data if pointer1 else 0
                digit2 = pointer2.data if pointer2 else 0
                total = digit1 + digit2 + carry
                carry = total//10 # it returns value removing the last digit -> 543//10 == 54
                # // operator removes last digit
                # % operator returns last digit

                # storing the bits from the result
                result.digits.addLast(total%10)

                # Updating the pointers
                pointer1 = pointer1.next if pointer1 else None
                pointer2 = pointer2.next if pointer2 else None

            # strip the leading zeros 
            while len(result.digits) > 1 and result.digits.head.data == 0:
                    result.digits.removeFirst()
        return result
    
    def __sub__(self, other):
        result = BigNum() # creating a new BigNum object to hold the result
        borrow = 0
        pointer1 = self.digits.head
        pointer2 = other.digits.head

        while pointer1 or pointer2:
            # digit1 and digit2 holds the data of pointer1 and pointer2 if present otherwise it hold 0
            digit1 = pointer1.data if pointer1 else 0
            digit2 = pointer2.data if pointer2 else 0
            difference = digit1 - digit2 - borrow
            if difference < 0 :
                difference += 10
                borrow = 1
            else : borrow = 0

            # storing the bits from the result
            result.digits.addLast(difference)

            # Updating the pointers
            pointer1 = pointer1.next if pointer1 else None
            pointer2 = pointer2.next if pointer2 else None
            
            # strip the leading zeros 
            while len(result.digits) > 1 and result.digits.head.data == 0:
                    result.digits.removeFirst()
        return result
    
    def _eq_(self, other):
        return self.sign == other.sign and self.digits == other.digits

    def __str__(self):
        result = ''
        if self.sign == '-':
            result += '-'
        current = self.digits.tail
        while current:
            result += str(current.data)
            current = current.prev
        return result

    def __len__(self):
        return len(self.digits)

# testing the BigNum class
# B1 = BigNum('100')
# B2 = BigNum('10')
# print(B1)
# print(B2)
# result = B1 * B2
# print(result)


