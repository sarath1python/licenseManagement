<template>
  <v-layout row justify-center>
    <v-dialog
      :value="dialog"
      max-width="800"
    >
      <v-card>
        <v-toolbar color="indigo lighten-1" dark>
          <v-toolbar-title>{{action}}</v-toolbar-title>
          <v-spacer></v-spacer>
          <v-toolbar-items>
            <v-btn
              flat="flat"
              @click="$emit('close')"
            ><v-icon>close</v-icon></v-btn>
          </v-toolbar-items>
        </v-toolbar>
        <v-form>
          <v-container>
            <v-layout row wrap>
              <v-flex v-for="(violation, idx) in violations" :key="violation.date" xs-3>
                <v-text-field
                  label="Date"
                  id="id"
                  v-model="violation.date"
                ></v-text-field>
                <v-text-field
                  label="Details"
                  id="id"
                  v-model="violation.details"
                ></v-text-field>
              </v-flex>
            </v-layout>
          </v-container>
        </v-form>
        <v-card-actions>
          <v-spacer></v-spacer>
          <template v-if="action == 'Edit violation'">
            <v-btn
            flat="flat"
            @click="updateViolation"
          >
            <v-icon>edit</v-icon>Save
          </v-btn>
          </template>
          <template v-if="action == 'Add violation'">
            <v-btn
            flat="flat"
            @click="createViolation"
          >
            <v-icon>add</v-icon>Add
          </v-btn>
          </template>
          <template v-if="action == 'Delete violation'">
            <v-btn
            flat="flat"
            @click="deleteViolation"
          >
            <v-icon>delete</v-icon>Delete
          </v-btn>
          </template>
          <v-btn
            flat="flat"
            @click="$emit('close')"
          >
            Cancel
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-layout>
</template>

<script>
  import violation from '@/services/violation'
  export default {
    data () {
      return {}
    },
    props: ['showViolation', 'violations', 'action'],
    computed: {
      dialog: function () {
        return this.showViolation
      }
    },
    methods: {
      createViolation () {
        violation.createViolation(this.violation).then((data) => {
            alert(data);
        });
      },
      updateViolation () {
        violation.updateViolation(this.violation).then((data) => {
            alert(data);
        });
      },
      deleteViolation () {
        violation.deleteViolation(this.violation).then((data) => {
            alert(data);
        });
      },
    }
  }
</script>