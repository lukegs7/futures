npx serve

name,//商品名称
ticker,//商品体系的唯一标志符
description,//描述
type,//仪表的可选类型，stock，index，forex，futures，bitcoin，expression，spread，cfd
session,//商品交易时间,参考交易日细节
session_holidays,//商品的假期列表，这些将不显示在图表上
corrections,//此商品的更正列表。更正是指具有特定交易时段的日子。它们也可以应用于假期
exchange  //或者listed_exchange  现在，这两个字段都为某个交易所的略称。将被显示在图表的图例中，以表示此商品
timezone，// 这个商品的交易所时区。我们希望以olsondb格式获取时区的名称。Asia/Shanghai
format，//在价格刻度上显示标签的格式：
minmov，//最小波动
pricescale，//价格精度
minmov2，// 
fractional
pointvalue
has_intraday
supported_resolutions
intraday_multipliers
has_daily
has_seconds
seconds_multipliers
has_weekly_and_monthly
has_empty_bars
force_session_rebuild
has_no_volume
volume_precision
data_status
expired
expiration_date
sector
industry
original_currency_code
currency_code