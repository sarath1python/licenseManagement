<template>
  <v-app light>
    <NavBar />
    <v-content>
      <router-view/>
      <Footer />
    </v-content>
  </v-app>
</template>

<script>
  import NavBar from './views/Layout/components/Navbar'
  import Footer from './views/Layout/components/Footer'

  export default {
    name: 'App',
    components: {
      NavBar,
      Footer
    },
    data () {
      return {
        //
      }
    }
  }
</script>
