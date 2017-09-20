<template>
  <div class="row justify-content-md-center">
    <div class="col-md-12">
      <div v-for="n in 150">
        <a :href="'/#/psalm/'+n">Psalm {{ n }}</a><br/>
      </div>
    </div>
  </div>
</template>

<script>
import Psalms from '../psalms/psalms';

export default {
  name: 'Psalms',
  data() {
    return {
      psalms: Psalms.Psalms,
    };
  },
};
</script>

<style>
a {
  font-size: 25px;
}
</style>
