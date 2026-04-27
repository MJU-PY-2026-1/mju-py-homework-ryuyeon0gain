# 파일이름 : Project.py
# 작 성 자 : Choi Seo Yeon

# 0. AI 추천곡 정보
AI_TITLE = "소문의 낙원"
AI_ARTIST = "AKMU"
AI_GENRE = "발라드"
AI_PLAY_COUNT = 120
AI_RATING = 4.8

#1. 빈 리스트 생성
titles = []
artists = []
genres = []
play_counts = []
ratings = []
preference_scores = []
grades = []

#2. 첫 번째 곡 입력
title = input("첫 번째 곡 제목을 입력하세요: ")
artist = input("아티스트를 입력하세요: ")
genre = input("장르를 입력하세요: ")
play_count = int(input("재생 횟수를 입력하세요: "))
rating = float(input("개인 평점(0~5)을 입력하세요: "))

score = (play_count/2) + (rating*10)

if score >= 90:
  grade = "인생곡"
elif score >= 70:
  grade = "추천곡"
elif score >= 50:
  grade = "일반곡"
else:
  grade = "정리대상"

titles.append(title)
artists.append(artist)
genres.append(genre)
play_counts.append(play_count)
ratings.append(rating)
preference_scores.append(score)
grades.append(grade)

#3. 두 번째 곡 입력
title = input("\n두 번째 곡 제목을 입력하세요: ")
artist = input("아티스트를 입력하세요: ")
genre = input("장르를 입력하세요: ")
play_count = int(input("재생 횟수를 입력하세요: "))
rating = float(input("개인 평점(0~5)을 입력하세요: "))

score = (play_count/2) + (rating*10)

if score >= 90:
  grade = "인생곡"
elif score >= 70:
  grade = "추천곡"
elif score >= 50:
  grade = "일반곡"
else:
  grade = "정리대상"

titles.append(title)
artists.append(artist)
genres.append(genre)
play_counts.append(play_count)
ratings.append(rating)
preference_scores.append(score)
grades.append(grade)

backup_titles = titles[:]

titles.insert(1,AI_TITLE)
artists.insert(1,AI_ARTIST)
genres.insert(1,AI_GENRE)
play_counts.insert(1,AI_PLAY_COUNT)
ratings.insert(1,AI_RATING)

ai_score = (AI_PLAY_COUNT/2) + (AI_RATING*10)

if ai_score >= 90:
  ai_grade = "인생곡"
elif ai_score >= 70:
  ai_grade = "추천곡"
elif ai_score >= 50:
  ai_grade = "일반곡"
else:
  ai_grade = "정리대상"

preference_scores.insert(1,ai_score)
grades.insert(1,ai_grade)

# 4. 결과 출력
print("\n==== 전체 플레이리스트 분석 결과 ====")

print("\n1번 곡")
print(f"곡 제목 : {titles[0]}")
print(f"아티스트 : {artists[0]}")
print(f"장르 : {genres[0]}")
print(f"재생 횟수 : {play_counts[0]}회")
print(f"개인 평점 : {ratings[0]:.1f}점")
print(f"선호도 점수 : {preference_scores[0]:.2f}")
print(f"등급 : {grades[0]}")

print("\n2번 곡")
print(f"곡 제목 : {titles[1]}")
print(f"아티스트 : {artists[1]}")
print(f"장르 : {genres[1]}")
print(f"재생 횟수 : {play_counts[1]}회")
print(f"개인 평점 : {ratings[1]:.1f}점")
print(f"선호도 점수 : {preference_scores[1]:.2f}")
print(f"등급 : {grades[1]}")

print("\n3번 곡")
print(f"곡 제목 : {titles[2]}")
print(f"아티스트 : {artists[2]}")
print(f"장르 : {genres[2]}")
print(f"재생 횟수 : {play_counts[2]}회")
print(f"개인 평점 : {ratings[2]:.1f}점")
print(f"선호도 점수 : {preference_scores[2]:.2f}")
print(f"등급 : {grades[2]}")

# 리스트 복사 및 삽입 확인
print("\n==== 리스트 복사 및 삽입 확인 ====")
print(f"추천곡 삽입 전 곡 제목 리스트 : {backup_titles}")
print(f"추천곡 삽입 후 곡 제목 리스트 : {titles}")





