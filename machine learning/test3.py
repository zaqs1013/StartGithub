import requests

url = "https://bit.ly/fruits_300_data"
file_path = "fruits_300.npy"

response = requests.get(url, stream=True)

if response.status_code == 200:
    with open(file_path, "wb") as file:
        file.write(response.content)
    print("파일 다운로드 완료:", file_path)
else:
    print("다운로드 실패. URL을 확인하세요.")