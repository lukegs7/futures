<template>
  <div class="header" :style="{ height: height + 'px' }">
    <button
      v-for="item in symbolList"
      :key="item.symbol"
      :class="item.symbol === symbol ? 'primary' : 'secondary'"
      @click="$emit('onClick', item)"
    >
      {{ item["symbol"].toLocaleUpperCase() }}/{{
        item["description"].toLocaleUpperCase()
      }}
    </button>
  </div>
</template>

<script>
export default {
  name: "KLineHeader",
  props: {
    symbol: String,
    symbolList: Array,
  },
  data() {
    return {
      height: window.innerHeight,
    };
  },
};
</script>