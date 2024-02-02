def combine_files(start_number, end_number, output_file):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for number in range(start_number, end_number + 1):
            file_name = f"data_{number}.txt"
            try:
                with open(file_name, 'r', encoding='utf-8') as infile:
                    contents = infile.read()
                    outfile.write(contents + "\n")  # 파일 내용을 쓰고, 줄 바꿈 추가
                    print(f"Added data from {file_name} to {output_file}.")
            except FileNotFoundError:
                print(f"File {file_name} not found. Skipping.")

# 파일들을 하나로 합치기
combine_files(1, 81, "combined_data.txt")
