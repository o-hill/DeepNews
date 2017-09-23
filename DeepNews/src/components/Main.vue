<template>
  <div>
    <v-toolbar
      class = "white"
      floating
      dense
      >
       <v-text-field prepend-icon="search" hide-details single-line></v-text-field>
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

</style>
