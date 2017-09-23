<template>
  <gmap-map
    :center="center"
    :zoom="7"
    @dragend="mapViewChanged"
    @tilesloaded="mapIsLoaded">
  </gmap-map>
</template>

<script>
import * as VueGoogleMaps from 'vue2-google-maps';
import Vue from 'vue';

Vue.use(VueGoogleMaps, {
  load: {
    key: 'AIzaSyBSa_bbW6dWRsmAtJYgIJ2tuUOgplc2-5g',
    libraries: 'places'
  }
});

export default {
    components: {
      VueGoogleMaps
    },
    data () {
      return {
        center: {lat: 10.0, lng: 10.0},
        markers: [{
          position: {lat: 10.0, lng: 10.0}
        }, {
          position: {lat: 11.0, lng: 11.0}
        }],
        google: {}
      }
    },
    methods: {
      mapIsLoaded () {
        console.log("Map finished loading")
        this.google = window.google
      },
      mapViewChanged () {
        console.log(window.google)
      },
      reverseGeocode (lat, lng) {

      }
    }

  }
</script>

<style>
.vue-map-container {
  width: 75%;
  height: 100%;
}

</style>
