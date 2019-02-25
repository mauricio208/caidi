<template>
  <div id="app">
    <v-app v-bind:style="styleObject">
      <v-toolbar app color="primary" height=110 extension-height=50 scroll-off-screen scroll-threshold=30>
        <v-flex xs1>
          <v-img  v-bind:src="require('@/assets/logo.png')" width=80></v-img>
        </v-flex>
        <v-toolbar-title class="white--text page-title">
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
        <v-flex xs12>
          <v-card flat tile class="indigo lighten-1 white--text text-xs-center">
            <v-layout
              justify-center
              row
              wrap
            >
              <v-card-text>
                <v-btn icon><v-icon>fas fa-envelope</v-icon></v-btn>
                terapiascaidi@gmail.com
                <v-btn
                  href='https://www.instagram.com/centrocaidi/'
                  class="mx-3 white--text"
                  icon
                >
                  <v-icon  size="24px">fab fa-instagram</v-icon>
                </v-btn>
              </v-card-text>
              <v-flex xs12>
              <v-divider></v-divider>
                
              </v-flex>
              <v-flex xs6>
                <v-card-text class="white--text">
                    <v-btn color="tertiary" id="tab-somos" to="/" > Quiénes somos </v-btn>
                    <v-btn color="tertiary" id="tab-vm" to="/vm" >  Misión y Visión </v-btn>
                    <v-btn color="tertiary" id="tab-serv" to="/serv" >  Servicios</v-btn>
                    <v-btn color="tertiary" id="tab-inst" to="/inst" >  Instalaciones</v-btn>
                    <v-btn color="tertiary" id="tab-ubic" to="/ubic" >  Ubicación</v-btn>
                    <v-btn color="tertiary" id="tab-citas" to="/citas" > Citas</v-btn>
                    <v-btn color="tertiary" id="tab-conta" to="/contacto" > Contacto</v-btn>
                </v-card-text>
              </v-flex>
              <v-flex xs6>
                <v-card-text class="white--text">
                    <v-icon color="tertiary" size=20>fas fa-phone</v-icon>
                    ¿Estas interesado en hablar directamente con nosotros?, contactanos a los siguientes numeros:
                    <span class="font-weight-light">
                        <span>0424 8175669</span><br>
                        <span>0412 5747165</span>
                    </span>

                </v-card-text>
              </v-flex>

              <v-divider></v-divider>

              <v-card-text class="white--text">
                &copy;2019 — <strong>CAIDI</strong>
              </v-card-text>
            </v-layout>
          </v-card>  
        </v-flex>
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
#app {
  font-family: 'Roboto', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

.page-title {
  font-family: 'Noto Serif';
  font-style: italic;
}

#app-content{
  min-height: 100vh;
  font-size: 14pt;
  text-align: justify;
}

</style>
