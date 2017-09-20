<template>
    <div>
      <div class="row justify-content-md-center fixed-top" id="tone">
        <div class="col-md-4 my-2">
          <a href="/#">
            <img class="img-fluid" :src="tone_img">
          </a>
        </div>
      </div>
      <div class="row justify-content-md-center pt-5">
        <h3>Psalm {{ psalm_number }}</h3>
      </div>
      <div class="row justify-content-md-center pt-2">
        <p v-html="psalm_text"></p>
      </div>
    </div>
</template>

<script>
import Psalms from '../psalms/psalms';

export default {
  name: 'Psalm',
  data() {
    return {
      psalm_number: this.$route.params.id.toString(),
      psalm_text: Psalms.Psalms[this.$route.params.id.toString()].text,
      tone_img: `/static/tones/tone${Psalms.Psalms[this.$route.params.id.toString()].tone}.png`,
    };
  },
};
</script>

<style>
p {
  text-align: left;
}
#tone {
  background-color: white;
  border-bottom: 0.5px solid lightgrey;
}
</style>
