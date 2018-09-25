<template>
  <v-app> 
    <v-toolbar
      app
      :clipped-left="clipped"
    >
      <v-toolbar-title v-text="title"></v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn icon @click.stop='rankDialog = !rankDialog'>
        <v-icon>sort</v-icon>
      </v-btn>
      <v-btn icon @click.stop="helpDialog = !helpDialog">
        <v-icon>help</v-icon>
      </v-btn>
    
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
    <v-dialog
      v-model="rankDialog"
      scrollable fullscreen 
      persistent :overlay="false"
      transition="dialog-transition"
    >
      <v-card>
        <v-toolbar >
          <v-btn icon @click.native="rankDialog = false">
          <v-icon>close</v-icon>
          </v-btn>
          <v-toolbar-title>Ranking</v-toolbar-title>
        </v-toolbar>
        <v-tabs
          slider-color="yellow"
        >
          <v-tab
            v-for="n in diffList"
            :key="n"
            ripple
          >
            {{ n }}
          </v-tab>
          <v-tab-item
            v-for="n in diffList"
            :key="n"
          >
            <v-data-table
              :headers="headers"
              :items="rankItem[n]"
              hide-actions
              class="elevation-1"
              disable-initial-sort
            >
              <template slot="items" slot-scope="props">
                <td>{{ props.item.name }}</td>
                <td>{{ props.item.grade }}</td>
              </template>
              <template slot="no-data">
                <v-alert :value="true" color="error" icon="warning">
                  目前还没有dalao上榜 :(
                </v-alert>
              </template>
            </v-data-table>

          </v-tab-item>
        </v-tabs>
      </v-card>
    </v-dialog>
    <v-dialog
      v-model="helpDialog"
      scrollable fullscreen 
      persistent :overlay="false"
      transition="dialog-transition"
    >
      <v-card>
        <v-toolbar >
          <v-btn icon @click.native="helpDialog = false">
          <v-icon>close</v-icon>
          </v-btn>
          <v-toolbar-title>Help</v-toolbar-title>
        </v-toolbar>

      </v-card>
    </v-dialog>
  </v-app>
</template>

<script>
export default {
  data: () => ({
      isRouterAlive: true,
      clipped: false,
      fixed: false,
      rankDialog: false,
      helpDialog: false,
      diffList: [
        "Easy", "Normal", "Hard", "Lunatic", "Extra"
      ],
      rankItem: {
        'Easy': [],
        'Normal': [],
        'Hard': [],
        'Lunatic': [],
        'Extra': []
      },
      headers: [
        { text: "昵称", value: '昵称'}, 
        { text: '正确数', value: '正确数'}
      ],
      title: 'PhonismFestival'
  }),
  methods: {
    reload() {
      this.isRouterAlive = false
      this.$nextTick(() => (this.isRouterAlive = true))
    },
    getRank(difficulty) {
      this.axios.post('/api/rank', {
        "difficulty": difficulty
      }).then((response) => {
        if (response.status == 200) {
          if (response.data.retCode) {
            this.rankItem[difficulty] = response.data.data
          }
        }
      })
    }
  },
  name: 'App'
}
</script>
