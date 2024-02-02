import requests

def fetch_and_save_data(base_url, start_number, end_number):
    for number in range(start_number, end_number + 1):
        # URL에 number 값을 추가
        url = f"{base_url}&number={number}"

        # 데이터 요청
        response = requests.get(url)
        
        if response.status_code == 200:
            # JSON 데이터를 문자열로 변환
            data_str = response.text

            # 파일에 저장
            with open(f"data_{number}.txt", "w", encoding="utf-8") as file:
                file.write(data_str)

            print(f"Data for number {number} saved successfully.")
        else:
            print(f"Failed to fetch data for number {number}. Status code: {response.status_code}")

# 스크립트 실행
base_url = "https://open.jejudatahub.net/api/proxy/5D5a577taba7tbb71at1b1bt9tatata9/7__p2t727cjto6btr2b72rj_722tpj7t?startDate=20180101&endDate=20181231&limit=100"
fetch_and_save_data(base_url, 1, 81)
