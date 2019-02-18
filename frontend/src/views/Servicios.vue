<template>
  <div id="servicios">
    <v-container>
      <v-layout >
        <v-flex xs12>
          <v-expansion-panel popout mx-4>
            <v-expansion-panel-content v-bind:style="panelStyle" >
              <div slot="header" class="panel-title">Terapia ocupacional</div>
              <v-card>
                <v-flex xs12 v-bind:style="panelStyle">
                  <v-img  v-bind:src="require('@/assets/fondo2.jpg')" max-height=200></v-img>
                </v-flex>
                <v-card-text class="font-weight-light descripciones" v-bind:style="panelStyle" >
                  Esta disciplina se encarga del abordaje de todas aquellas dificultades que se encuentren interfiriendo en el correcto desempeño del niño dentro de sus contextos ocupacionales, ya sean estos relacionados al juego, al funcionamiento en el hogar o al colegio. Nuestros especialistas en el área brindan evaluación y abordaje en las áreas de desarrollo motor grueso y fino, procesamiento sensorial, coordinación, planificación y organización, tareas de cuidado personal, adquisición y aprendizaje de la escritura (Grafomotricidad)
                </v-card-text>
                <v-card-actions>
                  <v-btn flat color="accent" to='/citas'>Solicitar cita</v-btn>
                </v-card-actions>

              </v-card>
            </v-expansion-panel-content>
            <v-expansion-panel-content v-bind:style="panelStyle" >
              <div slot="header" class="panel-title">Terapia de lenguaje</div>
              <v-card>
                <v-flex xs12 v-bind:style="panelStyle">
                  <v-img  v-bind:src="require('@/assets/fondo2.jpg')" max-height=200></v-img>
                </v-flex>
                <v-card-text class="font-weight-light descripciones" v-bind:style="panelStyle" >
                  Es la disciplina encargada del tratamiento de la disfunción, retardos en la adquisición o problemas relacionados al habla, la voz y la comunicación. Nuestros especialistas en el área buscan potenciar al máximo las habilidades de comunicación del niño, valiéndose para ello de la integración de las estructuras neurológicas, psicológicas, lingüísticas y sociales
                </v-card-text>
                <v-card-actions>
                  <v-btn flat color="accent" to='/citas'>Solicitar cita</v-btn>
                </v-card-actions>

              </v-card>
            </v-expansion-panel-content>
            <v-expansion-panel-content v-bind:style="panelStyle" >
              <div slot="header" class="panel-title">Terapia de conducta</div>
              <v-card>
                <v-flex xs12 v-bind:style="panelStyle">
                  <v-img  v-bind:src="require('@/assets/fondo2.jpg')" max-height=200></v-img>
                </v-flex>
                <v-card-text class="font-weight-light descripciones" v-bind:style="panelStyle" >
                  Es la rama de la psicología que se encarga de la reducción de problemas conductuales y  la adquisición de habilidades de adaptación a través del análisis funcional del comportamiento. Nuestros especialistas en el área intervienen en situaciones tales como: Dificultades para adaptarse al colegio o socializar, presencia de berrinches, conductas agresivas, ansiedad o temor excesivo a determinados estímulos, ausencia de repertorios conductuales básicos, necesidades de autocontrol, etc. Además, ofrecen herramientas y entrenamiento a padres y docentes para controlar las conductas inadecuadas
                </v-card-text>
                <v-card-actions>
                  <v-btn flat color="accent" to='/citas'>Solicitar cita</v-btn>
                </v-card-actions>

              </v-card>
            </v-expansion-panel-content>
            <v-expansion-panel-content v-bind:style="panelStyle" >
              <div slot="header" class="panel-title">Psicopedagogía</div>
              <v-card>
                <v-flex xs12 v-bind:style="panelStyle">
                  <v-img  v-bind:src="require('@/assets/fondo2.jpg')" max-height=200></v-img>
                </v-flex>
                <v-card-text class="font-weight-light descripciones" v-bind:style="panelStyle" >
                  Esta disciplina se encarga del estudio, evaluación y tratamiento de los comportamientos relacionados al área de enseñanza y aprendizaje. Nuestros especialistas se encargan de aspectos tales como: manejo de problemas de aprendizaje, enseñanza de habilidades de lectoescritura y cálculo, apoyo en dificultades del aprendizaje, refuerzo académico, adaptación de currículums escolares, etc
                </v-card-text>
                <v-card-actions>
                  <v-btn flat color="accent" to='/citas'>Solicitar cita</v-btn>
                </v-card-actions>

              </v-card>
            </v-expansion-panel-content>
            <v-expansion-panel-content v-bind:style="panelStyle" >
              <div slot="header" class="panel-title">Baby Gym</div>
              <v-card>
                <v-flex xs12 v-bind:style="panelStyle">
                  <v-img  v-bind:src="require('@/assets/fondo2.jpg')" max-height=200></v-img>
                </v-flex>
                <v-card-text class="font-weight-light descripciones" v-bind:style="panelStyle" >
                  La estimulación temprana es el proceso que se lleva a cabo en el período comprendido entre los 30 días de nacido y los 3 años de edad, con la finalidad de brindar al niño oportunidades de desarrollo físico, intelectual y social; que le permiten el logro o el mejoramiento de habilidades aprovechándose de el proceso de interconexión sináptica que tiene lugar en esos primeros días y que resulta fundamental para la determinación de capacidades futuras. En nuestro Baby Gym, nos centramos en la aplicación de estimulación temprana, ya sea esta de tipo intervencional (Aplicada a bebés y niños que presenten retardo en alguna de sus áreas del desarrollo o se presuma que pueden llegar a tenerlo por condiciones propias de su nacimiento, antecedentes, etc.) o preventiva (Aplicada a niños sanos cuyas madres deseen aprender a estimular canalizadamente, acompañar durante su proceso de desarrollo, reforzar vínculos afectivos, etc.)
                </v-card-text>
                <v-card-actions>
                  <v-btn flat color="accent" to='/citas'>Solicitar cita</v-btn>
                </v-card-actions>

              </v-card>
            </v-expansion-panel-content>
            <v-expansion-panel-content v-bind:style="panelStyle" >
              <div slot="header" class="panel-title">Asesoría Familiar</div>
              <v-card>
                <v-flex xs12 v-bind:style="panelStyle">
                  <v-img  v-bind:src="require('@/assets/fondo2.jpg')" max-height=200></v-img>
                </v-flex>
                <v-card-text class="font-weight-light descripciones" v-bind:style="panelStyle" >
                  En CAIDI sabemos que el ser padres no es una tarea fácil y que en ocasiones, se requiere de un guía en el proceso para solventar exitosamente situaciones determinadas. Es por ello, que ofrecemos asesorías familiares para solventar dudas, apoyar en procesos post diagnósticos, orientar en procesos de crianza, brindar acompañamiento en procesos de escolarización y/o ofrecer herramientas de trabajo desde el hogar
                </v-card-text>
                <v-card-actions>
                  <v-btn flat color="accent" to='/citas'>Solicitar cita</v-btn>
                </v-card-actions>

              </v-card>
            </v-expansion-panel-content>
            <v-expansion-panel-content v-bind:style="panelStyle" >
              <div slot="header" class="panel-title">Grupos de habilidades sociales</div>
              <v-card>
                <v-flex xs12 v-bind:style="panelStyle">
                  <v-img  v-bind:src="require('@/assets/fondo2.jpg')" max-height=200></v-img>
                </v-flex>
                <v-card-text class="font-weight-light descripciones" v-bind:style="panelStyle" >
                  Las habilidades sociales son el conjunto de destrezas que permitan al niño mantener una comunicación asertiva y exitosa con el entorno que le rodea. Ofrecemos la posibilidad de trabajar en la adquisición y desarrollo de dichas habilidades, fortaleciendo a la vez el autoestima, el liderazgo y el sentido de compañerismo
                </v-card-text>
                <v-card-actions>
                  <v-btn flat color="accent" to='/citas'>Solicitar cita</v-btn>
                </v-card-actions>

              </v-card>
            </v-expansion-panel-content>
          </v-expansion-panel>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
import theme from '@/theme'
export default {
  name: 'servicios',
  data: () => ({
    panelStyle: {
      backgroundColor: theme.accent,
      color: 'white'
    }
  })
}
</script>
<style lang="scss">
  .descripciones{
    text-align: justify;
  }
</style>
