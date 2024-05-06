<template>
    <div class="main">
        <el-dialog
          v-model="editVisible"
          title="修改用户"
          width="500"
          :before-close="handleClose"
        >
          <span>ID:</span>
          <el-input 
            style="padding: 5px 0;"
            v-model="edited.userid"
            disabled
          />
          <span>用户名:</span>
          <el-input 
            style="padding: 5px 0;"
            v-model="edited.username"
          />
          <span>年龄:</span>
          <el-input 
            style="padding: 5px 0;"
            v-model="edited.age"
          />
          <span>地址:</span>
          <el-input 
            style="padding: 5px 0;"
            v-model="edited.address"
          />
          <br><br><el-button type="primary" @click="pwdclear();">修改密码</el-button>
          <template #footer>
            <div class="dialog-footer">
              <el-button @click="editVisible = false">取消</el-button>
              <el-button type="success" @click="editVisible = false;editsubmit();">确认</el-button>
            </div>
          </template>
        </el-dialog>
        <el-dialog
          v-model="pwdVisible"
          title="修改密码"
          width="600"
          :before-close="handleClose"
        >
          <span>请输入旧密码:</span>
          <el-input 
            style="padding: 5px 0;"
            v-model="oldpwd"
            type="password"
            show-password
          />
          <span>请输入新密码:</span>
          <el-input
            style="padding: 5px 0;"
            v-model="newpwd"
            type="password"
            show-password
          />
          <template #footer>
            <div class="dialog-footer">
              <el-button @click="pwdVisible = false">取消</el-button>
              <el-button type="success" @click="pwdVisible = false;pwdsubmit();">确认</el-button>
            </div>
          </template>
        </el-dialog>
        <el-dialog
          v-model="changeVisible"
          title="修改角色"
          width="600"
          :before-close="handleClose"
        >
          <el-transfer
            v-model="groupcheck"
            :props="{
              key: 'groupid',
              label: 'groupname',
            }"
            :data="group"
            :titles="['未分配角色', '已分配角色']"
          />
          <br><el-button type="success" @click="changeVisible = false;editgroup()">确认&ensp;<el-icon><Check /></el-icon></el-button>
        </el-dialog>
        <el-dialog
          v-model="deleteVisible"
          title="删除"
          width="500"
          :before-close="handleClose"
        >
          <span>确定删除用户{{ selected.username }}?</span>
          <template #footer>
            <div class="dialog-footer">
              <el-button @click="deleteVisible = false">取消</el-button>
              <el-button type="success" @click="deleteVisible = false;deletesubmit();">确认</el-button>
            </div>
          </template>
        </el-dialog>
        <Header></Header>
        <div class="title">用户管理</div>
        <el-divider></el-divider>
        <div v-if="auth">
          <el-row style="font-size: 25px;">
              <el-col :span="20"><el-input size="large" v-model="filter" style="width: 300px"/>&ensp;<el-button type="primary" @click="getuser">搜索&ensp;<el-icon><Search /></el-icon></el-button></el-col>
              <el-col :span="4" style="text-align: right;"><el-button type="success" @click="adduser">增加用户&ensp;+</el-button></el-col>
          </el-row>
          <br>
          <el-table :data="tableData" style="width: 100%">
            <el-table-column label="ID">
              <template #default="scope">{{ scope.row.userid }}</template>
            </el-table-column>
            <el-table-column label="用户名">
              <template #default="scope">{{ scope.row.username }}</template>
            </el-table-column>
            <el-table-column label="年龄">
              <template #default="scope">{{ scope.row.age }}</template>
            </el-table-column>
            <el-table-column label="地址">
              <template #default="scope">{{ scope.row.address }}</template>
            </el-table-column>
            <el-table-column label="操作" width="300px">
              <template #default="scope">
                <el-button type="warning" @click="editclear(scope.row);">修改用户</el-button>
                <el-button type="primary" @click="changeclear(scope.row);">修改角色</el-button>
                <el-button type="danger" @click="deleteVisible=true;selected=scope.row;">删除</el-button>
              </template>
            </el-table-column>
          </el-table>
        </div>
        <div v-if="!auth" style="width: 100%;text-align: center;font-size: 25px;color: red;">未授权!</div>
    </div>
</template>

<script setup>
import router from '..';
import { getCurrentInstance,onMounted, ref } from 'vue';
const {proxy} = getCurrentInstance()

var tableData=ref();
var auth=ref(false);
var selected=ref();

function getuser(){
  proxy.$http.post("http://localhost:8000/api/getuser/",{
    'token':localStorage.getItem("token"),
  },{
    headers: {'Content-Type': 'multipart/form-data'}
  }).then((res)=>{
    if(res.data.code==200){
      tableData.value=res.data.data;
      auth.value=true;
    }
  });
}

var edited=ref({});
var editVisible=ref(false);

function adduser(){
  router.push('/register');
}

function editclear(row){
  editVisible.value=true;
  selected.value=row;
  edited.value=JSON.parse(JSON.stringify(selected.value))
}

function editsubmit(){
  proxy.$http.post("http://localhost:8000/api/edituser/",{
    'userid':edited.value.userid,
    'username':edited.value.username,
    'age':edited.value.age,
    'address':edited.value.address,
    'token':localStorage.getItem("token"),
  },{
    headers: {'Content-Type': 'multipart/form-data'}
  }).then((res)=>{
    if(res.data.code==200&&edited.value.username==localStorage.getItem("username")){
      window.alert(res.data.msg);
      logout();
    }
    if(res.data.code==403) window.alert(res.data.msg);
  });
  setTimeout(() => {
    getuser();
  }, 200);
}

var pwdVisible=ref(false);
var oldpwd=ref();
var newpwd=ref();

function pwdclear(){
  oldpwd.value=null;
  newpwd.value=null;
  pwdVisible.value=true;
}

function pwdsubmit(){
  proxy.$http.post("http://localhost:8000/api/changepwd/",{
    'userid':selected.value.userid,
    'oldpwd':oldpwd.value,
    'newpwd':newpwd.value,
    'token':localStorage.getItem("token"),
  },{
    headers: {'Content-Type': 'multipart/form-data'}
  }).then((res)=>{
    if(res.data.code==200&&edited.value.username==localStorage.getItem("username")){
      window.alert(res.data.msg);
      logout();
    }
    if(res.data.code==403) window.alert(res.data.msg);
  })
}

var changeVisible=ref(false);
var group=ref();
var groupcheck=ref();

function changeclear(row){
  changeVisible.value=true;
  selected.value=row;
  edited.value=JSON.parse(JSON.stringify(selected.value));
  getgroup();
}

function getgroup(){
  proxy.$http.post("http://localhost:8000/api/getgroupbyuser/",{
    'userid':edited.value.userid,
    'token':localStorage.getItem("token"),
  },{
    headers: {'Content-Type': 'multipart/form-data'}
  }).then((res)=>{
    if(res.data.code==403) window.alert(res.data.msg);
    else{
      group.value=res.data.data;
      groupcheck.value=res.data.group;
    }
  });
}

function editgroup(){
  proxy.$http.post("http://localhost:8000/api/editgroupbyuser/",{
    'userid':edited.value.userid,
    'group':JSON.stringify(groupcheck.value),
    'token':localStorage.getItem("token"),
  },{
    headers: {'Content-Type': 'multipart/form-data'}
  }).then((res)=>{
    if(res.data.code==403) window.alert(res.data.msg);
  });
}

var deleteVisible=ref(false);

function deletesubmit(){
  proxy.$http.post("http://localhost:8000/api/deleteuser/",{
    'userid':selected.value.userid,
    'token':localStorage.getItem("token"),
  },{
    headers: {'Content-Type': 'multipart/form-data'}
  }).then((res)=>{
    if(res.data.code==403) window.alert(res.data.msg);
    getuser();
  });
}

function logout(){
  localStorage.removeItem('username');
  localStorage.removeItem('token');
  location.reload();
}

onMounted(()=>{
  getuser();
})
</script>

<style scoped>
.title{
    font-size: 20px;  
    background: #fff;
    color: #555;
}
.main{
    background: #fff;
    height: 100%;
    padding: 20px;
}
</style>