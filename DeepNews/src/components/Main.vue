<template>
  <div class="main-wrapper">
    <v-toolbar
      class="white"
      floating
      dense>
      <v-text-field></v-text-field>
    </v-toolbar>
    <google-map>
    </google-map>
    <sidebar></sidebar>
  </div>
</template>

<script>
import GoogleMap from './Map.vue'
import Sidebar from './Sidebar.vue'
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

</style>
