insert into countries (country_name)
select distinct target_country
FROM mission
where target_country is not NULL
on conflict (country_name) do nothing;

insert into cities (city_name, country_id)
select distinct
    m.target_city,
    c.id
from mission m
join countries c on m.country = c.country_name
where m.target_city is not null
on conflict (city_name) do nothing;

select target_industry from mission;

insert into target_types (target_type_name)
select distinct target_type
from mission
where target_type is not null
on conflict (target_type_name) do nothing;

insert into target_industries (industry_name)
select distinct target_industry
from mission
where target_industry is not null
on conflict (industry_name) do nothing;

INSERT INTO targets (city_id, type_id, industry_id, priority, latitude, longitude)
SELECT DISTINCT
    ci.id AS city_id,
    tt.id AS type_id,
    it.id AS industry_id,
    m.target_priority::integer AS priority,
    m.target_latitude::NUMERIC(10, 6) AS latitude,
    m.target_longitude::NUMERIC(10, 6) AS longitude
FROM mission m
INNER JOIN cities ci ON m.target_city = ci.city_name
INNER JOIN target_types tt ON m.target_type = tt.target_type_name
INNER JOIN target_industries it ON m.target_industry = it.industry_name
WHERE m.target_id IS NOT NULL
ON CONFLICT (id) DO NOTHING;