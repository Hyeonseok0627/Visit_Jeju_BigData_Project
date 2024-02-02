import csv
import requests
from bs4 import BeautifulSoup

# 크롤링할 웹페이지 URL 설정
url = 'https://7thchord.tistory.com/entry/%EC%A0%9C%EC%A3%BC%EB%8F%84-%ED%98%B8%ED%85%94-%EC%88%9C%EC%9C%84-Top-100-%EC%B6%94%EC%B2%9C-%EB%A6%AC%EC%8A%A4%ED%8A%B8'
res = requests.get(url)
res.raise_for_status()

print("응답코드 :", res.status_code)

# BeautifulSoup을 사용하여 HTML 파싱
soup = BeautifulSoup(res.text, 'html.parser')


# 첫 번째 테이블 추출
first_table_data_list = []
heading_text_1 = '선호도 순위 리스트'
heading_tag_1 = soup.find('h4', string=heading_text_1)
if heading_tag_1:
    first_table = heading_tag_1.find_next('table')
    if first_table:
        for item in first_table.select('tbody > tr:not(:first-child) > td'):
            data = item.text.strip()
            first_table_data_list.append(data)

# 두 번째 테이블 추출
second_table_data_list = []
heading_text_2 = '시별 분류 리스트'
heading_tag_2 = soup.find('h4', string=heading_text_2)
if heading_tag_2:
    second_table = heading_tag_2.find_next('table')
    if second_table:
        for item in second_table.select('tbody > tr:not(:first-child) > td'):
            data = item.text.strip()
            second_table_data_list.append(data)

# CSV 파일로 저장 (첫 번째 테이블)
csv_filename_first = '/제주호텔top100/jeju_hotel_top100.csv'
with open(csv_filename_first, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['순위', '호텔명', '검색건수']) 

    for i in range(0, len(first_table_data_list), 3):
        csv_writer.writerow([first_table_data_list[i], first_table_data_list[i+1], first_table_data_list[i+2]])

print(f'첫 번째 테이블 데이터가 {csv_filename_first}에 저장되었습니다.')

# CSV 파일로 저장 (두 번째 테이블)
csv_filename_second = '/제주호텔top100/jeju_hotel_sig_top100.csv'
with open(csv_filename_second, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['구분', '호텔명', '검색건수', '주소'])

    for i in range(0, len(second_table_data_list), 4):
        csv_writer.writerow([second_table_data_list[i], second_table_data_list[i+1], second_table_data_list[i+2], second_table_data_list[i+3]])

print(f'두 번째 테이블 데이터가 {csv_filename_second}에 저장되었습니다.')






