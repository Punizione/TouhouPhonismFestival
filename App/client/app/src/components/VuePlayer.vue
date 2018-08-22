<template>
  <div>
    <v-btn fab dark large color="purple" :disable="disable" @click.native="playing? stop(): play()">
      <v-icon v-if='playing === false || stop === true' >play_arrow</v-icon>
      <v-icon v-else>stop</v-icon>
    </v-btn>
    <audio id="player" ref="player" :src="file"></audio>
  </div>
</template>
<script>
  export default {
    'name': 'vueplayer',
    props: {
      file: {
        type: String,
        default: null
      },
      autoPlay: {
        type: Boolean,
        default: false
      },
      ended: {
        type: Function,
        default:() => {}
      },
      canPlay: {
        type: Function,
        default:() => {}
      },
      disable: {
        type: Boolean,
        default: false
      }
    },
    data () {
      return {
        isMuted: false,
        playing: false,
        audio: undefined
      }
    },
    methods: {
      stop() {
        this.playing = false,
        this.audio.pause()
        this.audio.currentTime = 0
      },
      play() {
        if (this.playing) {
          return 
        }
        this.stop = false
        this.audio.play()
        this.playing = true
      },
      _handleEnded() {
        this.stop = true
        this.playing = false
      },
      init: function () {
        this.audio.addEventListener('ended', this._handleEnded);
      }
    },
    mounted () {
      this.audio = this.$refs.player;
      this.init();
    },
    beforeDestory() {
      this.audio.removeEventListener('ended', this._handleEnded);
    }
  }
</script>