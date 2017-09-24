<template>
  <div id="sidebar-container">
    <v-container>
      <ul>
        <v-flex xs12 v-for="article in articles">
          <v-card>
            <v-card-media>
              <img :src = "article.image" height = 200px>
            </v-card-media>
            <v-card-title primary-title>
              <div>
                <h3>{{article.headline}}</h3>
              </div>
            </v-card-title>
            <v-card-actions>
                <v-btn dark icon='icon' @click.native="show = !show">
                  <v-icon>{{ show ? 'keyboard_arrow_down' : 'keyboard_arrow_up' }}</v-icon>
                </v-btn>
              </v-card-actions>
              <v-slide-y-transition>
                <v-card-text v-if="show">
                  {{article.text}}
                </v-card-text>
              </v-slide-y-transition>
          </v-card>
        </v-flex>
      </ul>
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
      show: false
>>>>>>> 01b38ae7c4f496bbfcfc97f2c99c5238c48a6562
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
  overflow-y: scroll;
}

</style>
