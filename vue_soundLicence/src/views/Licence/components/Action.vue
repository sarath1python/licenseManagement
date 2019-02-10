<template>
  <div>
    <v-menu left>
      <v-btn
        slot="activator"
        light
        icon
        :open-on-hover="true"
      >
        <v-icon>more_vert</v-icon>
      </v-btn>

      <v-list>
        <v-btn
          v-for="(item, index) in items"
          :key="index"
          :color=item.color
          small
          flat
          @click="detail(item.title, index)" 
        > 
          <v-icon>{{ item.icon }}</v-icon>
          {{item.title}}
        </v-btn>
      </v-list>
    </v-menu>
    <Detail :showdetails="showDetails" @close="showDetails = false"/>
  </div>
</template>

<script>
  import Detail from './Detail'

  export default {
    components: {
      Detail,
    },
    data: () => ({
      showDetails: false,
      items: [
        { title: 'Edit', icon: 'edit', color: 'green' },
        { title: 'Delete', icon: 'delete', color: 'red' },
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
    }),
    methods: {
      detail(item, idx) {
        console.log('showdetails')
        console.log(item)
        console.log(idx)
        this.showDetails = true;
        console.log(this.showDetails)
      }
    }
  }
</script>
