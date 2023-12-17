from openai import OpenAI
import re

#API Key는 환경 변수로 고정함
client = OpenAI()

# 사용자가 제시한 주사위
user_dice = [6, 3, 2, 3, 6]

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
  temperature=0.5, 
  messages=[
    {"role": "system", "content": "Yacht Dice assistant bot."},
    {"role": "user", "content": f"{user_dice}"},
    ]
)

# 어시스턴트의 답변에서 0과 1로 이루어진 5개의 숫자 추출
assistant_reply = completion.choices[0].message.content
fixed_dice = re.findall(r'[01]', assistant_reply)
fixed_dice = [int(i) for i in fixed_dice]

print("User Dice:", user_dice)
print("Fixed Dice:", fixed_dice)

