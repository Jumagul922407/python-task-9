
# Функциялар темасы боюнча кыскача мисалдар

# 1. Жөнөкөй функция
def salamdash():
    print("Салам, Жумагүл!")

salamdash()

# 2. Аргумент кабыл алган функция
def koshuu(a, b):
    return a + b

print("5 + 7 =", koshuu(5, 7))

# 3. Default мааниси менен функция
def country_info(name, country="Кыргызстан"):
    print(f"Аты: {name}, Мамлекети: {country}")

country_info("Айдана")
country_info("Эмир", "Казакстан")

# 4. Кайтаруучу функция
def kopoyтуу(a, b):
    natyija = a * b
    return natyija

print("6 * 4 =", kopoyтүү(6, 4))
