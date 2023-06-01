function tocaSom(seletorAudio){
  const elemento = document.querySelector(seletorAudio);

  if(elemento && elemento.localName === 'audio'){
    elemento.play();
  }
  else{
    alert('Elemento não encontrado ou seletor inválido.');
  }
}

const listaDeTeclas = document.querySelectorAll('.tecla');

/** estrutura de repetição WHILE
let i = 0;
while(i < listaDeTeclas.length){
  const tecla = listaDeTeclas[i];
  const instrumento = tecla.classList[1];
  const idAudio = `#som_${instrumento}`;
  listaDeTeclas[i].onclick = function(){
    tocaSom(idAudio);
  };
  i += 1;
}*/

/** Estrutura de repetição FOR */
for(let i = 0; i < listaDeTeclas.length; i++){
  const tecla = listaDeTeclas[i];
  const instrumento = tecla.classList[1];
  const idAudio = `#som_${instrumento}`;

  tecla.onclick = function(){
    tocaSom(idAudio);
  }

  tecla.onkeydown = function(evento){
    if(evento.code === "Enter" || evento.code === "Space"){
      tecla.classList.add('ativa');
    }
  }

  tecla.onkeyup = function(){
    tecla.classList.remove('ativa');
  }
}
