<template>
  <v-content style="height: 100%">
    <v-jumbotron src="" style="height: 100%">
        <v-flex xs12>
          <v-form ref='form'>
            <v-text-field
            :value="checkA"
            label="Your Answer"
            outline
            :loading="custom"
            readonly
            :rules='noEmpty'
          ></v-text-field>
          </v-form>
        </v-flex>
        <v-layout align-start justify-center row>
          <span class="headline font-weight-regular">
            ({{qCurrent}}/{{qLength}})
          </span>
        </v-layout>
        <v-layout align-start justify-center row>
            
            <v-btn fab dark large color="purple" @click.stop='sheet = !sheet' :disable="selectDisable">
              <v-icon dark>android</v-icon>
            </v-btn>
            <vueplayer :file='defaultMusic.src' :disable='playerDisable'/>
            <v-btn fab dark large color="purple" @click.stop='nextQ()' :disable="nextDisable">
              <v-icon dark>android</v-icon>
            </v-btn>
        </v-layout>
        <v-layout align-start justify-center row fill-height>
          <div id="container" ref="container">
            <live2dviewer></live2dviewer>
            <!-- <canvas id="glcanvas" style="height: 100%"></canvas> -->
          </div>
        </v-layout>
        <v-dialog v-model="sheet" fullscreen scrollable hide-overlay transition="dialog-bottom-transition">
          <v-card>
            <v-toolbar >
              <v-btn icon @click.native="sheet = false">
                <v-icon>close</v-icon>
              </v-btn>
              <v-toolbar-title>Select Answer</v-toolbar-title>
            </v-toolbar>
            <v-expansion-panel>
              <v-expansion-panel-content
                v-for="(item,index) in items"
                :key="index"
              >
                <div slot="header">{{item.tname}}</div>
                  <v-list>
                    <v-list-tile
                    v-for="(ite,i) in item.sub"
                    :key="i"
                    @click="check(ite.code,ite.sname)"
                    >
                      <v-list-tile-content>
                        <v-list-tile-title v-text="ite.sname"></v-list-tile-title>
                      </v-list-tile-content>
                    </v-list-tile>
                  </v-list>
              </v-expansion-panel-content>
            </v-expansion-panel>
          </v-card>
        </v-dialog>
    </v-jumbotron>
    <v-dialog
      v-model="result"
      scrollable fullscreen 
      persistent :overlay="false"
      transition="dialog-transition"
    >
      <v-card>
         <v-toolbar >
            <v-btn icon @click.native="result = false">
              <v-icon>close</v-icon>
            </v-btn>
            <v-toolbar-title>Result</v-toolbar-title>
          </v-toolbar>
        <v-data-table
          :headers="headers"
          :items="resultList"
          hide-actions
          class="elevation-1"
          disable-initial-sort
        >
          <template slot="items" slot-scope="props">
            <td>{{ props.item.q }}</td>
            <td>{{ props.item.a }}</td>
          </template>
        </v-data-table>
      </v-card>
    </v-dialog>
  </v-content>
</template>
<script>
import * as types from '@/store/types'
//import '@/utils/live2d.min.js'
//import * as Live2DHelper from '@/utils/live2d-helper.min.js'
import Live2DView from '@/components/Live2DView'
import vueplayer from '@/components/VuePlayer.vue'
export default {
  data:() => ({
    custom: false,
    qCurrent: 1,
    sheet: false,
    checkA: '',
    code: '',
    defaultMusic: {
      title: 'XXX',
      arttist: 'XXX',
      src: '',
      pic: ''
    },
    playerDisable: false,
    qLength: null,
    items: [
      { tname: '红魔乡', sub: [
        { sname: '01', code: '10000'},
        { sname: '02', code: '10001'},
        { sname: '03', code: '10002'},
        { sname: '04', code: '10003'},
        { sname: '05', code: '10004'}
      ]}
    ],
    noEmpty: [
      v => !!v || '不能为空'
    ],
    result: false,
    headers: [
      { text: "正确答案", value: '正确答案'}, 
      { text: '你的回答', value: '你的回答'}
    ],
    resultList: [],
    selectDisable: false,
    nextDisable: false,
    live2DHelper: null,
    l2dPath: null

  }),
  methods: {
    check(code, sname) {
      this.sheet = false
      this.code = code
      this.checkA = sname
    },
    nextQ() {
      if ( this.$refs.form ) {
        if( !this.$refs.form.validate() ) {
          return
        }
      }
      this.custom = true
      this.selectDisable = true
      this.nextDisable = true
      this.axios.post("/api/next", {
        answer: this.code
      }).then((response) => {
        this.custom = false
        if (response.status == 200) {
          if (response.data.retCode == 'success') {
            if (response.data.haveNext) {
              this.defaultMusic.src = 'http://localhost:5000/music/'+response.data.next+'.mp3'
              this.qCurrent = this.qCurrent+1
              this.checkA = ''
              this.code = ''
              this.$refs.form.reset()
            } else if(response.data.retCode == 'expired'){
              console.log(response.data)

            } else {
              console.log(response.data)
              this.result = true
              this.resultList = response.data.next.data
            }
            this.selectDisable = false
            this.nextDisable = false
          } else {
            console.log(response.data.retCode)
          }
        } else {
          console.log(response.status)
        }
      })
    },
    loadList() {
      this.axios.get("/music/list.json")
        .then((response) => {
          if (response.status == 200) {
            this.items = response.data
          }
        })
    }
  },
  created() {
    this.defaultMusic.src = 'http://localhost:5000/music/'+this.$route.query.question+'.mp3'
    this.qLength = this.$route.query.len
    // this.loadList()
  },
  mouted() {
  },
  components: {
    'vueplayer': vueplayer,
    'live2dviewer': Live2DView
  },
  name: 'Exam'
}
</script>