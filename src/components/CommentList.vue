<template>
  <div class="container">
    <div v-for="comment in comments">
      <h2><router-link :to="{ name: 'comment-view', params: { id: comment.id } }">{{ comment.title }} by {{ comment.author }}</router-link></h2>
      <p>{{ comment.text }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'comment-list',
  data () {
    return {
      comments: []
    }
  },
  mounted () {
    this.$http.get('http://127.0.0.1:4000/api/comments').then((response) => {
      this.comments = response.body
    }, (response) => {
      // error callback
    })
  }
}
</script>
