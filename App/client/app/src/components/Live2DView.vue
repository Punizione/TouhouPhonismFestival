<template>
  <canvas id="glcanvas" class="glcanvas" ref="glcanvas"></canvas>
</template>

<script>
  import Define from '@/utils/Define'

  const DEFINES = Define.data().defines
  let container
  let Live2Dmodeler = []
  let appUserId
  let recognition
  let nowRecognition = false
  let inputText
  let outputText

  export default {
    name: 'Live2DView',
    mounted: function () {
      // where is container?
      // container can be a wrap-in tag
      container = this.$refs.container
      this.create_Live2D(DEFINES.MODEL_PATH0, DEFINES.MODEL_JSON0,
      DEFINES.HARU_SUIT_SCALE, DEFINES.HARU_SUIT_POSX, DEFINES.HARU_SUIT_POSY)
    },
    methods: {
      create_Live2D(modelFilePath, modelFileJson, scale, posX, posY) {
        Live2Dmodeler[0] = new Live2DRender(
          DEFINES.ROOT_PATH,
          DEFINES.KEYWORD_JSON,
          modelFilePath,
          modelFileJson,
          scale,
          posX,
          posY,
          DEFINES.CAN_ID,
          DEFINES.CAN_SIZE)
      }

    }
  }
</script>