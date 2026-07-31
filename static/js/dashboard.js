const ctx = document.getElementById("progressChart");

new Chart(ctx,{

type:"line",

data:{

labels:["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],

datasets:[{

label:"Mood Score",

data:[45,52,60,58,67,75,82],

borderWidth:3,

fill:false

}]

}

});