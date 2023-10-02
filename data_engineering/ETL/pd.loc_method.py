# 데이터를 필터링할 때 사용하는 pd.loc[] 메서드를 알아보자 

# https://www.geeksforgeeks.org/python-pandas-dataframe-loc/

# pd.loc[row, column] 

def location(df):
    loc_list = ["hotel", "guesthouse", "pension", "motel", "None",
                "leisure", "bus", "train"]

    # 호텔인 경우만 Hotel -> hotel로 변경
    df["attribute_sub1"] = df["attribute_sub1"].apply(lambda x: "hotel" if x == "HOTEL" else x)
    df["attribute_sub1"] = df["attribute_sub1"].fillna("None")

    ###

# 호텔이면 hotel 1, 게스트하우스면 guesthouse 1 .... (원핫인코딩 방식), 없으면 0
    # 먼저 loc()의 첫번째 인자에서 row-wise로 아래로 쭉 데이터를 필터링하고, 
    ## 걸러진 row vector들의 loc 컬럼의 값을 1로 바꾸는 방식 => 이게 loc() 메서드의 사용 방식!
    for loc in loc_list:
        df.loc[df["attribute_sub1"] == loc, loc] = 1
        df.loc[df["attribute_sub1"] != loc, loc] = 0  # 원핫인코딩 방식으로 false에는 0, True에는 1
    return df
