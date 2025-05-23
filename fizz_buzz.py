def fizz_buzz(start, finish):
    """Print 'fizz' and 'buzz' when necessary"""
    #Loop through nums between start and finish
    for num in range(start, finish+1):

        #Initialize num_string as num in type string
        num_string=num.__str__()
        
        #Print num if no conditions for 'fizz' or 'buzz' are met
        if not (num%3==0 or num%5==0 or num_string.__contains__("3") or num_string.__contains__("5")):
            print(num)
        #Check met conditions, printing 'fizzbuzz', 'fizz', or 'buzz' when needed
        elif((num%3==0 or num_string.__contains__("3")) and (num%5==0 or num_string.__contains__("5"))):
            print('fizzbuzz')
        else:
            if num%3==0 or num_string.__contains__("3"):
                print('fizz')
            if num%5==0 or num_string.__contains__("5"):
                print('buzz')
    print('complete')