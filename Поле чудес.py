print('Pole Chudes')
inp = '0'
while inp != 'Exit' or inp != 'Выхлод':
  print('Choose the language:')
  print('1 English')
  print('2 Russian')
  lang = input()
  if lang == '1':
    dic = '''роскошный мак инструкция ир спокойствие недоумение психологический хоббит бинокль лысый вглядываться килограмм печально революционный меньший двойной марш вселенная прибавить тварь чайник лыжа спустить беспокойство опубликовать отпускать намек пробить воровать плач тревожный '''.split(' ')
    inpletts = []
    inpfletts = []
    tru = False
    word = dic.pop()
    lett = list(word)
    print('Вам подходят эти буквы')
    print([str(lettt) for lettt in int])
    inplett = input()
    print('Вы использовали эти буквы')
    print([str(lettt) for lettt in inpfletts])
    while inpletts != lett:
      time += 1
      if len(inplett) = 1:
        if inplett.isdigit():
          continue
        inpletts.append(input)
        if len(inpletts) == len(lett):
          break
      elif len(inplett) > 1:
        if inplett == word:
          tru = True
          break
      inpfletts.append(inplett)
      inplett = input()
    if tru:
      print('Победа')
      print('Поздравляю, вы смогли победить!')
      print(f'Вам понадобилось {time} попыток.')
    else:
      print('Проигрыш')
      print('К сожалению, вы проиграли.')
      print('Ну, не унываете, в следующий раз у вас получится.')
    print('Если хотите сыграть ещё раз то введите что угодно,')
    print('иначе введите "Выход" без ковычек')
    int = input()
