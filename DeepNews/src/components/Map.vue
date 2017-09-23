<template>
  <gmap-map
    :center="center"
    ref="map"
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
    props: ['currentLocation'],
    data () {
      return {
        center: {lat: 10.0, lng: 10.0},
        markers: [{
          position: {lat: 10.0, lng: 10.0}
        }, {
          position: {lat: 11.0, lng: 11.0}
        }],
        google: {},
        mapObject: {}
      }
    },
    watch: {
      currentLocation (newLocation) {
        this.panToLocation(newLocation)
      }
    },
<<<<<<< HEAD
    
=======
>>>>>>> 3a083e432be6ccdb8ef0f667953bac05e54323f1
    methods: {
      mapIsLoaded () {
        this.$emit('map-is-loaded', window.google)
        console.log("Map finished loading")
        this.google = window.google
        this.mapObject = this.$refs.map.$mapObject
      },
      mapViewChanged () {
        this.panToLocation(10, 0)
      },
      panToLocation (latlng) {
        this.mapObject.panTo(latlng)
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
