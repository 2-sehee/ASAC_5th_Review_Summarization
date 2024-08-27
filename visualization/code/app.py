import streamlit as st
import pandas as pd
import numpy as np
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import os


## DB 관련 함수 import 
from db_functions import fetch_business_list, find_business_in_db, get_reviews_for_business, get_users_for_review


## 페이지 설정 함수
def setup_page():
    st.set_page_config(page_title="ASAC_5th_Review", page_icon="🛵", layout="wide")
    st.markdown("""
    <style>
        .reportview-container .main .block-container { max-width: 1000px; }
    </style>
    """, unsafe_allow_html=True)

# 세션 상태 초기화
if 'search_clicked' not in st.session_state:
    st.session_state.search_clicked = False
if 'business_name' not in st.session_state:
    st.session_state.business_name = ""
if 'selected_categories' not in st.session_state:
    st.session_state.selected_categories = []
if 'selected_stars' not in st.session_state:
    st.session_state.selected_stars = []
if 'local_reviews' not in st.session_state:
    st.session_state.local_reviews = False

## main 화면 표시 함수
def show_main():
    # 페이지 타이틀 설정
    st.title("Welcome to ASAC-MAP")
    # 프로젝트 설명
    st.write("YELP 데이터셋을 활용한 고객 탐색경험 향상을 위한 키워드 요약 프로젝트입니다.")
    st.write("아래에서 원하는 가게 이름을 좌측에 입력해주세요.")
    business = fetch_business_list()
    business_df = business[['name', 'category', 'region', 'average_stars_biz']]
    st.dataframe(business_df)
    st.caption("© 2024 ASAC-5th-떡잎마을 방범대. All rights reserved. Unauthorized use prohibited.")



## 대분류 긍/부정 그래프
def display_bar_chart(business_info):
    # 점수 정보를 가져옴
    data = {
        'Category': ['Service', 'Others', 'Food', 'Price', 'Atmosphere', 'Facilities'],
        'Score': [
            business_info.service_score,
            business_info.others_score,
            business_info.food_score,
            business_info.price_score,
            business_info.atmosphere_score,
            business_info.facility_score
        ],
        'Keyword': [
            business_info.service_keyword,
            business_info.others_keyword,
            business_info.food_keyword,
            business_info.price_keyword,
            business_info.atmosphere_keyword,
            business_info.facility_keyword
        ]
    }

    df = pd.DataFrame(data)

    # 점수를 문자열로 변환하고 색상 지정하는 함수
    def score_to_text_and_color(row):
        score = row['Score']
        if score >= 0.80:
            return 'Excellent', '#0A306D'
        elif score >= 0.40:
            return 'Good', '#1565C0'  #800
        elif score > 0:
            return 'Not Bad', '#64B5F6'   #300
        elif score == 0:
            if row['Keyword'] == 'none':
                return 'No Data', '#90CAF9'  #200
            else:
                return 'Not Bad', '#90CAF9'
        elif score > -0.60:
            return 'Fair', '#FFB74D'  
        else:
            return 'Poor', '#EF6C00'

    # 문자열 및 색상 추가
    df[['Label', 'Color']] = df.apply(score_to_text_and_color, axis=1, result_type='expand')

    # 긍정 및 부정 점수를 각각 정렬(긍정->내림차순 / 부정->오름차순)
    df_positive = df[df['Score'] > 0].sort_values(by='Score', ascending=False)
    df_negative = df[df['Score'] <= 0].sort_values(by='Score', ascending=False)

    # 데이터프레임 재결합
    df_sorted = pd.concat([df_positive, df_negative])

    # 카테고리별 긍/부정 점수 시각화
    fig, ax = plt.subplots(figsize=(10, 3), constrained_layout=True)

    for index, row in df_sorted.iterrows():
        bar = ax.bar(row['Category'], row['Score'], color=row['Color'], width=0.4)
        # 각 막대 위에 문자열 표시
        ax.text(bar[0].get_x() + bar[0].get_width() / 2, 
                bar[0].get_height(), 
                f'{row["Label"]}', 
                ha='center', 
                va='bottom' if row['Score'] < 0 else 'bottom', 
                color='black')

    # 중앙선 추가 및 바깥선 제거
    ax.axhline(0, color='lightgrey', linewidth=0.8)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

    ax.set_ylabel('Scores')
    ax.set_title('Summary of Ratings by Category')

    # 스트림릿으로 플롯 출력
    st.pyplot(fig)


    
## 가게 정보 표시
def display_store_info(business_info):
    col1, col2 = st.columns([1.2, 1.8])
    with col1:
        image_path = os.path.join(os.path.dirname(__file__), 'assets/sample_img2.jpg')
        st.image(image_path, caption='Store Image', width=350)
    with col2:
        #display_map(business_info)
            # @@ 예외처리) 가게 리뷰가 10개 이상인 경우에만 차트 생성
        if business_info.review_count_biz >= 10:
            display_bar_chart(business_info)
        else :
            st.info("Summary available after 10+ reviews.")
        # 가게정보 표시
        display_additional_info(business_info)


## 가게 추가 정보 표시
def display_additional_info(business_info):
    with st.container(height=142):
        category_string = ' > '.join(eval(business_info.category)) if isinstance(business_info.category, str) else ' > '.join(business_info.category)
        st.write("⭐", round(business_info.average_stars_biz, 2))
        st.write("🍽️", category_string)
        if business_info.address == None:
            st.write("🏡", f"{business_info.region}")
        else : 
            st.write("🏡", f"{business_info.address}, {business_info.region}")


## 리뷰 요약 표시
def display_review_keywords(business_info):

    # 긍정 및 부정 키워드를 저장할 리스트
    good_keywords = []
    bad_keywords = []

    # 각 점수에 따라 긍정/부정 키워드 분류 및 저장
    if business_info.service_score != 0:
        score_keyword_pair = (business_info.service_score, business_info.service_keyword)
        if business_info.service_score > 0:
            good_keywords.append(score_keyword_pair)
        else:
            bad_keywords.append(score_keyword_pair)

    if business_info.others_score != 0:
        score_keyword_pair = (business_info.others_score, business_info.others_keyword)
        if business_info.others_score > 0:
            good_keywords.append(score_keyword_pair)
        else:
            bad_keywords.append(score_keyword_pair)

    if business_info.food_score != 0:
        score_keyword_pair = (business_info.food_score, business_info.food_keyword)
        if business_info.food_score > 0:
            good_keywords.append(score_keyword_pair)
        else:
            bad_keywords.append(score_keyword_pair)

    if business_info.price_score != 0:
        score_keyword_pair = (business_info.price_score, business_info.price_keyword)
        if business_info.price_score > 0:
            good_keywords.append(score_keyword_pair)
        else:
            bad_keywords.append(score_keyword_pair)

    if business_info.atmosphere_score != 0:
        score_keyword_pair = (business_info.atmosphere_score, business_info.atmosphere_keyword)
        if business_info.atmosphere_score > 0:
            good_keywords.append(score_keyword_pair)
        else:
            bad_keywords.append(score_keyword_pair)

    if business_info.facility_score != 0:
        score_keyword_pair = (business_info.facility_score, business_info.facility_keyword)
        if business_info.facility_score > 0:
            good_keywords.append(score_keyword_pair)
        else:
            bad_keywords.append(score_keyword_pair)

    # 긍정 및 부정 키워드 리스트를 점수 기준으로 정렬
    good_keywords.sort(reverse=True, key=lambda x: x[0])  # 점수 높은 순으로 정렬
    bad_keywords.sort(reverse=False, key=lambda x: x[0])  # 점수 낮은 순으로 정렬

    # 컬럼 레이아웃 정의
    col1, col2 = st.columns(2)
    
    # 첫 번째 컬럼에 긍정 키워드 추가
    with col1:
        st.subheader("Good Points 👍🏻")
        if good_keywords:
            for score, keyword in good_keywords:
                st.write(f"- {keyword}")
        else:
            st.write()
            #st.write("No positive feedback.")

    # 두 번째 컬럼에 부정 키워드 추가
    with col2:
        st.subheader("Bad Points 👎🏻")
        if bad_keywords:
            for score, keyword in bad_keywords:
                st.write(f"- {keyword} ")
        else:
            st.write()
            #st.write("No negative feedback.")



    
## 1. 리뷰 필터링 기능(대분류 별)
def filter_reviews_by_categories(merged_df, categories):

    if categories:
        return merged_df[merged_df[categories].apply(lambda x: x >= 1).any(axis=1)]
    return merged_df

## 2. 리뷰 필터링 기능 (별점)
def filter_reviews_by_stars(merged_df, star_ratings):
    """Filters reviews based on selected star ratings."""
    if star_ratings:
        return merged_df[merged_df['stars'].apply(np.floor).isin(star_ratings)]
    return merged_df

## 3. 리뷰 필터링 기능(로컬 리뷰)
def filter_local_reviews(merged_df, local_on, business_info):
    """Filters for local reviews if the toggle is on."""
    if local_on:
        return merged_df[(merged_df['most_visited_region'] == business_info.region) & (merged_df['visit_cnt'] >= 3)]
    return merged_df

## 리뷰 별점 찍기
def render_stars(rating):
    full_stars = int(rating)  # 전체 별 개수
    half_star = (rating - full_stars) >= 0.5  # 반 별이 필요한지
    empty_stars = 5 - full_stars - int(half_star)  # 빈 별 개수
    stars_html = '''
    <div style="font-size: 15px; color: orange; text-shadow: 0px 0px 3px orange; margin-top: -10px; margin-left: -8px;">
    '''
    stars_html += '★' * full_stars
    if half_star:
        stars_html += '☆'
    stars_html += '☆' * empty_stars
    stars_html += '</div>'
    return stars_html

## 리뷰 시각화
def display_reviews(business_info):
    # 세션 상태 초기화
    if 'selected_categories' not in st.session_state:
        st.session_state.selected_categories = []
    if 'selected_stars' not in st.session_state:
        st.session_state.selected_stars = []
    if 'local_reviews' not in st.session_state:
        st.session_state.local_reviews = False

    # 리뷰 데이터 가져오기 및 처리
    print("--------")
    business_id = int(business_info.business_id)
    print("business_id :", business_id)
    reviews = get_reviews_for_business(business_id)
    print("Number of reviews:", len(reviews))

    if not reviews:
        st.write("No reviews found for this business ID.")
        return
    
    review_df = pd.DataFrame(reviews)
    print(review_df.head())

    # 모든 사용자 정보 가져오기 및 DataFrame 생성
    user_ids = review_df.user_id.tolist()
    users = get_users_for_review(user_ids)  # 모든 사용자 정보를 한 번에 가져옴
    user_df = pd.DataFrame(users)
    print("user_df : ", user_df.head())

    # 리뷰 데이터와 사용자 데이터 병합
    merged_df = pd.merge(review_df, user_df, on='user_id', how='left')
    merged_df['date'] = pd.to_datetime(merged_df['date']).dt.date
    merged_df = merged_df.sort_values(by='date', ascending=False)
    print("merged_df : ", merged_df.head())
    

    # 리뷰 데이터 시각적으로 표시
    st.markdown("---")
    st.subheader(f"Reviews ({len(reviews)}) 💭")
    
    # 사용자에게 필터 선택 옵션 제공
    with st.expander("Filter Reviews") :
        col1, col2, col3 = st.columns([2, 0.5, 1])
        with col1:
            st.markdown("""
                <style>
                    /* 레이블 공간을 숨기는 CSS */
                    div[data-testid="stMultiSelect"] label {  
                        display: none !important;
                    }
                    .lightgray-bg {
                        background-color: white;
                        border-radius: 5px;
                        padding: 10px;
                    }
                </style>
                """, unsafe_allow_html=True)

            st.markdown('<div class="lightgray-bg">', unsafe_allow_html=True)
            st.caption("Select categories.")
            categories = st.multiselect(
                "",
                ['food', 'service', 'atmosphere', 'facility', 'price', 'others'],
                default=st.session_state.selected_categories
            )
            st.markdown('</div>', unsafe_allow_html=True)  # div 종료 태그
            # 2. 별점 필터
            st.caption("Select star ratings.")
            cols = st.columns(6)
            star_ratings = []
            for i, col in enumerate(cols):
                if col.checkbox(f"{i} stars", key=f"star_{i}"):
                    star_ratings.append(i)

            st.markdown('</div>', unsafe_allow_html=True)

        with col3 :
            st.write("")
            st.write("")
            st.write("")
            local_on = st.toggle("Local Reviews", value=st.session_state.local_reviews)
            if local_on :
                st.caption(f'Reviews from visitors with over three visits to')
                st.caption(f'{business_info.region}')

    # 상태 업데이트 및 재실행
    if categories != st.session_state.selected_categories or star_ratings != st.session_state.selected_stars or local_on != st.session_state.local_reviews:
        st.session_state.selected_categories = categories
        st.session_state.selected_stars = star_ratings
        st.session_state.local_reviews = local_on
        st.rerun()

    print("categories : ", categories)  # 선택된 카테고리 출력
    
    # 선택된 카테고리에 맞게 리뷰 필터링
    filtered_df = filter_reviews_by_categories(merged_df, categories)
    filtered_df = filter_reviews_by_stars(filtered_df, star_ratings)
    filtered_df = filter_local_reviews(filtered_df, local_on, business_info)
    
    # 선택된 카테고리에 해당하는 리뷰 갯수 출력
    st.write(f'Found {len(filtered_df)} reviews.')

    for index, row in filtered_df.iterrows():
        #print("filtered_df : ", filtered_df.head())
        with st.container():
            col1, col2, col3 = st.columns([0.8, 5, 1])
            with col1:
                st.markdown(f"**{row['name']}**")
                
            with col2:
                # 별점 HTML 적용
                stars_html = render_stars(row['stars'])
                components.html(f"""
                    <style>
                    .fa-star {{ color: orange; }}
                    .fa-star-half-alt {{ color: orange; }}
                    .fa-star-o {{ color: grey; }}
                    </style>
                    {stars_html}
                """, height=30)
            with col3:
                st.markdown(f"**{row['date']}**")
            #st.markdown(f"📍 {row['most_visited_region']}")
            st.markdown(f"{row['text']}")
            st.markdown("---")  # 각 리뷰 사이에 구분선 추가



## 결과 화면 표시
def show_result(business_name):
    business_info = find_business_in_db(business_name)
    # @@ 예외처리) 가게 이름이 DB에 없을 경우 - 가게명 없음 error 메세지
    if not business_info:
        st.error("No such store found. Please check the store name.")
        return

    st.title(f"{business_name}")
    display_store_info(business_info)
    
    # @@ 예외처리) 가게 리뷰가 10개 미만인 경우 - 키워드 요약 미제공
    if business_info.review_count_biz >= 10:
        display_review_keywords(business_info)
    display_reviews(business_info)


        

###### 페이지 설정 변경
st.set_page_config(
    page_title="ASAC_5th_Review",
    page_icon="🍽️",
    layout="wide",  # 'wide' layout 사용
)
####### sidebar #########
# CSS를 이용해 커스텀 스타일 적용
st.markdown("""
<style>
    .reportview-container .main .block-container {
        max-width: 1000px;  /* 최대 너비 설정 */
    }
</style>
""", unsafe_allow_html=True)


# 앱 실행
with st.sidebar :
    # 사이드바에 타이틀 추가
    st.sidebar.title("ASAC-MAP 🍽️")
    # 검색창 (* business_name 기준)
    input_name = st.text_input("Search...")

    #btn_submit = st.button("Go to Review", key='submit_btn', disabled=(input_name is False))

    # 버튼 클릭 시 검색 상태 유지
    if st.button("Go to Review", key='submit_btn'):
        st.session_state.search_clicked = True
        st.session_state.business_name = input_name

    # 팀 소개
    st.markdown("---")  # 구분선 추가
    st.markdown("""
    ### Team 떡잎마을 방범대      
    - **Team Members**
        - [박훈](https://github.com/daphoon) 
            - Sentimental Analytics
            - Keyword Extraction
        - [염혜지](https://github.com/yeomsta)
            - Keyword Extraction
        - [이세희](https://github.com/2-sehee)
            - Keyword Extraction
            - Streamlit Implementation
        - [장은지](https://github.com/Euunz2)
            - Keyword Extraction
            - Model Evaluation
    """)

    # GitHub 링크 버튼
    #st.markdown("### GitHub Repository")
    st.link_button('Visit our GitHub', 'https://github.com/bongho/Project_ASAC_5th_Review')


        
####### main page #########
# 메인 페이지 로직
if not st.session_state.search_clicked or not st.session_state.business_name:
    show_main()
## submit 버튼 onclick 이벤트
else: 
    business_name = st.session_state.business_name
    business_info = find_business_in_db(business_name)
    
    # @@ 예외처리) 입력이 없을 경우 - 에러 메시지
    if not business_info:
        st.error("No such store found. Please check the store name.")
    else:
        show_result(st.session_state.business_name)
