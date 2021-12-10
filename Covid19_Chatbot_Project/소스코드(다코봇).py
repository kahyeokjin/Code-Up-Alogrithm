from flask import Flask, request,jsonify
from bs4 import BeautifulSoup
from datetime import date, datetime, timedelta
import xmltodict
import urllib.request
import requests
import json

app = Flask(__name__)

@app.route('/api/seoulCorona', methods=['POST'])
def seoulCorona():
    body = request.get_json()
    print(body)
    url = 'http://openapi.seoul.go.kr:8088/594e6c44786a68393132324d436c7973/json/TbCorona19CountStatusJCG/1/10/'
    response = urllib.request.urlopen(url)
    result=response.read().decode("utf-8")
    body_json=json.loads(result)
    
    city = body["action"]["params"]["자치구"]
    total_list = body_json['TbCorona19CountStatusJCG']['row']
    today = total_list[0]
    
    total_city = today[city]
    today_city = today[city+"ADD"]
    total_city = "{:,}".format(int(total_city))
    
    city_hangeul = body["action"]["detailParams"]["자치구"]['origin']
    if city_hangeul[-1] != "구":
        city_hangeul = city_hangeul + '구'

    today_city_int=int(today_city)

    day=0
    average_sum=0
    while day <= 9:
        num=int(total_list[day][city+"ADD"])
        average_sum=average_sum+num
        day+=1
    average=round(average_sum/10)
    print(average)

    if today_city_int > average*1.2:
        text= "\"위험🔴\""
    elif today_city_int <average*0.5:
        text="\"안전🟢\""
    else:
        text="\"주의🟡\""
    print(today_city)
    return {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": f"{city_hangeul}의 전체 확진자 수는 {total_city}명 입니다.\n{city_hangeul}의 금일 확진자 수는 {today_city}명 입니다.\n{city_hangeul}의 10일간의 평균 확진자수는 {average}명이며,\n외출난이도는 {text}입니다."
                        
                    }
                }
            ]
        }
    }
@app.route('/api/koreaCorona', methods=['POST'])
def koreaCorona():
    body = request.get_json()
    print(body)
    global covid_level

    input_k_city = body["action"]["params"]["시도"]

    today = date.today()
    days = timedelta(days=-1)
    dataday = today+days
    dataday = dataday.strftime('%Y%m%d')

    url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?serviceKey=h327OuruPqwMMgLZ5kmrI2I6i2ORzZcmBZpFecofBV%2Bp8KGrSC1VOgKlv5OmAxgNc2Ri7afVgSl%2FW19yh8Z94Q%3D%3D&pageNo=1&numOfRows=10&startCreateDt='+dataday
    response = urllib.request.urlopen(url)
    result=response.read().decode("utf-8")
    results_to_json = xmltodict.parse(result)
    data = json.loads(json.dumps(results_to_json))
    
    url = 'https://www.data.go.kr/tcs/dss/selectHistAndCsvData.do?publicDataPk=15089317&publicDataDetailPk=uddi%3A23f5d02f-0047-46c8-a938-defadc2ab47c&url=%2Ftcs%2Fdss%2FselectHistAndCsvData.do'
    response = urllib.request.urlopen(url)
    result=response.read().decode("utf-8")
    results_to_json = xmltodict.parse(result)
    data_2 = json.loads(json.dumps(results_to_json))

    for i in range(19):
        if input_k_city == data["response"]["body"]["items"]["item"][i]['gubun']:
            total_k_city = data["response"]["body"]["items"]["item"][i]['defCnt']
            add_k_city = data["response"]["body"]["items"]["item"][i]['incDec']

    for i in range(1, 18):
        if input_k_city == data_2["div"]["div"][1]["div"]["table"]["tr"][i]["td"][1]["#text"]:
            covid_level = data_2["div"]["div"][1]["div"]["table"]["tr"][i]["td"][2]["#text"]
            level_plus = data_2["div"]["div"][1]["div"]["table"]["tr"][i]["td"][3]["#text"]

    if input_k_city == "강원" or input_k_city == "제주" or input_k_city == "경기":
        input_k_city = input_k_city + "도"

    total_k_city = "{:,}".format(int(total_k_city))
    add_k_city = "{:,}".format(int(add_k_city))

    return {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": f"{input_k_city}의 총 확진자 수는 {total_k_city}명 입니다. \n{input_k_city}의 오늘 확진자 수는 {add_k_city}명 입니다."
                    }
                },
                {
                    "simpleText": {
                        "text": f"{input_k_city}의 거리두기 단계는 {covid_level}단계 입니다. \n*추가정보*\n{level_plus}"
                    }
                }
                
            ],
             "quickReplies": [
                  {
        "messageText":f"{covid_level}단계기준 규제정보",
        "action": "message",
        "label": f"{input_k_city}의 거리두기 규범조회"
      }
    ]
        }
    }

@app.route('/api/coronaRules', methods=['POST'])
def coronaRules():
    with open('rules_level.csv') as file_object:
        lines = file_object.readlines()
    body = request.get_json()
    print(body)
    place_Typet = body["action"]["params"]["규제정보"]

    if place_Typet == "1모임" or place_Typet == "모임1":
        textt= lines[1]
        
    elif place_Typet=="1종교시설" or place_Typet == "종교시설1":
        textt= lines[2]
        
    elif place_Typet=="1식당" or place_Typet=="식당1" or place_Typet=="1카페" or place_Typet=="카페1":
        textt= lines[3]
        
    elif place_Typet=="1pc방" or place_Typet=="pc방1":
        textt= lines[4]
        
    elif place_Typet=="1노래방" or place_Typet=="노래방1":
        textt= lines[5]
        
    elif place_Typet=="1학교" or place_Typet == "학교1":
        textt= lines[6]
        
    elif place_Typet=="1독서실" or place_Typet=="독서실1" or place_Typet=="1스터디카페" or place_Typet=="스터디카페1":
        textt= lines[7]
        
    elif place_Typet=="1오락실" or place_Typet=="오락실1":
        textt= lines[8]
        
    elif place_Typet=="1실내체육시설" or place_Typet=="실내체육시설1":
        textt= lines[9]
        
    elif place_Typet=="1목욕탕" or place_Typet == "목욕탕1":
        textt= lines[10]
        
    elif place_Typet=="1유흥시설" or place_Typet=="유흥시설1" or place_Typet=="1술집" or place_Typet=="술집1":
        textt= lines[11]
        
    elif place_Typet=="1장례식" or place_Typet=="장례식1" or place_Typet=="1결혼식" or place_Typet=="결혼식1":
        textt= lines[12]
        
    elif place_Typet=="1마트" or place_Typet=="마트1" or place_Typet=="1상점" or place_Typet=="상점1"or place_Typet=="1백화점" or place_Typet=="백화점1":
        textt= lines[13]
        
    elif place_Typet=="1영화관" or place_Typet=="영화관1" or place_Typet=="1공연장" or place_Typet=="공연장1":
        textt= lines[14]


    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": textt
                    }
                }
            ]
        }
    }

    # 답변 전송
    return jsonify(res)

@app.route('/api/coronaRules2', methods=['POST'])
def coronaRules2():
    with open('rules_level.csv') as file_object:
        lines = file_object.readlines()
    body = request.get_json()
    print(body)
    place_Type = body["action"]["params"]["규제정보둘"]

    if place_Type == "2모임" or place_Type == "모임2":
        textt= lines[17]

    elif place_Type=="2종교시설" or place_Type == "종교시설2":
        textt= lines[18]
        
    elif place_Type=="2식당" or place_Type=="식당2" or place_Type=="2카페" or place_Type=="카페2":
        textt= lines[19]
        
    elif place_Type=="2pc방" or place_Type=="pc방2":
        textt= lines[20]
        
    elif place_Type=="2노래방" or place_Type=="노래방2":
        textt= lines[21]
        
    elif place_Type=="2학교" or place_Type == "학교2":
        textt= lines[22]
        
    elif place_Type=="2독서실" or place_Type=="독서실2" or place_Type=="2스터디카페" or place_Type=="스터디카페2":
        textt= lines[23]
        
    elif place_Type=="2오락실" or place_Type=="오락실2":
        textt= lines[24]
        
    elif place_Type=="2실내체육시설" or place_Type=="실내체육시설2":
        textt= lines[25]
        
    elif place_Type=="2목욕탕" or place_Type == "목욕탕2":
        textt= lines[26]
        
    elif place_Type=="2유흥시설" or place_Type=="유흥시설2" or place_Type=="2술집" or place_Type=="술집2":
        textt= lines[27]
        
    elif place_Type=="2장례식" or place_Type=="장례식2" or place_Type=="2결혼식" or place_Type=="결혼식2":
        textt= lines[28]
        
    elif place_Type=="2마트" or place_Type=="마트2" or place_Type=="2상점" or place_Type=="상점2"or place_Type=="2백화점" or place_Type=="백화점2":
        textt= lines[29]
        
    elif place_Type=="2영화관" or place_Type=="영화관2" or place_Type=="2공연장" or place_Type=="공연장2":
        textt= lines[30]


    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": text
                    }
                }
            ]
        }
    }

    # 답변 전송
    return jsonify(res)

@app.route('/api/coronaRules3', methods=['POST'])
def coronaRules3():
    with open('rules_level.csv') as file_object:
        lines = file_object.readlines()
    body = request.get_json()
    print(body)
    place_Typer = body["action"]["params"]["규제정보셋"]

    if place_Typer == "3모임" or place_Typer == "모임3":
        textt= lines[33]
        
    elif place_Typer=="3종교시설" or place_Typer == "종교시설3":
        textt= lines[34]
        
    elif place_Typer=="3식당" or place_Typer=="식당3" or place_Typer=="3카페" or place_Typer=="카페3":
        textt= lines[35]
        
    elif place_Typer=="3pc방" or place_Typer=="pc방3":
        textt= lines[36]
        
    elif place_Typer=="3노래방" or place_Typer=="노래방3":
        textt= lines[37]
        
    elif place_Typer=="3학교" or place_Typer == "학교3":
        textt= lines[38]
        
    elif place_Typer=="3독서실" or place_Typer=="독서실3" or place_Typer=="3스터디카페" or place_Typer=="스터디카페3":
        textt= lines[39]
        
    elif place_Typer=="3오락실" or place_Typer=="오락실3":
        textt= lines[40]
        
    elif place_Typer=="3실내체육시설" or place_Typer=="실내체육시설3":
        textt= lines[41]
        
    elif place_Typer=="3목욕탕" or place_Typer == "목욕탕3":
        textt= lines[42]
        
    elif place_Typer=="3유흥시설" or place_Typer=="유흥시설3" or place_Typer=="3술집" or place_Typer=="술집3":
        textt= lines[43]
        
    elif place_Typer=="3장례식" or place_Typer=="장례식3" or place_Typer=="3결혼식" or place_Typer=="결혼식3":
        textt= lines[44]
        
    elif place_Typer=="3마트" or place_Typer=="마트3" or place_Typer=="3상점" or place_Typer=="상점3"or place_Typer=="3백화점" or place_Typer=="백화점3":
        textt= lines[45]
        
    elif place_Typer=="3영화관" or place_Typer=="영화관3" or place_Typer=="3공연장" or place_Typer=="공연장3":
        textt= lines[46]

    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": textr
                    }
                }
            ]
        }
    }

    # 답변 전송
    return jsonify(res)

@app.route('/api/coronaRules4', methods=['POST'])
def coronaRules4():
    with open('rules_level.csv') as file_object:
        lines = file_object.readlines()
    body = request.get_json()
    print(body)
    place_Typez = body["action"]["params"]["규제정보넷"]

    if place_Typez == "4모임" or place_Typez == "모임4" or place_Typez == "4모임?" or place_Typez == "모임4 알려줘" or place_Typez == "4단계 모임?" or place_Typez == "모임4단계기준알려줘" or place_Typez == "4모임 궁금해":
        textz= lines[49]
        
    elif place_Typez=="4종교시설" or place_Typez == "종교시설4":
        textz= lines[50]
        
    elif place_Typez=="4식당" or place_Typez=="식당4" or place_Typez=="4카페" or place_Typez=="카페4":
        textz= lines[51]
        
    elif place_Typez=="4pc방" or place_Typez=="pc방4":
        textz= lines[52]
        
    elif place_Typez=="4노래방" or place_Typez=="노래방4":
        textz= lines[53]
        
    elif place_Typez=="4학교" or place_Typez == "학교4":
        textz= lines[54]
        
    elif place_Typez=="4독서실" or place_Typez=="독서실4" or place_Typez=="4스터디카페" or place_Typez=="스터디카페4":
        textz= lines[55]
        
    elif place_Typez=="4오락실" or place_Typez=="오락실4":
        textz= lines[56]
        
    elif place_Typez=="4실내체육시설" or place_Typez=="실내체육시설4":
        textz= lines[57]
        
    elif place_Typez=="4목욕탕" or place_Typez == "목욕탕4":
        textz= lines[58]
        
    elif place_Typez=="4유흥시설" or place_Typez=="유흥시설4" or place_Typez=="4술집" or place_Typez=="술집4":
        textz= lines[59]
        
    elif place_Typez=="4장례식" or place_Typez=="장례식4" or place_Typez=="4결혼식" or place_Typez=="결혼식4":
        textz= lines[60]
        
    elif place_Typez=="4마트" or place_Typez=="마트4" or place_Typez=="4상점" or place_Typez=="상점4"or place_Typez=="4백화점" or place_Typez=="백화점4":
        textz= lines[61]
        
    elif place_Typez=="4영화관" or place_Typez=="영화관4" or place_Typez=="4공연장" or place_Typez=="공연장4":
        textz= lines[62]

    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": textz
                    }
                }
            ]
        }
    }

    # 답변 전송
    return jsonify(res)

@app.route('/api/coronaRules0', methods=['POST'])
def coronaRules0():
    with open('with_corona.csv') as file_object:
        lines = file_object.readlines()
    body = request.get_json()
    print(body)
    place_Typef = body["action"]["params"]["규제정보영"]

    if place_Typef == "0모임" or place_Typef == "모임0":
        textf= lines[2]
        
    elif place_Typef=="0기념식" or place_Typef == "기념식0" or place_Typef == "행사0" or place_Typef == "행사0":
        textf= lines[3]
        
    elif place_Typef=="0식당" or place_Typef=="식당0" or place_Typef=="0카페" or place_Typef=="카페0":
        textf= lines[4]
        
    elif place_Typef=="0영화관" or place_Typef=="영화관0":
        textf= lines[5]
        
    elif place_Typef=="0헬스장" or place_Typef=="헬스장0":
        textf= lines[6]
        
    elif place_Typef=="0콘서트" or place_Typef == "콘서트0":
        textf= lines[7]
        
    elif place_Typef=="0야구장" or place_Typef=="야구장0" or place_Typef=="경기관람0" or place_Typef=="0경기관람":
        textf= lines[8]
        
    elif place_Typef=="0결혼식" or place_Typef=="결혼식0":
        textf= lines[9]
        
    elif place_Typef=="0노래방" or place_Typef=="노래방0":
        textf= lines[10]
        
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": textf
                    }
                }
            ]
        }
    }

    # 답변 전송
    return jsonify(res)


@app.route('/api/coronaRulesCh', methods=['POST'])
def coronaRulesCh():
    with open('rules_level.csv') as file_object:
        lines = file_object.readlines()
    body = request.get_json()
    print(body)
    place_Typ = body["action"]["params"]["지정된규제정보"]
    
    global tex
    
    if covid_level == "1":
        if place_Typ == "모임":
            tex= lines[1]

        elif place_Typ=="종교시설":
            tex= lines[2]
        
        elif place_Typ=="식당" or  place_Typ=="카페":
            tex= lines[3]
        
        elif place_Typ=="pc방":
            tex= lines[4]
        
        elif place_Typ=="노래방":
            tex= lines[5]
        
        elif place_Typ=="학교":
            tex= lines[6]
        
        elif place_Typ=="독서실" or place_Typ=="스터디카페":
            tex= lines[7]
        
        elif place_Typ=="오락실":
            tex= lines[8]
        
        elif place_Typ=="실내체육시설":
            tex= lines[9]
        
        elif place_Typ=="목욕탕":
            tex= lines[10]
        
        elif place_Typ=="유흥시설" or place_Typ=="술집":
            tex= lines[11]
        
        elif place_Typ=="장례식" or place_Typ=="결혼식":
            tex= lines[12]
        
        elif place_Typ=="마트" or place_Typ=="상점" or place_Typ=="백화점":
            tex= lines[13]
        
        elif place_Typ=="영화관" or place_Typ=="공연장":
            tex= lines[14]
    
    elif covid_level == "2":
        if place_Typ == "모임":
            tex= lines[17]
        
        elif place_Typ=="종교시설":
            tex= lines[18]
        
        elif place_Typ=="식당" or  place_Typ=="카페":
            tex= lines[19]
        
        elif place_Typ=="pc방":
            tex= lines[20]
            
        elif place_Typ=="노래방":
            tex= lines[21]
        
        elif place_Typ=="학교":
            tex= lines[22]
        
        elif place_Typ=="독서실" or place_Typ=="스터디카페":
            tex= lines[23]
        
        elif place_Typ=="오락실":
            tex= lines[24]
        
        elif place_Typ=="실내체육시설":
            tex= lines[25]
        
        elif place_Typ=="목욕탕":
            tex= lines[26]
        
        elif place_Typ=="유흥시설" or place_Typ=="술집":
            tex= lines[27]
        
        elif place_Typ=="장례식" or place_Typ=="결혼식":
            tex= lines[28]
        
        elif place_Typ=="마트" or place_Typ=="상점" or place_Typ=="백화점":
            tex= lines[29]
        
        elif place_Typ=="영화관" or place_Typ=="공연장":
            tex= lines[30]
    
    elif covid_level == "3":
        if place_Typ == "모임":
            tex= lines[33]
        
        elif place_Typ=="종교시설":
            tex= lines[34]
        
        elif place_Typ=="식당" or place_Typ=="카페":
            tex= lines[35]
        
        elif place_Typ=="pc방":
            tex= lines[36]
        
        elif place_Typ=="노래방":
            tex= lines[37]
        
        elif place_Typ=="학교":
            tex= lines[38]
        
        elif place_Typ=="독서실" or place_Typ=="스터디카페":
            tex= lines[39]
        
        elif place_Typ=="오락실":
            tex= lines[40]
        
        elif place_Typ=="실내체육시설":
            tex= lines[41]
        
        elif place_Typ=="목욕탕":
            tex= lines[42]
        
        elif place_Typ=="유흥시설" or place_Typ=="술집":
            tex= lines[43]
        
        elif place_Typ=="장례식" or place_Typ=="결혼식":
            tex= lines[44]
        
        elif place_Typ=="마트" or place_Typ=="상점" or place_Typ=="백화점":
            tex= lines[45]
        
        elif place_Typ=="영화관" or place_Typ=="공연장":
            tex= lines[46]
        
    elif covid_level == "4":
        
        if place_Typ == "모임" or place_Typ=="모임알려줘" or place_Typ=="모임규제정보궁금해" or place_Typ=="서울에서모임" or place_Typ=="몇명까지 모이는거 가능해?":
            tex= lines[49]
        
        elif place_Typ =="종교시설":
            tex= lines[50]
        
        elif place_Typ=="식당" or place_Typ=="카페":
            tex= lines[51]
        
        elif place_Typ=="pc방":
            tex= lines[52]
        
        elif place_Typ=="노래방":
            tex= lines[53]
        
        elif place_Typ=="학교":
            tex= lines[54]
        
        elif place_Typ=="독서실" or place_Typ=="스터디카페":
            tex= lines[55]
        
        elif place_Typ=="오락실":
            tex= lines[56]
        
        elif place_Typ=="실내체육시설":
            tex= lines[57]
        
        elif place_Typ=="목욕탕":
            tex= lines[58]
        
        elif place_Typ=="유흥시설" or place_Typ=="술집":
            tex= lines[59]
        
        elif place_Typ=="장례식" or place_Typ=="결혼식":
            tex= lines[60]
        
        elif place_Typ=="마트" or place_Typ=="상점" or place_Typ=="백화점":
            tex= lines[61]
        
        elif place_Typ=="영화관" or place_Typ=="공연장":
            tex= lines[62]


    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": tex
                    }
                }
            ]
        }
    }

    # 답변 전송
    return jsonify(res)

@app.route('/api/seoulCheck', methods=['POST'])
def seoulCheck():
    body = request.get_json()
    print(body)
    url = 'https://ncv.kdca.go.kr/restApi/traffic/?cid=naver&key=19acaddba0774badb8de6deb17f0eecc'
    response = urllib.request.urlopen(url)
    result=response.read().decode("utf-8")
    body_json=json.loads(result)

    list_check = []
    sort_check = []
    sort_name = []
    congestion = []
    city = body["action"]["params"]["검사소위치"]
    city = city.split()
    gu_name = city[0]
    seoul_list = body_json["seoul"]["body"]
    for i in range(len(seoul_list)):
        if gu_name == seoul_list[i]["COT_GU_NAME"]:
            list_check.append(seoul_list[i])

    for i in range(len(list_check)):
        if list_check[i]["COT_THEME_SUB_ID"] == "1":
            sort_check.append(list_check[i])
            congestion.append("🟢 보통 (30분 이내 검사가능)")
    for i in range(len(list_check)):
        if list_check[i]["COT_THEME_SUB_ID"] == "2":
            sort_check.append(list_check[i])
            congestion.append("🟠 붐빔 (60분 내외 검사가능)")
    for i in range(len(list_check)):
        if list_check[i]["COT_THEME_SUB_ID"] == "3":
            sort_check.append(list_check[i])
            congestion.append("🔴 혼잡 (검사시간 90분 이상 소요예정)")
    for i in range(len(list_check)):
        if list_check[i]["COT_THEME_SUB_ID"] == "43":
            sort_check.append(list_check[i])
            congestion.append("⚠ 혼잡도 조사중")
    for i in range(len(list_check)):
        if list_check[i]["COT_THEME_SUB_ID"] == "7":
            sort_check.append(list_check[i])
            congestion.append("❗ 소독 등 잠시중단")
    for i in range(len(sort_check)):
        sort_name.append(sort_check[i]["COT_CONTS_NAME"])
    for i in range(4):
        sort_name.append("")
        congestion.append("")
        
    print(sort_name)
    
    if len(sort_name[0]) == 0:
        res = {"version": "2.0","template": {"outputs": [{"simpleText": {"text": "현재 해당위치에 검사 가능한 검사소가 없습니다!"}}],
                                             "quickReplies": [
                                                 {"messageText":"자치구별 코로나검사소정보","action": "message","label": "초기화" }
                                             ]
                                            }
              }
                                                         
    else:
        res = {"version": "2.0","template": {"outputs": [
            {"listCard": {
                "header": {
                    "title": f"{gu_name} 근처 선별검사소 목록"
                },
                "items": [
                    {
                        "title": f"{sort_name[0]}",
                        "description": f"{congestion[0]}",
                        "link": {"web": f"https://map.kakao.com/?map_type=TYPE_MAP&q={sort_name[0]}"}
                    },
                    {
                        "title": f"{sort_name[1]}",
                        "description": f"{congestion[1]}",
                        "link": {"web": f"https://map.kakao.com/?map_type=TYPE_MAP&q={sort_name[1]}"}
                    },
                    {
                        "title": f"{sort_name[2]}",
                        "description": f"{congestion[2]}",
                        "link": {"web": f"https://map.kakao.com/?map_type=TYPE_MAP&q={sort_name[2]}"}
                    },
                    {
                        "title": f"{sort_name[3]}",
                        "description": f"{congestion[3]}",
                        "link": {"web": f"https://map.kakao.com/?map_type=TYPE_MAP&q={sort_name[3]}"}
                    }
                ],
                "buttons": [
                    {
                        "label": "자세한 정보 확인",
                        "action": "webLink",
                        "webLinkUrl": "https://map.seoul.go.kr/smgis2/short/6NjT7"
                    }
                ]
            }}]}}
    
    return jsonify(res)
            

######################################################  마스크 선별 프로그램
with open('MaskDatabase.json') as mask_file:
    mask_line = mask_file.reads().decode("utf-8")
    mask_data=json.loads(mask_line)
        
#마스크가 존재하지 않을 시
no_mask = {
  "version": "2.0",
  "template": {
    "outputs": [{"simpleText": {"text": "해당조건을 만족하는 마스크가 없습니다."}}],
                 "quickReplies": [
                     {"messageText":"초기화","action": "message","label": "초기화" }
                 ]}
}

maskSelect = [0, 0, 0, 0, 0]

maskQues1 = {
    "version": "2.0",
    "template": {"outputs": [{"simpleText": {"text": "일회용마스크인가요?\n다회용마스크인가요?"}}], 
                 "quickReplies": [
                     {"messageText":"일회용","action": "message","label": "일회용마스크" },
                     {"messageText":"다회용","action": "message","label": "다회용마스크" },
                     {"messageText":"초기화","action": "message","label": "초기화" }
                 ]
                }
}

maskQues2 = {
    "version": "2.0",
    "template": {"outputs": [{"simpleText": {"text": "피부가 예민하신가요?"}}],
                 "quickReplies": [
                     {"messageText":"민감함","action": "message","label": "민감해요" },
                     {"messageText":"민감하지않음","action": "message","label": "민감하지 않아요" },
                     {"messageText":"초기화","action": "message","label": "초기화" }
                 ]
                }
}

maskQues3 = {
    "version": "2.0",
    "template": {"outputs": [{"simpleText": {"text": "김서림 방지기능이 필요하신가요?"}}],
                 "quickReplies": [
                     {"messageText":"김서림방지","action": "message","label": "필요해요" },
                     {"messageText":"김서림방지필요없음","action": "message","label": "필요하지 않아요" },
                     {"messageText":"초기화","action": "message","label": "초기화" }
                 ]
                }
}

maskQues4 = {
    "version": "2.0",
    "template": {"outputs": [{"simpleText": {"text": "차단지수를 선택해주세요"}}],
                 "quickReplies": [
                     {"messageText":"KF99","action": "message","label": "KF-99" },
                     {"messageText":"KF94","action": "message","label": "KF-94" },
                     {"messageText":"KF80","action": "message","label": "KF-80" },
                     {"messageText":"KFAD","action": "message","label": "KF-AD" },
                     {"messageText":"초기화","action": "message","label": "초기화" }
                 ]
                }
}

###############################  다회용 + 민감X + 김서림방지X
mask1_1_1 = [mask_data["다회용"]["민감x"]["김서림x"]["KF99"],
             mask_data["다회용"]["민감x"]["김서림x"]["KF94"],
             mask_data["다회용"]["민감x"]["김서림x"]["KF80"],
             mask_data["다회용"]["민감x"]["김서림x"]["KFAD"]
            ]
###############################  다회용 + 민감X + 김서림방지
mask1_1_0 = [mask_data["다회용"]["민감x"]["김서림방지"]["KF99"],
             mask_data["다회용"]["민감x"]["김서림방지"]["KF94"],
             mask_data["다회용"]["민감x"]["김서림방지"]["KF80"],
             mask_data["다회용"]["민감x"]["김서림방지"]["KFAD"]
            ]
###############################  다회용 + 민감 + 김서림방지X
mask1_0_1 = [mask_data["다회용"]["민감"]["김서림x"]["KF99"],
             mask_data["다회용"]["민감"]["김서림x"]["KF94"],
             mask_data["다회용"]["민감"]["김서림x"]["KF80"],
             mask_data["다회용"]["민감"]["김서림x"]["KFAD"]
            ]
###############################  다회용 + 민감 + 김서림방지
mask1_0_0 = [mask_data["다회용"]["민감"]["김서림방지"]["KF99"],
             mask_data["다회용"]["민감"]["김서림방지"]["KF94"],
             mask_data["다회용"]["민감"]["김서림방지"]["KF80"],
             mask_data["다회용"]["민감"]["김서림방지"]["KFAD"]
            ]
###############################  일회용 + 민감X + 김서림방지X
mask0_1_1 = [mask_data["일회용"]["민감x"]["김서림x"]["KF99"],
             mask_data["일회용"]["민감x"]["김서림x"]["KF94"],
             mask_data["일회용"]["민감x"]["김서림x"]["KF80"],
             mask_data["일회용"]["민감x"]["김서림x"]["KFAD"]
            ]
###############################  일회용 + 민감X + 김서림방지
mask0_1_0 = [mask_data["일회용"]["민감x"]["김서림방지"]["KF99"],
             mask_data["일회용"]["민감x"]["김서림방지"]["KF94"],
             mask_data["일회용"]["민감x"]["김서림방지"]["KF80"],
             mask_data["일회용"]["민감x"]["김서림방지"]["KFAD"]
            ]
###############################  일회용 + 민감 + 김서림방지X
mask0_0_1 = [mask_data["일회용"]["민감"]["김서림x"]["KF99"],
             mask_data["일회용"]["민감"]["김서림x"]["KF94"],
             mask_data["일회용"]["민감"]["김서림x"]["KF80"],
             mask_data["일회용"]["민감"]["김서림x"]["KFAD"]
            ]
###############################  일회용 + 민감 + 김서림방지
mask0_0_0 = [mask_data["일회용"]["민감"]["김서림방지"]["KF99"],
             mask_data["일회용"]["민감"]["김서림방지"]["KF94"],
             mask_data["일회용"]["민감"]["김서림방지"]["KF80"],
             mask_data["일회용"]["민감"]["김서림방지"]["KFAD"]
            ]

@app.route('/api/mask', methods=['POST'])
def mask():
    body = request.get_json()
    select = body['userRequest']
    select = select['utterance']
    
    global maskQues1
    global maskQues2
    global maskQues3
    global maskQues4
    global maskAns
    global maskSelect
    
    if select == "일회용":
        response_data=maskQues2
        maskSelect[0] = 0
    elif select == "다회용":
        response_data=maskQues2
        maskSelect[0] = 1
    elif select == "민감함":
        response_data=maskQues3
        maskSelect[1] = 0
    elif select == "민감하지않음":
        response_data=maskQues3
        maskSelect[1] = 1
    elif select == "김서림방지":
        response_data=maskQues4
        maskSelect[2] = 0
    elif select == "김서림방지필요없음":
        response_data=maskQues4
        maskSelect[2] = 1
    elif select == "KF99":
        maskSelect[3] = 0
        maskSelect[4] = 1
    elif select == "KF94":
        maskSelect[3] = 1
        maskSelect[4] = 1
    elif select == "KF80":
        maskSelect[3] = 2
        maskSelect[4] = 1
    elif select == "KFAD":
        maskSelect[3] = 3
        maskSelect[4] = 1
    elif select == "초기화":
        maskSelect = [0, 0, 0, 0, 0]
        response_data = maskQues1
    
    else:
        maskSelect = [0, 0, 0, 0, 0]
        response_data = maskQues1
    
    if maskSelect[4] == 1:
        if maskSelect[0] == 1:
            if maskSelect[1] == 1:
                if maskSelect[2] == 1:
                    response_data = mask1_1_1[maskSelect[3]]
                else:
                    response_data = mask1_1_0[maskSelect[3]]
            else:
                if maskSelect[2] == 1:
                    response_data = mask1_0_1[maskSelect[3]]
                else:
                    response_data = mask1_0_0[maskSelect[3]]
        else:
            if maskSelect[1] == 1:
                if maskSelect[2] == 1:
                    response_data = mask0_1_1[maskSelect[3]]
                else:
                    response_data = mask0_1_0[maskSelect[3]]
            else:
                if maskSelect[2] == 1:
                    response_data = mask0_0_1[maskSelect[3]]
                else:
                    response_data = mask0_0_0[maskSelect[3]]
    if response_data == "No_data":
        response_data = no_mask

    return jsonify(response_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)