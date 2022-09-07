import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from bs4 import BeautifulSoup
import re
import json

# --크롬창을 숨기고 실행-- driver에 options를 추가해주면된다
# options = webdriver.ChromeOptions()
# options.add_argument('headless')

url = 'https://map.naver.com/v5/search'
driver = webdriver.Chrome('./chromedriver')  # 드라이버 경로
# driver = webdriver.Chrome('./chromedriver',chrome_options=options) # 크롬창 숨기기
driver.get(url)
# opt1
# searchName = "비지트"
# adress = "서울특별시 서초구 방배동"
# opt2
searchName = "바른치킨"
adress = "서울특별시 강남구 대치동"
key_word = searchName + " " + adress  # 검색어


# xpath 찾을때 까지 10초대기
def time_wait(num, code):
    try:
        wait = WebDriverWait(driver, num).until(
            EC.presence_of_element_located((By.XPATH, code)))
    except:
        print(code, '태그를 찾지 못하였습니다.')
        driver.quit()
    return wait


# css를 찾을때 까지 10초 대기
time_wait(5, '/html/body/app/layout/div[3]/div[2]/shrinkable-layout/div/app-base/search-input-box/div/div/div/input')

# 검색창 찾기
search = driver.find_element_by_css_selector('div.input_box > input.input_search')
search.send_keys(key_word)  # 검색어 입력
search.send_keys(Keys.ENTER)  # 엔터버튼 누르기

res = driver.page_source  # 페이지 소스 가져오기
soup = BeautifulSoup(res, 'html.parser')  # html 파싱하여  가져온다

sleep(1)


# frame 변경 메소드
def switch_frame(frame):
    driver.switch_to.default_content()  # frame 초기화
    driver.switch_to.frame(frame)  # frame 변경
    res
    soup


# 페이지 다운
def page_down(num):
    body = driver.find_element_by_css_selector('body')
    body.click()
    for i in range(num):
        body.send_keys(Keys.PAGE_DOWN)


# frame 변경
switch_frame('searchIframe')
page_down(40)
sleep(3)

# 매장 리스트
store_list = driver.find_elements_by_xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]')

# 페이지 리스트
# next_btn = driver.find_elements_by_css_selector('#app-root > div > div.XUrfU > div.zRM9F > a')

# dictionary 생성
store_dict = {'매장정보': []}
# 시작시간
start = time.time()
print('[크롤링 시작...]')
# print("next_btn 길이",len(next_btn))
# 크롤링 (검색 매장 갯수 만큼 )
# 검색된 매장 중 상호명이 일치하는 곳의 리뷰, 메뉴, 키워드 수집

# 검색 결과 리스트의 매장 상세 정보 띄우는 자스 버튼 추합/html/body/div[3]/div/div/div[1]/ul/li[1]/div[1]/a
stores = driver.find_elements_by_xpath('/html/body/div[3]/div/div/div[1]/ul/li')
print("storeList 길이",len(store_list), len(stores))
for data in range(len(stores)):  # 매장 리스트 만큼

    # data 번째 매장 상세 정보 버튼 클릭
    stores[data].find_element_by_css_selector().click()
    sleep(2)
    try:
        # 상세 페이지로 이동
        print("상세 페이지 띄우기")
        switch_frame('entryIframe')
        # 상세페이지 뜬지 확인, time_wait로 매장 이름 태크 찾기
        time_wait(3, '/html/body/div[3]/div/div/div/div[2]/div[1]/div[1]/span[1]')
        # 스크롤을 맨밑으로 1초간격으로 내린다.
        for down in range(3):
            sleep(1)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # -----매장명 가져오기-----
        # store_name = driver.find_element_by_css_selector('#_title > span.Fc1rA').text
        store_name = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[2]/div[1]/div[1]/span[1]").text
        print("매장이름")
        if store_name == searchName:
            print(store_name, "검색키워드와 일치. 수집 시작")
        else:
            print(store_name, "검색 키워드와 불일치.")
            continue
        # -----평점-----
        print("평점")
        try:
            store_rating = driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[2]/div[1]/div[2]/span[1]/em').text
        except:
            pass
        print("별점 :",store_rating)

        # # -----주소(위치)-----
        # print("주소")
        # store_addr = None
        # try:
        #     # store_addr = driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[6]/div/div[2]/div/ul/li[1]/div/a/span[1]').text
        #     store_addr = driver.find_element_by_css_selector("#app-root > div > div > div > div:nth-child(6) > div > div.place_section.no_margin.vKA6F > div > ul > li.SF_Mq.GFtzE > div > a > span.IH7VW").text
        # except:
        #     print("error here")
        #     pass
        # print("주소위치",store_addr)

        # -----전화번호 가져오기-----
        print("전화번호")
        try:
            store_tel = driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[7]/div/div[2]/div/ul/li[3]/div/span').text
            # store_tel = driver.find_element_by_css_selector("#app-root > div > div > div > div:nth-child(6) > div > div.place_section.no_margin.vKA6F > div > ul > li.SF_Mq.SjF5j > div > span.dry01").text
        except:
            print("error here")

        print("전화번호",store_tel)

        # -----영업시간-----
        # try:
        #     store_time_list = driver.find_elements_by_css_selector('._2vK84')  # 아니 태그가 그세 바뀌네ㅡ,.ㅡ
        #     for i in store_time_list:
        #         store_time = i.find_element_by_css_selector('._3uEtO > time').text
        # except:
        #     pass
        # print(store_time)

        # -----메뉴-----/ 대표 메뉴만 추출
        print("메뉴")
        try:
            menu_list = driver.find_elements_by_xpath('/html/body/div[3]/div/div/div/div[7]/div/div[3]/div[1]/ul/li')
            menu_name = []  # 메뉴이름
            menu_price = []  # 메뉴가격

            for i in menu_list:
                # name = i.find_elements_by_xpath('._1q3GD').text
                name = i.find_element_by_css_selector("div > div").text
                menu_name.append(name)

                price = i.find_element_by_css_selector('div > em').text  # 텍스트를 넣을 변수 생성
                price = re.sub('원\d{2},\d{3}', '', price)  # 할인 전 가격 제거  # 재정의
                menu_price.append(price)  # 추가

        except:
            pass
        print(menu_name)
        print(menu_price)
        # -----키워드 리뷰 가져오기-----
        try:
            keyword_list = driver.find_element_by_css_selector('._28hFN')  # 키워드가 담긴 리스트 클릭
            keyword_list.click()

        except:  # 키워드리뷰 없으면 다음 음식점으로
            print('키워드리뷰 없음 >>> 다음으로',)
            switch_frame('searchIframe')
            continue

        try:
            keyword_review_list = driver.find_elements_by_css_selector('._3FaRE')  # 리뷰 리스트
            kwd_title = []
            kwd_count = []
            sleep(2)

            for i in keyword_review_list:
                keyword_title = i.find_element_by_css_selector('._1lntw').text  # 키워드리뷰
                keyword_count = i.find_element_by_css_selector('.Nqp-s').text   # 리뷰를 선택한 수

                # db에 넣을 때 편의를 위해 요청하였음
                title_re = re.sub('"', '', keyword_title) \
                    .replace('양이 많아요', '1').replace('음식이 맛있어요', '2').replace('재료가 신선해요', '3') \
                    .replace('가성비가 좋아요', '4').replace('특별한 메뉴가 있어요', '5').replace('화장실이 깨끗해요', '6') \
                    .replace('주차하기 편해요', '7').replace('친절해요', '8').replace('특별한 날 가기 좋아요', '9').replace(
                    '매장이 청결해요',
                    '10') \
                    .replace('인테리어가 멋져요', '11').replace('단체모임 하기 좋아요', '12').replace('뷰가 좋아요', '13').replace(
                    '매장이 넓어요',
                    '14') \
                    .replace('혼밥하기 좋아요', '15')

                title_num = list(map(str, range(1, 16)))  # 1~15만 리스트에추가 (이외에 다른 키워드들은 추가하지않음)
                count_keyword = re.sub('이 키워드를 선택한 인원\n', '', keyword_count)
                if title_re in title_num:
                    kwd_title.append(title_re)
                    kwd_count.append(count_keyword)
                else:
                    pass
        except:
            pass
        kwd_count = list(map(int, kwd_count))  # int 형변환

        print(kwd_title)
        print(kwd_count)

        # -----썸네일 사진 주소-----
        try:
            thumb_list = driver.find_element_by_css_selector('.cb7hz') \
                .value_of_css_property('background-image')  # css 속성명을 찾는다
            store_thumb = re.sub('url|"|\)|\(', '', thumb_list)  # url , (" ") 제거
        except:
            pass
        print(store_thumb)

        # ---- dict에 데이터 집어넣기----
        dict_temp = {
            'name': store_name,
            'tel': store_tel,
            'star': store_rating,
            # 'addr': store_addr,
            # 'time': store_time,
            'menu': menus,
            'price': prices,
            'kwd': kwd_title,
            'kwd_count': kwd_count,
            'thumb': store_thumb
        }

        store_dict['매장정보'].append(dict_temp)

        print(f'{store_name} ...완료')
        switch_frame('searchIframe')
        sleep(1)

    except:
        print('ERROR!' * 3)

# 다음 페이지 버튼
# if stores[-1]:  # 마지막 매장일 경우 다음버튼 클릭
#     next_btn[-1].click()
#     sleep(2)
# else:
#     print('페이지 인식 못함')
#     break

print('[데이터 수집 완료]\n소요 시간 :', time.time() - start)
# driver.quit()  # 작업이 끝나면 창을닫는다.
print(store_dict)
# # json 파일로 저장
# with open('data/store_data.json', 'w', encoding='utf-8') as f:
#     json.dump(store_dict, f, indent=4, ensure_ascii=False)