update ods.bar1m set timestamp=extract(epoch from to_timestamp(date,'YYYY-MM-DD HH24:MI:SS'));
update ods.bar5m set timestamp=extract(epoch from to_timestamp(date,'YYYY-MM-DD HH24:MI:SS'));
update ods.bar15m set timestamp=extract(epoch from to_timestamp(date,'YYYY-MM-DD HH24:MI:SS'));
update ods.bar30m set timestamp=extract(epoch from to_timestamp(date,'YYYY-MM-DD HH24:MI:SS'));
update ods.bar60m set timestamp=extract(epoch from to_timestamp(date,'YYYY-MM-DD HH24:MI:SS'));
update ods.bar1d set timestamp=extract(epoch from to_timestamp(date,'YYYY-MM-DD'));

