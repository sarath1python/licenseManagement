<template>
	<v-layout row wrap>
	  <v-flex v-for="i in 4" :key="`2${i}`" xs-3>
	    <v-card dark color="secondary">
	    	<v-card-text class="p-0">
	    	  content
	    	</v-card-text>
	    </v-card>
	  </v-flex>
	</v-layout>
</template>

