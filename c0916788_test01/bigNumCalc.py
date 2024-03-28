from bigNum import BigNum

def calculate(numbers, operators):
    result = BigNum(numbers[0])
    for i in range(1, len(numbers)):
        if operators[i-1] == '+':
            print(result,'+', BigNum(numbers[i]))
            result = result + BigNum(numbers[i])
        elif operators[i-1] == '-':
            print(result,'-', BigNum(numbers[i]))
            result = result - BigNum(numbers[i])
        elif operators[i-1] == '*':
            print(result,'*', BigNum(numbers[i]))
            result = result * BigNum(numbers[i])
        elif operators[i-1] == '/':
            print(result,'/', BigNum(numbers[i]))
            result = result / BigNum(numbers[i])
    return result

def main():
    file_path = 'bigNums.txt'  # storing the file path
    
    # Reading the string numbers and operators from the file
    numbers = [] # to hold the numbers
    operators = [] # to hold the operators
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip() # removes the extra whitespace
            if line:
                if line in ['+' , '-' , '*', '/']:
                    operators.append(line)
                else: numbers.append(line)
    
    # Perform the operations
    result = calculate(numbers, operators)
    
    # Display the result
    print('******************')
    print("Final Result:")
    print('******************')
    print(result)


if __name__ == "__main__":
    print('******************')
    print('BigNum Calculator')
    print('******************')

    main()
