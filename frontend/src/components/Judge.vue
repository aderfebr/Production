<template>
  <el-row style="height: 100vh">
    <el-col :span="4">
      <el-scrollbar class="aside">
        <div class="side-top">推理系统</div>
        <el-menu
        boder="none"
        active-text-color="#ffd04b"
        background-color="#427eff"
        text-color="#fff"
        :default-active="activeIndex"
        :unique-opened=true
        :router=true
        >
          <el-menu-item index="/rule">规则库</el-menu-item>
          <el-menu-item index="/judge">推理</el-menu-item>
        </el-menu>
      </el-scrollbar>
    </el-col>
    <el-col :span="20">
      <div class="main">
        <div class="title">节点&ensp;</div>
        <el-divider></el-divider>
        <el-table :data="nodeData" :table-layout="auto" :height="300">
          <el-table-column label="ID">
            <template #default="scope">{{ scope.row.id }}</template>
          </el-table-column>
          <el-table-column label="描述">
            <template #default="scope">{{ scope.row.description }}</template>
          </el-table-column>
        </el-table>
      </div>
      <div class="main">
        <div class="title">推理</div>
        <el-divider></el-divider>
        <span class="judge">请输入已知事实的节点号,以逗号分隔:</span><br><br>
        <el-input v-model="judge"></el-input><br><br>
        <el-button type="success" @click="forward">正向推理</el-button><br><br>
        <span class="judge">请输入假设的节点号:</span><br><br>
        <el-input v-model="fact"></el-input><br><br>
        <el-button type="success" @click="backward">反向推理</el-button>
      </div>
    </el-col>
  </el-row>
</template>

<script setup>
import { getCurrentInstance,onMounted, ref } from 'vue';
const {proxy} = getCurrentInstance()

var nodeData=ref();
var edgeData=ref();
var judge=ref('1,2,3,4,5,6,7');
var fact=ref('17');

function getnode(){
  proxy.$http.post("http://localhost:8000/api/getnode/",{
  },{
    headers: {'Content-Type': 'multipart/form-data'}
  }).then((res)=>{
    if(res.data.code==200){
      nodeData.value=res.data.data;
    }
  });
}

function getedge(){
  proxy.$http.post("http://localhost:8000/api/getedge/",{
  },{
    headers: {'Content-Type': 'multipart/form-data'}
  }).then((res)=>{
    if(res.data.code==200){
      edgeData.value=res.data.data;
    }
  });
}

function forward(){
  proxy.$http.post("http://localhost:8000/api/forward/",{
    'judge':judge.value,
  },{
    headers: {'Content-Type': 'multipart/form-data'}
  }).then((res)=>{
    window.alert(res.data.msg)
  });
}

function backward(){
  proxy.$http.post("http://localhost:8000/api/backward/",{
    'judge':judge.value,
    'fact':fact.value,
  },{
    headers: {'Content-Type': 'multipart/form-data'}
  }).then((res)=>{
    window.alert(res.data.msg)
  });
}

onMounted(()=>{
  getnode();
  getedge();
})
</script>

<style scoped>
.title{
    font-size: 20px;  
    background: #fff;
    color: #555;
}
.judge{
  font-size: 15px; 
  color: #555;
}
.side-top{
  padding: 50px 0;
  font-size: 25px;
  text-align: center;
  color: #fff;
}
.aside {
  background: #427eff;
}
.main{
    background: #fff;
    height: 360px;
    padding: 20px;
}
</style>