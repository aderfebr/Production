<template>
  <el-row style="height: 100vh">
    <el-dialog
      v-model="addnodeVis"
      title="新增节点"
      width="500"
      :before-close="handleClose"
    >
      <span>ID:</span>
      <el-input 
        style="padding: 5px 0;"
        v-model="node.id"
      />
      <span>描述:</span>
      <el-input 
        style="padding: 5px 0;"
        v-model="node.description"
      />
      <span>是否为解:</span><br>
      <el-switch
        v-model="node.ans"
        active-text="是"
        inactive-text="否"
        style="padding: 5px 0;"
      />
      <template #footer>
        <div class="dialog-footer">
          <el-button @click="addnodeVis=false">取消</el-button>
          <el-button type="success" @click="addnodeVis=false;addnode();">确认</el-button>
        </div>
      </template>
    </el-dialog>
    <el-dialog
      v-model="addedgeVis"
      title="新增边"
      width="500"
      :before-close="handleClose"
    >
      <span>节点1:</span>
      <el-input 
        style="padding: 5px 0;"
        v-model="edge.node1"
      />
      <span>节点2:</span>
      <el-input 
        style="padding: 5px 0;"
        v-model="edge.node2"
      />
      <template #footer>
        <div class="dialog-footer">
          <el-button @click="addedgeVis=false">取消</el-button>
          <el-button type="success" @click="addedgeVis=false;addedge();">确认</el-button>
        </div>
      </template>
    </el-dialog>
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
        <div class="title">节点&ensp;<el-button type="success" @click="node={};addnodeVis=true;">新增</el-button></div>
        <el-divider></el-divider>
        <el-table :data="nodeData" :table-layout="auto" :height="300">
          <el-table-column label="ID">
            <template #default="scope">{{ scope.row.id }}</template>
          </el-table-column>
          <el-table-column label="描述">
            <template #default="scope">{{ scope.row.description }}</template>
          </el-table-column>
          <el-table-column label="是否为可能解">
            <template #default="scope"><p v-if="scope.row.ans">是</p><p v-if="!scope.row.ans">否</p></template>
          </el-table-column>
          <el-table-column label="操作">
            <template #default="scope">
              <el-button type="danger" @click="deletenode(scope.row.id)">删除</el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>
      <div class="main">
        <div class="title">边&ensp;<el-button type="success" @click="edge={};addedgeVis=true;">新增</el-button></div>
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
              <el-button type="danger" @click="deleteedge(scope.row.id)">删除</el-button>
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
var addnodeVis=ref(false);
var node=ref({});
var addedgeVis=ref(false);
var edge=ref({});

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

function addnode(){
  proxy.$http.post("http://localhost:8000/api/addnode/",{
    'id':node.value.id,
    'description':node.value.description,
    'ans':node.value.ans,
  },{
    headers: {'Content-Type': 'multipart/form-data'}
  }).then((res)=>{
    if(res.data.code!=200){
      window.alert(res.data.msg);
    }
    getnode();
  });
}

function deletenode(id){
  proxy.$http.post("http://localhost:8000/api/deletenode/",{
    'id':id,
  },{
    headers: {'Content-Type': 'multipart/form-data'}
  }).then((res)=>{
    getnode();
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

function addedge(){
  proxy.$http.post("http://localhost:8000/api/addedge/",{
    'node1':edge.value.node1,
    'node2':edge.value.node2,
  },{
    headers: {'Content-Type': 'multipart/form-data'}
  }).then((res)=>{
    if(res.data.code!=200){
      window.alert(res.data.msg);
    }
    getedge();
  });
}

function deleteedge(id){
  proxy.$http.post("http://localhost:8000/api/deleteedge/",{
    'id':id,
  },{
    headers: {'Content-Type': 'multipart/form-data'}
  }).then((res)=>{
    getedge();
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