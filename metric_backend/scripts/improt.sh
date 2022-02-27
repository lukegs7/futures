PGPASSWORD=postgres psql -U postgres -d finance -c '\copy ods.bar1m(instrument,date,open,high,low,close,volume,amount,open_intl) from learn/invest/fit_data/1m.csv csv'
PGPASSWORD=postgres psql -U postgres -d finance -c '\copy ods.bar5m(instrument,date,open,high,low,close,volume,amount,open_intl) from learn/invest/fit_data/5m.csv csv'
PGPASSWORD=postgres psql -U postgres -d finance -c '\copy ods.bar15m(instrument,date,open,high,low,close,volume,amount,open_intl) from learn/invest/fit_data/15m.csv csv'
PGPASSWORD=postgres psql -U postgres -d finance -c '\copy ods.bar30m(instrument,date,open,high,low,close,volume,amount,open_intl) from learn/invest/fit_data/30m.csv csv'
PGPASSWORD=postgres psql -U postgres -d finance -c '\copy ods.bar60m(instrument,date,open,high,low,close,volume,amount,open_intl) from learn/invest/fit_data/60m.csv csv'
PGPASSWORD=postgres psql -U postgres -d finance -c '\copy ods.bar1d(instrument,date,open,high,low,close,volume,amount,open_intl) from learn/invest/fit_data/1d.csv csv'


