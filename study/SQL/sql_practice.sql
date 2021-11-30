#Q1. 2021-08 한달에 대해 일별로 "APP_OPEN" 이벤트 수, "APP_OPEN" 이벤트를 발생시킨 유저 수, 유저 당 평균 "APP_OPEN" 이벤트 수를 세는 SQL을 작성하라.

select
  count(case when event_name = "APP_OPEN" then 1 end) as "app open" count(user_id case when event_name = "APP_OPEN" then 1 end) as "users" count("app open" / "users")
  date_format(from_unixtime(event_at), "%yyyy %mm %dd") as "event_time"

from event
where "event_time" like "2021-08%"
group by "event_time"

#Q2. 2021-08 한달에 대해 일별로 그 날짜에 가입한(="SIGN_UP" 이벤트 발생) 유저 수, 그 중 가입 후 24시간 이내에 검색을 해본(="SEARCH 이벤트") 유저 수와 비율을 계산하는 SQL을 작성해주세요.

select
  count(user_id case when event_name = "SIGN_UP" then 1 end) as "sign_up_users"
  count(user_id case when event_name = "SIGN_UP" and event_name = "SEARCH" then 1 end) as "sign_up_24h_search" count("sign_up_24h_search" / "sign_up_users") date_format(from_unixtime(event_at), "%yyyy %mm %dd") as "event_time"
from event

where "event_time" like "2021-08%" and timestampdiff(DAY, "", "") 
group by "event_time"


#Q3. 2021-08-31 하루 동안 발생한 "VIEW_CONTENT" 이벤트에 대해서, "VIEW_CONTENT" 이벤트의 직전 이벤트 종류 별로 개수를 세는 SQL을 작성해주세요.
select count(event_name)
from event
where "event_time" == "2021-08-31" and
"event_time" < (select "event_time" case when event_name = "VIEW_CONTENT" then 1 end)
group by "event_name"
