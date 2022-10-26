import time
from random import random, randint

array = {
    '1': "Мирный",
    '2': 'Мафия',
    '3': 'Шриф',
    '4': 'Доктор',
    '5': 'maniac'
}
count_mafia = 0
count_doctor = 0
count_mirn = 0
count_shrif = 0
count_maniac = 0
count_players = int(input('кол-во игроков: '))

if count_players == 4:
    count_mafia = 1
    count_doctor = 1
    count_mirn = 2

if count_players == 5:
    count_mafia = 2
    count_doctor = 1
    count_mirn = 1
    count_shrif = 1

if count_players == 6:
    count_mafia = 2
    count_doctor = 1
    count_mirn = 2
    count_shrif = 1

if count_players == 7:
    count_mafia = 2
    count_maniac = 1
    count_doctor = 1
    count_mirn = 2
    count_shrif = 1

if count_players == 8:
    count_mafia = 2
    count_maniac = 1
    count_doctor = 1
    count_mirn = 3
    count_shrif = 1

for i in range(count_players):
    flag = 0
    input('напиши что-нибудь для полученя роли: ')
    while not flag:
        rnint = randint(1, 5)
        if rnint == 1 and count_mirn > 0:
            count_mirn -= 1
            print("""
            ============================
            ТЫ МИРНЫЙ =)
            ============================
            """)
            flag = 1
        if rnint == 2 and count_mafia > 0:
            count_mafia -= 1
            print("""
            ============================
            ТЫ МАФИЯ!!!
            ============================
            """)
            flag = 1
        if rnint == 3 and count_shrif > 0:
            count_shrif -= 1
            print("""
            ============================
            ТЫ ШРИФ!
            ============================
            """)
            flag = 1
        if rnint == 4 and count_doctor > 0:
            count_doctor -= 1
            print("""
            ============================
            ТЫ Доктор +
            ============================
            """)
            flag = 1
        if rnint == 5 and count_maniac > 0:
            count_maniac -= 1
            print("""
            ============================
            ТЫ МАНЬЯК у-ха-ха-ха!!!
            ============================
            """)
            flag = 1
    time.sleep(3)
    print('\n'*100)
print("""
<---- для переигровки



ВСЁ!!!!!""")
