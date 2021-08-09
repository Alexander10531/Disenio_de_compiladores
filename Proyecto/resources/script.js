const containerMode = document.getElementsByClassName('container-mode')[0];
const butttonMode = document.getElementsByClassName('button')[0];
var positionB = false;
containerMode.addEventListener('click', ()=>{
    if(!positionB){
        positionB = !positionB;
        console.log("Estoy entrando aqui")
        butttonMode.style.left = 'calc(100% - 27px)'
    }else{
        butttonMode.style.left = '2px'
        positionB = !positionB;
    }
})
