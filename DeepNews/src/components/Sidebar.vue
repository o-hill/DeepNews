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
<<<<<<< HEAD
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
=======
      currentNews: []
>>>>>>> e4c3b77d78b65903acb8449424bb324af9445698
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
  background-color: #888888;
  display: inline-block;
}

</style>
