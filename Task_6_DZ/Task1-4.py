

data_to_prove = '28.2.2001'

def data_good_format(data):
    day, month, year = [int(i) for i in data.split('.')]
    leap_year = False
    if year % 4 == 0 and (year % 100 != 0 or year % 4 == 0):
        leap_year = True
    if (day <  1 or day > 31) or (month < 1 or month > 12) or (year < 1 or year > 9999):
        return False
    if leap_year == True and month == 2 and (day <  1 or day > 29):
        return False
    elif leap_year == False and month == 2 and (day <  1 or day > 28):
        return False
    else:
        return True

result = data_good_format(data_to_prove)
print(result)






#
# fsqp x67 rw;<=> qAyC
#
# FGH JKLMNOPIRSTU` XYZT g
#     cde1gh j06 f>pq: i v iy 1 BF xP=:L < >?@ BC E HVM dQN` P RST V4 YZ[
#
# bdf xdpnjgnivwkqoouK stu? R
#     4567N :;<=>U ABCD m ZIJK^M2OPd S37 0<Y7 5; 5E=>286J<hLJGEQnopqrs
#     RP eROa 7 9 dh q^[m ; 89:; sw twwPs I @ WX Z[\]^ X MO ef hijk c Z qr tuvw q hgq
#         9>=?=: D0<D7
#     A? HKKRG JP Z[\ ^_ ab def SaX ZXl^ 9 0t9
#         5o789: Vr>?y
#     FG IJKLM `a X TUV XYZ[\]^[3abca fgh jk:m o wrs
#         I=MOMJ :@LTG
#     QO X[[bW MN P We\ hjp gr_mgdtablie3 mir trnx S IPS
#         56789: p=>?@
#     FG020K M48P
#
# 0T 60:oZA7Gu ` bc
#     MPHNUnYEQOKtJ\RbH0L23
# X`h[1
#     mphnuDyeqok0mkMqlPQoSTUVW @A
#
