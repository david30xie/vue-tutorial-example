<template>
  <div class="col-md-6">
    <h1>Create a new comment</h1>
    <form class="form">
        <div class="form-group">
            <label for="title">Title</label>
            <input type="text" class="form-control" id="title" name="title" />
        </div>

        <div class="form-group">
            <label for="author">Author</label>
            <input type="text" class="form-control" id="author" name="author" />
        </div>

        <div class="form-group">
            <label for="text">Comment Text</label>
            <textarea id="text" class="form-control" name="text"></textarea>
        </div>

        <button type="submit" class="btn btn-default">Submit</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'comment-create',
  data () {
    return {
      comment: {}
    }
  },
  mounted () {

  }
}
</script>
