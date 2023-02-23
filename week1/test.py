def crackle_pop(n: int = 100) -> None:
    """
    This function prints the numbers from 1 to n (inclusive). 
    If the number is divisible by 3, it prints "Crackle" instead of the number.
    If it's divisible by 5, it prints "Pop". 
    If it's divisible by both 3 and 5, it prints "CracklePop".

    :param n: The last number to print (inclusive). Default is 100.
    :type n: int
    :return: None
    """
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("CracklePop")
        elif i % 3 == 0:
            print("Crackle")
        elif i % 5 == 0:
            print("Pop")
        else:
            print(i)
            
crackle_pop(1)