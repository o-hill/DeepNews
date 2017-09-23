<template>
  <v-layout row>
  <v-flex xs12 sm6 offset-sm3>
      <v-card>
        <v-card-media>
          <img :src = "image" height = 200px>
        </v-card-media>
        <v-card-title primary-title>
          <div>
            <h3>{{headline}}</h3>
          </div>
        </v-card-title>
        <v-card-actions>
            <v-btn icon @click.native="show = !show">
              <!-- <v-icon v-if="show">arrow_downward</v-icon>
              <v-icon v-else>arrow_upward</v-icon> -->
              <v-icon>{{ show ? arrow_downward : arrow_upward }}</v-icon>
            </v-btn>
          </v-card-actions>
          <v-slide-y-transition>
            <v-card-text v-show="show">
              I'm a thing. But, like most politicians, he promised more than he could deliver. You won't have time for sleeping, soldier, not with all the bed making you'll be doing. Then we'll go with that data file! Hey, you add a one and two zeros to that or we walk! You're going to do his laundry? I've got to find a way to escape.
            </v-card-text>
          </v-slide-y-transition>
      </v-card>
    </v-flex>
 </v-layout>
</template>



<script>
  export default{
    //props: ['headline', 'image', 'text']
    data: () => {
      return {
        headline: 'Hills hills hills',
        image: "static/hills.jpg",
        text: "Rock or stone is a natural substance",
        show: false
      }
    }

  }
</script>


<style>
div {
}
</style>
