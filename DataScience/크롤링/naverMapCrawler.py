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
options = webdriver.ChromeOptions()
options.add_argument('headless')

url = 'https://map.naver.com/v5/search'
driver = webdriver.Chrome('./chromedriver')  # 드라이버 경로
# driver = webdriver.Chrome('./chromedriver',chrome_options=options) # 크롬창 숨기기
driver.get(url)
# opt0 기본
# searchName = "상호명"
# *nameCnt = "호점"/ 옵션으로
# adress = "도로명주소"
# # opt1 그냥 밥집
# searchName = "국수찾아닭만리"
# adress = " 서울특별시 종로구 낙원동"
# # opt2 프랜차이즈 밥집
# searchName = "바른치킨"
# adress = "서울특별시 강남구 선릉로86길 17"
# opt3 감성밥집
searchName = "비지트"
adress = "서울 서초구 동광로18길 82"
key_word = searchName + " " + adress  # 검색어

# xpath 찾을때 까지 10초대기
def time_wait(num, code):
    try:
        wait = WebDriverWait(driver, num).until(
            EC.presence_of_element_located((By.XPATH, code)))
        print(wait.text)
        return True
    except:
        print(code, '태그를 찾지 못하였습니다.')
        return False

# css를 찾을때 까지 10초 대기
time_wait(10, '/html/body/app/layout/div[3]/div[2]/shrinkable-layout/div/app-base/search-input-box/div/div/div/input')

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
# 페이지 다운
def page_down(num):
    body = driver.find_element_by_css_selector('body')
    body.click()
    for i in range(num):
        body.send_keys(Keys.PAGE_DOWN)
# frame 변경
# # switch_frame('searchIframe')
# iframes = driver.find_elements_by_css_selector('nm-external-frame-bridge > nm-iframe > iframe') # 창에 있는 모든 iframe 출력
# print(len(iframes))
# for iframe in iframes:
#     print(iframe.get_attribute('id'))
driver.switch_to.default_content()
# driver.switch_to.frame("searchIframe")
iframes = driver.find_elements_by_css_selector('iframe') # 창에 있는 모든 iframe 출력
print(len(iframes))
for iframe in iframes:
    print(iframe.get_attribute('id'))

try:
    time_wait(10,'/html/body/app/layout/div[3]/div[2]/shrinkable-layout/div/app-base/search-layout/div[2]/entry-layout/entry-place-bridge/div/nm-external-frame-bridge/nm-iframe/iframe')
    # iframes = driver.find_elements_by_css_selector('iframe')  # 창에 있는 모든 iframe 출력
    switch_frame("entryIframe")
    print("entryIframe find")
except:
    print("entryIframe 못찾음")
# page_down(40)

sleep(3)

store_dict = {'매장정보': []}
# 시작시간
start = time.time()
print("크롤링 시도")
try:
    # storeName = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[2]/div[1]/div[1]/span[1]")
    storeName = driver.find_element_by_css_selector("#_title > span.Fc1rA")
    print("데이터 확인. 크롤링 시작 :",storeName.text)
    print("평점")
    try:
        store_rating = driver.find_element_by_xpath(
            '/html/body/div[3]/div/div/div/div[2]/div[1]/div[2]/span[1]/em').text
    except:
        pass
    print("별점 :", store_rating)

    # -----전화번호 가져오기-----
    print("전화번호")
    try:
        store_tel = driver.find_element_by_xpath(
            '/html/body/div[3]/div/div/div/div[6]/div/div[2]/div/ul/li[3]/div/span[1]').text
        # store_tel = driver.find_element_by_css_selector("#app-root > div > div > div > div:nth-child(6) > div > div.place_section.no_margin.vKA6F > div > ul > li.SF_Mq.SjF5j > div > span.dry01").text
    except:
        print("error here")

    print("전화번호", store_tel)

    # -----영업시간-----
    # try:
    #     store_time_list = driver.find_elements_by_css_selector('._2vK84')  # 아니 태그가 그세 바뀌네ㅡ,.ㅡ
    #     for i in store_time_list:
    #         store_time = i.find_element_by_css_selector('._3uEtO > time').text
    # except:
    #     pass
    # print(store_time)


    # 메뉴 탭 이동시 다른 탭들의 xpath 변경됨 주의할것.
    # -----메뉴-----/ 대표 메뉴만 추출
    # print("메뉴")
    # try:
    #     tabBtns = driver.find_elements_by_xpath("/html/body/div[3]/div/div/div/div[5]/div/div/div/div/a")
    #     for tab in tabBtns:
    #         if tab.text == "메뉴":
    #             sleep(1)
    #             tab.click()
    #             print("메뉴 찾음")
    #             page_down(40)
    #         #     menu_list = driver.find_element_by_xpath('/html/body/').find_element_by_tag_name("li")
    #         #     print(menu_list.text)
    #         #     # menu_name = []  # 메뉴이름
    #         #     # menu_price = []  # 메뉴가격
    #         #     #
    #         #     # for i in menu_list:
    #         #     #     # name = i.find_elements_by_xpath('._1q3GD').text
    #         #     #     name = i.find_element_by_css_selector("div > div").text
    #         #     #     menu_name.append(name)
    #         #     #
    #         #     #     price = i.find_element_by_css_selector('div > em').text  # 텍스트를 넣을 변수 생성
    #         #     #     price = re.sub('원\d{2},\d{3}', '', price)  # 할인 전 가격 제거  # 재정의
    #         #     #     menu_price.append(price)  # 추가
    #             break
    # except:
    #     pass

    # 리뷰
    # print("리뷰")
    # try:
    #     time_wait(10,
    #           '/html/body/app/layout/div[3]/div[2]/shrinkable-layout/div/app-base/search-layout/div[2]/entry-layout/entry-place-bridge/div/nm-external-frame-bridge/nm-iframe/iframe')
    #     switch_frame("entryIframe")
    # except:
    #     print("line 160")

    try:
        tabBtns = driver.find_elements_by_xpath("/html/body/div[3]/div/div/div/div[5]/div/div/div/div/a")
        for tab in tabBtns:
            if tab.text == "리뷰":
                tab.click()
                sleep(2)
                print("리뷰 찾음")
                break
        reviewList = []
        # searchedReviewList = driver.find_elements_by_xpath("/html/body/div[3]/div/div/div/div[7]/div[2]/div[3]/div[1]/ul/li")
        try:
            time_wait(10,"/html/body/div[3]/div/div/div/div[7]/div[2]/div[3]/div[1]/ul")
            searchedReviewList = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[7]/div[2]/div[3]/div[1]/ul")
            reviewList = searchedReviewList.find_element_by_tag_name("li")
            print("review len",len(searchedReviewList))
            print("reviewlist len",len(reviewList))
        except:
            print("review 찾기 실패")
        idx = 0
        for review in searchedReviewList:
            reviewList.append(review.text)
            print(idx, review.text)
            idx += 1

        for clickIdx in range(5):
            page_down(40)
            if time_wait(10,"/html/body/div[3]/div/div/div/div[7]/div[2]/div[3]/div[2]/a"):
                print("리뷰 더보기 클릭")
                driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[7]/div[2]/div[3]/div[2]").click()
            else:
                print("더보기없음 리뷰 수집시작")
                continue

    except:
        pass


    # # ---- dict에 데이터 집어넣기----
    # dict_temp = {
    #     # 'name': store_name,
    #     # 'tel': store_tel,
    #     # 'star': store_rating,
    #     # # 'addr': store_addr,
    #     # # 'time': store_time,
    #     # 'menu': menus,
    #     # 'price': prices,
    #     # 'kwd': kwd_title,
    #     # 'kwd_count': kwd_count,
    #     # 'thumb': store_thumb
    # }
    #
    # store_dict['매장정보'].append(dict_temp)
    #
    # print(f'{store_name} ...완료')
    sleep(1)
except:
    print("ERROR ERROR")
# dictionary 생성

# print("next_btn 길이",len(next_btn))
# 크롤링 (검색 매장 갯수 만큼 )
# 검색된 매장 중 상호명이 일치하는 곳의 리뷰, 메뉴, 키워드 수집


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