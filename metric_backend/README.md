has_intraday: 是否具有日内分钟数据
intraday_multipliers <[]>:  这是一个包含日内周期(分钟单位)的数组，datafeed将会自行构建它。
举例来说：如果datafeed报告说它支持 ["1", "5", "15"]，但事实上股票X只有1分钟的数据，股票X将设定 intraday_multipliers = [1]，那么Charting Library将自行构建5分钟和15分钟的周期。


如果某个时间段内的k线没有加载完全，则图标会持续发出请求，知道countback加载完为止
如果K线的数量少于 countBack，图表库将再次调用 getBars
示例 1：假设图表在请求中请求 300 根K线，范围为 [2019-06-01T00:00:00..2020-01-01T00:00:00]。 如果您在请求的时间段 ([2019-06-01T00:00:00..2020-01-01T00:00:00]) 中只有 250 根K线并且您返回这 250 根K线，则图表将再次请求在2019-06-01T00:00:00日期之前的数据，以在加载 50 根K线。
示例 2：假设图表在请求中请求 300 根K线，范围为 [2019-06-01T00:00:00..2020-01-01T00:00:00]。 如果您在请求的时间段内没有K线，也可以不需返回 {noData: true，和等于下一个可用数据的时间的nextTime}。您可以简单地返回 2020-01-01T00:00:00 之前的 300 根K线，即使该数据早于 from 日期。

start 1615939200  2021-03-17
end  1645401600   2022-02-21
countback：244

intraday_multipliers: 数据库中实际包含的数据，
supported_resolutions：可以从现有数据中构建出来的数据