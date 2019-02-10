<template>
  <div>
    <v-container fluid grid-list-lg text-xs-center>
      <v-layout row wrap>
        <LicenceBlocks />

        <v-flex xs12>
          <v-layout row wrap>
            <v-flex xs6>
              <LicenceExpiry />
              <LicenceVerification class="mt-2 mb-5"/>
            </v-flex>
            <v-flex xs6>
              <LicenceDistribution />
            </v-flex>
          </v-layout>
        </v-flex>

      </v-layout>
    </v-container>
  </div>
</template>

<script>
  import LicenceBlocks from './components/LicenceBlocks'
  import LicenceExpiry from './components/LicenceExpiry'
  import LicenceVerification from './components/LicenceVerification'
  import LicenceDistribution from './components/LicenceDistribution'

  export default {
    components: {
      LicenceBlocks,
      LicenceExpiry,
      LicenceVerification,
      LicenceDistribution
    }
  }
</script>
