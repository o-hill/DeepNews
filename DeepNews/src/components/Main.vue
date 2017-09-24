<template>
  <div class="main-wrapper">
    <v-toolbar
      id="bar"
      class = "white"
      floating
      dense
    >
    <v-icon class="mr-3">search</v-icon>
    <v-spacer></v-spacer>
      <gmap-autocomplete @place_changed="update_view" width=100px></gmap-autocomplete>
    </v-toolbar>
    <google-map
      :current-location="currentLocation">
    </google-map>
    <sidebar
      :query-string="queryString"></sidebar>
  </div>
</template>

<script>
import GoogleMap from './Map.vue'
import Sidebar from './Sidebar.vue'
import * as VueGoogleMaps from 'vue2-google-maps'
import jQuery from 'jQuery'

export default {
  components: {
    GoogleMap,
    Sidebar,
    VueGoogleMaps
  },
  data () {
    return {
      currentLocation: {},
      queryString: '',
      reverseGeocodeUrl: 'https://maps.googleapis.com/maps/api/geocode/json',
      mapsKey: 'AIzaSyBSa_bbW6dWRsmAtJYgIJ2tuUOgplc2-5g'
    }
  },
  methods: {
    update_view(response) {
      this.queryString = this.pickBestResult(response.address_components).long_name
      this.currentLocation = response.geometry.location;
    },
    // reverseGeocode(latlng) {
    //   let that = this;
    //   jQuery.ajax({
    //     url: this.reverseGeocodeUrl,
    //     data: {
    //       apikey: this.mapsKey,
    //       latlng: latlng.lat() + "," + latlng.lng(),
    //     },
    //     complete (response) {
    //       let results = response.responseJSON.results
    //       debugger
    //       that.queryString = that.pickBestResult(results[0].address_components).long_name
    //     }
    //   })
    // },
    pickBestResult(address_components) {
      for(let i = 0; i < address_components.length; ++i) {
        let types = address_components[i].types
        if(types.includes("locality")
          || types.includes("political")
          || types.includes("country")) {
          return address_components[i]
        }
      }
      return address_components[0]
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
  top: 15px;
  left: 10px;
  width: 300px;
}

body {
  overflow: hidden;
}

input[type=text] {
  width: 225px;
}

</style>
