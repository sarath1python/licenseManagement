<template>
    <v-content>
      <v-container fluid>
        <v-layout align-center justify-center>
          <v-flex xs12 sm8 md5>
            <v-card class="elevation-12">
              <v-toolbar dark color="indigo">
                  <v-toolbar-title>Login</v-toolbar-title>
              </v-toolbar>
            
            <v-card-text>
              <v-form
                ref="form"
                v-model="valid"
                lazy-validation>

                <v-text-field
                  prepend-icon="person"
                  v-model="name"
                  :rules="nameRules"
                  label="Username"
                  required
                >
                </v-text-field>

                <v-text-field
                  prepend-icon="lock"
                  v-model="password"
                  :rules="passwordRules"
                  label="Password"
                  type="password"
                  required
                >
                </v-text-field>
                <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn
                  color="indigo"
                  @click="validate"
                  dark
                >Login
                </v-btn>
                <v-spacer></v-spacer>
                </v-card-actions>
              </v-form>
            </v-card-text>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
    </v-content> 
</template>

<script>
  export default {
    data: () => ({
      valid: true,
      username: '',
      nameRules: [
        v => !!v || 'Name is required',
      ],
      password: '',
      passwordRules: [
        v => !!v || 'Password is required',
      ]
    }),

    methods: {
      validate () {
       
      },
    }
  }
</script>