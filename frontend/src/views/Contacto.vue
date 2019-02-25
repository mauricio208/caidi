<template>
  <div class="contacto">
    <v-container grid-list-xs>
      <v-layout rpw wrap align-center
          justify-center>
          <p>En caso de que ud. requiera información adicional, lo invitamos a contactarnos a través de los siguientes medios:</p>
          <v-flex xs4 ma-3>
            
            <v-container>
              <v-layout justify-space-around column fill-height id="mvtext">
                <div>
                  <v-card>
                    <v-card-text>
                      <v-icon color="tertiary" size=80>fas fa-envelope</v-icon><p>Correo:</p>
                      <span class="font-weight-light">
                          terapiascaidi@gmail.com
                      </span>
                    </v-card-text>
                  </v-card>
                </div>
              </v-layout>
            </v-container>
          </v-flex>
          <v-flex xs4 ma-3>
            
            <v-container>
              <v-layout justify-space-around column fill-height id="mvtext">
                <div>
                  <v-card>
                    <v-card-text>
                      <v-icon color="tertiary" size=80>fab fa-instagram</v-icon>
                      <p>Instagram:</p>
                      <span class="font-weight-light">
                         @centrocaidi
                      </span>
                    </v-card-text>
                  </v-card>
                </div>
              </v-layout>
            </v-container>
          </v-flex>
          <v-flex xs4 ma-3>
            
              <v-container>
                <v-layout justify-space-around column fill-height id="mvtext">
                  <div>
                    <v-card>
                      <v-card-text>
                        <v-icon color="tertiary" size=80>fas fa-phone</v-icon>
                        <p>Teléfonos:</p>
                        <span class="font-weight-light">
                            <span>0424 8175669</span><br>
                            <span>0412 5747165</span>
                        </span>
                      </v-card-text>
                    </v-card>
                  </div>
                </v-layout>
              </v-container>
          </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>

export default {
  name: 'contacto',
  components: {
  }
}
</script>
