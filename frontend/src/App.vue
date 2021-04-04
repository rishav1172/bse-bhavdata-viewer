<template>
  <div id="app">
    <link rel="stylesheet" 
        href="https://use.fontawesome.com/releases/v5.2.0/css/all.css" 
        integrity="sha384-hWVjflwFxL6sNzntih27bfxkr27PmbbK/iSvJ+a4+0owXq79v+lsFkW54bOGbiDQ" 
        crossorigin="anonymous">
    <div class="row">
      <SearchComponent @clicked="onClickChild"/>
      <DownloadBhavCopy v-bind:bhavCopyData="bhavCopyData"/>
    </div>
    <div class="row">
      <BhavCopy v-bind:bhavCopyData="bhavCopyData"/>
    </div>    
  </div>
</template>

<script>
import constant from '../public/constant';
import BhavCopy from './components/bhavCopy.vue';
import DownloadBhavCopy from './components/downloadBhavCopy';
import SearchComponent from './components/searchComponent';
import axios from 'axios';
export default {
  name: 'App',
  components: {
    BhavCopy,
    DownloadBhavCopy,
    SearchComponent
  },
  data() {
    return {
      bhavCopyData: []
    }
  },
  mounted() {
    this.getData()
  },
  methods: {
    onClickChild(value) {
      this.bhavCopyData = value
    },
    getData() {
      axios({
        method: 'get',
        url: constant.apiEndpointUrl,
      }).then(response => this.bhavCopyData = response.data);
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
