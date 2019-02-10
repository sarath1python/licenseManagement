<template>
    <v-container>
    <v-layout align-center justify-center>
        <v-form
    ref="form"
    v-model="valid"
    lazy-validation
  >
    <v-text-field
      v-model="username"
      :rules="usernameRules"
      label="Username"
      required
    ></v-text-field>

    <v-text-field
      v-model="password"
      :rules="passwordRules"
      label="Password"
      type="password"
      required
    ></v-text-field>
      </v-form>
    </v-layout>
    <v-layout align-center justify-center>
            <v-flex xs6>
                <div class="text-xs-center">
                    <v-btn
                        absolute-center
                        color="success"
                        dark
                        @click="validateAndLogin"
                    >
                    Login
                    </v-btn>
                </div>
            </v-flex>
    </v-layout>
  </v-container>
</template>


<script>
  export default {
    data: () => ({
      valid: true,
      username:"",
      password:"",
      usernameRules: [
        v => !!v || 'Username is required',
      ],
      passwordRules: [
        v => !!v || 'Password is required',
      ]
    }),
    methods: {
      validateAndLogin () {
          if(this.username != "" && this.password != "") {
              if(this.username == this.$store.state.sampleUserData.name && this.password == this.$store.state.sampleUserData.password)
                {   
                     Promise.all([
                        this.$store.dispatch('loggIn',this.username),
                    ]).then(() => {
                    });
                }
              this.$router.replace({ name: "dashboard" });
            }
          else {}
      }
    }
  }
</script>