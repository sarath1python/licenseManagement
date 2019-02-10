<template>
  <v-app>
    <NavBar />
    <v-content>
      <router-view/>
      <Footer />
    </v-content>
  </v-app>
</template>

<script>
  import NavBar from './components/Navbar'
  import Footer from './components/Footer'

  export default {
    components: {
      NavBar,
      Footer
    }
  }
</script>
