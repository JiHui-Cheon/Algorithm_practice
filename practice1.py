daum = 89000
naver = 751000
print(daum * 100 + naver * 20)

duam = 89000 * 0.05
naver = 751000 * 0.1
print(daum + naver)

F = 50
C = (F-32)/1.8
print(C)

print('pizza\n' * 10)

naver_s = 1000000
naver_me = naver_s * 0.7
naver_te = naver_me * 0.7
naver_we = naver_te * 0.7
print(naver_we)

print("이름: 파이썬 생년월일: 2014년 12월 12일 주민등록번호: 20141212-1623210")

s = "Daum KaKao"
s_split = s.split(' ')
print(s_split[1] + " " + s_split[0])

a = "hello world"
print ("hi " + a[6:])

x = "abcdef"
print(x[1:] + "a")

kospi_top10 = ['삼성전자', 'SK하이닉스', '현대차', '한국전력', '아모레퍼시픽', '제일모직', '삼성전자우', '삼성생명', 'NAVER', '현대모비스']
kospi_top10.append('sk텔레콤')
print(kospi_top10)
kospi_top10.insert(2, '카카오')
print(kospi_top10)
del kospi_top10[-1]
print(kospi_top10)