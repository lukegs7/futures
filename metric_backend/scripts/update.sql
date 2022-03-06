truncate table dw.bar5m;
truncate table dw.bar15m;
truncate table dw.bar30m;
truncate table dw.bar60m;
truncate table dw.bar1d;

insert into dw.bar5m(
	instrument,date,open,high,low,close,volume,amount,open_intl,timestamp
)
select
	instrument,date,open,high,low,close,volume,amount,open_intl,timestamp
from(
select
	instrument,date,open,high,low,close,volume,amount,open_intl,update_time,timestamp,
	row_number() over (partition by instrument, date order by instrument, date desc) as nu
from ods.bar5m
) t
where nu=1
order by instrument,date;

insert into dw.bar15m(
	instrument,date,open,high,low,close,volume,amount,open_intl,timestamp
)
select
	instrument,date,open,high,low,close,volume,amount,open_intl,timestamp
from(
select
	instrument,date,open,high,low,close,volume,amount,open_intl,update_time,timestamp,
	row_number() over (partition by instrument, date order by instrument, date desc) as nu
from ods.bar15m
) t
where nu=1
order by instrument,date;

insert into dw.bar30m(
	instrument,date,open,high,low,close,volume,amount,open_intl,timestamp
)
select
	instrument,date,open,high,low,close,volume,amount,open_intl,timestamp
from(
select
	instrument,date,open,high,low,close,volume,amount,open_intl,update_time,timestamp,
	row_number() over (partition by instrument, date order by instrument, date desc) as nu
from ods.bar30m
) t
where nu=1
order by instrument,date;

insert into dw.bar60m(
	instrument,date,open,high,low,close,volume,amount,open_intl,timestamp
)
select
	instrument,date,open,high,low,close,volume,amount,open_intl,timestamp
from(
select
	instrument,date,open,high,low,close,volume,amount,open_intl,update_time,timestamp,
	row_number() over (partition by instrument, date order by instrument, date desc) as nu
from ods.bar60m
) t
where nu=1
order by instrument,date;

insert into dw.bar1d(
	instrument,date,open,high,low,close,volume,amount,open_intl,timestamp
)
select
	instrument,date,open,high,low,close,volume,amount,open_intl,timestamp
from(
select
	instrument,date,open,high,low,close,volume,amount,open_intl,update_time,timestamp,
	row_number() over (partition by instrument, date order by instrument, date desc) as nu
from ods.bar1d
) t
where nu=1
order by instrument,date;