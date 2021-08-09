const containerMode = document.getElementsByClassName('container-mode')[0];
const butttonMode = document.getElementsByClassName('button')[0];
const body = document.querySelector('body');
var positionB = false;

containerMode.addEventListener('click', ()=>{
    if(!positionB){
        positionB = !positionB;
        butttonMode.style.left = 'calc(100% - 27px)'
        body.classList.toggle('darkMode')
    }else{
        butttonMode.style.left = '2px'
        positionB = !positionB;
        body.classList.toggle('darkMode')

    }
})

function loadTable(){
    fetch('usuario.json')
        .then((response)=>{
            console.log(typeof(response))
        })
}