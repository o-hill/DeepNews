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
    <google-map :current-location="currentLocation">
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
    update_view(response) {
      this.currentLocation = response.geometry.location;
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
  left: 10px;
  top: 10px;
  left: 10px;
}

</style>
