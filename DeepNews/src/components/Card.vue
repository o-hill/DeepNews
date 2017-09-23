<template>
  <v-layout>
  <v-flex xs12 sm6 offset-sm3>
      <v-card>
        <v-card-media>
          <img src = "static/hills.jpg" height = 200px>
        </v-card-media>
        <v-card-title primary-title>
          <div>
            <a href="https://i.ytimg.com/vi/kfv-1CNomcU/maxresdefault.jpg" target="_blank">{{ msg }}</a>
          </div>
        </v-card-title>
      </v-card>
    </v-flex>
 </v-layout>

</template>


<script>
  export default{
    data(){
      return{
        msg: 'Hills hills hills'
      }
    }
  }
</script>


<style>
div {
}
</style>
