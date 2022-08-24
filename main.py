import sys

first_num = input('FIRST NUM: ')

second_num = input('SECOND NUM: ')

ask_operator = input('+, -, /, *, **: ')

if ask_operator == '+':
  sum = float(first_num) + float(second_num)
  print(sum)

if ask_operator == '-':
  sum = float(first_num) - float(second_num)

if ask_operator == '/':
  if second_num == '0':
    print('Cant do this operation')
    sys.exit('Zero_Division_Error')

  ask_round = input('Would you like to round you answer? y/n: ').lower()
  if ask_round == 'y':
    sum = float(first_num) // float(second_num)
    print(sum)
  if ask_round == 'n':
    sum = float(first_num) / float(second_num)
    print(sum)

if ask_operator == '*':
  sum = float(first_num) * float(second_num)
  print(sum)

if ask_operator == '**':
  sum = float(first_num) ** float(second_num)
  print(sum)
