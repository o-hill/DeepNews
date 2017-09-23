<template>
  <div class="main-wrapper">
    <v-toolbar
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
  top: 30px;
  bottom: 0;
  left: 0;
  right: 0;
}

#search {
  z-index: 1;
}

</style>
