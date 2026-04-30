from pathlib import Path  # 파일/폴더 경로를 운영체제에 맞게 안전하게 다루기 위한 표준 라이브러리
import pandas as pd # 데이터 분석용 라이브러리 pandas를 pd라는 별칭으로 불러오기

csv_path = Path(__file__).parent / "Titanic-Dataset.csv" # 현재 이 .py 파일이 있는 폴더(apps) 안의 CSV 경로 만들기
df = pd.read_csv(csv_path) # 위에서 만든 경로의 CSV 파일을 읽어서 DataFrame(df)으로 로드
print(df.head()) # 데이터의 앞 5행만 출력해서 형태를 빠르게 확인
print(df.shape)# (행 개수, 열 개수)를 튜플로 출력