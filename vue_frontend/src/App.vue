<template>
  <div id="app">
    <div class="box">
      <div class="left-box">
        <KLineWidget
          v-if="!!symbolInfo.symbol"
          :symbolInfo="symbolInfo"
          ref="kLineWidget"
        />
      </div>
      <div class="right-box">
        <KLineHeader
          :symbol="symbol"
          :symbolList="symbolList" 
          @onClick="onClick"
        />
      </div>
      
    </div>
  </div>
</template>

<script>
import { apiGet } from "./api";
import KLineHeader from "./components/KLineHeader";
import KLineWidget from "./components/KLineWidget";

export default {
  name: "App",
  components: {
    KLineHeader,
    KLineWidget,
  },
  data() {
    return {
      symbol: "FG2205",
      symbolInfo: {},
      symbolList: [],
    };
  },
  methods: {
    fetchSymbolList() {
      apiGet("/main_futures").then((res) => {
        console.log(res)
        if (!res) {
          return;
        }                
        const list = [];
        for (let i = 0; i < res.length; i++) {          
            list.push(res[i]);          
        }
        console.log(list)
        const symbol = list.length ? list[0].symbol : "";
        this.symbol = symbol;
        this.symbolInfo = list[0];
        this.symbolList = list;
      });
    },    
    onClick(item) {
      this.$refs.kLineWidget.setSymbol(item.symbol);
      this.symbol=item.symbol
    },
  },
  created() {    
    this.fetchSymbolList();    
  },
};
</script>

<style>
body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Roboto", "Oxygen",
    "Ubuntu", "Cantarell", "Fira Sans", "Droid Sans", "Helvetica Neue",
    sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
.box {
  display: flex;  
}
.left-box {
  margin-left: 10px;  
  border-color: black;  
  width: auto;
  flex-grow: 1;  
}
.right-box {
  width: 200px;
  background: #fff;  
  border: 1px solid #eaeaea;
}
.header {
  overflow: scroll;
}
.primary {
  line-height: 1.5715;
  position: relative;
  display: inline-block;
  font-weight: 400;
  white-space: nowrap;
  text-align: center;
  background-image: none;
  box-shadow: 0 2px 0 rgba(0, 0, 0, 0.015);
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.645, 0.045, 0.355, 1);
  touch-action: manipulation;
  height: 32px;
  padding: 2px 4px;
  font-size: 14px;
  border-radius: 2px;
  color: #ff4d4f;
  background: #fff;
  border-color: #ff4d4f;
  margin: 3px 3px;
  width: 180px
}
.secondary {
  line-height: 1.5715;
  position: relative;
  display: inline-block;
  font-weight: 400;
  white-space: nowrap;
  text-align: center;
  background-image: none;
  box-shadow: 0 2px 0 rgba(0, 0, 0, 0.015);
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.645, 0.045, 0.355, 1);
  touch-action: manipulation;
  height: 32px;
  padding: 4px 15px;
  font-size: 14px;
  border-radius: 2px;
  background: #fff;
  color: rgba(0, 0, 0, 0.85);
  border: 1px solid #d9d9d9;
  margin: 3px 3px;
  width: 180px
}
</style>
