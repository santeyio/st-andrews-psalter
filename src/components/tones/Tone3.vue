<template>
  <div class="row justify-content-md-center fixed-top" id="tone">
    <div class="col-md-4 my-2">
      <a href="/#">
        <img class="img-fluid" src="../../assets/tones/tone3.png">
      </a>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Tone3',
  data() {
    return {
      tone: 3,
    };
  },
};
</script>

<style>
#tone {
  background-color: white;
  border-bottom: 0.5px solid lightgrey;
}
</style>
