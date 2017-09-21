<template>
    <div>
      <component :is="tone_component"></component>
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
import Tone1 from './tones/Tone1';
import Tone2 from './tones/Tone2';
import Tone3 from './tones/Tone3';
import Tone4 from './tones/Tone4';
import Tone5 from './tones/Tone5';
import Tone5b from './tones/Tone5b';
import Tone6 from './tones/Tone6';
import Tone7 from './tones/Tone7';
import Tone7b from './tones/Tone7b';
import Tone7c from './tones/Tone7c';
import Tone8 from './tones/Tone8';
import Tone8b from './tones/Tone8b';
import Tone9 from './tones/Tone9';

export default {
  name: 'Psalm',
  data() {
    return {
      psalm_number: this.$route.params.id.toString(),
      psalm_text: Psalms.Psalms[this.$route.params.id.toString()].text,
      tone_component: `tone${Psalms.Psalms[this.$route.params.id.toString()].tone}`,
    };
  },
  components: {
    Tone1,
    Tone2,
    Tone3,
    Tone4,
    Tone5,
    Tone5b,
    Tone6,
    Tone7,
    Tone7b,
    Tone7c,
    Tone8,
    Tone8b,
    Tone9,
  },
};
</script>

<style>
p {
  text-align: left;
}
</style>
