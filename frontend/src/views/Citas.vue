<template>
  <div class="citas">
    
    <v-container grid-list-xs>
      <v-layout column wrap align-center
          justify-center>
          <p>En pro de ofrecerle siempre la mejor atención, nuestros servicios son brindados previa cita, si desea concretar una cita de evaluación, le invitamos a hacerlo a través del siguiente formulario</p>
          <v-form
          ref="citaForm"
          v-model="valid"
          lazy-validation
          >
            <v-layout wrap>
              <v-flex xs6>
                <v-text-field
                v-model="formData.parent_name"
                outline
                :rules="nameRules"
                label="Nombre completo del representante"
                required
                ></v-text-field>
              </v-flex>
              <v-flex xs6>
                <v-text-field
                v-model="formData.pacient_name"
                outline
                :rules="nameRules"
                label="Nombre del representado"
                required
                ></v-text-field>
              </v-flex>
              <v-flex xs6>
                <v-text-field
                v-model="formData.email"
                outline
                :rules="emailRules"
                label="E-mail de contacto"
                required
                ></v-text-field>
              </v-flex>
              <v-flex xs6>
                <v-text-field
                v-model="formData.phone_number"
                outline
                :rules="[v=> !!v]"
                label="Número telefonico de contacto"
                required
                ></v-text-field>
              </v-flex>

              <v-flex xs2>
                <v-text-field
                v-model="formData.pacient_age"
                outline
                :rules="ageRules"
                type='number'
                label="Edad del representado"
                required
                ></v-text-field>
              </v-flex>
              <v-flex xs8>
                <v-select
                v-model="formData.therapy_field"
                :items="especialidades"
                outline
                :rules="[v => !!v || 'Campo requerido']"
                label="Especialidad por la que solicita la cita"
                required
                ></v-select>
              </v-flex>
              <v-flex xs2>
                <v-select
                v-model="formData.time_preference"
                :items="turnos"
                outline
                :rules="[v => !!v || 'Campo requerido']"
                label="Turno de preferencia"
                required
                ></v-select>                
              </v-flex>
              
              <v-flex xs12>
                <div class="text-xs-center">
                  <v-btn
                  :disabled="!valid"
                  large
                  @click="validate"
                  color="success"
                  >
                  Solicitar Cita
                  </v-btn>
                  <v-dialog
                    v-model="dialogConfirmation"
                    width="500"
                  >
                    <v-card>
                      <v-card-title
                        class="headline grey lighten-2"
                        primary-title
                      >
                        <v-icon large color="info">info</v-icon>Verifique los datos para su cita
                      </v-card-title>
                      <v-card-text>
                        <p>Nombre completo del representante : {{formData.parent_name}}</p>              
                        <p>Nombre del representado : {{formData.pacient_name}}</p>              
                        <p>E-mail de contacto : {{formData.email}}</p>              
                        <p>Número telefonico de contacto : {{formData.phone_number}}</p>       
                        <p>Edad del representado : {{formData.pacient_age}}</p>             
                        <p>Especialidad por la que solicita la cita : {{formData.therapy_field}}</p>              
                        <p>Turno de preferencia : {{formData.time_preference}}</p>
                      </v-card-text>
                      <v-divider></v-divider>
                      <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn
                          color="primary"
                          flat
                          @click="submit"
                        >
                          Enviar Solicitud
                        </v-btn>
                      </v-card-actions>
                    </v-card>
                  </v-dialog>
                  <v-dialog
                    v-model="dialogLoad"
                    persistent
                    width="300"
                  >
                    <v-card>
                      <v-card-text class="overflow-hidden">
                        <div class="text-xs-center">
                          <v-progress-circular 
                            indeterminate
                            :size="100"
                            :width="10"
                          ></v-progress-circular>
                        </div>
                      </v-card-text>
                    </v-card>
                  </v-dialog>
                  <v-dialog
                    v-model="dialogDone"
                    width="300"
                  >
                    <v-card>
                      <v-card-text>
                        <div class="text-xs-center">
                          <p v-bind:style="{ fontSize: 20 + 'pt' }">Solicitud Enviada</p>
                          <v-icon large color="success">far fa-check-circle</v-icon>
                          <v-icon large color="success">fas fa-envelope</v-icon>
                        </div>
                      </v-card-text>
                    </v-card>
                  </v-dialog>
                  <v-dialog
                    v-model="dialogError"
                    width="300"
                  >
                    <v-card>
                      <v-card-text>
                        <div class="text-xs-center">
                          <v-icon large color="red">fas fa-exclamation-triangle</v-icon>
                          <p v-bind:style="{ fontSize: 12 + 'pt'}">Ocurrio un error interno y su solicitud no pudo ser procesada, considere contactarnos por otro medio, gracias por su comprensión</p>
                        </div>
                      </v-card-text>
                      <v-card-actions class="justify-center">
                        <v-btn to='/contacto'>Contactanos</v-btn>
                      </v-card-actions>
                    </v-card>
                  </v-dialog>
                </div>                
              </v-flex>
            </v-layout>
          </v-form>
      </v-layout>
    </v-container>
        
  </div>
</template>

<script>
export default {
  data: () => ({
    dialogConfirmation: false,
    dialogDone: false,
    dialogLoad: false,
    dialogError: false,
    valid: true,
    formData:{
      parent_name: '',
      pacient_name: '',
      phone_number: '',
      email: '',
      pacient_age: '',
      therapy_field: null,
      time_preference: null
    },
    nameRules: [
      v => !!v || 'Campo requerido'
    ],
    emailRules: [
      v => !!v || 'Campo requerido',
      v => /.+@.+/.test(v) || 'E-mail debe ser valido'
    ],
    ageRules: [
      v => !!v || 'Campo requerido',
      v => /\d+/.test(v)
    ],
    especialidades: [
      'Terapia ocupacional',
      'Terapia de lenguaje',
      'Terapia de conducta',
      'Psicopedagogía',
      'Baby Gym',
      'Asesoría Familiar'
    ],
    turnos: [
      'AM',
      'PM',
    ],
    checkoutline: false
  }),

  methods: {
    validate(){
      if(this.$refs.citaForm.validate()){
        this.dialogConfirmation = true;
      }
    },
    submit () {
      if (this.$refs.citaForm.validate()) {
        this.dialogConfirmation = false
        this.dialogLoad = true
        var csrftoken = this.$cookies.get('csrftoken');
        this.axios.post('/appointment_register/', this.formData, {'headers': {X_CSRFTOKEN: csrftoken}})
        .then(res => {
          this.dialogLoad = false;    
          this.dialogDone = true;
        })
        .catch(erro => {
          this.dialogLoad = false;
          this.dialogError = true;
        })
      }
    },    
  }
}
</script>
