<template>
  <div class="main-wrapper">
    <v-toolbar
      id="bar"
      class = "white"
      floating
      dense
    >
      <v-text-field id="search"></v-text-field>
    </v-toolbar>
    <google-map>
    </google-map>
    <sidebar></sidebar>
  </div>
</template>

<script>
import GoogleMap from './Map.vue'
import Sidebar from './Sidebar.vue'

var autocomplete = new window.google.maps.places.Autocomplete(document.getElementById('search'));

export default {
  components: {
    GoogleMap,
    Sidebar
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
