import streamlit as st
import datetime
import pandas as pd
import FinanceDataReader as fdr
import plotly.graph_objects as go
import unicodedata

#스트림릿 -> 페이지 설정(타이틀, )
st.set_page_config(page_title='주식 차트 대시보드')
st.title('KOSPI 주식 차트 대시보드')

# 문자열 정규화 함수 -> 한글 종목명 띄어쓰기/특수문자 문제를 방지하는 목적
def normalize_str(s):
    return unicodedata.normalize('NFKC', s).strip()

# KOSPI 시장 전체 종목 정보 가져오기
market = 'KOSPI'
df_market = fdr.StockListing(market) # 코스피 종목 가져와서 저장
df_market['Name'] = df_market['Name'].apply(normalize_str) # 종목명 정규화
stocks = df_market['Name'].tolist() # 종목명 리스트형태로
# 시가총액 상위 10개 종목 막대그래프 생성
top10 = df_market.nlargest(10, 'Marcap').iloc[::-1] # 상위10개를 시가총액 역순(막대그래프 수평 정렬을 위해)

fig = go.Figure(go.Bar(
    x = top10['Marcap'] / 1e12, # 시가총액을 '조' 단위로 변환 
    y = top10['Name'], # y명 -> 종목명
    orientation ='h', # 가로 막대그래프
    text = top10['Marcap'] /1e12, # 그래프에 표시되는 텍스트 (조 단위)
    texttemplate='%{text:.1f}조'    # 텍스트 포맷 지정 (소수점 1자리, 조 단위)
))
fig.update_layout(
    title = 'KOSPI 시가총액 TOP10',
    xaxis_title='시가총액(조)',
    yaxis_title='종목명',
    bargap=0.115
)
# 스트림릿에서 화면에 그래프 출력
st.plotly_chart(fig)

# 사이드바에서 종목 선택 (최대 10개)
selected_stocks = st.sidebar.multiselect(
    '종목을 선택하세요. (최대 10개)', # 안내 문구
    stocks, # 선택할 수 있는 목록
    max_selections=10 # 최대 선택 가능 개수 제한
)
# 선택 종목명도 정규화 (위에서 만든 정규화 함수 호출)
#--> 리스트 컴프리헨션(리스트 내포) -> for 를 적용시겨 결과를 리스트로
selected_stocks = [normalize_str(s) for s in selected_stocks]

# 선택 종목명을 종목 코드로 변환
codes = []
for name in selected_stocks:
    # 종목명에 맞는 코드의 값 가지고 온다
    # 데이터프레임.loc[행,열]
    matched = df_market.loc[df_market['Name'] == name,'Code'].values
    # 선택된 내용이 화면에 나온다
    st.sidebar.write(f'선태 :{name} -> 코드: {matched}')
    if len (matched) > 0:
        codes.append(matched[0]) # array (['005930'],dtype=object)


# 선택한 종목 코드가 없으면 경고 후 실행 중지
if not codes:
    st.warning("종목 코드를 찾을 수 없습니다. 종목을 다시 선택해주세요.")
    st.stop()

    # 날짜 입력 -> 시작일 (2022년 1월 1일), 종료일(오늘날짜) -> 기본값으로 설정
start_data = st.sidebar.date_input('시작 날짜', datetime.date(2022,1,1))
end_date = st.sidebar.date_input('종료 날짜',datetime.datetime.now().date())

#  주식 데이터 불러오는 함수 (예외 처리 포함 -try ~except)
def get_stock_data(code,start,end):
    try: # 예외 (오류)가 발생할 가능성이 있는 경우에 넣는다
        df=fdr.DataReader(code,start,end) # 데이터 조회
        if df.empty: # 데이터가 비었다
            return None # None (없다) 반환
        return df # 데이터가 있다면 df 내용을 반환
    except Exception as e: # 예외 메세지 -> e라고 부르겠다
        st.error(f'{code} 데이터 로드 실페 : {e}') #  오류(예외) 메세지 출력 
        return None
# 선택한 종목별 현재가와 변동폭(전일 대비) 표시
for i, code in enumerate(codes): # i-> 인덱스번호,code->실제 값
    # 주식 데이터를 불로온다 (위에서 만든 함수 호출)
    df = get_stock_data(code,start_data.strftime('%Y-%m-%d'),end_date.strftime('%Y-%m-%d'))
    if df is not None and len(df) >= 2: # 2개 이상일 경우
        current = df['Close'].iloc[-1] # 가장 최신 종가
        prev = df['Close'].iloc[-2] # 그 전일 종가
        delta = current - prev # 변동폭 계산
        #화면에 종목명, 그 아래레 최신 종가 ,그 아래에 변동폭
        st.metric(label=selected_stocks[i],value=f'{current:,}원',delta=f'{delta:,}원')
    else:
        st.warning(f'{selected_stocks[i]} 데이터가 총분하지 않습니다.') 
    
# 그래프 탭: 라인 차트와 캔들스틱 차트 선택 가능
tab1,tab2 = st.tabs(['라인 차트','캔들스틱 차트'])

with tab1:
    if len(codes) ==1: # 종목을 하나만 선택 했다면 차트도 하나만 나온다
        df=get_stock_data(codes[0],start_data.strftime('%Y-%m-%d'),end_date.strftime('%Y-%m-%d'))
        if df is not None:
            st.line_chart(df['Close'])
        else:
            st.warning('데이터를 불러올 수 없습니다.')

    else:
        dfs = []
        for code in codes:
            df = get_stock_data(code,start_data.strftime('%Y-%m-%d'),end_date.strftime('%Y-%m-%d'))
            if df is not None:

                df_temp = df[['Close']].rename(columns={'Close':code})
                dfs.append(df_temp)
        if dfs:
            merged_df = pd.concat(dfs,axis=1)  # 수평 방향으로 병합
            merged_df.columns = selected_stocks # 컬럼명에 종목명으로 변경
            st.line_chart(merged_df) # 라인 차트 출력
        else:
            st.warning('선택한 종목의 데이터를 불러올 수 없습니다')
with tab2:
    # 캔들스틱 차트 -> 각 종목별 시가,고가,저가,종가 표시
    for i,code in enumerate(codes):
        df = get_stock_data(code,start_data.strftime('%Y-%m-%d'),end_date.strftime('%Y-%m-%d'))
        if df is not None:
            fig = go.Figure(data=[go.Candlestick(
                x=df.index,
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close']
            )])
            fig.update_layout(
                title=f'{selected_stocks[i]} 캔들스틱 차트',
                xaxis_title='날짜',
                yaxis_title='가격(원)'
            )
            st.plotly_chart(fig)
        else:
            st.warning(f"{selected_stocks[i]} 캔들스틱 차트를 불러올 수 없습니다.")
