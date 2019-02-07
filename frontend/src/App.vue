<template>
  <div id="app">
    <v-app v-bind:style="styleObject">
      <v-toolbar app color="primary" height=85 extension-height=50>
        <v-flex xs1>
          <v-img  v-bind:src="require('@/assets/logo-no-text.png')" width=80></v-img>
        </v-flex>
        <v-toolbar-title class="white--text">
          Centro de Atención Integral del Desarrollo Infantil
        </v-toolbar-title>
        <v-tabs slot="extension" centered fixed-tabs color="primary" dark>
          <v-tab id="tab-somos" to="/" > Quiénes somos </v-tab>
          <v-tab id="tab-vm" to="/vm" >  Misión y Visión </v-tab>
          <v-tab id="tab-serv" to="/serv" >  Servicios</v-tab>
          <v-tab id="tab-inst" to="/inst" >  Instalaciones</v-tab>
          <v-tab id="tab-ubic" to="/ubic" >  Ubicación</v-tab>
          <v-tab id="tab-citas" to="/citas" > Citas</v-tab>
          <v-tab id="tab-conta" to="/contacto" > Contacto</v-tab>
        </v-tabs>
      </v-toolbar>
      <v-content id="app-content">
          <router-view></router-view>
      </v-content>
      <v-footer dark height="auto">
        <v-card flat tile class="indigo lighten-1 white--text text-xs-center">
          <v-card-text>
            <!-- <v-btn
              v-for="icon in icons"
              :key="icon"
              class="mx-3 white--text"
              icon
            >
              <v-icon size="24px">{{ icon }}</v-icon>
            </v-btn> -->
          </v-card-text>

          <v-card-text class="white--text pt-0">
            Phasellus feugiat arcu sapien, et iaculis ipsum elementum sit amet. Mauris cursus commodo interdum. Praesent ut risus eget metus luctus accumsan id ultrices nunc. Sed at orci sed massa consectetur dignissim a sit amet dui. Duis commodo vitae velit et faucibus. Morbi vehicula lacinia malesuada. Nulla placerat augue vel ipsum ultrices, cursus iaculis dui sollicitudin. Vestibulum eu ipsum vel diam elementum tempor vel ut orci. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.
          </v-card-text>

          <v-divider></v-divider>

          <v-card-text class="white--text">
            &copy;2019 — <strong>CAIDI</strong>
          </v-card-text>
        </v-card>
      </v-footer>
    </v-app>
  </div>
</template>

<script>
import theme from './theme'
export default {
  data: () => ({
    styleObject:{
      backgroundColor: theme.secondary
    }
  })
}
</script>

<style lang="scss">
// #app {
//   font-family: 'Roboto', Helvetica, Arial, sans-serif;
//   -webkit-font-smoothing: antialiased;
//   -moz-osx-font-smoothing: grayscale;
//   color: #2c3e50;
// }

#app-content{
  min-height: 100vh;
  font-size: 16pt;
  text-align: justify;
}

</style>
