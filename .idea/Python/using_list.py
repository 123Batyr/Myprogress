shoplist = ['apple,', 'mango,', 'banana,', 'carrot']

print('Я должен сделать ', len(shoplist), 'покупок')

print('покупки:', end=' ')
for item in  shoplist:
    print(item, end=' ')

print('\nТак же нужно купить риса.')
shoplist.append('rice')
print('Теперь мой список покупок таков:', shoplist)

print('Отсортирую-ка я свой список')
shoplist.sort()
print('Отсортированный список покупок выглядит так:', shoplist)

print('Первое что мне нужно купить это', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('Я купил', olditem)
print('Теперь мой список покупок:', shoplist)