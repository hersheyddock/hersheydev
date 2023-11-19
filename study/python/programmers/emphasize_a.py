# 문자열 myString이 주어집니다. 
# myString에서 알파벳 "a"가 등장하면 전부 "A"로 변환하고, "A"가 아닌 모든 대문자 알파벳은 소문자 알파벳으로 변환하여 return 하는 solution 함수를 완성하세요.

def solution(myString):
    myString = myString.lower().replace("a", "A")
    return myString

# lower() 메서드를 쓴다고 해서 결과값이 자동으로 myString 변수에 반영되는 구조가 아니고,
## 새롭게 변수를 바인딩해줘야 한다 !
