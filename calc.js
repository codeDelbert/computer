const show = document.getElementById('input');
const symbol = document.getElementById('label');

calc = ""

function numberclick(number){
    if (show.value === '0'){
        show.value = number;
    }else if(symbol.innerText !==""){
        show.value = number;
        symbol.innerText = ""
    }else{
        show.value += number;
    }
    cale += (number)
}

function calculation(sym){
    symbol.innerText = sym
    console.log(sym)
    if (sym === "+"){
        calc += "+"
    }else if(sym === "-"){
        calc += "-"
    }else if(sym ==="÷"){
        calc += '/'
    }
}

function equals(){
    console.log()
    resault = eval(calc)
    console.log(resualt)
}