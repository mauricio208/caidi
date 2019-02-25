<template>
  <v-container fill-height>
    <v-layout column wrap>
      <v-layout align-center justify-space-around row >
        <v-flex xs7 align-self-center px-3>
          <v-carousel hide-delimiters>
            <v-carousel-item
              v-for="(item,i) in carouselImages"
              :key="i"
              :src="item.src"
            ></v-carousel-item>
          </v-carousel>
        </v-flex>
        <v-flex xs5>
          <v-card id='quienesomostext' elevation=24 class="font-weight-light">
            <v-card-text >
              <p>
                En CAIDI (Centro de Atención Integral del Desarrollo Infantil) somos un equipo de especialistas experimentadas en el área de desarrollo infantil que trabajamos de manera transdisciplinaria en pro del bienestar biopsicosocial de cada uno de los niños que nos acompaña.
              </p>
              <p>
                Nos encontramos en un constante crecimiento profesional y trabajamos día a día para mantenernos en la vanguardia en lo que respecta al dominio de herramientas y técnicas que nos permitan brindar a cada una de las familias que nos acompañan los mejores resultados, en conjunto con la integración de los contextos familiar, escolar y terapéutico.
              </p>
              
            </v-card-text>
            
          </v-card>
        </v-flex>
      </v-layout>
      <v-layout align-center justify-space-around row wrap ma-5>
        <v-flex xs12 ma-5>
          <h3>Nuestro Equipo</h3>
        </v-flex>
        <v-flex xs5 ma-3
          v-for="t in equipo"
          v-bind:key="t.id"
          v-bind:t="t"
        >
          <v-card flat color="transparent">
            <v-layout>
                <v-avatar
                  :size="90"
                >
                  <img v-bind:src="t.avatar" alt="alt">
                </v-avatar>
              <v-flex xs7>
                <v-card-title primary-title>
                  <div>
                    <div class="headline">{{t.nombre}}</div>
                    <div class="subheading ">{{t.rol}}</div>
                  </div>
                </v-card-title>
              </v-flex>
            </v-layout>
            <v-divider light></v-divider>
            <v-card-text class="body-1">
              {{t.descripcion}}
            </v-card-text>
          </v-card>
        </v-flex>
        
      </v-layout>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  name: 'quiensomos',
  data: ()=> ({
    equipo:[
      {id: 1, nombre: 'Barbara Rojas', rol:'Terapeuta Ocupacional', descripcion:'Diplomado en psicomotricidad, Diplomado en alteraciones del desarrollo infantil, Certificación en Estimulación Temprana, Certificación en ABA Tech. Especialista en grafomotricidad', avatar:require('@/assets/images/quienesomos/stephy.jpg')},
      {id: 2, nombre: 'Anly Mata', rol:'Psicólogo Clínico', descripcion:'Especialista en descarte de autismo y modificación conductual', avatar:require('@/assets/images/quienesomos/anly.jpg')},
      {id: 3, nombre: 'Alejandra Hernandez', rol:'Terapeuta de lenguaje', descripcion:' Lic en educ. Especial. Msc en modificación de conducta,Diplomado: estimulación temprana Autismo. Trastornos del Desarrollo. Modificación de Conducta, Certificación en Escuela para Padres', avatar:require('@/assets/images/quienesomos/no-avatar.jpg')},
      {id: 4, nombre: 'Belkis Pernía C.', rol:'Terapeuta Ocupacional', descripcion:'Psicopedagoga. Educación Especial, Dificultades del Aprendizaje.\nProfesora de Educación Integral.\nMagíster Scientiarium en Tecnología Educativa.\nDiplomado en T.E.Autista.', avatar:require('@/assets/images/quienesomos/belkys.jpg')},
      {id: 5, nombre: 'Hilvic Garcia', rol:'Terapeuta Ocupacional', descripcion:'Diplomado en autismo Universidad Monteavila, Instructora certificada en masaje infantil, Certificación en Integración Sensorial', avatar:require('@/assets/images/quienesomos/hilvic.jpg')},
    ],
    carouselImages: [
      {src:require('@/assets/images/quienesomos/carousel/cr1.jpg')},
      {src:require('@/assets/images/quienesomos/carousel/cr2.jpg')},
      {src:require('@/assets/images/quienesomos/carousel/cr4.jpg')},
      {src:require('@/assets/images/quienesomos/carousel/cr5.jpg')},
      {src:require('@/assets/images/quienesomos/carousel/cr6.jpg')},
      {src:require('@/assets/images/quienesomos/carousel/cr7.jpg')},
    ]
  })
}
</script>

<style lang="scss" scoped>
#quienesomostext{
  border-radius: 25px;
  border-style: solid;
  border-width: 8px;
  // border-color: #42A5F5;
}
</style>
