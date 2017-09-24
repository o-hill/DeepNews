<template>
  <div id="sidebar-container">
    <v-container>
      <v-for="article in articles">
        <card></card>
      </v-for>
    </v-container>
  </div>
</template>

<script>
import Card from './Card.vue'

export default {
  name: 'sidebar',
  components: {
    Card
  },
  props: ['gcResp'],
  data () {
    return {
      articles: [
        {
          text: "HelloWorld!",
          headline: "Computers"
        },
        {
          text: "rocks are cool",
          headline: "rock climbing"
        }
      ],
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
  background-color: #888888;
  display: inline-block;
}

</style>
