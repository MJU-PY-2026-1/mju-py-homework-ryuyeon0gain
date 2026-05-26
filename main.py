름 : Project.py
# 작 성 자 : Choi Seo Yeon

# 0. AI 추천곡 정보
AI_TITLE = "소문의 낙원"
AI_ARTIST = "AKMU"
AI_GENRE = "발라드"
AI_PLAY_COUNT = 120
AI_RATING = 4.8

# 1. 빈 리스트 생성
titles = []
artists = []
genres = []
play_counts = []
ratings = []
preference_scores = []
grades = []

# 2. 첫 번째 곡 입력
title = input("첫 번째 곡 제목을 입력하세요: ")
artist = input("아티스트를 입력하세요: ")
genre = input("장르를 입력하세요: ")
play_count = int(input("재생 횟수를 입력하세요: "))
rating = float(input("개인 평점(0~5)을 입력하세요: "))

score = (play_count / 2) + (rating * 10)

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

# 3. 두 번째 곡 입력
title = input("\n두 번째 곡 제목을 입력하세요: ")
artist = input("아티스트를 입력하세요: ")
genre = input("장르를 입력하세요: ")
play_count = int(input("재생 횟수를 입력하세요: "))
rating = float(input("개인 평점(0~5)을 입력하세요: "))

score = (play_count / 2) + (rating * 10)

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

# 4. AI 추천곡 삽입
backup_titles = titles[:]

titles.insert(1, AI_TITLE)
artists.insert(1, AI_ARTIST)
genres.insert(1, AI_GENRE)
play_counts.insert(1, AI_PLAY_COUNT)
ratings.insert(1, AI_RATING)

ai_score = (AI_PLAY_COUNT / 2) + (AI_RATING * 10)

if ai_score >= 90:
    ai_grade = "인생곡"
elif ai_score >= 70:
    ai_grade = "추천곡"
elif ai_score >= 50:
    ai_grade = "일반곡"
else:
    ai_grade = "정리대상"

preference_scores.insert(1, ai_score)
grades.insert(1, ai_grade)

# 5. 메뉴 시스템 시작
while True:
    print("\n==== 음악 취향 분석 및 플레이리스트 관리 시스템 ====")
    print("1. 전체 플레이리스트 분석 결과 출력")
    print("2. 등급별 곡 출력")
    print("3. 최고 선호도 곡 찾기")
    print("4. 평균 선호도 계산")
    print("5. 등급별 곡 개수 출력")
    print("0. 프로그램 종료")
    print("======================================================")

    menu = int(input("메뉴 번호를 선택하세요: "))

    if menu == 1:
        print("\n==== 전체 플레이리스트 분석 결과 출력 ====")

        for i in range(len(titles)):
            print(f"\n{i + 1}번 곡은 '{titles[i]}'입니다.")
            print(f"아티스트는 '{artists[i]}'이고, 장르는 '{genres[i]}'입니다.")
            print(f"재생 횟수는 {play_counts[i]}회이고, 개인 평점은 {ratings[i]:.1f}점입니다.")
            print(f"선호도 점수는 {preference_scores[i]:.2f}점이고, 등급은 '{grades[i]}'입니다.")

    elif menu == 2:
        search_grade = input("\n출력할 등급을 입력하세요(인생곡/추천곡/일반곡/정리대상): ")

        print(f"\n==== {search_grade} 곡 목록 ====")
        found = False

        for i in range(len(titles)):
            if grades[i] == search_grade:
                print(f"'{search_grade}' 등급의 곡은 '{titles[i]}'이며, 아티스트는 '{artists[i]}'입니다.")
                print(f"해당 곡의 선호도 점수는 {preference_scores[i]:.2f}점입니다.")
                found = True

        if found == False:
            print(f"'{search_grade}' 등급에 해당하는 곡은 없습니다.")

    elif menu == 3:
        max_score = preference_scores[0]
        max_index = 0

        for i in range(len(preference_scores)):
            if preference_scores[i] > max_score:
                max_score = preference_scores[i]
                max_index = i

        print("\n==== 최고 선호도 곡 ====")
        print(f"최고 선호도 곡은 '{titles[max_index]}'입니다.")
        print(f"아티스트는 '{artists[max_index]}'이고, 장르는 '{genres[max_index]}'입니다.")
        print(f"선호도 점수는 {preference_scores[max_index]:.2f}점이며, 등급은 '{grades[max_index]}'입니다.")

    elif menu == 4:
        total_score = 0

        for score in preference_scores:
            total_score += score

        average_score = total_score / len(preference_scores)

        print("\n==== 평균 선호도 계산 ====")
        print(f"현재 플레이리스트에는 총 {len(preference_scores)}곡이 저장되어 있습니다.")
        print(f"전체 곡의 평균 선호도 점수는 {average_score:.2f}점입니다.")

    elif menu == 5:
        life_count = 0
        recommend_count = 0
        normal_count = 0
        delete_count = 0

        for grade in grades:
            if grade == "인생곡":
                life_count += 1
            elif grade == "추천곡":
                recommend_count += 1
            elif grade == "일반곡":
                normal_count += 1
            else:
                delete_count += 1

        print("\n==== 등급별 곡 개수 ====")
        print(f"'인생곡' 등급의 곡 개수는 {life_count}곡입니다.")
        print(f"'추천곡' 등급의 곡 개수는 {recommend_count}곡입니다.")
        print(f"'일반곡' 등급의 곡 개수는 {normal_count}곡입니다.")
        print(f"'정리대상' 등급의 곡 개수는 {delete_count}곡입니다.")

    elif menu == 0:
        print("\n음악 취향 분석 및 플레이리스트 관리 시스템을 종료합니다.")
        break

    else:
        print("\n잘못된 메뉴 번호입니다. 0번부터 5번 사이의 번호를 다시 입력하세요.")



