<template>
  <v-toolbar 
    color="indigo darken-1"
    dark
    app
    clipped-right
  >
    <v-toolbar-title class="headline text-uppercase" :to="{name: 'dashboard'}">
      <span>Noise licence management</span>
    </v-toolbar-title>
    <v-spacer></v-spacer>
    <v-toolbar-items>
    </v-toolbar-items>
    <v-spacer></v-spacer>
    <v-toolbar-items>
      <v-btn flat :to="{name: 'dashboard'}" exact>Dashboard</v-btn>
      <v-btn flat :to="{name: 'licence'}" exact>Licences</v-btn>
      <v-spacer></v-spacer>
      <v-btn flat>Login</v-btn>
    </v-toolbar-items>
  </v-toolbar>
</template>

color="blue-grey"
      dark
      fixed
      app
clipped-right