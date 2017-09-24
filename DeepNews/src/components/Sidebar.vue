<template>
  <div id="sidebar-container">
    <v-container>
      <v-for="article in articles">
        <v-card>
        </v-card>
      </v-for>
    </v-container>
  </div>
</template>

<script>
export default {
  name: 'sidebar',
  props: ['gcResp'],
  data () {
    return {
      currentNews: {},
      articles: [
        {
          text: "HelloWorld!",
          headline: "Computers"
        },
        {
          text: "rocks are cool",
          headline: "rock climbing"
        }
      ]
    }
  },
  watch: {
    gcResp (newResp) {
      this.buildQuery(newResp)
    }
  },
  methods: {
    buildQuery (resp) {

    }
  }
}

</script>

<style>
#sidebar-container {
  width: 24%;
  height: 100%;
  background-color: #888888;
  display: inline-block;
}

</style>
