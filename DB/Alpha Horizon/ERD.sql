// Use DBML to define your database structure
// Docs: https://dbml.dbdiagram.io/docs

Table indicators {
  indicator_id varchar [primary key]
  name text
  type text
  parameters varchar 
}

Table assets {
  asset_id varchar [primary key]
  symbol text
  name text
  exchange varchar
}

Table signals {
  signal_id varchar [primary key]
  indicator_id varchar
  asset_id varchar 
  timestamp timestamp
  type varchar 
  confidence_level integer
}


Ref: indicators.indicator_id > assets.symbol // many-to-one

Ref: assets.symbol < signals.signal_id 
