 /* https://www.hackerrank.com/challenges/weather-observation-station-5/problem?isFullScreen=true */

WITH group2 AS (
    SELECT city as c1, length(city) as len
    from station 
    order by len desc, city asc 
    /* we can use order by with two variables sequentially*/
    limit 1
),

/* Using With, we can create a table from which we can query */

group1 AS (
    SELECT city as c2, length(city) as len
    from station 
    order by len, city asc /* we can use order by with two variables sequentially*/
    limit 1
)

/* this is the way of combining two seperate results of each query */

select * from group1 

union all

select * from group2

