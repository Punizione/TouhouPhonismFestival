<template>
  <v-content style="height: 100%">
    <v-img :src="bgImage" style="height: 100%">
      <v-stepper v-model="e1" class="transparent">
        <v-stepper-header>
          <v-stepper-step :complete="e1 > 1" step="1">Step1</v-stepper-step>
          <v-divider></v-divider>
          <v-stepper-step :complete="e1 > 2" step="2">Step2</v-stepper-step>
          <v-divider></v-divider>
          <v-stepper-step :complete="e1 > 3" step="3">Step3</v-stepper-step>
          <v-divider></v-divider>
          <v-stepper-step step="4">Step4</v-stepper-step>
        </v-stepper-header>

        <v-stepper-items>
          <v-stepper-content step="1">
            <v-container fill-height>
              <v-layout align-center column fill-height>
                <img src="@/assets/logo.png" alt="Vuetify.js" class="mb-5">
                <v-form ref='form'>
                  <v-flex xs12 sm8>
                  <v-text-field
                  v-model="uname"
                  solo
                  label="Input Your Name"
                  clearable
                  :rules='noEmpty'
                  ></v-text-field>
                </v-flex>
                </v-form>
                

              </v-layout>
            </v-container>     
            <v-layout row>
              <v-flex xs6>
                <v-spacer></v-spacer>              
              </v-flex>
              <v-flex xs6>
                <v-btn
                  color="primary"
                  @click="checkName()"
                  >
                下一步
                </v-btn>
              </v-flex>
            </v-layout>
          </v-stepper-content>
          <v-stepper-content step="2">
            <v-container fill-height>
              <v-layout align-center column fill-height>
               选择难度
                  <v-btn flat large @click='setDifficulty("easy")'>Easy</v-btn>
                  <v-btn flat large @click='setDifficulty("normal")'>Normal</v-btn>
                  <v-btn flat large @click='setDifficulty("hard")'>Hard</v-btn>
                  <v-btn flat large @click='setDifficulty("lunatic")'>Lunatic</v-btn>
                  <v-btn flat large @click='setDifficulty("extra")'>Extra</v-btn>
              </v-layout>
            </v-container>
            <v-layout row>
              <v-flex xs6>
                <v-btn flat @click="e1 = 1">上一步</v-btn>
                <v-spacer></v-spacer>
                
              </v-flex>
              <v-flex xs6>
                <v-btn
                  color="primary"
                  @click="e1 = 3"
                  >
                下一步
                </v-btn>
              </v-flex>
            </v-layout>
          </v-stepper-content>
           
          <v-stepper-content step="3">
              <v-select
                :items="lengthItems"
                v-model="len"
                auto
                label="题目数量"
                single-line
                ></v-select>
              <v-layout row wrap>
                <v-flex xs12 sm4 md4>
                  <v-checkbox
                    v-model="typ"
                    label="整数作(不含黑历史)"
                    color="red"
                    value="1"
                    hide-details
                  ></v-checkbox>
                  <v-checkbox
                    v-model="typ"
                    label="小数点作"
                    color="red"
                    value="2"
                    hide-details
                  ></v-checkbox>
                  <v-checkbox
                    v-model="typ"
                    label="秘封厨专用"
                    color="red"
                    value="3"
                    hide-details
                  ></v-checkbox>
                </v-flex>
              </v-layout>

            <v-layout row>
              <v-flex xs6>
                <v-btn flat @click="e1 = 2">上一步</v-btn>
                <v-spacer></v-spacer>
              </v-flex>
              <v-flex xs6>
                <v-btn
                  color="primary"
                  @click="e1 = 4"
                  >
                下一步
                </v-btn>
              </v-flex>
            </v-layout>
          </v-stepper-content>

          <v-stepper-content step="4">
            <v-alert
              :value="true"
              type="success"
            >
              Name: {{uname}}
            </v-alert>
            <v-alert
              :value="true"
              type="success"
            >
              Difficulty: {{difficulty}}
            </v-alert>
            <v-alert
              :value="true"
              type="success"
            >
              Length : {{len}}
            </v-alert>
            <v-alert
              :value="true"
              type="success"
            >
              Type : {{ parseType(typ) }}
            </v-alert>
            <v-layout row>
              <v-flex xs6>
                <v-btn flat @click="e1 = 3">上一步</v-btn>
                <v-spacer></v-spacer>
              </v-flex>
              <v-flex xs6>
                <v-btn
                  color="primary"
                  @click="start()"
                  >
                开始
                </v-btn>
              </v-flex>
            </v-layout>
          </v-stepper-content>
        </v-stepper-items>
      </v-stepper>
    </v-img> 
  </v-content>
</template>

<script>
  import * as types from '@/store/types'
  export default {
    data: () => ({
      e1: 1,
      step: 1,
      uname: '',
      difficulty: 'easy',
      len: 10,
      noEmpty: [
        v => !!v || '不能为空'
      ],
      lengthItems: [
        '10',
        '20',
        '50'
      ],
      typ: ['1','2','3'],
      typMap: {
        '1': '整数作(不含黑历史)',
        '2': '小数点作',
        '3': '秘封厨专用'
      },
      bgImage: "http://p0s30qphu.bkt.clouddn.com/18-7-2/5372312.jpg"
    }),
    methods: {
      start() {
        this.axios.post('/api/start', {
          difficulty: this.difficulty,
          name: this.uname,
          typ: this.typ,
          randomID: ''+Math.floor((Math.random()+Math.floor(Math.random()*9+1))*Math.pow(10,7)),
          length: this.len
        }).then((response) => {
          if (response.status == 200){
            if (response.data.retCode == 'success') {
              this.$store.commit(types.TESTING, response.data.token)
              this.$router.push({
                path: '/exam',
                query: {
                  question: response.data.question,
                  len: this.len
                }
              })
            } else {
              console.log(response.data.retCode)
            }
          } else {
            console.log(response.data.status)
          }
        })
      },
      setDifficulty(difficulty) {
        this.difficulty = difficulty
        if (difficulty == 'easy') {
          this.bgImage = "http://p0s30qphu.bkt.clouddn.com/18-2-18/67879947.jpg"
        } else if (difficulty == 'normal') {
          this.bgImage = "http://p0s30qphu.bkt.clouddn.com/18-1-5/5971020.jpg"
        } else if (difficulty == 'hard') {
          this.bgImage = "http://p0s30qphu.bkt.clouddn.com/18-2-18/67879947.jpg"
        } else if (difficulty == 'lunatic') {
          this.bgImage = "http://p0s30qphu.bkt.clouddn.com/18-1-5/5971020.jpg"
        } else {
          this.bgImage = "http://p0s30qphu.bkt.clouddn.com/18-2-18/67879947.jpg"
        }
      },
      changeBgImage() {
        if (this.e1 == 2) {
          this.bgImage = "http://p0s30qphu.bkt.clouddn.com/18-2-18/67879947.jpg"
        } else {
          this.bgImage = "http://p0s30qphu.bkt.clouddn.com/18-7-2/5372312.jpg"
        }
      },
      checkName() {
        if( this.$refs.form ){
          if( this.$refs.form.validate() ){
            this.e1 = 2
          }
        }
      },
      parseType(typ) {
        let str = ''
        for (var i = 0; i <typ.length ; i++) {
          str += this.typMap[typ[i]] + ","
        }
        return str.substring(0,str.length-1)
      }
    },
    watch: {
      'e1': 'changeBgImage'
    },
    
    name: 'Start'
  }
</script>
