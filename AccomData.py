import requests


#Open API Json형식 데이터 txt 파일로 저장
base_url = "https://api.visitjeju.net/vsjApi/contents/searchList?apiKey=qsrmyedxqq5zvf9u&locale=kr&category=c3"

def fetch_and_save_combined_data(base_url, start_page, end_page):
    # 모든 데이터를 저장할 문자열 변수 초기화
    all_Accom_data = "" 
    
    # base url 뒤에 page파라미터 추가,
    # page수 만큼 ++page하면서 반복 
    for page in range(start_page, end_page + 1):
        url = f"{base_url}&page={page}"

        # Url로 부터 데이터 request get으로 받아옴
        response = requests.get(url)
        if response.status_code == 200:
            data_str = response.text
            all_Accom_data += data_str + "\n" 
            # 각 페이지의 데이터를 all_data에 추가

            print(f"Data for page {page} fetched successfully.")
        else:
            # 실패 시 콜백 받기
            print(f"Failed to fetch data for page {page}.Status code: {response.status_code}")

    # 모든 페이지의 데이터를 하나의 파일에 저장
    with open("Accom.txt", "w", encoding="utf-8") as file:
        file.write(all_Accom_data)
    print("All data combined and saved in combined_data.txt.")

# 스크립트 실행
fetch_and_save_combined_data(base_url, 1, 11)
