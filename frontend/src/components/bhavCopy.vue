<template>
    <div>
        <section>
            <div class="tbl-header">
                <table cellpadding="0" cellspacing="0" border="0">
                    <thead>
                        <tr>
                            <th>Code</th>
                            <th>Company</th>
                            <th>Open Price</th>
                            <th>High</th>
                            <th>Low</th>
                            <th>Close</th>
                        </tr>
                    </thead>
                </table>
            </div>
        
            <div class="tbl-content">
                <table cellpadding="0" cellspacing="0" border="0">
                    <tbody class="striped-table" v-bind:key="item.CODE" v-for="item in bhavCopyData">
                        <tr>
                            <td>{{item.CODE}}</td>
                            <td>{{item.NAME}}</td>
                            <td>{{item.OPEN}}</td>
                            <td>{{item.HIGH}}</td>
                            <td>{{item.LOW}}</td>
                            <td>{{item.CLOSE}}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </section>
    </div>
</template>

<script>
export default {
    name: "BhavCopy",
    props: ["bhavCopyData"]
}
</script>

<style>
    @import '../assets/style.css'
</style>
