<template>
  <v-layout row justify-center>
    <v-dialog
      :value="dialog"
      max-width="800"
    >
      <v-card>
        <v-toolbar color="indigo lighten-1" dark>
          <v-toolbar-title v-model="licencee_name"></v-toolbar-title>
          <v-toolbar-title v-model="licencee_number"></v-toolbar-title>
          <v-spacer></v-spacer>
          <v-toolbar-items>
            <v-btn
              flat="flat"
              @click="$emit('close')"
            ><v-icon>close</v-icon>close</v-btn>
          </v-toolbar-items>
        </v-toolbar>
        <v-form>
          <v-container>
            <v-layout row wrap>
              <v-flex xs12 md4>
                <v-text-field
                  label="Serial number"
                  id="id"
                  v-model="serial_number"
                ></v-text-field>
              </v-flex>
              <v-flex xs12 md4>
                <v-text-field
                  label="Licence status"
                  id="id"
                  v-model="licence_status"
                ></v-text-field>
              </v-flex>
              <v-flex xs12 md4>
                <v-text-field
                  label="Date of issue"
                  id="id"
                  v-model="issued_date"
                ></v-text-field>
              </v-flex>
              <v-flex xs12>
                <v-text-field
                  label="Details"
                  id="id"
                  v-model="details"
                ></v-text-field>
              </v-flex>
              <v-flex xs12>
                <h4>Violations</h4>
              </v-flex>
              <v-flex v-for="(violation, idx) in violations" :key="violation.date" xs-3>
                <v-card>
                  <v-card-title primary-title>
                    {{violation.date}}
                  </v-card-title>
                  <v-card-text class="p-0">
                    {{violation.details}}
                  </v-card-text>
                </v-card>
              </v-flex>
            </v-layout>
          </v-container>
        </v-form>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            flat="flat"
            @click="$emit('close')"
          >
            Close
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-layout>
</template>

<script>
  export default {
    data () {
      return {
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
    props: ['showdetails'],
    computed: {
      dialog: function () {
        return this.showdetails
      }
    }

  }
</script>