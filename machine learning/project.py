import random
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

# 랜덤 시드 설정
random.seed(42)

# 사용자 데이터 생성
users = []
#randint는 파이썬의 random 모듈에서 제공하는 함수로, 특정 범위 내의 정수(random integer)를 무작위로 생성할 때 사용
for _ in range(50):  # 50명 남성 데이터 생성
    age = random.randint(18, 80)
    preferred_genre = 4 if age >= 60 else (1 if age >= 30 else random.choice([0, 1, 2]) if age >= 20 else 2)
    
    users.append({ #남자인 경우
        "age": age,
        "gender": 0,
        "preferred_genre": preferred_genre,
        "listening_time": random.randint(1, 120)
    })

for _ in range(50):  # 50명 여성 데이터 생성
    age = random.randint(18, 80)
    preferred_genre = 3 if age >= 50 else (0 if age >= 30 else random.choice([0, 1, 2]) if age >= 20 else 2)
    
    users.append({ #여자인 경우
        "age": age,
        "gender": 1,
        "preferred_genre": preferred_genre,
        "listening_time": random.randint(1, 120)
    })

# DataFrame 생성
users_df = pd.DataFrame(users) #Pandas 라이브러리에서 제공하는 DataFrame 객체를 생성하는 함수

# 데이터 분리
data = users_df[['age', 'gender', 'listening_time']]
target = users_df['preferred_genre']

# 훈련 / 테스트 데이터 분할 stratify=target은 데이터를 훈련 세트와 테스트 세트로 나눌 때, 클래스(타겟 변수)의 비율을 유지하도록 하는 역할
train_input, test_input, train_target, test_target = train_test_split(data, target, test_size=0.2, random_state=42, stratify=target)

# 데이터 정규화 
ss = StandardScaler() #객체생성
train_scaled = ss.fit_transform(train_input) #훈련 데이터에 대해 fit(적용)하고 변환(transform)하여 정규화
test_scaled = ss.transform(test_input) # 테스트 데이터도 같은 스케일링 기준으로 변환

# 최적 k 값 찾기
best_k = 0
best_score = 0
for k in range(1, 51):
    kn = KNeighborsClassifier(n_neighbors=k)
    kn.fit(train_scaled, train_target)
    score = kn.score(test_scaled, test_target)
    if score > best_score:
        best_k = k
        best_score = score

# 최적 k 값을 적용한 모델
kn = KNeighborsClassifier(n_neighbors=best_k)
kn.fit(train_scaled, train_target)

# 음악 데이터베이스들
music_db = {
    0: ["Pop Song 1", "Pop Song 2", "Pop Song 3", "Pop Song 4", "Pop Song 5",
        "Pop Song 6", "Pop Song 7", "Pop Song 8", "Pop Song 9", "Pop Song 10"], #Pop

    1: ["Rock Song 1", "Rock Song 2", "Rock Song 3", "Rock Song 4", "Rock Song 5",
        "Rock Song 6", "Rock Song 7", "Rock Song 8", "Rock Song 9", "Rock Song 10"], #Rock Song

    2: ["HipHop Song 1", "HipHop Song 2", "HipHop Song 3", "HipHop Song 4", "HipHop Song 5",
        "HipHop Song 6", "HipHop Song 7", "HipHop Song 8", "HipHop Song 9", "HipHop Song 10"], #HipHop Song

    3: ["Jazz Song 1", "Jazz Song 2", "Jazz Song 3", "Jazz Song 4", "Jazz Song 5",
        "Jazz Song 6", "Jazz Song 7", "Jazz Song 8", "Jazz Song 9", "Jazz Song 10"], #Jazz song

    4: ["Classical Song 1", "Classical Song 2", "Classical Song 3", "Classical Song 4", "Classical Song 5",
        "Classical Song 6", "Classical Song 7", "Classical Song 8", "Classical Song 9", "Classical Song 10"] #Classical Song
}

genre = {0:'Pop',1:'Rock',2:'Hiphop',3:'Jazz',4:'Classical'} #딕셔너리

#사용자 입력 기반 추천 함수
def recommend_music(age, gender, listening_time): #매개변수로 나이,성별,청취시간을 둠.
    user_input = [[age, gender, listening_time]]
    df = pd.DataFrame(user_input, columns=['age', 'gender', 'listening_time'])
    user_scaled = ss.transform(df)
    
    # 예측된 선호 장르
    predicted_genre = kn.predict(user_scaled)[0]
    
    # 해당 장르에서 랜덤 추천
    recommended_songs = random.sample(music_db[predicted_genre], 3)
    
    print(f"\n추천된 장르: {genre[predicted_genre]}")
    print("추천 음악 리스트:")
    for song in recommended_songs:
        print(f"- {song}")

# 예제 사용자 입력
age = int(input("나이를 입력하세요: "))
gender = int(input("성별을 입력하세요 (남: 0, 여: 1): "))
listening_time = int(input("하루 평균 청취 시간을 입력하세요 (분): "))

# 추천 실행
recommend_music(age, gender, listening_time)

# 모델의 훈련 데이터 정확도
train_accuracy = kn.score(train_scaled, train_target)

# 모델의 테스트 데이터 정확도
test_accuracy = kn.score(test_scaled, test_target)

print(f"훈련 데이터 정확도: {train_accuracy:.4f}")
print(f"테스트 데이터 정확도: {test_accuracy:.4f}")