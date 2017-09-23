<template>
  <div id='google-map'></div>
</template>

<script>
export default {
  name: 'google-map',
  mounted () {
    loadScript()
  },
  data () {
    return {
      map: '',
      key: 'AIzaSyBSa_bbW6dWRsmAtJYgIJ2tuUOgplc2-5g',
      url: 'https://maps.googleapis.com/maps/api/js?key=AIzaSyBSa_bbW6dWRsmAtJYgIJ2tuUOgplc2-5g&callback=initialize'
    }
  },
  methods: {
    initialize () {
      let latlng = new google.maps.LatLng(0.00, 0.00)
      let config = {
        zoom: 10,
        center: latlng
      },
      map = new google.maps.Map(document.getElementById('map'))
    },

    loadScript () {
      let script = document.createElement('script')
      script.type = 'text/javascript'
      script.src = this.url
      document.body.appendChild(script)
    }
  }
}
</script>

<style>

</style>
