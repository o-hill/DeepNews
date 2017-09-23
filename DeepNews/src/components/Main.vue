<template>
  <div class="google-map-wrapper">
    <v-toolbar
      class = "white"
      floating
      dense
      >
      <v-text-field id="search"></v-text-field>
    </v-toolbar>
    <google-map>
    </google-map>
  </div>
</template>

<script>
import GoogleMap from './Map.vue'
export default {
  components: {
    GoogleMap
  }
}
</script>

<style>
.google-map-wrapper {
  position: absolute;
  top: 30px;
  bottom: 0;
  left: 0;
  right: 0;
}

#search {
  z-index: 1;
}

</style>
