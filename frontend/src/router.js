import Vue from 'vue'
import Router from 'vue-router'
import QuienesSomos from './views/QuienesSomos.vue'
import VisionMision from './views/VisionMision.vue'
import Servicios from './views/Servicios.vue'
import Instalaciones from './views/Instalaciones.vue'
import Ubicacion from './views/Ubicacion.vue'
import Citas from './views/Citas.vue'
import Contacto from './views/Contacto.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'quienes-somos',
      component: QuienesSomos
    },
    {
      path: '/vm',
      name: 'vision-mision',
      component: VisionMision
    },
    {
      path: '/serv',
      name: 'servicios',
      component: Servicios
    },
    {
      path: '/inst',
      name: 'instalaciones',
      component: Instalaciones
    },
    {
      path: '/ubic',
      name: 'ubicacion',
      component: Ubicacion
    },
    {
      path: '/citas',
      name: 'citas',
      component: Citas
    },
    {
      path: '/contacto',
      name: 'contacto',
      component: Contacto
    }
    // {
    //   path: '/about',
    //   name: 'about',
    //   // route level code-splitting
    //   // this generates a separate chunk (about.[hash].js) for this route
    //   // which is lazy-loaded when the route is visited.
    //   component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    // }
  ]
})
