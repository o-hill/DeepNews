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
            <v-btn dark icon='icon' @click.native="show = !show">
              <v-icon>{{ show ? 'keyboard_arrow_down' : 'keyboard_arrow_up' }}</v-icon>
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
