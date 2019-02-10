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
              <td>{{ props.item.licence_number }}</td>
              <td>{{ props.item.licencee_name }}</td>
              <td>{{ props.item.location }}</td>
              <td>{{ props.item.licence_date }}</td>
              <td id='action-td'>
                <Action />
              </td>
            </tr>
          </template>
        </v-data-table>
      </v-flex>
    </v-layout>
    <Detail :showdetails="showDetails" @close="showDetails = false"/>
  </v-container>
</template>

<script>
  import Action from './Action'
  import Detail from './Detail'

  export default {
    components: {
      Action,
      Detail
    },
    data () {
      return {
        showDetails: false,
        headers: [
          {
            text: 'Status',
            sortable: false,
            value: 'status',
            align: 'center' 
          },
          { text: 'Licence Number', value: 'licence_number', align: 'center' },
          { text: 'Owner name', value: 'licencee_name', align: 'center' },
          { text: 'Location', value: 'location', align: 'center' },
          { text: 'Licence date', value: 'licence_date', align: 'center' },
          { text: 'Actions', value: '', align: 'center' },
        ],
        contents: [
          {
            status: '3 Warnings',
            licence_number: 122129,
            licencee_name: 'Licencee name',
            location: 'Technopark',
            licence_date: '10th Jan 2019',
          },
          {
            status: 'Cancelled',
            licence_number: 122129,
            licencee_name: 'Licencee name',
            location: 'Technopark',
            licence_date: '10th Jan 2019',
          },
          {
            status: 'Approved',
            licence_number: 122129,
            licencee_name: 'Licencee name',
            location: 'Technopark',
            licence_date: '10th Jan 2019',
          },
          {
            status: 'Approved',
            licence_number: 122129,
            licencee_name: 'Licencee name',
            location: 'Technopark',
            licence_date: '10th Jan 2019',
          },
          {
            status: 'Approved',
            licence_number: 122129,
            licencee_name: 'Licencee name',
            location: 'Technopark',
            licence_date: '10th Jan 2019',
          },
          {
            status: 'Approved',
            licence_number: 122129,
            licencee_name: 'Licencee name',
            location: 'Technopark',
            licence_date: '10th Jan 2019',
          },
          {
            status: 'Approved',
            licence_number: 122129,
            licencee_name: 'Licencee name',
            location: 'Technopark',
            licence_date: '10th Jan 2019',
          },
          {
            status: 'Approved',
            licence_number: 122129,
            licencee_name: 'Licencee name',
            location: 'Technopark',
            licence_date: '10th Jan 2019',
          }
        ],
        licence_status: 'Active',
        licencee_number: 123123123,
        licencee_name: 'John',
        serial_number: 123123,
        issued_date: '10th Feb 2019',
        details: 'Details about the agent',
        violations: [
          {date: '9th Feb 2019', details: 'some details'},
          {date: '10th Feb 2019', details: 'some other details'},
        ]
      }
    },
    methods: {
      viewDetails (event) {
        if (event && event.target && event.target.type == 'button') {
          event.preventDefault()
        } else {
          this.showDetails = true;
        }
      }
    }
  }
</script>

<style>
  .table-container {
    padding: 0 !important;
  }
</style>
