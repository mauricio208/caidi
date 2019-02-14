<template>
  <v-container fill-height>
    <v-layout column wrap>
      <v-layout align-center justify-space-around row >
        <v-flex xs4 align-self-center px-3>
          <v-img  v-bind:src="require('@/assets/logo.png')" max-width=400 ></v-img>
        </v-flex>
        <v-flex xs8>
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
                  <img v-bind:src="require('@/assets/'+t.avatar)" alt="alt">
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
      {id: 1, nombre: 'Barbara Rojas', rol:'Terapeuta Ocupacional', descripcion:'Phasellus feugiat arcu sapien, et iaculis ipsum elementum sit amet. Mauris cursus commodo interdum. Praesent ut risus eget metus luctus accumsan id ultrices nunc. Sed at orci sed massa consectetur dignissim a sit amet dui. Duis commodo vitae velit et faucibus. Morbi vehicula lacinia malesuada. Nulla placerat augue vel ipsum ultrices, cursus iaculis dui sollicitudin. Vestibulum eu ipsum vel diam elementum tempor vel ut orci. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.', avatar:'fondo2.jpg'},
      {id: 2, nombre: 'Barbara Rojas', rol:'Terapeuta Ocupacional', descripcion:'Phasellus feugiat arcu sapien, et iaculis ipsum elementum sit amet. Mauris cursus commodo interdum. Praesent ut risus eget metus luctus accumsan id ultrices nunc. Sed at orci sed massa consectetur dignissim a sit amet dui. Duis commodo vitae velit et faucibus. Morbi vehicula lacinia malesuada. Nulla placerat augue vel ipsum ultrices, cursus iaculis dui sollicitudin. Vestibulum eu ipsum vel diam elementum tempor vel ut orci. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.', avatar:'fondo2.jpg'},
      {id: 3, nombre: 'Barbara Rojas', rol:'Terapeuta Ocupacional', descripcion:'Phasellus feugiat arcu sapien, et iaculis ipsum elementum sit amet. Mauris cursus commodo interdum. Praesent ut risus eget metus luctus accumsan id ultrices nunc. Sed at orci sed massa consectetur dignissim a sit amet dui. Duis commodo vitae velit et faucibus. Morbi vehicula lacinia malesuada. Nulla placerat augue vel ipsum ultrices, cursus iaculis dui sollicitudin. Vestibulum eu ipsum vel diam elementum tempor vel ut orci. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.', avatar:'fondo2.jpg'},
      {id: 4, nombre: 'Barbara Rojas', rol:'Terapeuta Ocupacional', descripcion:'Phasellus feugiat arcu sapien, et iaculis ipsum elementum sit amet. Mauris cursus commodo interdum. Praesent ut risus eget metus luctus accumsan id ultrices nunc. Sed at orci sed massa consectetur dignissim a sit amet dui. Duis commodo vitae velit et faucibus. Morbi vehicula lacinia malesuada. Nulla placerat augue vel ipsum ultrices, cursus iaculis dui sollicitudin. Vestibulum eu ipsum vel diam elementum tempor vel ut orci. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.', avatar:'fondo2.jpg'},
      {id: 5, nombre: 'Barbara Rojas', rol:'Terapeuta Ocupacional', descripcion:'Phasellus feugiat arcu sapien, et iaculis ipsum elementum sit amet. Mauris cursus commodo interdum. Praesent ut risus eget metus luctus accumsan id ultrices nunc. Sed at orci sed massa consectetur dignissim a sit amet dui. Duis commodo vitae velit et faucibus. Morbi vehicula lacinia malesuada. Nulla placerat augue vel ipsum ultrices, cursus iaculis dui sollicitudin. Vestibulum eu ipsum vel diam elementum tempor vel ut orci. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.', avatar:'fondo2.jpg'}
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
