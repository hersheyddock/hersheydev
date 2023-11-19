# 문제 : 영어 알파벳으로 이루어진 문자열 str이 주어집니다. 각 알파벳을 대문자는 소문자로 소문자는 대문자로 변환해서 출력하는 코드를 작성해 보세요.

str = input()

# 접근 방식 : i번째 원소를 검색 및 마주칠 때마다 소문자면 대문자로 대체, (vice versa)
## 소문자 여부를 파악하기 위한 메서드 검색 (https://wikidocs.net/7031#:~:text=%ED%9E%8C%ED%8A%B8%2D1%20%3A%20islower()%20%ED%95%A8%EC%88%98,%EB%8A%94%20%EC%86%8C%EB%AC%B8%EC%9E%90%EB%A1%9C%20%EB%B3%80%EA%B2%BD%ED%95%A9%EB%8B%88%EB%8B%A4.)

ls = []

for i in range(0, len(str)): #원소 개수만큼 값 탐색 
    if str[i].islower() == True:
        ls.append(str[i].upper())
    else: 
        ls.append(str[i].lower())

print("".join(ls)) # 공백없이 ls 값을 모두 순서대로 합치기 (join 메서드)

# The 'str' is an immutable data type. Therefore str type object doesn't support item assignment. 
    # => 빈 리스트에 가공된 String 값을 밀어넣고 join 메서드를 활용하여 이를 string화 시키는 것으로 처리
        
