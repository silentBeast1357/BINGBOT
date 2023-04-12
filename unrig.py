def decode():
    with open("code","r") as file:
        nums = file.read().split(" ")
    
    output = ""
    for num in nums:
        output += chr(int(num))
    
    return output