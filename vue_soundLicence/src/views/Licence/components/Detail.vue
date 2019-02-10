<template>
  <v-layout row justify-center>
    <v-dialog
      :value="dialog"
      max-width="800"
    >
      <v-card>
        <v-toolbar color="indigo lighten-1" dark>
          <v-toolbar-title>{{action}} Licence</v-toolbar-title>
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
              <v-flex xs6>
                <v-text-field
                  label="Licencee name"
                  id="id"
                  v-model="licence.name"
                ></v-text-field>
              </v-flex>
              <v-flex xs6>
                <v-text-field
                  label="Licence number"
                  id="id"
                  v-model="licence.number"
                ></v-text-field>
              </v-flex>
              <v-flex xs12 md4>
                <v-text-field
                  label="Serial number"
                  id="id"
                  v-model="licence.serial_number"
                ></v-text-field>
              </v-flex>
              <v-flex xs12 md4>
                <v-text-field
                  label="Licence status"
                  id="id"
                  v-model="licence.status"
                ></v-text-field>
              </v-flex>
              <v-flex xs12 md4>
                <v-text-field
                  label="Date of issue"
                  id="id"
                  v-model="licence.issued_date"
                ></v-text-field>
              </v-flex>
              <v-flex xs12>
                <v-text-field
                  label="Details"
                  id="id"
                  v-model="licence.details"
                ></v-text-field>
              </v-flex>
              <v-flex xs12 v-if="licence.violations.length > 0">
                <h4>Violations</h4>
              </v-flex>
              <v-flex v-for="(violation, idx) in licence.violations" :key="violation.date" xs-3>
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
          <template v-if="action == 'Edit'">
            <v-btn
            flat="flat"
            @click="updateLicence"
          >
            <v-icon>edit</v-icon>Save
          </v-btn>
          </template>
          <template v-if="action == 'Add'">
            <v-btn
            flat="flat"
            @click="createLicence"
          >
            <v-icon>add</v-icon>Add
          </v-btn>
          </template>
          <template v-if="action == 'Delete'">
            <v-btn
            flat="flat"
            @click="deleteLicence"
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
  import licence from '@/services/licence'
  export default {
    data () {
      return {}
    },
    props: ['showdetails', 'licence', 'action'],
    computed: {
      dialog: function () {
        return this.showdetails
      }
    },
    methods: {
      createLicence () {
        licence.createLicence(this.licence).then((data) => {
            alert(data);
        });
      },
      updateLicence () {
        licence.updateLicence(this.licence).then((data) => {
            alert(data);
        });
      },
      deleteLicence () {
        licence.deleteLicence(this.licence).then((data) => {
            alert(data);
        });
      },
    }
  }
</script>