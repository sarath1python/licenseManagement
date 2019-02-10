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
    <Detail :showdetails="showDetails" :licence="licence" :action="action" @close="showDetails = false"/>
    <Violation :showViolation="showViolation" :violations="licence.violations" :action="action" @close="showViolation = false"/>
    {{licence}}
  </div>
</template>

<script>
  import Detail from './Detail'
  import Violation from './Violation'

  export default {
    components: {
      Detail,
      Violation
    },
    props: ["licence"],
    data: () => ({
      showDetails: false,
      showViolation: false,
      action:'View',
      items: [
        { title: 'Edit', icon: 'edit', color: 'green' },
        { title: 'Delete', icon: 'delete', color: 'red' },
        { title: 'Add violation', icon: 'add', color: 'green' },
        { title: 'Edit violation', icon: 'edit', color: 'green' },
        { title: 'Delete violation', icon: 'delete', color: 'red' },
      ]
    }),
    methods: {
      detail(__action, __idx) {
        this.action = __action;
        console.log(this.action)
        console.log(this.licence.violations)
        if (__action.indexOf('violation') > -1) {
          if (this.licence.violations.length < 1) {
            this.licence.violations = [{'details': '', 'date': ''}]
            this.action = 'Add Violation'
          }
          this.showViolation = true;
        } else {
          this.showDetails = true;
        }
      }
    }
  }
</script>
