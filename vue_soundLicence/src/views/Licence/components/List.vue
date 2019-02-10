<template>
  <v-container fluid class="table-container">
    <v-layout row wrap>
      <v-flex xs12>
        <v-data-table
          :headers="headers"
          :items="contents"
          class="elevation-1"
        >
          <template slot="items" slot-scope="props">
            <tr @click="viewDetails($event)" >
              <td>{{ props.item.status }}</td>
              <td>{{ props.item.number }}</td>
              <td>{{ props.item.name }}</td>
              <td>{{ props.item.location }}</td>
              <td>{{ props.item.issued_date }}</td>
              <td id='action-td'>
                <Action :licence="props.item" />
              </td>
            </tr>
          </template>
        </v-data-table>
      </v-flex>
    </v-layout>
    <Detail :showdetails="showDetails" :licence="licence" @close="showDetails = false"/>
  </v-container>
</template>

<script>
  import Action from './Action'
  import Detail from './Detail'
  import licence from '@/services/licence'

  export default {
    components: {
      Action,
      Detail
    },
    data () {
      return {
        showDetails: false,
        licence: {},
        headers: [
          { text: 'Status', sortable: false, value: 'status', align: 'center' },
          { text: 'Licence Number', value: 'number', align: 'center' },
          { text: 'Owner name', value: 'name', align: 'center' },
          { text: 'Location', value: 'location', align: 'center' },
          { text: 'Licence date', value: 'issued_date', align: 'center' },
          { text: 'Actions', value: '', align: 'center' },
        ],
        contents: []
      }
    },
    methods: {
      viewDetails (event) {
        if (event && event.target && event.target.type == 'button') {
          event.preventDefault()
        } else {
          this.showDetails = true;
          console.log(this.value);
          this.licence = this.value;
        }
      },
      getLicences () {
        licence.getLicences().then((data) => {
            this.contents = data.results;
        });
      }
    },
    mounted() {
      this.getLicences();
    }
  }
</script>

<style>
  .table-container {
    padding: 0 !important;
  }
</style>
