import pyupbit
import math

access = ""          # 본인 값으로 변경
secret = ""          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print("현재 보유 현금 : ", math.floor(upbit.get_balance("KRW")), "원")         # 보유 현금 조회
print("현재 보유 리플 : ",upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
math