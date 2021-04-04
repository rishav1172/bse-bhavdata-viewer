<template>
    <div class="col-md-6" style="text-align:left; padding-left:30px">
        <button class="btn" @click="downloadAxios()"><i class="fa fa-download"></i> Download as CSV</button>
    </div>
</template>


<script>
import axios from 'axios';
import constant from '../../public/constant';
export default {
    name: "DownloadBhavCopy",
    props: ["bhavCopyData"],
    methods: {
        downloadAxios() {
            axios({
                method: 'post',
                data: this.bhavCopyData,
                headers: {
                    "content-type": "application/json"
                },
                url: 'http:127.0.0.1:8000/download',
            }).then(response => {
                var fileURL = window.URL.createObjectURL(new Blob([response.data]));
                var fileLink = document.createElement('a');

                fileLink.href = fileURL;
                fileLink.setAttribute('download', 'BhavCopyData.csv');
                document.body.appendChild(fileLink);

                fileLink.click();
            });
        }
    }
}
</script>

<style >

</style>