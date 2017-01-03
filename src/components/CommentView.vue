<template>
  <div class="container">
    <div v-if="comment">
      <h2>{{ comment.title }} by {{ comment.author }}</h2>
      <p>{{ comment.text }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'comment-view',
  data () {
    return {
      comment: {}
    }
  },
  mounted () {
    this.$http.get('http://127.0.0.1:4000/api/comments/' + this.$route.params.id).then((response) => {
      this.comment = response.body
    }, (response) => {
      // error callback
    })
  }
}
</script>
