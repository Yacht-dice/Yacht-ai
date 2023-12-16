from openai import OpenAI
import re


client = OpenAI()

# 사용자가 제시한 주사위
user_dice = [2, 3, 6, 6, 2]

# 사용자가 주사위를 제시하고 어시스턴트의 답변을 받아옴
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are the assistant helping the player in Yacht Dice. \
        This is the score rule. \
        Aces\
        1이 나온 주사위 눈의 총합. 최대 5점.\
        Deuces\
        2가 나온 주사위 눈의 총합. 최대 10점.\
        Threes\
        3이 나온 주사위 눈의 총합. 최대 15점.\
        Fours\
        4가 나온 주사위 눈의 총합. 최대 20점.\
        Fives\
        5가 나온 주사위 눈의 총합. 최대 25점.\
        Sixes\
        6이 나온 주사위 눈의 총합. 최대 30점.\
        Choice\
        주사위 눈 5개의 총합. 최대 30점.\
        4 of a Kind\
        동일한 주사위 눈이 4개 이상일 때,\
        주사위 눈 5개의 총합. 최대 30점.\
        Full House\
        주사위를 3개, 2개로 묶었을 때 각각의 묶음 안에서 주사위 눈이 서로 동일할 때,\
        주사위 눈 5개의 총합. 최대 30점.\
        Small Straight\
        이어지는 주사위 눈이 4개 이상일 때. 고정 15점.\
        Large Straight\
        이어지는 주사위 눈이 5개일 때. 고정 30점.\
        Yacht\
        동일한 주사위 눈이 5개일 때. 고정 50점."},
        {"role": "user", "content": f"I have {', '.join(map(str, user_dice))} as my dice. \
         Which ones should I fix to be 'small straight'? Answer with 0 for fixed and 1 for not fixed. \
         Answer just 5 words with only numbers without comma, 1 space between numbers"},
    ]
)


# 어시스턴트의 답변에서 0과 1로 이루어진 5개의 숫자 추출
#assistant_reply = completion.choices[0].message
#fixed_dice = [int(char) for char in assistant_reply if char in ('0', '1')]

# 결과 출력
#print("Fixed Dice:", assistant_reply)

# 어시스턴트의 답변에서 0과 1로 이루어진 5개의 숫자 추출
assistant_reply = completion.choices[0].message.content
fixed_dice = re.findall(r'[01]', assistant_reply)
fixed_dice = [int(i) for i in fixed_dice]

print("Fixed Dice:", fixed_dice)

