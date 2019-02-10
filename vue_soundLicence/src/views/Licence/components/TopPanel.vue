<template>
	<v-toolbar flat>
		<v-toolbar-items>
	      	<v-text-field
	      	  name="search"
	      	  label="Search"
	      	  id="id"
	      	></v-text-field>
	      </v-toolbar-items>
      	  <v-spacer></v-spacer>
	      <v-toolbar-items>
	      	<v-select
	      	  :items="items"
	      	  v-model="value"
	      	  label="Year"
	      	></v-select>
	    </v-toolbar-items>
      	<v-spacer></v-spacer>
	    <v-toolbar-items>
	      	<v-btn small flat color="success">Add new</v-btn>	    	
	    </v-toolbar-items>
	</v-toolbar>
</template>

<script>
	export default {
		data: () => ({
			items: ['2019', '2018'],
			value: '2019'
		})
	}
</script>