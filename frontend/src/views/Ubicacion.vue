<template>
  <v-container grid-list-xs>
    <v-layout column wrap fill-height
          align-center
          justify-center>
      <v-flex xs1>
        <p>Estamos ubicados dentro de los espacios del "Preescolar Tulipan" en Calle Cubagua, Edif. Tulipan, Macaracuay, Caracas.</p>
      </v-flex>
      <v-flex xs12 >
        <v-layout
          slot="placeholder"
          fill-height
          align-center
          justify-center
          ma-0
        >
          <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3923.4448135296825!2d-66.82212498577702!3d10.465557392532924!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8c2a5819dfb586d7%3A0xd1eb942569669bc9!2sPreescolar+Tulipan!5e0!3m2!1ses!2sve!4v1549325398991" width="600" height="450" frameborder="0" style="border:0" allowfullscreen></iframe>
          <!-- <v-progress-circular 
            indeterminate color="white lighten-5"
            :size="100"
            :width="10"
            :position="absolute"
          ></v-progress-circular> -->
        </v-layout>        
      </v-flex>
    </v-layout>
  </v-container>
  
</template>

<script>

export default {
  name: 'ubicacion',
  components: {
  }
}
</script>
