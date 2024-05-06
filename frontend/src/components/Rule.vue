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
        <div class="title">节点&ensp;<el-button type="success" @click="">新增</el-button></div>
        <el-divider></el-divider>
        <el-table :data="nodeData" :table-layout="auto" :height="300">
          <el-table-column label="ID">
            <template #default="scope">{{ scope.row.id }}</template>
          </el-table-column>
          <el-table-column label="描述">
            <template #default="scope">{{ scope.row.description }}</template>
          </el-table-column>
          <el-table-column label="操作">
            <template #default="scope">
              <el-button type="danger" @click="">删除</el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>
      <div class="main">
        <div class="title">边&ensp;<el-button type="success" @click="">新增</el-button></div>
        <el-divider></el-divider>
        <el-table :data="edgeData" :table-layout="auto" :height="300">
          <el-table-column label="ID">
            <template #default="scope">{{ scope.row.id }}</template>
          </el-table-column>
          <el-table-column label="节点1">
            <template #default="scope">{{ scope.row.node1 }}</template>
          </el-table-column>
          <el-table-column label="节点2">
            <template #default="scope">{{ scope.row.node2 }}</template>
          </el-table-column>
          <el-table-column label="操作" width="200px">
            <template #default="scope">
              <el-button type="danger" @click="">删除</el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>
    </el-col>
  </el-row>
</template>

<script setup>
import { getCurrentInstance,onMounted, ref } from 'vue';
const {proxy} = getCurrentInstance()

var nodeData=ref();
var edgeData=ref();

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