def avalanche_effect_calc(input1, input2):
    if len(input2) < 512:
        input2 = input2.zfill(512)

    if len(input2) > 512:
        raise ValueError("Input numbers cannot exceed 512-bits long.")
    
    # Convert hexadecimal string input into integer
    input1_int = int(input1, 16)
    input2_int = int(input2, 16)
    
    # XORing 2 integer
    xorResult = (input1_int ^ input2_int)
    #print("xorResult: ", xorResult)
    
    # Convert the Resulting XOR into binary
    xorResultBin = bin(xorResult)
    #print("xorResultBin: ", xorResultBin)
    
    # Calculate the total numbers of bit '1' in Resulting XOR (Binary)
    bit_tertukar = xorResultBin.count('1')
    
    # Calculate the number of total flipped bits
    persentase = (bit_tertukar / 512) * 100
    return bit_tertukar, persentase

# Example Use Case
input1 = "1e2a94e16a3978bf5fe442c09a19f8d2b9649783df5b05083e56901b79402bd504ad7ad9cb9572173b860116b52c37ff22e0e689ce772e83033345a740051b52"

print("\nThe original hexadecimal number:", input1)
input2 = input("\nInput the secondary hexadecimal number that will be compared to the first one: ")

bit_tertukar, persentase = avalanche_effect_calc(input1, input2)

print('\nThe total numbers of the flipped bits:', bit_tertukar, 'bit(s).')
print('\nThus, the percentage value of the Avalanche Effect Rate is equal to:', persentase,'%\n')
