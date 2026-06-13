# 이름 : Project.py
# 작 성 자 : Choi Seo Yeon

# 0. 전역 리스트 생성
users = []
titles = []
genres = []
play_counts = []
ratings = []
preference_scores = []
grades = []

playlist_data = []

total_song_count = 0

# 1. AI 추천곡 정보

AI_TITLES = ["소문의 낙원", "Super Shy", "사이렌", "Snooze", "APT.", "첫 눈"]
AI_GENRES = ["발라드","케이팝","랩","R&B","팝송","OST"]
AI_PLAY_COUNTS = [120, 150, 130, 110, 100, 140]
AI_RATINGS = [4.8,4.7,4.6,4.9,4.5,4.8]

#2. 선호도 점수 계산 함수
def calculate_score(play_count, rating):
    score = (play_count / 2) + (rating*10)
    return score

#3. 등급 계산 함수
def get_grade(score):
    if score >= 90:
        grade = "인생곡"
    elif score >= 70:
        grade = "추천곡"
    elif score >= 50:
        grade = "일반곡"
    else:
        grade = "정리대상"
    return grade


#4. 곡 추가 함수
def add_song(user_name, title, genre, play_count, rating) :
    global total_song_count

    score = calculate_score(play_count, rating)
    grade = get_grade(score)

    users.append(user_name)
    titles.append(title)
    genres.append(genre)
    play_counts.append(play_count)
    ratings.append(rating)
    preference_scores.append(score)
    grades.append(grade)

    song_info = [user_name, title, genre, play_count, rating, score, grade]
    playlist_data.append(song_info)

    total_song_count += 1

#5. 같은 곡 개수 세를 함수
def count_same_title(title) :
    count = 0

    for i in range(len(titles)):
        if titles[i] == title :
            count += 1

    return count

#6. 전체 플레이리스트 출력 함수
def print_all_playlist():
    print("\n==== 현재까지 누적된 전체 플레이리스트 ====")

    if len(titles) == 0:
        print("아직 입력된 곡이 없습니다.")
    else : 
        for i in range(len(titles)) :
            print(f"\n{i+1}번 곡")
            print(f"등록자 : {users[i]}")
            print(f"곡 제목 : {titles[i]}")
            print(f"장르 : {genres[i]}")
            print(f"재생 횟수 : {play_counts[i]}회")
            print(f"개인 평점 : {ratings[i]:.1f}점")
            print(f"선호도 점수 : {preference_scores[i]:.2f}점")
            print(f"등급 : {grades[i]}")

#7. 공동 인기곡 출력 함수
def print_popular_songs():
    print("\n==== 공동 인기곡 확인 ====")

    checked_titles = []
    found = False

    for i in range(len(titles)) : 
        if titles[i] not in checked_titles:
            same_count = count_same_title(titles[i])

            if same_count >= 3:
                print(f"{titles[i]}은 공동 인기곡입니다.")
                found = True

            checked_titles.append(titles[i])

    if found == False :
        print("아직 3번 이상 입력된 공동 인기곡은 없습니다.")

#8. 플레이리스트 입력 함수
def input_playlist():
    user_name = input("\n사용자 이름을 입력하세요: ")
    try:
        song_count = int(input("입력할 곡 수를 입력하세요: "))
    except ValueError:
        print("곡 수는 숫자로 입력해야 합니다.")
        return

    for i in range(song_count):
        print(f"\n[{user_name}님의 {i + 1}번째 곡 입력]")

        title = input("곡 제목을 입력하세요: ")
        genre = input("장르를 입력하세요(발라드/케이팝/랩/R&B/팝송/OST 중 선택): ")

        if genre != "발라드" and genre != "케이팝" and genre != "랩" and genre != "R&B" and genre != "팝송" and genre != "OST":
            print("후보에 없는 장르이므로 '기타'로 저장합니다.")
            genre = "기타"

        try:
            play_count, rating = input("재생 횟수(0회~300회)와 개인 평점(0점~5점)을 띄어쓰기로 입력하세요(예: 120 4.8): ").split()
            play_count = int(play_count)
            rating = float(rating)
        except ValueError:
            print("입력 형식이 잘못되었습니다. 예시처럼 120 4.8 형태로 입력해야 합니다.")
            continue

        if play_count < 0:
            print("재생 횟수가 0보다 작아서 0회로 저장합니다.")
            play_count = 0
        elif play_count > 300:
            print("재생 횟수가 300회를 넘어서 300회로 저장합니다.")
            play_count = 300

        if rating < 0:
            print("개인 평점이 0점보다 작아서 0점으로 저장합니다.")
            rating = 0
        elif rating > 5:
            print("개인 평점이 5점을 넘어서 5점으로 저장합니다.")
            rating = 5

        add_song(user_name, title, genre, play_count, rating)
 
    print_all_playlist()
    print_popular_songs()

#9. 사용자가 존재하는지 확인하는 함수
def check_user(user_name):
    found = False

    for i in range(len(users)):
        if users[i] == user_name:
            found = True

    return found

#10. 사용자 평균 선호도 계산 함수
def calculate_user_average_score(user_name):
    total_score = 0
    count = 0

    for i in range(len(users)):
        if users[i] == user_name : 
            total_score += preference_scores[i]
            count +=1

    if count == 0:
        return 0
    else :
        average_score = total_score / count
        return average_score
    

#11. 사용자 대표 장르 찾기 함수
def find_favorite_genre(user_name):
    favorite_genre = ""
    max_count = 0

    for i in range(len(genres)):
        if users[i] == user_name :
            current_genre = genres[i]
            count = 0

            for j in range(len(genres)):
                if users[j] == user_name and genres[j] == current_genre:
                    count += 1

            if count > max_count :
                max_count = count
                favorite_genre = current_genre

    return favorite_genre


# 12. 두 사용자의 공통 장르 개수 계산 함수
def count_common_genres(user1, user2):
    common_count = 0
    checked_genres = []

    for i in range(len(genres)):
        if users[i] == user1 and genres[i] not in checked_genres:
            current_genre = genres[i]

            for j in range(len(genres)):
                if users[j] == user2 and genres[j] == current_genre:
                    common_count += 1
                    checked_genres.append(current_genre)
                    break

    return common_count

# 13. 취향 비교 함수
def compare_taste():
    print("\n==== 취향 비교 기능 ====")

    user1 = input("첫 번째 사용자 이름을 입력하세요: ")
    user2 = input("두 번째 사용자 이름을 입력하세요: ")

    if check_user(user1) == False:
        print(f"'{user1}'님의 플레이리스트가 없습니다.")
    elif check_user(user2) == False:
        print(f"'{user2}'님의 플레이리스트가 없습니다.")
    else:
        user1_favorite_genre = find_favorite_genre(user1)
        user2_favorite_genre = find_favorite_genre(user2)

        user1_average = calculate_user_average_score(user1)
        user2_average = calculate_user_average_score(user2)

        common_genre_count = count_common_genres(user1, user2)

        print(f"\n{user1}님의 대표 장르는 '{user1_favorite_genre}'입니다.")
        print(f"{user2}님의 대표 장르는 '{user2_favorite_genre}'입니다.")

        print(f"\n{user1}님의 평균 선호도 점수는 {user1_average:.2f}점입니다.")
        print(f"{user2}님의 평균 선호도 점수는 {user2_average:.2f}점입니다.")

        print(f"\n두 사람이 공통으로 좋아하는 장르는 {common_genre_count}개입니다.")

        if user1_favorite_genre == user2_favorite_genre:
            print("분석 결과: 두 사람은 대표 장르가 같아서 음악 취향이 매우 비슷합니다.")
        elif common_genre_count >= 2:
            print("분석 결과: 두 사람은 여러 장르가 겹쳐서 취향이 꽤 비슷합니다.")
        elif common_genre_count == 1:
            print("분석 결과: 두 사람은 일부 취향이 비슷합니다.")
        else:
            print("분석 결과: 두 사람은 서로 다른 음악 취향을 가지고 있습니다.")


# 14. 특정 사용자의 특정 장르 개수 계산 함수
def count_user_genre(user_name, genre_name):
    count = 0

    for i in range(len(users)):
        if users[i] == user_name and genres[i] == genre_name:
            count += 1

    return count


# 15. 전체 플레이리스트의 특정 장르 개수 계산 함수
def count_total_genre(genre_name):
    count = 0

    for i in range(len(genres)):
        if genres[i] == genre_name:
            count += 1

    return count


# 16. AI 추천곡 함수
def recommend_ai_song():
    print("\n==== 사용자를 위한 AI 추천곡 ====")

    user_name = input("AI 추천을 받을 사용자 이름을 입력하세요: ")

    if check_user(user_name) == False:
        print(f"'{user_name}'님의 플레이리스트가 없습니다.")
    else:
        favorite_genre = find_favorite_genre(user_name)
        average_score = calculate_user_average_score(user_name)

        selected_index = 0
        min_user_genre_count = 999
        max_total_genre_count = -1

        for i in range(len(AI_GENRES)):
            user_genre_count = count_user_genre(user_name, AI_GENRES[i])
            total_genre_count = count_total_genre(AI_GENRES[i])

            if user_genre_count < min_user_genre_count:
                selected_index = i
                min_user_genre_count = user_genre_count
                max_total_genre_count = total_genre_count
            elif user_genre_count == min_user_genre_count and total_genre_count > max_total_genre_count:
                selected_index = i
                max_total_genre_count = total_genre_count

        ai_title = AI_TITLES[selected_index]
        ai_genre = AI_GENRES[selected_index]
        ai_play_count = AI_PLAY_COUNTS[selected_index]
        ai_rating = AI_RATINGS[selected_index]

        print(f"\n{user_name}님의 대표 장르는 '{favorite_genre}'이고, 플레이리스트에서 가장 부족한 장르는 '{ai_genre}'입니다.")
        print(f"{user_name}님의 평균 선호도 점수는 {average_score:.2f}점입니다.")

        if average_score >= 90:
            print("분석 결과: 전체적으로 선호도가 높은 편이라 새로운 장르를 확장해도 좋습니다.")
        elif average_score >= 70:
            print("분석 결과: 안정적인 취향을 가지고 있어 부족한 장르를 보완하는 추천이 적절합니다.")
        else:
            print("분석 결과: 아직 강한 취향이 형성되지 않아 다양한 장르를 시도해보는 것이 좋습니다.")

        print(f"\nAI 추천곡은 '{ai_title}'입니다.")
        print(f"추천 장르는 '{ai_genre}'입니다.")

        add_song(user_name, ai_title, ai_genre, ai_play_count, ai_rating)

        print(f"\n'{ai_title}'이/가 {user_name}님의 플레이리스트에 추가되었습니다.")

        print_all_playlist()
        print_popular_songs()

# 4차 과제. 이중 순회 조건 만족
def print_playlist_table():
    print("\n==== 이중 리스트 플레이리스트 표 ====")

    if len(playlist_data) == 0:
        print("저장된 데이터가 없습니다.")
    else:
        headers = ["사용자", "곡 제목", "장르", "재생 횟수", "평점", "선호도", "등급"]

        for header in headers:
            print(header, end=" | ")
        print()

        for row in playlist_data:
            for item in row:
                print(item, end=" | ")
            print()

# 4차 과제. 파일 관련 함수 추가
def save_playlist_file():
    try:
        with open("playlist_data.txt", "w", encoding="utf-8") as file:
            file.write("사용자,곡 제목,장르,재생 횟수,평점,선호도,등급\n")

            for row in playlist_data:
                for i in range(len(row)):
                    file.write(str(row[i]))

                    if i < len(row) - 1:
                        file.write(",")

                file.write("\n")

        print("playlist_data.txt 파일로 저장되었습니다.")

    except OSError:
        print("파일 저장 중 오류가 발생했습니다.")


# 17. 최고 선호도 곡과 평균 선호도 분석 함수
def analyze_score():
    print("\n==== 최고 선호도 곡 및 평균 선호도 분석 ====")

    if len(preference_scores) == 0:
        print("아직 입력된 곡이 없습니다.")
    else:
        max_score = preference_scores[0]
        max_index = 0
        total_score = 0

        for i in range(len(preference_scores)):
            total_score += preference_scores[i]

            if preference_scores[i] > max_score:
                max_score = preference_scores[i]
                max_index = i

        average_score = total_score / len(preference_scores)

        print(f"최고 선호도 곡은 '{titles[max_index]}'입니다.")
        print(f"등록자는 '{users[max_index]}'입니다.")
        print(f"장르는 '{genres[max_index]}'입니다.")
        print(f"선호도 점수는 {preference_scores[max_index]:.2f}점이며, 등급은 '{grades[max_index]}'입니다.")

        print(f"\n현재 전체 플레이리스트에는 총 {total_song_count}곡이 저장되어 있습니다.")
        print(f"전체 곡의 평균 선호도 점수는 {average_score:.2f}점입니다.")



# 18. 공동 플레이리스트 종합 리포트 함수
def print_playlist_report():
    print("\n==== 공동 플레이리스트 종합 리포트 ====")

    print_playlist_table()

    if len(titles) == 0:
        print("아직 입력된 곡이 없습니다.")
    else:
        checked_users = []
        user_count = 0

        for i in range(len(users)):
            if users[i] not in checked_users:
                checked_users.append(users[i])
                user_count += 1

        checked_genres = []
        top_genre = ""
        top_genre_count = 0

        for i in range(len(genres)):
            if genres[i] not in checked_genres:
                genre_count = 0

                for j in range(len(genres)):
                    if genres[i] == genres[j]:
                        genre_count += 1

                if genre_count > top_genre_count:
                    top_genre_count = genre_count
                    top_genre = genres[i]

                checked_genres.append(genres[i])

        checked_titles = []
        popular_song_count = 0

        for i in range(len(titles)):
            if titles[i] not in checked_titles:
                same_count = count_same_title(titles[i])

                if same_count >= 3:
                    popular_song_count += 1

                checked_titles.append(titles[i])

        delete_count = 0

        for i in range(len(grades)):
            if grades[i] == "정리대상":
                delete_count += 1

        print(f"총 등록 곡 수: {total_song_count}곡")
        print(f"참여 사용자 수: {user_count}명")
        print(f"가장 많이 등록된 장르: {top_genre}")
        print(f"'{top_genre}' 장르의 등록 곡 수: {top_genre_count}곡")
        print(f"공동 인기곡 수: {popular_song_count}곡")
        print(f"정리대상 곡 수: {delete_count}곡")

        print("\n==== 분석 결과 ====")

        if top_genre_count >= total_song_count / 2:
            print(f"현재 플레이리스트는 '{top_genre}' 장르에 많이 치우쳐 있습니다.")
            print("다른 장르를 추가하면 더 균형 있는 공동 플레이리스트가 될 수 있습니다.")
        else:
            print("현재 플레이리스트는 여러 장르가 비교적 고르게 섞여 있습니다.")

        if popular_song_count >= 1:
            print("공동 인기곡이 존재하므로 사용자들 사이에 공통 취향이 형성되어 있습니다.")
        else:
            print("아직 3명 이상이 함께 선택한 공동 인기곡은 없습니다.")

        if delete_count >= 1:
            print("정리대상 곡이 있으므로 플레이리스트 정리가 필요합니다.")
        else:
            print("정리대상 곡이 없어 전체적인 만족도가 좋은 편입니다.")



# 19. 메뉴 시스템
while True:
    print("\n==== 공동 플레이리스트 분석 및 추천 시스템 ====")
    print("1. 플레이리스트 입력")
    print("2. 취향 비교 기능")
    print("3. 사용자를 위한 AI 추천곡")
    print("4. 최고 선호도 곡 및 평균 선호도 계산")
    print("5. 공동 플레이리스트 종합 리포트")
    print("6. 플레이리스트 파일 저장")
    print("0. 프로그램 종료")
    print("===============================================")

    menu = input("메뉴 번호를 선택하세요: ")

    if menu == "1":
        input_playlist()

    elif menu == "2":
        compare_taste()

    elif menu == "3":
        recommend_ai_song()

    elif menu == "4":
        analyze_score()

    elif menu == "5":
        print_playlist_report()

    elif menu == "6":
        save_playlist_file()

    elif menu == "0":
        save_playlist_file()
        print("\n공동 플레이리스트 분석 및 추천 시스템을 종료합니다.")
        break

    else:
        print("\n잘못된 메뉴 번호입니다. 0번부터 6번 사이의 번호를 다시 입력하세요.")

