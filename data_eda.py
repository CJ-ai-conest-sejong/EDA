import matplotlib.pyplot as plt
import seaborn as sns
plt.rc('font', family='NanumBarunGothic') 
def data_eda(data): 
  col_dic = {'CORP_ID' : '창고코드', 
            'REF_ORD_NO' : '고객 주문번호', 
            'BKG_NO' : 'CJ대한통운 주문번호(예약번호)', 
            'BKG_TYP' : '주문유형',#(7: B2C출고, 8: 정상반출, 9: 불량반출) 
            'BKG_DATE' : '주문날짜',
            'BKG_TIME' : '주문시간',
            'SHPR_CD' : '고객사코드',
            'INV_AMT' : '주문금액',
            'ITEM_SEQ' : '품목순번',
            'ITEM_CD' : '품목코드',
            'BRAND_NM' : '브랜드',
            'ITEM_QTY' : '품목수량',
            'ITEM_AMT' : '품목금액',
            'IF_YN' : '수신여부',
            'ORDER_CRT_DATETIME' : '주문생성시간',
            'DLV_DV' : '택배구분',
            'REF_ITEM_SEQ' : '상품주문번호',
            'ORDER_IDX' : '중개업체 주문번호',
            'ORDER_YN' : '접수여부',
            'DLVPREARRBRANCD' : '배달예정점소코드',
            'DLVPREARREMPNICKNM' : '배달예정사원분류코드',
            'DLVCLSFCD' : '배달터미널코드',
            'DLVSUBCLSFCD' : '배달터미널 소분류코드',
            'INS_ID' : '입력자ID',
            'INS_DATE' : '입력일자(인터페이스 시간)',
            'INS_TIME' : '입력시간(인터페이스 시간)',
            'POST_ZONE' : '권역구분',
            'SPLIT_EXEC_YN' : '배송처별 주문분할여부',
            'SHPR_ADDR_1' : '송화인 주소1',
            'SHPR_ADDR_2' : '송화인 주소2',
            'CNEE_ADDR_1' : '수화인 주소1',
            'CNEE_ADDR_2' : '수화인 주소2'
            }
  data.rename(columns = col_dic, inplace = True)
  return data

def sum_qty(data):
  date = sorted(data.주문날짜.unique())
  date_dic = {}
  for d in date:
    date_dic[d] = sum(data.loc[(data.주문날짜 == d)].품목수량) #/ sum(data.품목수량)
  return date_dic


def qty_plot(date_dic):
  date_per_cnt = list(date_dic.values())
  order_date = list(date_dic.keys())
  df2 = pd.DataFrame(order_date,columns=['주문날짜'])
  df2['일별수량'] = date_per_cnt
  df2.주문날짜 = df2.주문날짜 % 100
  plt.figure(figsize=(20,10))
  sns.barplot(
      data= df2,
      x= "주문날짜",
      y= "일별수량"
  )
  plt.ylim(0, 100000) 