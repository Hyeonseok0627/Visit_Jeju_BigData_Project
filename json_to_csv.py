import json
import csv

def convert_json_to_csv(json_file_path, csv_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as file:
        # 모든 JSON 객체를 하나의 리스트로 결합
        json_data = json.loads("[" + ",".join(file.readlines()) + "]")

    # CSV 파일 생성
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=json_data[0].keys())
        
        # CSV 헤더 작성
        writer.writeheader()

        # JSON 데이터를 CSV로 쓰기
        for item in json_data:
            writer.writerow(item)

    print(f"JSON data from {json_file_path} has been converted to CSV format in {csv_file_path}")

# 함수 호출
convert_json_to_csv('combined_data.txt', 'output11.csv')
