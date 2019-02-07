<template>
  <v-container>
    <v-layout row wrap>
      <v-flex xs4>
        <v-img  v-bind:src="require('@/assets/logo.png')" width=300></v-img>
      </v-flex>
      <v-flex xs8>
        <p>
          En CAIDI (Centro de Atención Integral del Desarrollo Infantil) somos un equipo de especialistas experimentadas en el área de desarrollo infantil que trabajamos de manera transdisciplinaria en pro del bienestar biopsicosocial de cada uno de los niños que nos acompaña.
        </p>
        
        <p>
          Nos encontramos en un constante crecimiento profesional y trabajamos día a día para mantenernos en la vanguardia en lo que respecta al dominio de herramientas y técnicas que nos permitan brindar a cada una de las familias que nos acompañan los mejores resultados, en conjunto con la integración de los contextos familiar, escolar y terapéutico.
        </p>
        
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>

export default {
  name: 'quiensomos',
  components: {
  }
}
</script>
