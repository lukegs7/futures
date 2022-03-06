## 目标品种
淀粉,生猪,棕榈,大豆1号,大豆2号,鸡蛋,焦炭,焦煤,豆油,铁矿,沥青,
原油,苯乙烯,热轧卷板,聚氯乙烯,短纤,豆粕,精对苯二甲酸,菜籽粕,锰硅,
硅铁,线型低密度聚乙烯,白砂糖,花生,玉米,螺纹,漂针浆,甲醇,玻璃,纯碱,
燃料油,尿素,铅,白银

农产品：
淀粉,生猪,棕榈,大豆1号,大豆2号,鸡蛋,豆油,
豆粕,精对苯二甲酸,菜籽粕,白砂糖,花生,玉米

原油,焦炭,焦煤,沥青,苯乙烯,热轧卷板,聚氯乙烯,短纤,锰硅,硅铁,螺纹,铁矿,
线型低密度聚乙烯,漂针浆,甲醇,玻璃,纯碱,燃料油

## 期货交易所
CZC  郑州商品交易所
SHF 上海期货交易所
DCE 大连商品交易所
INE 上海国际能源

# 主力合约
农产品的主力合约是1、5、9

## charting—library部分参数
(1)has_intraday: 是否具有日内分钟数据
(2)intraday_multipliers <[]>:  这是一个包含日内周期(分钟单位)的数组，datafeed将会自行构建它。
举例来说：如果datafeed报告说它支持 ["1", "5", "15"]，但事实上股票X只有1分钟的数据，股票X将设定 intraday_multipliers = [1]，那么Charting Library将自行构建5分钟和15分钟的周期。
如果某个时间段内的k线没有加载完全，则图标会持续发出请求，知道countback加载完为止
如果K线的数量少于 countBack，图表库将再次调用 getBars
示例 1：假设图表在请求中请求 300 根K线，范围为 [2019-06-01T00:00:00..2020-01-01T00:00:00]。 如果您在请求的时间段 ([2019-06-01T00:00:00..2020-01-01T00:00:00]) 中只有 250 根K线并且您返回这 250 根K线，则图表将再次请求在2019-06-01T00:00:00日期之前的数据，以在加载 50 根K线。
示例 2：假设图表在请求中请求 300 根K线，范围为 [2019-06-01T00:00:00..2020-01-01T00:00:00]。 如果您在请求的时间段内没有K线，也可以不需返回 {noData: true，和等于下一个可用数据的时间的nextTime}。您可以简单地返回 2020-01-01T00:00:00 之前的 300 根K线，即使该数据早于 from 日期。
(3)intraday_multipliers: 数据库中实际包含的数据，
(4)supported_resolutions：可以从现有数据中构建出来的数据

## 数据表
bar1d_CN_FUTURE
bar1m_CN_FUTURE
bar5m_CN_FUTURE
bar15m_CN_FUTURE
bar30m_CN_FUTURE
bar60m_CN_FUTURE

# config界面显示


# FG2205和FG205不同

# 商品期货数据
https://blog.csdn.net/dodo668/article/details/82382675

RB0 螺纹钢
AG0 白银
AU0 黄金
CU0 沪铜
AL0 沪铝
ZN0 沪锌
PB0 沪铅
RU0 橡胶
FU0 燃油
WR0 线材
A0 大豆
M0 豆粕
Y0 豆油
J0 焦炭
C0 玉米
L0 乙烯
P0 棕油
V0 PVC
RS0 菜籽
RM0 菜粕
FG0 玻璃
CF0 棉花
WS0 强麦
ER0 籼稻
ME0 甲醇
RO0 菜油
TA0 甲酸
品种名 + 0 （数字0），代表品种连续，如果是其他月份，请使用品种名 + YYYMM
例如豆粕 2013年09月，M1309

最大查询点数为242个

商品期货
http://stock2.finance.sina.com.cn/futures/api/json.php/IndexService.getInnerFuturesMiniKLineXm?symbol=CODE
例子：
http://stock2.finance.sina.com.cn/futures/api/json.php/IndexService.getInnerFuturesMiniKLine5m?symbol=M0
5分钟http://stock2.finance.sina.com.cn/futures/api/json.php/IndexService.getInnerFuturesMiniKLine5m?symbol=M0
15分钟
http://stock2.finance.sina.com.cn/futures/api/json.php/IndexService.getInnerFuturesMiniKLine15m?symbol=M0
30分钟
http://stock2.finance.sina.com.cn/futures/api/json.php/IndexService.getInnerFuturesMiniKLine30m?symbol=M0
60分钟
http://stock2.finance.sina.com.cn/futures/api/json.php/IndexService.getInnerFuturesMiniKLine60m?symbol=M0
日K线
http://stock2.finance.sina.com.cn/futures/api/json.php/IndexService.getInnerFuturesDailyKLine?symbol=M0
http://stock2.finance.sina.com.cn/futures/api/json.php/IndexService.getInnerFuturesDailyKLine?symbol=M1401


# 主力合约
LH2205
P2205
B2205
JD2205
JM2205
J2205
Y2205
A2207
I2205
BU2206
SC2205
EB2204
HC2205
V2205
PF2205
M2205
TA2205
RM2205
SM2205
SF2205
L2205
SR2205
PK2204
C2205
CS2205
RB2205
SP2205
MA2205
FG2205
SA2205