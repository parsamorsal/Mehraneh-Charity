//
// var person={
// "name": "مهدیس تاجداری", "type": "نیکوکار", "linkk": "benefactorsProfileView.html"};
// var temp=document.createElement('a');
// temp.innerHTML=person.name+", "+person.type;
// temp.setAttribute("href",person.linkk);
//
// var pic=document.createElement('img');
// pic.setAttribute("src","images/mahdis.jpg");
// var profile=document.getElementById("profile");
//
// profile.appendChild(pic);
// profile.appendChild(temp);

function rate (e1,e2) {
  document.getElementById("f"+e1).value = e2;
  var id1 = "button" + e1;
  for (var i = 1; i <= e2; i++) {
    document.getElementById(id1+i).style.backgroundColor = "#12beff";
  }
  for (var i = e2+1; i < 6; i++) {
    document.getElementById(id1+i).style.background = "none";
  }
}

function changed() {
    document.getElementById("box").value = document.getElementById("textbox").value;
}

document.getElementById("button11").style.backgroundColor = "#12beff";
document.getElementById("button21").style.backgroundColor = "#12beff";
document.getElementById("button31").style.backgroundColor = "#12beff";
document.getElementById("button41").style.backgroundColor = "#12beff";
document.getElementById("button51").style.backgroundColor = "#12beff";


