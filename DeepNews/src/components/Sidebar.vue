<template>
  <div id="sidebar-container">
    <v-container>
      <ul>
        <v-flex xs12 v-for="article in currentNews">
          <v-card class = "white mb-3 mr-3">
            <v-layout row wrap>
              <!-- <v-flex xs5> -->
                <v-card-media>
                  <img :src = "getImageUrl(article)" height = 250px width=160px>
                </v-card-media>
              <!-- </v-flex> -->
              <!-- <v-flex xs7> -->
              <v-card-text>
                  <a :href="article.web_url" target="_blank"><h6>{{article.headline.main}}</h6></a>
              </v-card-text>
              <v-card-text class="grey--text">
                <div id="arttext">{{article.snippet}}</div>
              </v-card-text>
              <!-- </v-flex> -->
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
  props: ['queryString'],
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
    queryString (newQueryString) {
      this.currentNews = []
      this.getNews(newQueryString, 0)
    }
  },
  methods: {
    getNews (queryString, page) {
      let that = this;
      jQuery.ajax({
        url: this.articleSearchUrl,
        data: {
          apikey: this.api,
          q: queryString,
          sort: 'newest',
          page: page
        },
        crossDomain: true,
        xhrFields: {
          withCredentials: true
        },
        complete (response) {
          that.parseResponse(response.responseJSON, page)
        }
      })
    },
    parseResponse (respJson, page) {
      console.log('ss')
      let snippets = respJson.response.docs
      snippets.forEach( (snippet) => {
        this.currentNews.push(snippet)
        // if(snippet.multimedia.length > 0) {
        //   this.currentNews.push(snippet)
        // }
      })
      // if(this.currentNews.length < 10) {
      //   this.getNews(this.queryString, page + 1)
      // }
    },
    getImageUrl (article) {
      let images = article.multimedia
      for(let i = 0; i < images.length; ++i) {
        if(images[i].subtype === "xlarge") {
          return "https://www.nytimes.com/" + images[i].url
        }
      }
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
  text-align: left;
  line-height: 120%;
  vertical-align: top;
}


</style>
