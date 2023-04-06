import itertools

def solution(expression):
    # print(expression)
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    operators = ['+', '-', '*']
    nums = []
    ops = []
    temp = ''

    
    # separate numbers and operators from expression
    for i, x in enumerate(expression):
        if x in numbers:
            temp+=x
        elif x in operators:
            nums.append(temp)
            ops.append(x)
            temp = ''
        if i==len(expression)-1:
            nums.append(temp)
    nums = list(map(int, nums))
          
    # get operation result
    results = []
    for operator_set in itertools.permutations(operators, len(operators)): #from sets of operation priorities
        results.append(abs(get_result(nums.copy(), ops.copy(), operator_set)))

    return max(results)

#function that returns calculation result
def get_result(nums, ops, operators):
    for j in operators:
        i = 0
        while i < len(nums)-1:
            n = nums[i]
            o = ops[i]
            if o==j: #calculate
                m = nums[i+1]
                if o == '+':
                    nums[i] = n+m
                elif o == '-':
                    nums[i] = n-m
                elif o == '*':
                    nums[i] = n*m
                nums.pop(i+1)
                ops.pop(i)
            else:
                i += 1
    return nums[0]
                

def test(expression):
    print(solution(expression))

test("100-200*300-500+20")
test("50*6-3*2")