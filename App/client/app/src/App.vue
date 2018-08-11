<template>
  <v-app> 
    <v-toolbar
      app
      :clipped-left="clipped"
    >
    <v-toolbar-title v-text="title"></v-toolbar-title>
    </v-toolbar>
    <v-content>
      <v-container fluid fill-height class="px-0 py-0">
        <v-layout class="px-0 py-0">
          <v-flex xs12>
            <v-fade-transition mode="out-in">
              <router-view class="px-0 py-0" v-if="isRouterAlive"></router-view>
            </v-fade-transition>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
    <v-footer :fixed="fixed" app>
      <span>&copy; 2017</span>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  data: () => ({
      isRouterAlive: true,
      clipped: false,
      fixed: false,
      title: 'Vuetify.js'
  }),
  methods: {
    reload() {
      this.isRouterAlive = false
      this.$nextTick(() => (this.isRouterAlive = true))
    }
  },
  name: 'App'
}
</script>
