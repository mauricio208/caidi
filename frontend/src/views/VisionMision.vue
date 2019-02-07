<template>
  <v-container>
    <v-parallax v-bind:src="require('@/assets/fondo2.jpg')" height=400>
      <v-container>      
        <v-layout justify-space-around column fill-height id="mvtext">
          <div>
            <p>Misión</p>
            <span class="font-weight-light">
                Brindar apoyo, asesoramiento y atención terapéutico integral a la población infantil y sus familias
            </span>
          </div>
          <v-divider dark></v-divider>
          <div>
            <p>Visión</p>
            <span class="font-weight-light">
                Ser un grupo de profesionales en constante expansión y fortalecimiento profesional que constituya la opción preferida por las familias en lo que respecta a atención terapéutica infantil, asesoramiento y formación
            </span>
          </div>
          <!-- <v-card color="transparent" class="white--text">
              <v-card-title primary-title>
                <div>
                  <div class="headline">Mision</div>
                </div>
              </v-card-title>
              <v-card-text>
              <span class="font-weight-light">
                Brindar apoyo, asesoramiento y atención terapéutico integral a la población infantil y sus familias
              </span>
              </v-card-text>
          </v-card>
          <v-card color="transparent" class="white--text">
              <v-card-title primary-title>
                <div>
                  <div class="headline">Visión</div>
                </div>
              </v-card-title>
              <v-card-text>
              <span class="font-weight-light">
                Ser un grupo de profesionales en constante expansión y fortalecimiento profesional que constituya la opción preferida por las familias en lo que respecta a atención terapéutica infantil, asesoramiento y formación
              </span>
                
              </v-card-text>
          </v-card> -->
        </v-layout>
      </v-container>
    </v-parallax>
  </v-container>
</template>

<style lang="scss">
  #mvtext{
    text-align: center;
  }
</style>

<script>

export default {
  name: 'ubicacion',
  components: {
  }
}
</script>


