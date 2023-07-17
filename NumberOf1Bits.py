def numberOf1Bits(number):
    count = 0

    while number > 0:
        if number & 1:
            count += 1
        number >>= 1

    return count


if __name__ == "__main__":
    number = int(input())

    print(numberOf1Bits(number))
