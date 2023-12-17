from openai import OpenAI
import re

#API Key는 환경 변수로 고정함
client = OpenAI()

# 사용자가 제시한 주사위
user_dice = [4, 5, 1, 1, 1]

# fine-tuning은 코드로도 가능하고 openAI 사이트 안에서도 가능
"""
#JSONL 파일 삽입
client.files.create(
  file=open("YachtDice_fine_tune.jsonl", "rb"),
  purpose="fine-tune"
)

#Fine-tuning 실시 (traning_file : File ID)
client.fine_tuning.jobs.create(
  training_file="file-Cs8EpEQqvIIXnnplJRfOLUC3",
  model="gpt-3.5-turbo-1106"
)
"""

# 사용자가 주사위를 제시하고 어시스턴트의 답변을 받아옴 (model : fine-tuning된 모델 이름)
completion = client.chat.completions.create(
  model="ft:gpt-3.5-turbo-1106:personal::8WinSuKM",
  messages=[
    {"role": "system", "content": "Yacht Dice assistant bot. Score rule is like this. \
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
      Which ones should I reroll? Answer sequentially with 0 for not reroll, and 1 for reroll"},
    ]
)

# 어시스턴트의 답변에서 0과 1로 이루어진 5개의 숫자 추출
assistant_reply = completion.choices[0].message.content
fixed_dice = re.findall(r'[01]', assistant_reply)
fixed_dice = [int(i) for i in fixed_dice]

print("Fixed Dice:", fixed_dice)

