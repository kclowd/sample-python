'''
Accepts a string of comma separated numbers
Returns the total sum of numbers 1000 or less
'''
def string_add(numbers: str):
    num_list = numbers.split(',')
    print(num_list)
    negative_nums = []
    
    total_sum = 0
    
    for num in num_list:
        if not num:
            return 0
        
        num_int = int(num)
        if 0 < num_int <= 1000:
            total_sum = total_sum + num_int
        elif num_int < 0:
            negative_nums.append(num_int)
    
    if len(negative_nums) > 0:
        err = f'Negative numbers are not allowed: {','.join([str(s) for s in negative_nums])}'
        raise ValueError(err)
            
    return total_sum