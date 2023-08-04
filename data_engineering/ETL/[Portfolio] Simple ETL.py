# 라이브러리 임포트
from datetime import timedelta
import os
import pandas as pd
import numpy as np

index_cols = ["media_source", "channel", "campaign", "adset", "ad", "keywords"]
event_name_metrics = ["install", "re-attribution", "re-engagement", "af_complete_registration", "af_purchase"]

def csv_reader(csv):
    try:
        df = pd.read_csv(csv, low_memory=False)
    except UnicodeDecodeError:
        df = pd.read_csv(csv, encoding="utf-8-sig", low_memory=False)
    return df

def manual_appsflyer_file_reader(path, end_date):
    df = pd.DataFrame()
    file_list = os.listdir(path)
    for file in file_list:
        if end_date in file:
            file_df = csv_reader(path + "/" + file)
            print(file)
            df = pd.concat([df, file_df])

    return df

def filter_data(df):
    # CTIT, ITET, is_primary 필터링을 위한 데이터 처리
    # ctit, itet 윈도우 모두 7일 이내 & is_primary_attribution == False

    df = df.loc[df['Is Primary Attribution'] != False]

    time_cols = ["Attributed Touch Time", "Install Time", "Event Time"]
    df[time_cols] = df[time_cols].astype(str)

    df['Attributed Touch Time'] = pd.to_datetime(df['Attributed Touch Time'], format='%Y-%m-%d %H:%M:%S')
    df['Install Time'] = pd.to_datetime(df['Install Time'], format='%Y-%m-%d %H:%M:%S')
    df['Event Time'] = pd.to_datetime(df['Event Time'], format='%Y-%m-%d %H:%M:%S')

    df['ctit'] = df['Install Time'] - df['Attributed Touch Time']
    df['itet'] = df['Event Time'] - df['Install Time']

    # "ctit"가 Null값인 부분에 대해서 ctit는 0으로 처리하여 ctit, itet를 timdelta 필터 적용시 해당 데이터가 포함되게끔 전처리
    df.loc[df["Attributed Touch Time"].isnull(), "ctit"] = timedelta(days=0)

    df = df.loc[(df['ctit'] <= timedelta(days=7)) & (df['itet'] <= timedelta(days=7))]

    return df

def return_report(df):
    df.columns = [x.lower() for x in df.columns]
    df.columns = [i.replace(" ", "_") for i in df.columns]

    df[index_cols] = df[index_cols].fillna("-")
    df["keywords"] = df["keywords"].astype(str)
    df["keywords"] = [x.replace(".0", "") for x in df["keywords"]]

    # # event 기준 피봇
    df_event = df.loc[df["event_name"].isin(event_name_metrics)]

    df_event = df_event[index_cols + ["event_name"]]
    df_event["count"] = 1

    # # df_event = df_event.groupby(index_cols + ["event_name"]).size().reset_index(name = 'count')

    df_event = pd.pivot_table(df_event, index=index_cols, columns=['event_name'], values='count', aggfunc=np.sum,
                              fill_value=0)

    df_event = df_event.reset_index(level=index_cols).rename_axis(None, axis=1)

    df_event

    # revenue 기준 피봇
    df_revenue = df.pivot_table(index=index_cols, values="event_revenue", aggfunc="sum").reset_index()

    return df_event, df_revenue

if __name__ == "__main__":
    pd.set_option("mode.chained_assignment", None)
    readme = """-----------------------------------------
    앱스플라이어 수기 다운로드 리포트 머징 및 피봇 코드입니다.
    기준일 입력 시, 해당일의 앱스플라이어 데이터 파일들이 생성됩니다
    -----------------------------------------"""
    print(readme)

    # 경로 설정 (AF RD 데이터 경로, 저장 경로)
    manual_path = {MANUAL_PATH}
    save_path = {SAVE_PATH}

    end_date = input("데이터 조회 기준일을 입력하세요 ex)2022-01-01 : ")

    df = manual_appsflyer_file_reader(manual_path, end_date)

    df = filter_data(df)

    event_pivot, revenue_pivot = return_report(df)

    event_pivot_name = f"시코르_af_event_name_pivot_{end_date}.csv"
    revenue_pivot_name = f"시코르_af_revenue_pivot_{end_date}.csv"

    event_pivot.to_csv(save_path + "/" + event_pivot_name, encoding="utf-8-sig", index=False)
    revenue_pivot.to_csv(save_path + "/" + revenue_pivot_name, encoding="utf-8-sig", index=False)

    print(f"{end_date}까지의 csv 파일 저장이 완료되었습니다")