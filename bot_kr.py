import random

# This list contains the random responses (you can add your own or translate them into your own language too)
random_responses = ["꽤 흥미롭네요, 자세히 알려주세요.",
                    "그러시군요. 계속하세요.",
                    "왜 그런 말을 해요?",
                    "요즘 날씨가 참 재미있네요, 그렇죠?",
                    "화제를 바꾸겠습니다.",
                    "어젯밤 경기는 잡으셨나요?"]

print("안녕하세요, 저는 간단한 로봇 마빈입니다.")
print("'안녕'을 입력하면 언제든지 이 대화를 끝낼 수 있습니다")
print("각 답을 입력한 후 '엔터'를 누릅니다")
print("오늘 어때요?")

while True:
    # wait for the user to enter some text
    user_input = input("> ")
    if user_input.lower() == "안녕":
        # if they typed in '안녕' (or even BYE, ByE, byE etc.), break out of the loop
        break
    else:
        response = random.choices(random_responses)[0]
    print(response)

print("만나서 반가웠어요, 안녕히 계세요!")