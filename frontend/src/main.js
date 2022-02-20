// Datafeed implementation, will be added later
// import Datafeed from './datafeed.js';

console.log("I'm in");
window.tvWidget = new TradingView.widget({
	symbol: 'BINANCE:BTCUSDT', // default symbol
	interval: '1h', // default interval
	fullscreen: true, // displays the chart in the fullscreen mode
	container_id: 'tv_chart_container',
	// datafeed: Datafeed,
	datafeed: new Datafeeds.UDFCompatibleDatafeed("http://127.0.0.1:5000"),
	library_path: '../charting_library_clonned_data/charting_library/',

	// locale: getLanguageFromURL() || 'en',
	locale:'zh',
	disabled_features: ['use_localstorage_for_settings'],
	enabled_features: ['study_templates'],
	charts_storage_url: 'http://localhost:8000',
	charts_storage_api_version: 1.1,
	auto_save_delay: 1,
	// 搜索延迟
	// symbol_search_request_delay:100,
	load_last_chart: true,
	client_id: 'future',
	user_id: 'geshuai',
	fullscreen: true,
	autosize: true,
	// studies_overrides: this.studiesOverrides,
	// watch list
	widgetbar: {
		details: true,
		watchlist: true,
		watchlist_settings: {
			default_symbols: ["NYSE:AA", "NYSE:AAL", "NASDAQ:AAPL"],
			readonly: false
		}
	}
});

window.tvWidget.onChartReady(() => {
	window.tvWidget.subscribe('onAutoSaveNeeded',()=>{
	window.tvWidget.saveChartToServer(function(){console.log('auto save success')},function(){console.log('auto save failed')},false);  
})
});

