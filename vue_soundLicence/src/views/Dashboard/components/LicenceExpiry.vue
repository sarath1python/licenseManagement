<template>
    <v-card>
    	<v-toolbar color="indigo lighten-1" dark>
    		<v-toobar-title>LICENCE AGREEMENT EXPIRY</v-toobar-title>
    	</v-toolbar>
    	<v-list>
    		<v-template v-for="(item, index) in items">
		    	<v-list-tile>
		    	  <v-list-tile-content>
		    	    <v-list-tile-title>{{item.title}} </v-list-tile-title>
		    	  </v-list-tile-content>
		     	  <v-spacer></v-spacer>
		    	  <v-list-tile-action>
		    	    <v-chip
		    	      color="green"
		    	      text-color="white"
		    	    >3</v-chip> 
		    	  </v-list-tile-action>
		    	</v-list-tile>
		    	<v-divider></v-divider>
		    </v-template>
    	</v-list>	
    </v-card>
</template>

<script>
	export default {
		data () {
			return {
				items: [
					{"title": "Expires in 30days", "value": 3},
					{"title": "Expires in 30days", "value": 3},
					{"title": "Expires in 30days", "value": 3},
					{"title": "Expires in 30days", "value": 3},
				]
			}
		}
	}
</script>