<template>
  <gmap-map
    :center="center"
    :zoom="7">
    <gmap-marker
      :key="index"
      v-for="(m, index) in markers"
      :position="m.position"
      :clickable="true"
      :draggable="true"
      @click="center=m.position">
    </gmap-marker>
  </gmap-map>
</template>

<script>

import * as VueGoogleMaps from 'vue2-google-maps';
import Vue from 'vue';

Vue.use(VueGoogleMaps, {
  load: {
    key: 'AIzaSyBSa_bbW6dWRsmAtJYgIJ2tuUOgplc2-5g',
    libraries: places
  }
});


export default {
    data () {
      return {
        center: {lat: 10.0, lng: 10.0},
        markers: [{
          position: {lat: 10.0, lng: 10.0}
        }, {
          position: {lat: 11.0, lng: 11.0}
        }]
      }
    }
  }
</script>

<style>
.vue-map-container {
  width: 100%;
  height: 100%;
}

</style>
