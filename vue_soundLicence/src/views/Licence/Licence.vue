<template>
  <div>
    <v-container fluid grid-list-lg text-xs-center>
      <v-layout row wrap>
        <TopPanel />
        <List />
      </v-layout>
    </v-container>
  </div>
</template>

<script>
  import TopPanel from './components/TopPanel'
  import List from './components/List'

  export default {
    components: {
      TopPanel,
      List
    }
  }
</script>
