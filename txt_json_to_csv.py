import json
import csv

def read_json_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.loads("[" + ",".join(file.readlines()) + "]")
    except Exception as e:
        print(f"An error occurred while reading the file: {str(e)}")
        return None

def convert_json_to_csv(json_data, csv_filename):
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)

        # 컬럼명선택 및 정렬
        columns = ['title','contentsid','type_value','type_label',
                    'address', 'roadaddress','postcode', 'phoneno',
                    'latitude', 'longitude','region1cd_value','region1cd_label',
                    'region2cd_value', 'region2cd_label',
                    'photoid','imgpath', 'thumbnailpath',
                    'introduction','alltags','tag']
        csvwriter.writerow(columns)
        
        # 데이터 처리
        for data in json_data:
            for item in data['items']:
                try:
                    row = [
                        item.get('title', ''),
                        item.get('contentsid', ''),
                        item.get('contentscd', {}).get('value', ''),
                        item.get('contentscd', {}).get('label', ''),
                        item.get('address', ''),
                        item.get('roadaddress', ''),
                        item.get('postcode', ''),
                        item.get('phoneno', ''),
                        item.get('latitude', ''),
                        item.get('longitude', ''),
                        item.get('region1cd', {}).get('value', ''),
                        item.get('region1cd', {}).get('label', ''),
                        item.get('region2cd', {}).get('value', ''),
                        item.get('region2cd', {}).get('label', ''),
                        # 예외 처리 추가
                        item.get('repPhoto', {}).get('photoid', {}).get('photoid', ''), 
                        item.get('repPhoto', {}).get('photoid', {}).get('imgpath', ''),
                        item.get('repPhoto', {}).get('photoid', {}).get('thumbnailpath', ''),
                        item.get('introduction', ''),
                        item.get('alltag', ''),
                        item.get('tag', '')
                    ]
                    csvwriter.writerow(row)
                except AttributeError as e:
                    # 'repPhoto'가 null일 때 예외 처리
                    print(f"AttributeError: {e}. Skipping this item.")
                    continue
# 파일 읽기
json_data = read_json_file('Accom.txt')
# CSV로 변환 및 저장
convert_json_to_csv(json_data, 'Accom.csv')

