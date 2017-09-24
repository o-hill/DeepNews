<template>
  <div id="sidebar-container">
    <v-container>
    </v-container>
  </div>
</template>

<script>
export default {
  name: 'sidebar',
  props: ['gcResp'],
  data () {
    return {
      currentNews: []
    }
  },
  watch: {
    gcResp (newResp) {
      this.buildQuery(newResp)
    }
  },
  methods: {
    buildQuery (resp) {

    },
    parseResponse (respJson) {
      respObj = JSON.parse(respJson)
      snippets = respObj.response.docs
      this.currentNews = []
      snippets.forEach( (snippet) => {
        this.currentNews.push(snippet)
      })
      console.log(this.currentNews)
    }
  }
}

</script>

<style>
#sidebar-container {
  width: 24%;
  height: 100%;
  background-color: blue;
  display: inline-block;
}

</style>
