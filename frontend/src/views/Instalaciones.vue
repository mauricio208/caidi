<template>
  <div class="instalaciones">
    <v-container grid-list-xs>
    <v-layout column>
      <v-flex xs1>
        <p>Te invitamos a conocer nuestras instalaciones, lugares donde día a día trabajamos en pro del bienestar y el logro de los objetivos de nuestros niños</p>
      </v-flex>
      
      <v-flex xs12 sm6>
        <v-container grid-list-sm fluid>
          <v-layout row wrap>
            <v-flex
              v-for="i in instalaciones"
              :key="i.id"
              xs4
              d-flex
            >
              <v-card flat tile class="d-flex">
                <v-img
                  :src="i.src"
                  aspect-ratio="1"
                  class="grey lighten-2"
                  @click="openImg(i.src)"
                >
                  <v-layout
                    slot="placeholder"
                    fill-height
                    align-center
                    justify-center
                    ma-0
                  >
                    <v-progress-circular indeterminate color="grey lighten-5"></v-progress-circular>
                  </v-layout>
                </v-img>
              </v-card>
            </v-flex>
          </v-layout>
        </v-container>
        
    </v-flex>
    <v-dialog
      v-model="imgDialog"
      scrollable 
      :overlay="false"
      max-width="500px"
      transition="dialog-transition"
    >
      <v-card-media
        
        height="auto"
        :src="largeImg"
      >
      </v-card-media>
    </v-dialog>
    </v-layout>
</v-container>
  </div>
</template>

<script>

export default {
  name: 'instalaciones',
  data: ()=> ({
    imgDialog: false,
    largeImg: '',
    instalaciones:[
      {id:1, src:require('@/assets/images/instalaciones/in1.jpeg')},
      {id:1, src:require('@/assets/images/instalaciones/in3.jpeg')},
      {id:1, src:require('@/assets/images/instalaciones/in4.jpeg')},
      {id:1, src:require('@/assets/images/instalaciones/in5.jpeg')},
      {id:1, src:require('@/assets/images/instalaciones/in6.jpeg')},      
    ]
  }),
  methods: {
    openImg(imgSrc){
      this.largeImg = imgSrc
      this.imgDialog = true;
    }
  }
}
</script>
