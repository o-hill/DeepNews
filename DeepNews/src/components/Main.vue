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
      <v-flex xs12 sm6>
      <v-dialog
          persistent
          v-model="modal"
          lazy
          full-width>
          <v-text-field
            slot="activator"
            label="After"
            v-model="date"
            prepend-icon="event"
            readonly></v-text-field>
          <v-date-picker v-model="date" scrollable dark>
            <template scope="{ save, cancel }">
              <v-card-actions>
                <v-btn flat primary @click.native="cancel()">Cancel</v-btn>
                <v-btn flat primary @click.native="save()">Save</v-btn>
              </v-card-actions>
            </template>
          </v-date-picker>
        </v-dialog>
        </v-flex>
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
      mapsKey: 'AIzaSyBSa_bbW6dWRsmAtJYgIJ2tuUOgplc2-5g',
      date: null,
      menu: false,
      modal: false,
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

.dialog__container {
  display: inline-block;
  margin-top: 25px;
  margin-left: 10px;
  width: 125px;
}

#bar {
  position: absolute;
  z-index: 1;
  left: 10px;
  top: 20px;
  left: 10px;
  width: 410px;
  height: 60px;
}

#bar label {
  color: grey;
}

body {
  overflow: hidden;
}

.mr-3 {
  margin-top: 15px;
}

.picker__body {
  background-color: white;
  color: black;
}

.card__actions {
  background-color: white;
}

input[type=text] {
  margin-top: 20px;
  font-size: 16px;
  width: 200px;
}

</style>
