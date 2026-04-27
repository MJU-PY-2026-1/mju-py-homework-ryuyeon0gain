# 파일이름 :
# 작 성 자 : Choi Seo Yeon

# 1. 곡 정보 입력
title = input("곡 제목을 입력하세요: ")
artist = input("아티스트를 입력하세요: ")
genre = input("장르를 입력하세요: ")
play_count = int(input("재생 횟수를 입력하세요: "))
rating = float(input("개인 평점(0~5)을 입력하세요: "))

# 2. 선호도 점수 계산
preference_score = (play_count/2) + (rating*10)

# 3. 결과 출력
print(f"\n==== 음악 취향 분석 결과 ====")
print(f"곡 제목 : {title}")
print(f"아티스트 : {artist}")
print(f"장르 : {genre}")
print(f"재생 횟수 : {play_count}회")
print(f"개인 평점 : {rating:.1f}점")
print(f"선호도 점수 : {preference_score:.2f}")

