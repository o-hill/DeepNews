<template>
  <div class="google-map-wrapper">
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
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
}

</style>
