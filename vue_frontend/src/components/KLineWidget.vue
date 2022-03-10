<template>
  <div className="kline">
    <div id="tv_chart_container"></div>
  </div>
</template>

<script>
import { widget } from '../../public/charting_library';

export default {
  name: "KLineWidget",
  props: {         
  },
  data() {
    return {
      symbol: 'FG2205'
    };
  },
  methods: {   
    initTradingView() {      
      this.widget = new widget({
        // debug: true,        
        symbol: 'SA2205',
        interval: '15',        
        fullscreen: true,
        container_id: "tv_chart_container",                        
        datafeed: new window.Datafeeds.UDFCompatibleDatafeed('http://localhost:5000'),
        library_path: "/charting_library/",

        locale:'zh',
        timezone:'Etc/UTC',
        disabled_features: [],
        enabled_features: ['study_templates','items_favoriting','use_localstorage_for_settings','items_favoriting'],
        charts_storage_url: 'http://localhost:8000',            
        charts_storage_api_version: 1.1,
        auto_save_delay: 1,
        theme: 'Light', // 'Light'
        // 搜索延迟
        // symbol_search_request_delay:100,
        load_last_chart: true,
        client_id: 'future',
        user_id: 'John',        
        autosize: true,
        // studies_overrides: this.studiesOverrides,
        // watch list       
      });
      this.widget.onChartReady(() => {		
          this.widget.subscribe('onAutoSaveNeeded',()=>{		
          this.widget.saveChartToServer(function(){console.log('auto save success')},function(){console.log('auto save failed')},false);  
      });
    });
    },    
    setSymbol(symbol){
      this.symbol = symbol;      
      this.widget?.setSymbol(symbol, this.widget.symbolInterval().interval, () => {
        console.log("setSymbol", this.symbol);
      });
    }
  },
  mounted() {
    this.initTradingView();
  },
};
</script>