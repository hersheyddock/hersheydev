# 파이썬 시작하기

# Q1. 화면에 Hello World 문자열을 출력하세요.
print("Hello World")

# Q2. 화면에 Mary's cosmetics을 출력하세요
print("Mary's cosmetics")

# Q3. 문장 [신씨가 소리질렀다. "도둑이야".]를 출력하세요
print('신씨가 소리질렀다. "도둑이야".')
    ## 표현하고 싶은 문장에 ""가 있으므로, ''로 감싸서 표현해준다

# Q4. 화면에 "C:\Windows"를 출력하세요.
print("C:\Windows")

# Q5. print 탭과 줄바꿈 : 다음 코드를 실행해보고 \t와 \n의 역할을 설명해보세요.
print("안녕하세요.\n만나서\t\t반갑습니다.")

# Q6. print 함수에 두 개의 단어를 입력한 예제입니다. 아래 코드의 출력 결과를 예상해봅시다.
print ("오늘은", "일요일") #오늘은일요일 => 땡. "오늘은"과 "일요일" 사이에 공백이 있음

# Q7. print() 함수를 사용하여 naver;kakao;sk;samsung을 출력하세요.
print("naver;kakao;sk;samsung")
# 모범답안
print("naver","kakao","sk","samsung",sep=";")

# Q8. print()함수를 사용하여 naver/kakao/sk/samsung을 출력하세요
print("naver/kakao/sk/samsung")
# 모범답안
print("naver","kakao","sk","samsung",sep="/")

# Q9. 다음 코드를 수정하여 줄바꿈이 없이 출력하세요.
print("first");print("second")
    # (힌트: end='') print 함수는 두 번 사용합니다. 세미콜론 (;)은 한줄에 여러 개의 명령을 작성하기 위해 사용합니다.
print("first", end="");print("second")

# Q10. 5/3의 결과를 화면에 출력하세요.
print(5/3)
