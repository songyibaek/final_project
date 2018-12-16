"""
배열 설명
[i][0] = 팀 이름
[i][1] = 승
[i][2] = 무
[i][3] = 패
[i][4] = 승률
"""
list_TeamInform = [[0] for rows in range(8)]  # 8팀을 입력받음
list_remainGame = []  # 문제: 각 잔여 경기에 대한 정보인 R 행이 그 다음에 주어진다.
remain_GameNum = 0  # 메인에서 남은 게임 수를 입력 받음
My_Team = ''  # 내 팀을 입력받음

def find_Team(Team_name):
    # 원하는 Team의 index값 반환
    for i in range(8):
        if list_TeamInform[i][0] == Team_name:
            return i

def calculate_All_Rating():
    # 승률 계산 및 순위별로 정렬
    for i in range(8):
        All_game = list_TeamInform[i][1] + list_TeamInform[i][2] + list_TeamInform[i][3]  # 전체 게임 수 세기(승+무+패)
        list_TeamInform[i].append(float(list_TeamInform[i][1]) / float(All_game))  # [i][4]에 "승/전체 게임"으로 승률 입력.
    list_TeamInform.sort(key=lambda x: x[4])  # [i][4]를 기준으로 배열 재정렬
    list_TeamInform.reverse()  # sort는 내림차순이므로 오름차순으로 재정의


def who_winner():
    # 내가 응원하는 Team이 포스트시즌에 진출했는지 판별
    is_it_done = 0
    post_season = 4
    while list_TeamInform[3][4] == list_TeamInform[post_season][4]:
        # list_TeamInfo[3][4]는 4위의 승률, list_TeamInfo[4][4]는 5위의 승률. 공동일 수 있으므로.
        post_season += 1
        # 몇 번째까지 공동 4위일지 모르니 계속 확인
    for i in range(post_season):  # 몇 등까지 공동 4위인가.
        if list_TeamInform[i][0] == My_Team:
            is_it_done = 1
            break
            # 포스트시즌에 진출한 팀들 중 내가 응원하는 팀이 있는지 찾음
    for i in range(8):
        del list_TeamInform[i][4]  # TC 1회가 돌 때마다, 배열의 열이(4, 5, 6 ...) 증가(append)하지 않도록 삭제
    if is_it_done == 1:
        return 1
    else:
        return 0

'''
Main 코드
'''
T = int(input())
for test_case in range(T):  # 입력된 TC 수 만큼, TC 처리.(예제는 2)
    for i in range(8):      # 8팀의 팀명, 승무패 입력받고 승무패를 정수형으로 변환
        list_TeamInform[i] = input().split()  # ex. SK 80 2 45, [i][0]=SK, [i][1]=80, [i][2]=2, [i][3]=45
        list_TeamInform[i][1:4] = map(int, list_TeamInform[i][1:4])  # 승/무/패를 int형태로 변환
    My_Team = input()
    remain_GameNum = int(input())  # 문제: 잔여 경기의 수 R (0 <= R <= 25) 가 주어짐
    My_Team_num = find_Team(My_Team)  # 내 Team의 index값을 행 번호로 반환
    for i in range(remain_GameNum):  # 남은 게임 수 만큼 돎
        list_remainGame = input().split()  # 문제: 각 잔여 경기에 대한 정보인 R 행이 그 다음에 주어짐
        left_Team = find_Team(list_remainGame[0])
        right_Team = find_Team(list_remainGame[1])
        # 남은 경기들을 순서대로 입력받으며 각 Team의 index값 반환
        if list_remainGame[0] == My_Team:
            list_TeamInform[My_Team_num][1] += 1
            list_TeamInform[right_Team][3] += 1
        elif list_remainGame[1] == My_Team:
            list_TeamInform[My_Team_num][1] += 1
            list_TeamInform[left_Team][3] += 1
        # 내가 응원하는 Team의 경기가 이겨야하므로, 내 팀이 왼쪽일 때 +1, 오른쪽일 때 +1하여 응원 Team이 이기도록 설계
        else:
            list_TeamInform[left_Team][2] += 1
            list_TeamInform[right_Team][2] += 1
        # 내가 응원하는 Team의 경기가 아니라면 둘 다 무승부.
        # 승률 계산 시, 무승부 경기를 포함하여 합한 후 승리로 나눔
        # 두 팀 다 무승부로 설계하면 모두 승률이 낮아짐

    calculate_All_Rating()

    if who_winner() == 1:
        print("Yes")
    else:
        print("No")
