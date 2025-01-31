import requests
import json
import asyncio

async def get_school_code(school_name:str,area_code:str):
    if False:
        pass
    else:
        url = f'https://open.neis.go.kr/hub/schoolInfo?KEY=f20a483f903d4dabb871d08683910077&Type=json&pIndex=1&pSize=100&SCHUL_NM={school_name}&ATPT_OFCDC_SC_CODE={area_code}'
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
        response = requests.get(url,headers=headers)
        school_data=json.loads(response.text)

        #검색해서 나온 학교가 하나 밖에 없으면 그 학교의 코드를 반환
        if 'schoolInfo' in school_data.keys():
            try:
                #학교코드
                school_code = school_data['schoolInfo'][1]["row"][0]['SD_SCHUL_CODE']
                return school_code
                pass
            except:
                return None
                pass
        else:
            return None
            pass
'''
async def get_school_ATPT_OFCDC_SC_CODE(school_name:str=None):
    if school_name==None:
        return None
        pass
    else:
        try:
            url = f'https://open.neis.go.kr/hub/schoolInfo?KEY=f20a483f903d4dabb871d08683910077&Type=json&pIndex=1&pSize=100&SCHUL_NM={school_name}'
            response = requests.get(url)
            school_data=json.loads(response.text)

            #검색해서 나온 학교가 하나 밖에 없으면 그 학교의 코드를 반환
            if len(school_data['schoolInfo'][1]["row"])==1:
                #시도교육청코드
                school_ATPT_OFCDC_SC_CODE = school_data['schoolInfo'][1]["row"][0]['ATPT_OFCDC_SC_CODE']
                return school_ATPT_OFCDC_SC_CODE
            else:

                school_codes = {}
                for i in school_data['schoolInfo'][1]["row"]:
                    school_codes[i['SCHUL_NM']]=(i['SD_SCHUL_CODE'])
                return school_codes

                return None
                pass
        except:
            return None
            pass
'''
async def get_area_code(school_area:str):

    Souel = ['서울', '서울시', '서울교육청', '서울시교육청', '서울특별시']
    Busan = ['부산', '부산광역시', '부산시', '부산교육청', '부산광역시교육청']
    Deagu = ['대구', '대구광역시', '대구시', '대구교육청', '대구광역시교육청']
    Incheon = ['인천', '인천광역시', '인천시', '인천교육청', '인천광역시교육청']
    Gwangju = ['광주', '광주광역시', '광주시', '광주교육청', '광주광역시교육청']
    Daejeon = ['대전', '대전광역시', '대전시', '대전교육청', '대전광역시교육청']
    Ulsan = ['울산', '울산광역시', '울산시', '울산교육청', '울산광역시교육청']
    Sejong = ['세종', '세종특별시', '세종시', '세종교육청', '세종특별자치시', '세종특별자치시교육청']
    Gyeonggi = ['경기', '경기도', '경기교육청', '경기도교육청']
    Gangwon = ['강원', '강원도', '강원교육청', '강원도교육청']
    Chungcheongbuk = ['충북', '충청북도', '충북교육청', '충청북도교육청']
    Chungcheongnam = ['충남', '충청남도', '충남교육청', '충청남도교육청']
    Jeollabuk = ['전북', '전라북도', '전북교육청', '전라북도교육청']
    Jeollanam = ['전남', '전라남도', '전남교육청', '전라남도교육청']
    Gyeongsangbuk = ['경북', '경상북도', '경북교육청', '경상북도교육청']
    Gyeongsangnam = ['경남', '경상남도', '경남교육청', '경상남도교육청']
    Jeju = ['제주', '제주도', '제주특별자치시', '제주교육청', '제주도교육청', '제주특별자치시교육청', '제주특별자치도']

    school_code = ""

    if school_area in Souel:
        school_code = "B10"
    elif school_area in Busan:
        school_code = "C10"
    elif school_area in Deagu:
        school_code = "D10"
    elif school_area in Incheon:
        school_code = "E10"
    elif school_area in Gwangju:
        school_code = "F10"
    elif school_area in Daejeon:
        school_code = "G10"
    elif school_area in Ulsan:
        school_code = "H10"
    elif school_area in Sejong:
        school_code = "I10"
    elif school_area in Gyeonggi:
        school_code = "J10"
    elif school_area in Gangwon:
        school_code = "K10"
    elif school_area in Chungcheongbuk:
        school_code = "M10"
    elif school_area in Chungcheongnam:
        school_code = "N10"
    elif school_area in Jeollabuk:
        school_code = "P10"
    elif school_area in Jeollanam:
        school_code = "Q10"
    elif school_area in Gyeongsangbuk:
        school_code = "R10"
    elif school_area in Gyeongsangnam:
        school_code = "S10"
    elif school_area in Jeju:
        school_code = "T10"
    else:
        school_code = "V10"

    return school_code

async def get_school_cafeteria(school_code, area_code,day):
    try:
        url = f'https://open.neis.go.kr/hub/mealServiceDietInfo?KEY=f20a483f903d4dabb871d08683910077&Type=json&ATPT_OFCDC_SC_CODE={area_code}&SD_SCHUL_CODE={school_code}&MLSV_YMD={day}'
        print(url)
        response = requests.get(url)
        school_data=json.loads(response.text)

        school_cafeteria = []
        temp_item = ""

        for i in school_data["mealServiceDietInfo"][1]["row"][0]["DDISH_NM"].split("<br/>"):
            for j in list(i):
                if j == " " or j.isdigit() or j == ".":
                    pass
                else:
                    temp_item += j
            if temp_item != "":
                if temp_item[0] == "-":
                    temp_item = temp_item[1:]
                if temp_item[-1] == "*":
                    temp_item = temp_item[:-1]
                school_cafeteria.append(temp_item)
                temp_item = ""

        return school_cafeteria
    except:
        return None

async def get_school_timetable(school_code, area_code,day,school_type,school_grade, school_class):
    school_type_high = ['고등학교', '고','고등']
    school_type_middle = ['중학교', '중','중등']
    school_type_elementary = ['초등학교', '초','초등']
    school_type_special = ['특수학교', '특','특수','특별']
    try:
        if school_type in school_type_high:
            url = f"https://open.neis.go.kr/hub/hisTimetable?KEY=f20a483f903d4dabb871d08683910077&Type=json&ATPT_OFCDC_SC_CODE={area_code}&SD_SCHUL_CODE={school_code}&GRADE={school_grade}&CLASS_NM={school_class}&TI_FROM_YMD={day}&TI_TO_YMD={day}"
            temp = "hisTimetable"
        elif school_type in school_type_middle:
            url = f"https://open.neis.go.kr/hub/misTimetable?KEY=f20a483f903d4dabb871d08683910077&Type=json&ATPT_OFCDC_SC_CODE={area_code}&SD_SCHUL_CODE={school_code}&GRADE={school_grade}&CLASS_NM={school_class}&TI_FROM_YMD={day}&TI_TO_YMD={day}"
            temp = "misTimetable"
        elif school_type in school_type_elementary:
            url = f"https://open.neis.go.kr/hub/elsTimetable?KEY=f20a483f903d4dabb871d08683910077&Type=json&ATPT_OFCDC_SC_CODE={area_code}&SD_SCHUL_CODE={school_code}&GRADE={school_grade}&CLASS_NM={school_class}&TI_FROM_YMD={day}&TI_TO_YMD={day}"
            temp = "elsTimetable"
        elif school_type in school_type_special:
            url = f"https://open.neis.go.kr/hub/spsTimetable?KEY=f20a483f903d4dabb871d08683910077&Type=json&ATPT_OFCDC_SC_CODE={area_code}&SD_SCHUL_CODE={school_code}&GRADE={school_grade}&CLASS_NM={school_class}&TI_FROM_YMD={day}&TI_TO_YMD={day}"
            temp = "spsTimetable"
        print(url)
        response = requests.get(url)
        timetable_data=json.loads(response.text)

        timetable_list = [0 for i in range(len(timetable_data[temp][1]['row']))]

        for i in timetable_data[temp][1]['row']:
            #시간표 맨 앞에 - 제거
            if i['ITRT_CNTNT'][0] == "-":
                timetable_list[int(i['PERIO'])-1] = str(i['ITRT_CNTNT'])[1:]
            else:
                timetable_list[int(i['PERIO'])-1] = i['ITRT_CNTNT']

        return timetable_list
    except:
        return None

async def get_school_schedule(school_code,area_code,day):
    url = f"https://open.neis.go.kr/hub/SchoolSchedule?KEY=f20a483f903d4dabb871d08683910077&Type=json&SD_SCHUL_CODE={school_code}&ATPT_OFCDC_SC_CODE={area_code}&AA_YMD={day[:-2]}"
    print(url)
    response = requests.get(url)
    schedule_data=json.loads(response.text)

    if "RESULT" not in schedule_data.keys():
        schedule_dict = {}

        for i in schedule_data["SchoolSchedule"][1]["row"]:
            schedule_dict[i["AA_YMD"]] = i['EVENT_NM']
        
        if day in schedule_dict.keys():
            return schedule_dict[day]
        else:
            return None
    else:
        return None
