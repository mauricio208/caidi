<template>
  <div class="contacto">
    <v-container grid-list-xs>
      <v-layout rpw wrap align-center
          justify-center>
          <p>En caso de que ud. requiera información adicional, lo invitamos a contactarnos a través de los siguientes medios:</p>
          <v-parallax v-bind:src="require('@/assets/images/contacto/email.jpg')" height=200>
            <v-container>
              <v-layout justify-space-around column fill-height id="mvtext">
                <div>
                  <v-card>
                    <v-card-text>
                      <p>Correo:</p>
                      <span class="font-weight-light">
                          asjdasd@askjfdhsfd.com
                      </span>
                    </v-card-text>
                  </v-card>
                </div>
              </v-layout>
            </v-container>
          </v-parallax>
          <v-parallax v-bind:src="require('@/assets/images/contacto/instagram.jpg')" height=200>
            <v-container>
              <v-layout justify-space-around column fill-height id="mvtext">
                <div>
                  <v-card>
                    <v-card-text>
                      <p>Instagram:</p>
                      <span class="font-weight-light">
                          asjdasd@askjfdhsfd.com
                      </span>
                    </v-card-text>
                  </v-card>
                </div>
              </v-layout>
            </v-container>
          </v-parallax>
          <v-parallax v-bind:src="require('@/assets/images/contacto/cell.jpg')" height=200>
            <v-container>
              <v-layout justify-space-around column fill-height id="mvtext">
                <div>
                  <v-card>
                    <v-card-text>
                      <p>Teléfonos:</p>
                      <span class="font-weight-light">
                          <span>0400 - 000 00 00</span><br>
                          <span>0400 - 000 00 00</span>
                          
                          
                      </span>
                    </v-card-text>
                  </v-card>
                </div>
              </v-layout>
            </v-container>
          </v-parallax>
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
