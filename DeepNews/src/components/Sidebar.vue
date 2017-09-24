<template>
  <div id="sidebar-container">
    <button v-on:click="testQuery">Test</button>
    <v-container>
      <ul>
        <v-flex xs12 v-for="article in articles">
          <v-card class = "white mb-3 mr-3">
            <v-layout row wrap>
              <v-flex xs4>
                <v-card-media>
                  <img :src = "article.image" height = 150px>
                </v-card-media>
              </v-flex>
              <v-flex xs8>
              <v-card-text>
                  <a :href="article.image"><h6>{{article.headline}}</h6></a>
              </v-card-text>
              <v-card-text class="grey--text">
                <div id="arttext">{{article.text}}</div>
              </v-card-text>
              </v-flex>
            </v-layout>
          </v-card>
        </v-flex>
      </ul>
    </v-container>
  </div>
</template>

<script>
import Card from './Card.vue'
import jQuery from 'jQuery'

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
          headline: "Rocks",
          text: "Rocks are cool",
          image: 'https://ww2.kqed.org/science/wp-content/uploads/sites/35/2016/01/Wyoming-rocks-e1452554382152.jpg'
        },
        {
          headline: "Hills",
          text: "Hills are great",
          image: 'https://upload.wikimedia.org/wikipedia/commons/3/36/Chocolate_Hills.jpg'
        }
      ],
      currentNews: [],
      show: false,
      api: "eb7c9ef23d6343dbbb7ba47b1d760610",
      articleSearchUrl: "https://api.nytimes.com/svc/search/v2/articlesearch.json"
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
    testQuery () {
      console.log('test')
      let that = this;
      jQuery.ajax({
        url: this.articleSearchUrl,
        data: {
          apikey: this.api,
          q: "Ann Arbor"
        },
        crossDomain: true,
        xhrFields: {
          withCredentials: true
        },
        complete (response) {
          that.parseResponse(response.responseJSON)
        }
      })
    },
    parseResponse (respJson) {
      console.log('ss')
      debugger
      let snippets = respJson.response.docs
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
  float: right;
  width: 33%;
  height: 100%;
  background-color: #666666;
  display: inline-block;
  overflow-y: scroll;
}

h6 {
  float: left;
  color: black;
}

h6:hover {
  color: grey;
}

#arttext {
  position: absolute;
  left: 39%;
}


</style>
