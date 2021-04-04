<template>
    <div class="col-md-2" style="padding-left:25px">
        <form class="example" method="post" @submit.prevent="performSearch" style="margin:auto;max-width:300px">
            <input type="text" placeholder="Search.." name="search2" v-model="searchKey">
            <button class="btn" type="submit"><i class="fa fa-search"></i></button>
        </form>
    </div>
</template>

<script>
import constant from '../../public/constant';
import axios from 'axios';
export default {
    name: "SearchComponent",
    data() {
        return {
            searchKey: '',
        };
    },
    methods: {
        performSearch() {
            axios({
                method: 'post',
                data: this.searchKey,
                headers: {
                    "content-type": "application/json"
                },
                url: constant.apiEndpointUrl + '/search',
            }).then(response => this.$emit('clicked', response.data));
        }
    }
}
</script>


<style scoped>

form.example input[type=text] {
  padding: 10px;
  font-size: 21px;
  border: 1px solid teal;
  border-radius: 0px im !important;
  float: left;
  width: 80%;
  background: #f1f1f1;
}

form.example button {
  float: left;
  width: 20%;
  padding: 10px;
  font-size: 23px;
}

form.example::after {
  content: "";
  clear: both;
  display: table;
}

</style>