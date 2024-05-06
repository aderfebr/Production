<template>
  <div id="bg">
  <RouterView></RouterView>
  </div>
</template>

<script>

</script>

<style>
*{
    padding: 0;
    margin: 0;
}
#bg{
    width: 100vw;
    height: 100vh;
    overflow: hidden;
    background: linear-gradient(to right, #74ebd5, #acb6e5);
    background-size: cover;
}
</style>