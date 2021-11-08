def arithmetic_arranger(test_lst, solve=False):

  # Test so that number of problems is not more than 5
  if(len(test_lst) > 5):
    return 'Error: Too many problems.'
  else:
    pass
  # Variables to store the full strings (the ones to return)
  top = ''
  den = ''
  line = ''
  ans = ''

  # Temporary variables for each problem until added to the overall string
  for x in test_lst:
    temp = x.split()
    first = temp[0]
    operand = temp[1]
    second = temp[2]
    temp_ans = ''

    # Test the operator
    if (operand not in ['-', '+']):
      return "Error: Operator must be '+' or '-'."
    else:
      pass

    # Test length of numbers in problems
    if (len(first) > 4 or len(second) > 4):
      return "Error: Numbers cannot be more than four digits."
    else:
      pass

    # if solve is marked True, this is where the problem gets solved
    if (solve and (operand == '+' or operand == '-')):
      if(operand == '+'):
        temp_ans = str(int(first)+int(second))
      else:
        temp_ans = str(int(first)-int(second))
    else:
      pass

    # Check so that all figures in problems is numeric
    if (not first.isnumeric() or not second.isnumeric()):
      return "Error: Numbers must only contain digits."
    else:
      pass

    # Calculate the length of the line
    line_len = max(len(first), len(second)) + 2

    # Adjust spaces
    first = first.rjust(line_len)
    second = second.rjust(line_len-1)
    temp_ans = temp_ans.rjust(line_len)

    # Put together the string
    if (x != test_lst[-1]):
      line += '-'*line_len + '    '
      ans += temp_ans + '    '
      top += first + '    '
      den += operand + second + '    '
    else:
      line += '-'*line_len
      ans += temp_ans
      top += first
      den += operand + second
  if(solve):
    arrenged_problems = top+'\n'+den+'\n'+line+'\n'+ans
  else:
    arrenged_problems = top+'\n'+den+'\n'+line
  return arrenged_problems
