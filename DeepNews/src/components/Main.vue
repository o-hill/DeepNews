<template>
  <div class="main-wrapper">
    <v-toolbar
      id="bar"
      class = "white"
      floating
      dense
    >
      <!-- <v-text-field id="search" @place_changed="update_view"></v-text-field> -->
      <gmap-autocomplete @place_changed="update_view"></gmap-autocomplete>
    </v-toolbar>
    <google-map :current-location="currentLocation" @map-is-loaded="enable_autocomplete">
    </google-map>
    <sidebar></sidebar>
  </div>
</template>

<script>
import GoogleMap from './Map.vue'
import Sidebar from './Sidebar.vue'
import * as VueGoogleMaps from 'vue2-google-maps';

export default {
  components: {
    GoogleMap,
    Sidebar,
    VueGoogleMaps
  },
  data () {
    return {
      currentLocation: {}
    }
  },

  methods: {
    // enable_autocomplete(google) {
    //   var autocomplete = new google.maps.places.Autocomplete(document.getElementById('search'));
    // },
    update_view(response) {
      debugger;
      this.currentLocation = response.geometry.location;
      debugger;
    }
  }
}
</script>

<style>
.main-wrapper {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
}

#bar {
  position: absolute;
  z-index: 1;
  margin: 10px;
  top: 10px;
}

</style>
