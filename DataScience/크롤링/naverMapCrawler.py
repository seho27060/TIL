import time
from pprint import pprint

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from bs4 import BeautifulSoup

import blogCrawler

# opt0 기본
# searchName = "상호명"
# *nameCnt = "호점"/ 옵션으로
# adress = "도로명주소"
# opt1 그냥 밥집
# searchName = "국수찾아닭만리"
# adress = " 서울특별시 종로구 낙원동"
# # opt2 프랜차이즈 밥집
# searchName = "바른치킨"
# adress = "서울특별시 강남구 선릉로86길 17"
# # opt3 감성밥집
# searchName = "비지트"
# adress = "서울 서초구 동광로18길 82"
#
# searchKeyword = searchName + " " + adress  # 검색어


def crawler(searchWord):
    # --크롬창을 숨기고 실행-- driver에 options를 추가해주면된다
    options = webdriver.ChromeOptions()
    options.add_argument('headless')

    url = 'https://map.naver.com/v5/search'
    driver = webdriver.Chrome('./chromedriver')  # 드라이버 경로
    driver = webdriver.Chrome('./chromedriver',chrome_options=options) # 크롬창 숨기기
    driver.get(url)

    # xpath 찾을때 까지 10초대기
    def time_wait(num, code):
        try:
            wait = WebDriverWait(driver, num).until(
                EC.presence_of_element_located((By.XPATH, code)))
            print(code, "찾음")
            return True
        except:
            print(code, '태그를 찾지 못하였습니다.')
            return False

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

    result = {}
    # css를 찾을때 까지 10초 대기
    time_wait(10,
              '/html/body/app/layout/div[3]/div[2]/shrinkable-layout/div/app-base/search-input-box/div/div/div/input')

    # 검색창 찾기
    search = driver.find_element_by_css_selector('div.input_box > input.input_search')
    search.send_keys(searchWord)  # 검색어 입력
    search.send_keys(Keys.ENTER)  # 엔터버튼 누르기

    res = driver.page_source  # 페이지 소스 가져오기
    soup = BeautifulSoup(res, 'html.parser')  # html 파싱하여  가져온다

    sleep(1)

    # frame 변경
    # # switch_frame('searchIframe')
    # iframes = driver.find_elements_by_css_selector('nm-external-frame-bridge > nm-iframe > iframe') # 창에 있는 모든 iframe 출력
    # print(len(iframes))
    # for iframe in iframes:
    #     print(iframe.get_attribute('id'))
    driver.switch_to.default_content()
    # driver.switch_to.frame("searchIframe")
    iframes = driver.find_elements_by_css_selector('iframe')  # 창에 있는 모든 iframe 출력
    print(len(iframes))
    for iframe in iframes:
        print(iframe.get_attribute('id'))

    try:
        time_wait(10,
                  '/html/body/app/layout/div[3]/div[2]/shrinkable-layout/div/app-base/search-layout/div[2]/entry-layout/entry-place-bridge/div/nm-external-frame-bridge/nm-iframe/iframe')
        # iframes = driver.find_elements_by_css_selector('iframe')  # 창에 있는 모든 iframe 출력
        switch_frame("entryIframe")
        print("entryIframe find")
    except:
        print("entryIframe 못찾음")
    # page_down(40)

    sleep(2)

    # 시작시간
    start = time.time()
    print("크롤링 시도")

    storeRating = ""
    storeTell = ""
    reviewList = []
    blogUrlList = []
    blogReviewList = []
    try:
        # storeName = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[2]/div[1]/div[1]/span[1]")
        storeName = driver.find_element_by_css_selector("#_title > span.Fc1rA")
        print("데이터 확인. 크롤링 시작 :", storeName.text)
        print("별점")
        if time_wait(3, '/html/body/div[3]/div/div/div/div[2]/div[1]/div[2]/span[1]/em'):
            storeRating = driver.find_element_by_xpath(
                '/html/body/div[3]/div/div/div/div[2]/div[1]/div[2]/span[1]/em').text
        else:
            print("평점 없음")
        print("점수 :", storeRating)

        # -----전화번호 가져오기-----
        print("전화번호")
        if time_wait(3, '/html/body/div[3]/div/div/div/div[6]/div/div[2]/div/ul/li[3]/div/span[1]'):
            storeTell = driver.find_element_by_xpath(
                '/html/body/div[3]/div/div/div/div[6]/div/div[2]/div/ul/li[3]/div/span[1]').text
            # store_tel = driver.find_element_by_css_selector("#app-root > div > div > div > div:nth-child(6) > div > div.place_section.no_margin.vKA6F > div > ul > li.SF_Mq.SjF5j > div > span.dry01").text
        else:
            print("전화번호 없음")
        print("전화번호", storeTell)

        # 방문자 리뷰
        try:
            tabBtns = driver.find_elements_by_xpath("/html/body/div[3]/div/div/div/div[5]/div/div/div/div/a")
            for tab in tabBtns:
                if tab.text == "리뷰":
                    tab.click()
                    print("리뷰 탭 클릭")
                    break

            for clickIdx in range(5):
                # page_down(40)
                if time_wait(3, "/html/body/div[3]/div/div/div/div[7]/div[2]/div[3]/div[2]/a"):
                    print("리뷰 리스트 더보기 클릭")
                    sleep(1)
                    driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[7]/div[2]/div[3]/div[2]/a").click()
                else:
                    print("더보기없음 리뷰 수집시작")
                    break
            reviews = driver.find_elements_by_xpath("/html/body/div[3]/div/div/div/div[7]/div[2]/div[3]/div[1]/ul/li")
            print("리뷰 개수 :", len(reviews))
            for idx in range(len((reviews))):
                # 리뷰 찾고, 리뷰 더보기 클릭 후 리뷰 수집
                try:
                    reviews[idx].find_element_by_class_name("rvCSr").click()
                except:
                    # print("상세 더보기 없음")
                    pass
                review = reviews[idx].find_element_by_class_name("ZZ4OK").text.replace("\n", " ")
                # print(review)
                reviewList.append(review)
        except:
            pass

        # 블로그 리뷰
        try:
            reviewTabBtn = driver.find_elements_by_class_name("YGvdM")
            for reviewTab in reviewTabBtn:
                if reviewTab.text == "블로그리뷰":
                    print(reviewTab.text, "찾았다")
                    reviewTab.send_keys(Keys.ENTER)
                    break
            print("블로그 리뷰 탭 전환")
            for clickIdx in range(5):
                # page_down(40)
                if time_wait(3, "/html/body/div[3]/div/div/div/div[7]/div[2]/div[2]/div[2]/a"):
                    print("블로그 리스트 더보기 클릭")
                    sleep(1)
                    driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[7]/div[2]/div[2]/div[2]/a").click()
                else:
                    print("더보기없음 블로그 url 수집시작")
                    break
            blogUrls = driver.find_elements_by_xpath("/html/body/div[3]/div/div/div/div[7]/div[2]/div[2]/div[1]/ul/li")
            print("블로그 url 개수: ",len(blogUrls))
            for blogUrlIdx in range(len(blogUrls)):
                aTag = blogUrls[blogUrlIdx].find_element_by_tag_name("a")
                getUrl = aTag.get_attribute("href")
                blogReview = blogCrawler.blogCrawler(getUrl)
                blogUrlList.append(getUrl)
                blogReviewList.append(blogReview)
        except:
            print("블로그 리뷰 에러")

        # ---- dict에 데이터 집어넣기----
        result = {
            "rating": storeRating,
            "tell": storeTell,
            "reviews": reviewList,
            "blogUrls" : blogUrlList,
            "blogReviews" : blogReviewList,
        }
        print(f'{searchWord} ...완료')
        print(f"리뷰 개수 : {len(result['reviews'])} 블로그 url 개수 : {len(result['blogUrls'])} 블로그 리뷰 개수 : {len(result['blogReviews'])}")
        sleep(1)
    except:
        print("ERROR ERROR")
    print('[데이터 수집 완료]\n소요 시간 :', time.time() - start)
    print("수집 결과")

    driver.quit()  # 작업이 끝나면 창을닫는다.
    if result:
        return result
    # pprint(result)



# crawler(searchKeyword)


