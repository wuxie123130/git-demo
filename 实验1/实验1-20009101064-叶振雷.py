# Fermat 素性检验
from random import randint
from math import gcd
import gmpy2


# test1
def su_test(case=0, k=0):
    print(f"Get m = {case}")
    print(f"m 的长度为:", len(str(case)))
    for t in range(k):
        a = randint(2, case - 2)  # 2 <= a <= (m-2)
        print(f"Choose a{t} = {a}")
        print()
        g = gcd(a, case)  # 先求最大公因数
        if g != 1:
            print("m 为合数")
            print("-----------------------------------------")  # 分隔符
            return False
        r = pow(a, (case - 1), case)  # 快速幂取模
        if r == 1:
            continue
        else:
            print("m 为合数")
            print("-----------------------------------------")  # 分隔符
            return False
    print(f"m 有 1-(1/2)^{k} 的概率为素数")
    print("-----------------------------------------")  # 分隔符
    return True


test_num = [
    743476040059754298379331647007684224429004972336533937786799284757790400765316630522369642718204165253922832684184615021404737105614714107158733905598636152327037707290538422718453498125366750918857659068838460954633737911274770976191590193809661578032117496009853673140977556559136466107768672598883924301125589893895001253674886100289402530711221893,
    5434520625653357625890820149570485819447986258433769976634917091398967074086679540928507095017715540385352266035820823142060119390272763774034231321959236056764511968630360067353876686142517564224926196131349204754111599877101485686283117193149781387816214484583521923017500621725053392290279263586984207169423800476914654441473576611460323772832328657,
    876147742992673125957404768949712978720573116974723188491435550196169965040848206868200084918233743662847668000971402407461887306389122707315529364807593342507936022301657320206278702095378618110195051280478534126716517153056984269659532882692418682262081495725304483536777013188527470348249542840277926802938912332306310470632601156641005608958891,
    9876147742992673125957404768949712978720573116974723188491435550196169965040848206868200084918233743662847668000971402407461887306389122707315529364807593342507936022301657320206278702095378618110195051280478534126716517153056984269659532882692418682262081495725304483536777013188527470348249542840277926802938912332306310470632601156641005608958891
]

if __name__ == "__main__":
    print("Fermat 素性检验")
    k = int(input("请输入安全参数："))  # 安全参数
    print(f"Set k = {k}")
    for i in range(len(test_num)):  # 遍历数据包
        su_test(test_num[i], k)
