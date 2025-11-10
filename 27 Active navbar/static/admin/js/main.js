document.addEventListener("DOMContentLoaded", function(){
  try {
    var el = document.querySelector(".welcome-sign") || document.querySelector(".content h1") || null;
    if(!el) return;
    var text = el.innerText.trim();
    var i = 0;
    el.innerText = "";
    var cursor = document.createElement("span");
    cursor.className = "hacker-cursor";
    el.parentNode.insertBefore(cursor, el.nextSibling);

    function typeTick(){
      if(i <= text.length){
        el.innerText = text.slice(0, i);
        i++;
        setTimeout(typeTick, 40 + Math.random()*60);
      } else {
        cursor.parentNode.removeChild(cursor);}
    }
    typeTick();
  } catch(e){
    console.error(e);
  }
});
