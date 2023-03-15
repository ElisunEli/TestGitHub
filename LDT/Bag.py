things = {'зажигалка': 20, 'компас': 100, 'фрукты': 500, 'рубашка': 300,
          'термос': 1000, 'аптечка': 200, 'куртка': 600, 'бинокль': 400, 'удочка': 1200,
          'салфетки': 40, 'бутерброды': 820, 'палатка': 5500, 'спальный мешок': 2250, 'жвачка': 10}

height = int(input()) * 1000

things_sorted = dict(sorted(things.items(), key=lambda x: -x[1]))
print(things_sorted)
for k, v in things_sorted.items():
    if v <=  height:
        print(k)
        height -= v