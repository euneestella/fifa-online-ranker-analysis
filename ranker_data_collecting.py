# import module
import json
import pandas as pd
import requests

from pandas import DataFrame
from tqdm.notebook import tqdm


# 넥슨 개발자센터에서 발급받은 키를 입력하세요
api_key = 'your_api_key'


# 선수 고유 식별자 조회
spId_url = requests.get('https://static.api.nexon.co.kr/fifaonline4/latest/spid.json')
spId_parsed_data = spId_url.json()
spId = pd.DataFrame(spId_parsed_data)


# 선수 포지션 조회
spposition_url = requests.get('https://static.api.nexon.co.kr/fifaonline4/latest/spposition.json')
spposition_parsed_data = spposition_url.json()
spposition = pd.DataFrame(spposition_parsed_data)


# 랭커 유저가 이용한 특정 선수의 포지션 조합 조회
positions = list(spposition['spposition'])
player_positions = messi_positions = json.dumps([{"id":proper_spId, "po":x} for x in positions]) # "id": 에는 선수 고유 식별자를 입력합니다

headers = {'Authorization' : api_key}
jsonurl = "https://api.nexon.co.kr/fifaonline4/v1.0/rankers/status?matchtype=50&players="

try :
    for i in tqdm(range(len(positions))):
        response = requests.get(jsonurl+player_positions, headers = headers)
        json = response.json()
        player_ranker = pd.json_normalize(json)

except Exception as e :
    print("Error message: ", e)